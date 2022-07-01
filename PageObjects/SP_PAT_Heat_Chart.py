import csv
import os
import re
import time
from datetime import date
import pandas as pd

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path
from filenames import file_extention
from get_dir import pwd
from utilities.readProperties import ReadConfig
from selenium.common import exceptions


class PAT_Heat_Chart:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    def __init__(self, driver):
        self.driver = driver

    def page_loading(self, driver):
        self.data = Locator_Path
        try:
            driver.implicitly_wait(20)
            self.driver = driver
            for x in range(1, 10):
                elem = self.driver.find_element_by_id(self.data.loader).text
                if str(elem) == "Loading…":
                    time.sleep(5)
                if str(elem) != "Loading…":
                    time.sleep(5)
                    break
        except NoSuchElementException:
            pass

    def get_current_date(self):
        today = date.today()
        dates = today.strftime('%d-%m-%Y')
        return dates

    def get_management_selected_option(self):
        self.data = Locator_Path
        self.driver.implicitly_wait(10)
        management_name = self.driver.find_element_by_id(self.data.Management).text
        management_name = management_name[16:].strip().lower()
        return management_name

    def navigate_to_heatchart_report(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id(self.data.menu_icon).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.data.std_performance).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.data.PAT_HC).click()
        time.sleep(4)

    def click_on_state(self, driver):
        self.driver = driver
        self.data = Locator_Path
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        time.sleep(4)

    def login(self, username, password):
        self.data = Locator_Path()
        self.driver.maximize_window()
        self.driver.find_element_by_id(self.data.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(password)
        self.driver.find_element_by_id(self.data.Submit_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.data.cQube_Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.data.std_performance).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.data.PAT_HC).click()
        time.sleep(5)
        
    def Blocks_select_box(self, setup):
        self.p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(self.data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(self.data.blocks_dropdown))
        # grade = Select(self.driver.find_element_by_id(self.data.grade))
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        # grade.select_by_index(2)
        gradename = (grade.options[2].text).strip()
        gradenum = re.sub('\D', '', gradename).strip()
        value = self.driver.find_element_by_id(self.data.blocks_dropdown).get_attribute('value')
        value = value.split(":")
        self.SP.page_loading(self.driver)
        for k in range(1,len(grade.options)):
            grade.select_by_index(k)
            self.SP.page_loading(self.driver)
            for i in range(len(dists.options)-1, len(dists.options)):
                dists.select_by_index(i)
                self.SP.page_loading(self.driver)
                for j in range(len(Blocks.options)-1, len(Blocks.options)):
                    Blocks.select_by_index(j)
                    self.SP.page_loading(self.driver)
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_clusters()+management+'_'+gradenum+ \
                "_blocks_of_district_"+value[1].strip()+'_'+self.month+'_'+self.year+'_'+self.SP.get_current_date()+'.csv'
                    file = os.path.isfile(self.filename)
                    if file != True:
                        print(Blocks.options[i].text,'Block wise records csv file is not downloaded ')
                        count = count + 1
                os.remove(self.filename)

            self.SP.page_loading(self.driver)
        return count

    def Clusters_select_box(self, setup):
        self.driver = setup
        self.p = pwd()
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        self.year , self.month = self.SP.get_pat_month_and_year_values()
        clust = Select(self.driver.find_element_by_id(self.data.cluster_dropdown))
        dists = Select(self.driver.find_element_by_id(self.data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(self.data.blocks_dropdown))
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        self.SP.page_loading(self.driver)
        for m in range(2, len(grade.options)):
            grade.select_by_index(m)
            gradename = grade.options[m].text
            gradenum = re.sub('\D','',gradename).strip()
            self.SP.page_loading(self.driver)
            for i in range(len(dists.options)-1, len(dists.options)):
                dists.select_by_index(i)
                self.SP.page_loading(self.driver)
                for j in range(len(Blocks.options)-1, len(Blocks.options)):
                    Blocks.select_by_index(j)
                    self.SP.page_loading(self.driver)
                    for k in range(1, len(clust.options)):
                        clust.select_by_index(k)
                        time.sleep(5)
                        self.SP.page_loading(self.driver)
                        value =self.driver.find_element_by_id(self.data.cluster_dropdown).get_attribute('value')
                        value = value.split(":")
                        if 'No data found' in self.driver.page_source:
                            print(clust.options[k].text , "not having data ")
                        else:
                            self.driver.find_element_by_id(self.data.Downloads).click()
                            time.sleep(3)
                            self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_schools()+management+'_'+gradenum+"_schools_of_cluster_"+value[1].strip()+"_"+self.month+'_'+self.year+'_'+self.SP.get_current_date()+'.csv'
                            print(self.filename)
                            file = os.path.isfile(self.filename)
                            if file != True:
                                print(clust.options[k].text, 'Cluster wise records csv file is not downloaded')
                                count = count + 1
                            self.SP.page_loading(self.driver)
                            os.remove(self.filename)
        return count


    def viewbys_options(self, setup):
        self.p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()

        grades = Select(self.driver.find_element_by_id(self.data.grade))
        grades.select_by_index(2)
        gradename = grades.options[2].text
        gradenum = re.sub('\D','',gradename).strip()
        self.SP.page_loading(self.driver)

        view_by = Select(self.driver.find_element_by_id(self.data.view_by))
        # view_by.select_by_visible_text(' Question Id ')
        view_by.select_by_index(1)
        self.SP.page_loading(self.driver)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + self.fname.pchart_views()+management+"_"+ gradenum + '_' + self.data.question_id + self.month + '_' \
                        + self.year + '_' + self.SP.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print(self.data.question_id, 'csv file is not downloaded')
            count = count + 1
        # view_by.select_by_visible_text(' Indicator ')
        view_by.select_by_index(2)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.file = self.p.get_download_dir() + "/" + self.fname.pchart_views()+management+"_"+gradenum + '_' + self.data.indicator_id + self.month + '_' \
                    + self.year + '_' + self.SP.get_current_date() + '.csv'
        print(self.file)
        if os.path.isfile(self.file) != True:
            print(self.data.indicator_id, 'csv file is not downloaded')
            count = count + 1
        os.remove(self.filename)
        os.remove(self.file)
        return count

    def test_questions_records(self, setup):
        self.p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        grade.select_by_index(2)
        gradename = grade.options[2].text
        gradenum = re.sub('\D', '', gradename).strip()
        self.SP.page_loading(self.driver)
        view_by = Select(self.driver.find_element_by_id(self.data.view_by))
        view_by.select_by_index(1)
        self.SP.page_loading(self.driver)
        if view_by.options[1].text in self.driver.page_source:
            print(view_by.options[1].text, 'is displayed records in heat chart')
        else:
            print(view_by.options[1].text, 'Records are not displayed')
            count = count + 1
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + self.fname.pchart_views()+management+'_'+ gradenum + '_' + self.data.question_id + self.month + '_' \
                    + self.year + '_' + self.SP.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print(view_by.options[1].text, 'csv file is not downloaded')
            count = count + 1
        else:
            print(view_by.options[1].text, 'csv file is downloaded')
        os.remove(self.filename)
        return count

    def test_indicator_records(self, setup):
        self.p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        management = self.SP.get_management_selected_option()
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        grade.select_by_index(4)
        gradename = grade.options[4].text
        gradenum = re.sub('\D', '', gradename).strip()
        self.SP.page_loading(self.driver)
        view_by = Select(self.driver.find_element_by_id(self.data.view_by))
        view_by.select_by_index(2)
        self.SP.page_loading(self.driver)
        if view_by.options[2].text in self.driver.page_source:
            print(view_by.options[2].text, 'is displayed records in heat chart')
        else:
            print(view_by.options[2].text, 'Records are not displayed')
            count = count + 1
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + self.fname.pchart_views()+management+'_'+ gradenum + '_' + 'allDistricts_' + self.month + '_' \
                    + self.year + '_' + self.SP.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print(view_by.options[2].text, 'csv file is not downloaded')
            count = count + 1
        else:
            print(view_by.options[2].text, 'csv file is downloaded')
        os.remove(self.filename)
        return count

    def download_all_district_records(self, setup):
        self.p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        # self.year,self.month = cal.pat_month_and_year_values()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_id(self.data.cQube_logo).click()
        self.SP.page_loading(self.driver)
        self.SP.navigate_to_heatchart_report()
        month = Select(self.driver.find_element_by_id('month'))
        month.select_by_index(1)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_all_districts()+management+'_overall_allDistricts_'+self.month+'_'+self.year+'_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
             print("Districtwise csv file is not downloaded")
        else:
              print('District wise csv file is downloaded ')
        os.remove(self.filename)
        self.SP.page_loading(self.driver)
        return count

    def exams_dates(self, setup):
        self.p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        grade.select_by_index(4)
        self.SP.page_loading(self.driver)
        examdates = Select(self.driver.find_element_by_id(self.data.exam_dates))
        for i in range(1, len(examdates.options)):
            examdates.select_by_index(i)
            self.SP.page_loading(self.driver)
            if examdates.options[i].text in self.driver.page_source:
                print(examdates.options[i].text ,'is displaying chart table ')
                self.SP.page_loading(self.driver)
            else:
                print(examdates.options[i].text ,'is not displayed ')
                count = count + 1
        self.SP.page_loading(self.driver)
        return count

    def subjects_types(self, setup):
        self.p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(self.data.cQube_logo).click()
        self.SP.page_loading(self.driver)
        self.SP.navigate_to_heatchart_report()
        self.SP.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id(self.data.sar_year))
        month = Select(self.driver.find_element_by_id(self.data.sar_month))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        grade.select_by_index(4)
        gradename =(grade.options[4].text).strip()
        gradenum = re.sub('\D','',gradename)
        self.SP.page_loading(self.driver)
        subject = Select(self.driver.find_element_by_id(self.data.subjects))
        for i in range(2, len(subject.options)):
            subject.select_by_index(i)
            self.SP.page_loading(self.driver)
            time.sleep(6)
            if "No data found" in  self.driver.page_source:
                print(subject.options[i].text, 'HAVING NO DATA FOUND ')
                self.SP.page_loading(self.driver)
            else:
                print(subject.options[i].text, 'is displayed chart table ')
                self.driver.find_element_by_id(self.data.Downloads).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_subjects()+management+'_'+gradenum+'_'+(subject.options[i].text).strip()+\
                                '_allDistricts_'+self.month+'_'+self.year+'_'+self.SP.get_current_date()+'.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(subject.options[i].text, 'csv file is not downloaded')
                    count = count + 1
                self.SP.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def test_homeicons(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        grade.select_by_index(2)
        self.SP.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_id(self.data.exam_dates))
        timeseries.select_by_index(2)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)

    def test_homebutton(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.cQube_logo).click()
        self.SP.page_loading(self.driver)
        # self.driver.find_element_by_xpath("//div[@id='heatChart']").click()
        self.SP.navigate_to_heatchart_report()
        self.SP.page_loading(self.driver)
        if 'heat-chart' in self.driver.current_url:
            print('Pat heat chart is present ')
        else:
            print('Home button is not working ')
            count = count + 1
        self.SP.page_loading(self.driver)
        return count


    def test_year_dropdown(self, setup):
        self.driver = setup
        self.p = pwd()
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        year_select = Select(self.driver.find_element_by_id(self.data.year_select))
        for i in range(1, len(year_select.options)):
            year_select.select_by_index(i)
            self.SP.page_loading(self.driver)
            if year_select.options[i].text in self.driver.page_source:
                print(year_select.options[i].text, 'is displaying chart table ')
                self.SP.page_loading(self.driver)
            else:
                print(year_select.options[i].text, 'is not displayed ')
                count = count + 1
        self.SP.page_loading(self.driver)
        return count

    def District_select_box(self, setup):
        self.driver = setup
        self.p = pwd()
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grades = Select(self.driver.find_element_by_id(self.data.grade))
        grades.select_by_index(2)
        gradename = (grades.options[2].text).strip()
        gradenum =re.sub('\D','',gradename).strip()
        dists = Select(self.driver.find_element_by_id(self.data.district_dropdown))
        view_by = Select(self.driver.find_element_by_id(self.data.view_by))
        for j in range(len(view_by.options)):
            view_by.select_by_index(j)
            self.SP.page_loading(self.driver)
            for i in range( len(dists.options)-4, len(dists.options)):
                dists.select_by_index(i)
                print(dists.options[i].text)
                value = self.driver.find_element_by_id(self.data.district_dropdown).get_attribute('value')
                value = value.split(":")
                self.SP.page_loading(self.driver)
                self.driver.find_element_by_id(self.data.Downloads).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_blocks()+management+'_'+gradenum+ \
                "_blocks_of_district_"+value[1].strip()+'_'+self.month+'_'+self.year+'_'+self.SP.get_current_date()+'.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, 'District wise records csv file is not downloaded')
                    count = count + 1
                self.SP.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def get_pat_month_and_year_values(self):
        year = Select(self.driver.find_element_by_id(self.data.sar_year))
        month = Select(self.driver.find_element_by_id(self.data.sar_month))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        return self.year, self.month

    def check_block_select_box(self, setup):
        self.p = pwd()
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        self.year , self.month = self.SP.get_pat_month_and_year_values()
        dists = Select(self.driver.find_element_by_id(self.data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(self.data.blocks_dropdown))
        grade = Select(self.driver.find_element_by_id(self.data.grade))
        self.SP.page_loading(self.driver)
        for m in range(2, len(grade.options)):
            grade.select_by_index(m)
            gradename = grade.options[m].text
            gradenum = re.sub('\D','',gradename).strip()
            self.SP.page_loading(self.driver)
            for i in range(len(dists.options)-1, len(dists.options)):
                dists.select_by_index(i)
                self.SP.page_loading(self.driver)
                for j in range(len(Blocks.options)-1, len(Blocks.options)):
                    Blocks.select_by_index(j)
                    self.SP.page_loading(self.driver)
                    value = self.driver.find_element_by_id(self.data.blocks_dropdown).get_attribute('value')
                    bvalue = value.split(":")
                    val = bvalue[1].strip()
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(4)
                    self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_clusters() + management + '_' + gradenum + "_clusters_of_block_" + val +'_'+ self.month + '_' + self.year + '_' + \
                                    self.SP.get_current_date() + '.csv'
                    print(self.filename)
                    file = os.path.isfile(self.filename)
                    if file != True:
                        print(Blocks.options[j].text, 'Block wise records csv file is not downloaded')
                        count = count + 1
                    self.SP.page_loading(self.driver)
                    os.remove(self.filename)
                return count

    def test_hyperlink(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        examdates = Select(self.driver.find_element_by_id('grade'))
        examdates.select_by_index(4)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)


    def grades_files(self, setup):
        self.driver = setup
        self.p = pwd()
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grades = Select(self.driver.find_element_by_id(self.data.grade))
        self.SP.page_loading(self.driver)
        for i in range(2, len(grades.options)):
            time.sleep(2)
            grades.select_by_index(i)
            gradename = grades.options[i].text
            gradenum = re.sub('\D','',gradename).strip()
            self.SP.page_loading(self.driver)
            if grades.options[i].text in self.driver.page_source:
                print(grades.options[i].text ,'is displayed in chart ')
                self.SP.page_loading(self.driver)
            else:
                print(grades.options[i].text ,'is not displayed ')
                count = count + 1
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + self.fname.pchart_grades()+management+'_'+gradenum+'_'+'allDistricts_'+self.month+'_'+self.year+'_'+self.SP.get_current_date()+'.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(grades.options[i].text,'csv file is not downloaded ')
                count = count + 1
            else:
                print(grades.options[i].text,"csv file is downloaded")
            os.remove(self.filename)
        self.SP.page_loading(self.driver)
        return count

    def test_randoms(self, setup):
        self.driver = setup
        self.p = pwd()
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PAT_Heat_Chart(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grades = Select(self.driver.find_element_by_id(self.data.grade))
        grades.select_by_index(4)
        if grades.options[4].text in self.driver.page_source:
            print(grades.options[4].text, 'is displayed in chart ')
            self.SP.page_loading(self.driver)
        else:
            print(grades.options[4].text, 'is not displayed ')
            count = count + 1
        subject = Select(self.driver.find_element_by_id(self.data.subjects))
        subject.select_by_index(3)
        if subject.options[3].text in self.driver.page_source:
            print(subject.options[3].text, 'is displayed in chart ')
            self.SP.page_loading(self.driver)
        else:
            print(subject.options[3].text, 'is not displayed ')
            count = count + 1
        self.SP.page_loading(self.driver)

        grades = Select(self.driver.find_element_by_id(self.data.grade))
        grades.select_by_index(3)
        if grades.options[3].text in self.driver.page_source:
            print(grades.options[3].text, 'is displayed in chart ')
            self.SP.page_loading(self.driver)
        else:
            print(grades.options[3].text, 'is not displayed ')
            count = count + 1
        subject = Select(self.driver.find_element_by_id(self.data.subjects))
        subject.select_by_index(2)
        if subject.options[2].text in self.driver.page_source:
            print(subject.options[2].text, 'is displayed in chart ')
            self.SP.page_loading(self.driver)
        else:
            print(subject.options[2].text, 'is not displayed ')
            count = count + 1
        self.SP.page_loading(self.driver)
        return count