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


class SATReport:
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
        self.driver.find_element_by_id(self.data.SAT).click()


    def click_download_icon_of_schools(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        self.driver.find_element_by_id(self.data.School_button).click()
        self.SP.page_loading(self.driver)
        time.sleep(10)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(15)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.sr_school()+management+'_all_allGrades__allSchools_'+self.SP.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('School level csv file is not download')
            count = count + 1
        return count

    def check_markers_on_block_map(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Block_button).click()
        self.SP.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        return dots

    # def check_last_30_days(self, setup):
    #     self.driver = setup
    #     self.data = Locator_Path()
    #     self.driver.get(self.baseUrl)
    #     self.SP = SATReport(self.driver)
    #     self.SP.login(self.username, self.password)
    #     self.SP.page_loading(self.driver)
    #     count = 0
    #     self.SP.click_on_state(self.driver)
    #     self.SP.page_loading(self.driver)
    #     times= Select(self.driver.find_element_by_id('period'))
    #     times.select_by_index(2)
    #     print(times.first_selected_option.text)
    #     time.sleep(3)
    #     schools = self.driver.find_element_by_id('schools').text
    #     students = self.driver.find_element_by_id('students').text
    #     attended = self.driver.find_element_by_id('studentsAttended').text
    # 
    #     schol = re.sub('\D', "", schools)
    #     std = re.sub('\D', "", students)
    #     attd = re.sub('\D', "", attended)
    # 
    #     print('Expected footer values : ', schol, std, attd)
    # 
    #     print('***************Block level footer values******************')
    # 
    #     self.driver.find_element_by_id(self.data.Block_button).click()
    #     # cal = GetData()
    #     self.SP.page_loading(self.driver)
    #     time.sleep(5)
    #     dots = self.driver.find_elements_by_class_name(self.data.markers)
    #     markers = len(dots) - 1
    #     if markers == 0:
    #         print("Block level markers are not present ")
    #         count = count + 1
    #     else:
    #         print('*********Block level markers are displayed***********')
    #         bschools = self.driver.find_element_by_id('schools').text
    #         bsch = re.sub('\D', "", bschools)
    # 
    #         bstudents = self.driver.find_element_by_id('students').text
    #         bstd = re.sub('\D', "", bstudents)
    # 
    #         battended = self.driver.find_element_by_id('studentsAttended').text
    #         battd = re.sub('\D', "", battended)
    # 
    #         print('after Clicking of block footer values ', bsch, bstd, battd)
    #         count = 0
    #         if int(bsch) != int(schol):
    #             print('Block level footer mismatch found', int(bsch), int(schol))
    #             count = count + 1
    #         # if int(bstd) != int(std):
    #         #     print('Block level footer mismatch found', int(bstd), int(std))
    #         #     count = count + 1
    #         if int(battd) != int(attd):
    #             print('Block level footer mismatch found', int(battd), int(attd))
    #             count = count + 1
    # 
    #         print('***************Cluster level footer values******************')
    # 
    #         self.driver.find_element_by_id(self.data.Cluster_button).click()
    #         # cal = GetData()
    #         self.SP.page_loading(self.driver)
    #         dots = self.driver.find_elements_by_class_name(self.data.markers)
    #         dots = len(dots) - 1
    #         if dots == 0:
    #             print("Cluster level markers are not present ")
    #             count = count + 1
    # 
    #         cschools = self.driver.find_element_by_id('schools').text
    #         csch = re.sub('\D', '', cschools)
    # 
    #         cstudents = self.driver.find_element_by_id('students').text
    #         cstd = re.sub('\D', '', cstudents)
    # 
    #         cattended = self.driver.find_element_by_id('studentsAttended').text
    #         cattd = re.sub('\D', '', cattended)
    # 
    #         print('after Clicking of cluster footer values ', csch, cstd, cattd)
    # 
    #         if int(csch) != int(schol):
    #             print('Cluster level footer mismatch found', int(csch), int(schol))
    #             count = count + 1
    #         # if int(cstd) != int(std):
    #         #     print('Cluster level footer mismatch found', int(cstd), int(std))
    #         #     count = count + 1
    #         if int(cattd) != int(attd):
    #             print('Cluster level footer mismatch found', int(cattd), int(attd))
    #             count = count + 1
    # 
    #         print('***************School level footer values******************')
    # 
    #         self.driver.find_element_by_id(self.data.School_button).click()
    #         # cal = GetData()
    #         self.SP.page_loading(self.driver)
    #         result = self.driver.find_elements_by_class_name(self.data.markers)
    #         dots = len(result) - 1
    #         if dots == 0:
    #             print("Cluster level markers are not present ")
    #             count = count + 1
    # 
    #         sschools = self.driver.find_element_by_id('schools').text
    #         ssch = re.sub('\D', '', sschools)
    # 
    #         sstudents = self.driver.find_element_by_id('students').text
    #         sstd = re.sub('\D', '', sstudents)
    # 
    #         sattended = self.driver.find_element_by_id('studentsAttended').text
    #         sattd = re.sub('\D', '', sattended)
    # 
    #         print('after Clicking of School footer values ', ssch, sstd, sattd)
    # 
    #         if int(ssch) != int(schol):
    #             print('School level footer mismatch found', int(ssch), int(schol))
    #             count = count + 1
    #         # if int(sstd) != int(std):
    #         #     print('School level footer mismatch found', int(sstd), int(std))
    #         #     count = count + 1
    #         if int(sattd) != int(attd):
    #             print('Cluster level footer mismatch found', int(sattd), int(attd))
    #             count = count + 1
    #     return count
    
    def check_markers_on_clusters_map(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        self.SP.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        return dots
    
    def check_markers_on_school_map(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.School_button).click()
        self.SP.page_loading(self.driver)
        time.sleep(15)
        result = self.driver.find_elements_by_class_name(self.data.markers)
        return result


    def click_on_hyperlinks(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        dist.select_by_index(1)
        self.SP.page_loading(self.driver)
        block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        block.select_by_index(1)
        self.SP.page_loading(self.driver)
        cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
        cluster.select_by_index(1)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.sr_school_hyper).click()
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.sr_cluster_hyper).click()
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.sr_dist_hyper).click()
        self.SP.page_loading(self.driver)
        result1 = self.driver.find_element_by_id(self.data.Choose_Block).is_displayed()
        time.sleep(2)
        result2 = self.driver.find_element_by_id(self.data.Choose_Cluster).is_displayed()
        time.sleep(2)
        dist = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        choose_dist= dist.first_selected_option.text
        return result1,result2,choose_dist

    def click_download_icon_of_district(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        count = 0
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.sr_district()+management+'_all_allGrades__allDistricts_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
           return "File Not Downloaded"
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                dots = len(markers) - 1
                if dots != row_count:
                    print('Markers records and csv file records are not matching ', dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return count

    def click_download_icon_of_blocks(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        year =Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        self.driver.find_element_by_id(self.data.Block_button).click()
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.sr_block()+management+'_'+self.year.strip()+'_'+self.semester+'_allGrades__allBlocks_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)

    def click_download_icon_of_clusters(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        management = self.SP.get_management_selected_option()
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(10)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.sr_cluster()+management+'_'+self.year.strip()+'_'+self.semester+'_allGrades__allClusters_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)


    def check_grade_dropdown_options(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        count = 0
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        grade =Select(self.driver.find_element_by_id(self.data.Grade))
        counter = len(grade.options)
        for i in range(1,len(grade.options)):
            grade.select_by_index(i)
            print(grade.options[i].text)
            time.sleep(2)
            self.SP.page_loading(self.driver)
        return counter

    def click_each_grades(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        count = 0
        p = pwd()
        files = file_extention()
        self.driver.implicitly_wait(100)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.SP.get_management_selected_option()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        grade =Select(self.driver.find_element_by_id(self.data.Grade))
        for i in range(1,len(grade.options)):
            grade.select_by_index(i)
            time.sleep(3)
            gradename = (grade.options[i].text).strip()
            gradenum = re.sub('\D','',gradename)
            self.SP.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(self.data.markers)
            markers = len(dots)-1
            self.SP.page_loading(self.driver)
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(4)
            self.filename = p.get_download_dir() + '/'+ files.sr_gradewise()+management+"_"+self.year.strip()+"_"+self.semester+"_Grade "+gradenum.strip()+'__allDistricts_'+self.SP.get_current_date()+'.csv'
            print(self.filename)
            time.sleep(1)
            if os.path.isfile(self.filename) != True:
                print('Grade '+gradenum.strip()+'wise csv file is not downloaded')
                count = count + 1
            else:
                file = open(self.filename)
                read = file.read()
                if grade.options[i].text in read:
                    print(grade.options[i].text ,"is present")
                self.SP.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def select_subjects_dropdown(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        p = pwd()
        count = 0
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.SP.get_management_selected_option()
        grade = Select(self.driver.find_element_by_id(self.data.Grade))
        subjects = Select(self.driver.find_element_by_id(self.data.Subject))
        subcount = len(subjects.options)-1
        files = file_extention()
        for i in range(1,len(grade.options)-1):
            grade.select_by_index(i)
            time.sleep(2)
            print(grade.options[i].text)
            self.SP.page_loading(self.driver)
            gradename = (grade.options[i].text).strip()
            gradenum = re.sub('\D','',gradename)
            for j in range(1,len(subjects.options)-1):
                time.sleep(1)
                subjects.select_by_index(j)
                time.sleep(2)
                print(subjects.options[j].text)
                if 'No data found' in self.driver.page_source:
                    print(grade.options[i].text+', '+subjects.options[j].text+" is not having data")
                    return count
                else:
                    self.SP.page_loading(self.driver)
                    sub = (subjects.options[j].text).strip()
                    time.sleep(3)
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + '/' + files.sr_gradewise()+management+"_"+self.year.strip()+"_"+self.semester+"_Grade "+gradenum.strip()+'_'+sub+'_allDistricts_' + self.SP.get_current_date()+'.csv'
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(files.sr_gradewise()+gradenum.strip() ,' wise csv file is not downloaded')
                        count = count + 1

                    os.remove(self.filename)
                    self.SP.page_loading(self.driver)
                return count

    def remove_csv(self):
        os.remove(self.filename)

    def check_district(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.SP.get_management_selected_option()
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.SP.page_loading(self.driver)
            value = self.driver.find_element_by_id(self.data.Choose_Dist).get_attribute('value')
            value = value.split(":")
            val = value[1].strip()
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            time.sleep(3)
            if (len(markers) - 1) == 0 :
                print("District" + select_district.first_selected_option.text +"no data")
                count = count + 1
            else:
                time.sleep(2)
                self.driver.find_element_by_id(self.data.Downloads).click()
                time.sleep(3)
                p = pwd()
                self.filename = p.get_download_dir() + "/" + self.fname.sr_districtwise()+management+'_'+self.year.strip()+'_'+self.semester+'_allGrades__blocks_of_district_'+val+'_'+self.SP.get_current_date()+'.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                        dots = len(markers)-1
                        if dots != row_count:
                            print('Markers records and csv file records are not matching ',dots,row_count)
                            count = count + 1
                    self.remove_csv()

        return count

    def check_districts_block(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.SP.get_management_selected_option()
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            self.SP.page_loading(self.driver)
            for y in range(len(select_block.options)-2, len(select_block.options)):
                select_block.select_by_index(y)
                self.SP.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value.split(":")
                markers = self.driver.find_elements_by_class_name(self.data.markers)
                if len(markers) - 1 == 0:
                    print("District" + select_district.first_selected_option.text +"Block"+ select_block.first_selected_option.text +"No Data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_blockwise()+management+'_'+self.year.strip()+'_'+self.semester+'_allGrades__clusters_of_block_'+value[1].strip()+'_'+self.SP.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text +"Block "+ select_block.first_selected_option.text+"csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            dots = len(markers) - 1
                            if dots != row_count:
                                print('Markers records and csv file records are not matching ', dots, row_count)
                                count = count + 1
                        self.remove_csv()

                return count

    def check_district_block_cluster(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = SATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        management = self.SP.get_management_selected_option()
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        select_cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            self.SP.page_loading(self.driver)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                self.SP.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    time.sleep(3)
                    self.SP.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value[3:]
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(4)
                    p = pwd()
                    self.filename = p.get_download_dir() +"/" + self.fname.sr_clusterwise()+management+'_'+self.year.strip()+'_'+self.semester+'_allGrades__schools_of_cluster_'+value.strip()+'_'+self.SP.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + " Block: " + select_block.first_selected_option.text + " Cluster: " + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            dots = len(markers) - 1
                            if dots != row_count:
                                print('Markers records and csv file records are not matching ', dots, row_count)
                                count = count + 1
                        self.remove_csv()
                return count