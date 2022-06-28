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


class UdiseReport:
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

    def get_management_selected_option(self):
        self.data = Locator_Path
        self.driver.implicitly_wait(10)
        management_name = self.driver.find_element_by_id(self.data.Management).text
        management_name = management_name[16:].strip().lower()
        return management_name

    def get_current_date(self):
        today = date.today()
        dates = today.strftime('%d-%m-%Y')
        return dates

    def login(self, username, password):
        self.data = Locator_Path()
        self.driver.maximize_window()
        self.driver.find_element_by_id(self.data.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(password)
        self.driver.find_element_by_id(self.data.Submit_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.data.cQube_Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.data.UdiseReport).click()

    def test_mouse_over(self):
        self.driver.implicitly_wait(20)
        lists = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(lists) - 1
        time.sleep(5)

        def mouseover(i):
            action = ActionChains(self.driver)
            action.move_to_element(lists[i]).perform()
            time.sleep(3)
            del action

        i = 0
        while i < len(lists):
            mouseover(i)
            i = i + 1
        return count

    def test_link(self,setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        count = 0
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Block_button).click()
        time.sleep(5)
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        count1 = len(markers)-1
        self.driver.find_element_by_xpath(self.self.data.hyper_link).click()
        time.sleep(3)
        marker = self.driver.find_elements_by_class_name(self.data.markers)
        count2 = len(marker)-1
        if count1!=count2:
            print("Hyperlink is working as expected...",count1,count2)
        else:
            print("Hyperlink is not working ",count1,count2)
            count = count + 1
            self.UR.page_loading(self.driver)
        return count


    def test_districtwise(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        cal = pwd()
        self.fname =file_extention()
        management_name = self.UR.get_management_selected_option()
        count = 0
        self.driver.find_element_by_xpath(self.self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        time.sleep(3)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management_name+'_Infrastructure_Score_allDistricts_'+self.UR.get_current_date()+'.csv'
        self.UR.page_loading(self.driver)
        print(self.filename)
        file = os.path.isfile(self.filename)
        if True == file:
            print('Udise districtwise csv file is downloaded')
        else:
            print('Districtwise csv file is not downloaded ')
            count = count + 1
        self.UR.page_loading(self.driver)
        os.remove(self.filename)
        return count

    def check_download_csv1(self, setup):
        p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        select_cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
        count = 0
        management_name = self.UR.get_management_selected_option()
        self.fname = file_extention()
        for x in range( int(len(select_district.options))-1, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.UR.page_loading(self.driver)
            for y in range(len(select_block.options)-1,len(select_block.options)):
                select_block.select_by_index(y)
                self.UR.page_loading(self.driver)
                time.sleep(2)
                for z in range(1,len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.UR.page_loading(self.driver)
                    time.sleep(2)
                    value = self.driver.find_element_by_id(self.data.Choose_Cluster).get_attribute('value')
                    # values = value[3:]+'_'
                    value = value.split(":")
                    nodata = self.driver.find_element_by_id("errMsg").text
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    if len(markers)-1 == 0:
                            print(select_cluster.options[z].text,"does not contains markers on map")
                    else:
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" +"UDISE_report_"+management_name+"_Infrastructure_Score_schools_of_cluster_"+value[1].strip()+'_'+self.UR.get_current_date()+'.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(select_district.options[x].text,select_block.options[y].text,select_cluster.options[z].text ,"csv file is not downloaded!")
                            count = count + 1
                        schools = self.driver.find_element_by_id('footer').text
                        sc = re.sub('\D','',schools)
                        if len(markers)-1 != int(sc):
                            print('Total no of school mis match found with no of markers ',len(markers),sc)
                            count = count + 1
                        os.remove(self.filename)
        return count

    def test_check_total_schoolvalue(self,setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        try:
            school = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            res = re.sub('\D', "", school)
            self.UR.page_loading(self.driver)

            self.driver.find_element_by_id(self.data.Block_button).click()
            self.UR.page_loading(self.driver)
            bschool = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            bres = re.sub('\D',"",bschool)
            self.UR.page_loading(self.driver)

            self.driver.find_element_by_id(self.data.Cluster_button).click()
            self.UR.page_loading(self.driver)
            time.sleep(10)
            cschool = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            URes = re.sub('\D', "", cschool)
            self.UR.page_loading(self.driver)

            self.driver.find_element_by_id(self.data.School_button).click()
            time.sleep(15)
            sschool = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            sres = re.sub('\D', "", sschool)
            self.UR.page_loading(self.driver)

            return res ,bres ,URes,sres
        except exceptions.ElementClickInterceptedException :
            print("no of schools are same ")
            self.UR.page_loading(self.driver)

    def test_download_blockwise(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        management_name = self.UR.get_management_selected_option()
        self.driver.find_element_by_id(self.data.Block_button).click()
        self.UR.page_loading(self.driver)
        time.sleep(10)
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        self.UR.page_loading(self.driver)
        dots = len(markers)-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(4)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management_name+'_Infrastructure_Score_allBlocks_'+self.UR.get_current_date()+'.csv'
        self.UR.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        os.remove(self.filename)
        return file ,dots

    def test_clusterbtn(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        management_name = self.UR.get_management_selected_option()
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        self.UR.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(dots)-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management_name+'_Infrastructure_Score_allClusters_'+self.UR.get_current_date()+'.csv'
        self.UR.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.UR.page_loading(self.driver)
        os.remove(self.filename)
        return count, file

    def test_click_on_school_btn(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        management_name = self.UR.get_management_selected_option()
        self.driver.find_element_by_id(self.data.School_button).click()
        self.UR.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(dots)-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(20)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management_name+'_Infrastructure_Score_allSchools_'+self.UR.get_current_date() +'.csv'
        self.UR.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.UR.page_loading(self.driver)
        os.remove(self.filename)
        return count, file

    def test_click_blocks(self,setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Block_button).click()
        count = 0
        self.UR.page_loading(self.driver)
        time.sleep(10)
        scores = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        for i in range(1,len(scores.options)-12):
            time.sleep(2)
            scores.select_by_index(i)
            time.sleep(5)
            self.UR.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(markers)-1
            if dots == 0:
                # print(scores.options[i].text , 'does not contains markers on map ')
                count = count + 1
        self.UR.page_loading(self.driver)
        scores.select_by_index(1)
        time.sleep(2)
        return count

    def test_click_clusters(self, setup):
        self.driver.implicitly_wait(30)
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        count = 0
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        self.UR.page_loading(self.driver)
        time.sleep(5)
        scores = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        for i in range(len(scores.options)-12):
            time.sleep(2)
            scores.select_by_index(i)
            # infra_option = scores.options[i].text
            time.sleep(4)
            self.UR.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(markers) - 1
            if dots == 0:
                print('does not contains markers on map ')
                count = count + 1
        self.UR.page_loading(self.driver)
        return count

    #indices downloading functionality
    def infrastructure_score(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.fname = file_extention()
        management_name = self.UR.get_management_selected_option()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(1)
        self.UR.page_loading(self.driver)
        row_count = 0
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[1].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management_name+'_Infrastructure_Score_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            print(self.filename)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("infrastructure_score  is selected and csv file is downloaded")
            return row_count-1


    def administation(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(2)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[2].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Administration_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            row_count = 0
            if True != file:
                print('csv file not downloaded')
            else:

                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Administration is selected and csv file is downloaded")
            return row_count - 1

    def artslab(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(3)
        row_count = 0
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[3].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Arts_Lab_Index_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("artslab  is selected and csv file is downloaded")
            return row_count - 1

    def community(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        row_count = 0
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        time.sleep(3)
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(4)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[4].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Community_Participation_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:

                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Community  is selected and csv file is downloaded")
            return row_count - 1

    def Enrollment(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(5)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[5].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Enrollment_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Enrollment  is selected and csv file is downloaded")
            return row_count - 1

    def grant_expenditure(self,setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(6)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[6].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Grant_Expenditure_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Grant expenditure is selected and csv file is downloaded")
            return row_count - 1

    def ictlab(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(7)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[7].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_ICT_Lab_Index_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("ICTlab  is selected and csv file is downloaded")
            return row_count - 1

    def Medical(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(8)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[8].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Medical_Index_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Medical is selected and csv file is downloaded")
            return row_count - 1

    def nsqf(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(9)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[9].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_NSQF_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("nsqf is selected and csv file is downloaded")
            return row_count - 1

    def policy(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(10)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[10].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Policy_Implementation_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Policy is selected and csv file is downloaded")
            return row_count - 1

    def Safety(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(11)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[11].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Safety_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Safety  is selected and csv file is downloaded")
            return row_count - 1

    def School_infrastructure(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(12)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[12].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Infrastructure_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("School infrastructure is selected and csv file is downloaded")
            return row_count - 1

    def School_inspection(self,setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(13)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[13].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Inspection_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("school inspection  is selected and csv file is downloaded")
            return row_count - 1

    def School_perfomance(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(14)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[14].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Performance_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:

                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("School performance is selected and csv file is downloaded")
            return row_count - 1

    def Science_lab(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(15)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[15].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Science_Lab_Index_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Science lab is selected and csv file is downloaded")
            return row_count - 1

    def Teacher_profile(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        row_count = 0
        management = self.UR.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        chooseinfra.select_by_index(16)
        self.UR.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[16].text,'is not having data')
        else:
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Teacher_Profile_allDistricts_'+self.UR.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Teachers profile is selected and csv file is downloaded")
            chooseinfra.select_by_index(1)
            time.sleep(2)
        return row_count - 1

    def remove_csv(self):
        os.remove(self.filename)

    def test_download(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        cal = pwd()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        managmemnt =self.driver.find_element_by_id('name').text
        manage = managmemnt[16:]+''
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        self.UR.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        count =len(dots)-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(5)
        self.file = file_extention()
        self.filename = cal.get_download_dir() + '/' + self.file.udise_cluster()+(manage.lower()).strip()+'_Infrastructure_Score_allClusters_'+self.UR.get_current_date()+'.csv'
        self.UR.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        os.remove(self.filename)
        return file,count


    def test_districtwise_schools_count(self, setup):
        p = pwd()
        count = 0
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.implicitly_wait(30)
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.UR.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            if len(markers)-1 == 0:
                print(select_district.options[x].text,"has no data on map")
            else:
                count = 0
                schools = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
                sc = re.sub('\D', "", schools)
                if int(sc) == 0:
                    print(select_district.options[x],'has no no of school count')
                    count = count + 1
                time.sleep(2)

        return count


    def test_mousehover(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(markers)-1
        print("Mousehover on each markers..")
        self.UR.test_mouse_over()
        self.UR.page_loading(self.driver)
        return count


    def test_click_schools(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        self.UR.page_loading(self.driver)
        count = 0
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.School_button).click()
        time.sleep(15)
        scores = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        for i in range(1,len(scores.options)):
            # scores.select_by_index(i)
            print(scores.options[i].text,"is selected as indices")
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(markers) - 1
            if dots == 0:
                print(scores.options[i].text, 'does not contains markers on map ')
                count = count + 1
        self.UR.page_loading(self.driver)
        return count

    def test_district(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id('block').click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        print("home icon is working ")
        self.UR.page_loading(self.driver)


    def test_schools(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(2, len(select_district.options)):
            select_district.select_by_index(x)
            # print(select_district.options[x].text)
            self.UR.page_loading(self.driver)
            for y in range(1,len(select_block.options)):
                select_block.select_by_index(y)
                self.UR.page_loading(self.driver)
                nodata = self.driver.find_element_by_id("errMsg").text
                if nodata == "No data found":
                    print(select_district.options[x].text, "no data found!")
                    count = count + 1
                else:
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    if len(markers)-1 != 0:
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(4)
                        self.filename = p.get_download_dir() + "/Cluster_per_block_report.csv"
                        if not os.path.isfile(self.filename):
                            print(select_block.options[y].text,"csv is not dowloaded")
                            count = count + 1
                        # else:
                        #     with open(self.filename) as fin:
                        #         csv_reader = csv.reader(fin, delimiter=',')
                        #         header = list(csv_reader)
                        #         data = len(header)
                        #         # total = 0
                        #         # schools = 0
                        #         # for row in csv.reader(fin):
                        #         #     schools += int(row[2])
                        #         school = self.driver.find_element_by_id("schools").text
                        #         sc= re.sub('\D', "", school)
                        #         if int(sc) != header:
                        #             print(select_block.options[y].text,"schools:",header ,int(sc) ,"mismatch found" )
                        #         time.sleep(2)
                            os.remove(self.filename)
            return count

    def test_each_districtwise(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        managment_name = self.driver.find_element_by_id('name').text
        name = managment_name[16:].strip().lower()
        time.sleep(2)
        Districts = Select(self.driver.find_element_by_id('choose_dist'))
        self.UR.page_loading(self.driver)
        count = 0
        for i in range(1,len(Districts.options)-10):
            Districts.select_by_index(i)
            self.UR.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value.split(":")
            dist_name = Districts.options[i].text
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            marker_value = len(markers)-1
            self.UR.page_loading(self.driver)
            if marker_value == 0 or 'no data found' in self.driver.page_source:
                print(Districts.options[i].text , " does not have markers on map")
                count = count + 1
            else:
                cal = pwd()
                self.driver.find_element_by_id(self.data.Downloads).click()
                time.sleep(2)
                self.filename = cal.get_download_dir() + '/' +"UDISE_report_"+name +"_Infrastructure_Score_blocks_of_district_"+value[1].strip()+'_'+self.UR.get_current_date()+'.csv'
                print(self.filename)
                self.UR.page_loading(self.driver)
                if not os.path.isfile(self.filename):
                    print(dist_name," csv is not downloaded")
                    count = count + 1
                # else:
                #     df = pd.read_csv(self.filename)
                #     schools = df['']
                #     school = self.driver.find_element_by_id("schools").text
                #     sc = re.sub('\D', "", school)
                #     if int(sc) != int(schools):
                #         print("school count mismatched")
                #         count = count + 1
                os.remove(self.filename)

        return count

    def test_map(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        self.UR.page_loading(self.driver)
        count = len(dots)-1
        return count

    def test_dashboard(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.sch_infra).click()
        self.UR.page_loading(self.driver)
        self.driver.find_element_by_id(Data.udise_report).click()
        self.UR.page_loading(self.driver)
        count = 0
        if 'udise-report' in self.driver.current_url:
            print('UDISE map report is displayed')
        else:
            print('UDISE map report is not displayed')
            count = count + 1
        return count
