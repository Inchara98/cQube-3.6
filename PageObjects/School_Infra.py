import csv
import os
import re
import time
from datetime import date

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path
from filenames import file_extention
from get_dir import pwd
from utilities.readProperties import ReadConfig
from selenium.common import exceptions


class SchoolInfra:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.data = Locator_Path()
        self.driver.maximize_window()
        self.driver.find_element_by_id(self.data.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(password)
        self.driver.find_element_by_id(self.data.Submit_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.data.cQube_Dashboard).click()
        time.sleep(3)

    def Backbutton(self):
        self.data = Locator_Path()
        back = self.driver.find_element_by_id(self.data.BackButton)
        return back

    def logout(self):
        self.data = Locator_Path()
        Logout = self.driver.find_element_by_id(self.data.logoutbutton)
        return Logout

    def InfraMap(self):
        self.data = Locator_Path()
        Infra = self.driver.find_element_by_id(self.data.InfraMap)
        return Infra

    def HyperLink(self):
        self.data = Locator_Path()
        Hyperlink = self.driver.find_element_by_id(self.data.Hyperlink).text
        return Hyperlink

    def Blockbutton(self):
        self.data = Locator_Path()
        Block = self.driver.find_element_by_id(self.data.Block_button)
        return Block

    def Clusterbutton(self):
        self.data = Locator_Path
        Cluster = self.driver.find_element_by_id(self.data.Cluster_button)
        return Cluster

    def Schoolbutton(self):
        self.data = Locator_Path
        School = self.driver.find_element_by_id(self.data.School_button)
        return School

    def ChooseInfra(self):
        self.data = Locator_Path
        Infra = Select(self.driver.find_element_by_id(self.data.Choose_Infra))
        return Infra

    def Choosedist(self):
        self.data = Locator_Path
        Dist = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        return Dist

    def Chooseblock(self):
        self.data = Locator_Path
        Block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        return Block

    def Choosecluster(self):
        self.data = Locator_Path
        Cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
        return Cluster

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

    def test_Block_button(self, setup):
        # self.logger.info("********************verifying Hyperlink Test********************************")
        self.driver = setup
        self.data = Locator_Path
        cal = pwd()
        self.fname = file_extention()
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(5)
        self.SI.InfraMap().click()
        time.sleep(5)
        management_name = self.SI.get_management_selected_option()
        self.SI.Blockbutton().click()
        self.SI.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(dots) - 1
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + "/" + self.fname.scmap_block() + management_name + '_allBlocks_' + self.SI.get_current_date() + '.csv'
        print(self.filename)
        self.SI.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        if file == True:
            print(self.filename, "File is downloaded ")
            os.remove(self.filename)
        else:
            print("File not downloaded ")
        self.SI.page_loading(self.driver)
        return count, file

    def test_Cluster_button(self, setup):
        # self.logger.info("********************verifying Hyperlink Test********************************")
        self.driver = setup
        self.data = Locator_Path
        cal = pwd()
        self.fname = file_extention()
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(5)
        self.SI.InfraMap().click()
        time.sleep(5)
        management_name = self.SI.get_management_selected_option()
        self.SI.Clusterbutton().click()
        self.SI.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(dots) - 1
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + "/" + self.fname.scmap_cluster() + management_name + '_allClusters_' + self.SI.get_current_date() + '.csv'
        print(self.filename)
        self.SI.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        if file == True:
            print(self.filename, "File is downloaded ")
            os.remove(self.filename)
        else:
            print("File not downloaded ")
        self.SI.page_loading(self.driver)
        return count, file

    def test_School_button(self, setup):
        # self.logger.info("********************verifying Hyperlink Test********************************")
        self.driver = setup
        self.data = Locator_Path
        cal = pwd()
        self.fname = file_extention()
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        management_name = self.SI.get_management_selected_option()
        self.SI.Schoolbutton().click()
        self.SI.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(dots) - 1
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + "/" + self.fname.scmap_school() + management_name + '_allSchools_' + self.SI.get_current_date() + '.csv'
        print(self.filename)
        self.SI.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        if file == True:
            print(self.filename, "File is downloaded ")
            os.remove(self.filename)
        else:
            print("File not downloaded ")
        self.SI.page_loading(self.driver)
        return count, file

    def test_check_total_schoolvalue(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SI.page_loading(self.driver)
        try:
            school = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            res = re.sub('\D', "", school)
            self.SI.page_loading(self.driver)

            self.driver.find_element_by_id(self.data.Block_button).click()
            self.SI.page_loading(self.driver)
            bschool = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            bres = re.sub('\D', "", bschool)
            self.SI.page_loading(self.driver)

            self.driver.find_element_by_id(self.data.Cluster_button).click()
            self.SI.page_loading(self.driver)
            time.sleep(10)
            cschool = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            cres = re.sub('\D', "", cschool)
            self.SI.page_loading(self.driver)

            self.driver.find_element_by_id(self.data.School_button).click()
            time.sleep(15)
            sschool = self.driver.find_element_by_id(self.data.sc_no_of_schools).text
            sres = re.sub('\D', "", sschool)
            self.SI.page_loading(self.driver)

            return res, bres, cres, sres
        except exceptions.ElementClickInterceptedException:
            print("no of schools are same ")
            self.SI.page_loading(self.driver)

    def test_infrascores(self,setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        a = self.driver.find_element_by_xpath(self.data.hyper_link)
        a.click()
        self.SI.page_loading(self.driver)
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        count = len(chooseinfra.options)-1
        self.SI.page_loading(self.driver)
        for x in range(1, len(chooseinfra.options)):
            chooseinfra.select_by_index(x)
            print(chooseinfra.options[x].text ,'is selected')
            self.SI.page_loading(self.driver)
        return count

    def remove_csv(self):
        os.remove(self.filename)

    def infra_score_dropdown(self,setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        self.driver.find_element_by_css_selector('p >span').click()
        self.SI.page_loading(self.driver)
        management_name = self.SI.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(1)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Infra score percentage is selected and csv file is download")
        return row_count-1


    def Access_to_toilet(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(2)
        self.SI.page_loading(self.driver)
        management_name = self.SI.get_management_selected_option()
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Access to toilet percentage is selected and csv file is downloaded")
        return row_count-1

    def Access_to_water(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(3)
        self.SI.page_loading(self.driver)
        management_name = self.SI.get_management_selected_option()
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Access to water percentage is selected and csv file is downloaded")
        return row_count-1

    def Boys_toilet_percentage(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(4)
        self.SI.page_loading(self.driver)
        management_name = self.SI.get_management_selected_option()
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Boy's toilet percentage is selected and csv file is downloaded")
        return row_count-1

    def drinking_water(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(5)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Drinking water percentage is selected and csv file is downloaded")
        return row_count-1

    def Electricity(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(6)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Electricity percentage is selected and csv file is downloaded")
        return row_count-1

    def girls_toilet(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(7)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("girls toilet percentage is selected and csv file is downloaded")
        return row_count-1

    def Handpump(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(8)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Hand pump percentage is selected and csv file is downloaded")
        return row_count-1

    def Handwash(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(9)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Handwash percentage is selected and csv file is downloaded")
        return row_count-1

    def Library(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(10)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Library percentage is selected and csv file is downloaded")
        return row_count-1

    def Solar_panel(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(11)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("solar panel percentage is selected and csv file is downloaded")
        return row_count-1

    def Tapwater(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(12)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Tapwater percentage is selected and csv file is downloaded")
        return row_count-1

    def Toilet(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(13)
        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(2)
        p = pwd()
        management_name = self.SI.get_management_selected_option()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        row_count = 0
        with open(self.filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Toilet percentage is selected and csv file is downloaded")
        return row_count-1

    def test_download(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        cal = pwd()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SI.page_loading(self.driver)
        management_name = self.SI.get_management_selected_option()
        time.sleep(2)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' + self.fname.scmap_district()+management_name+'_allDistricts_'+self.SI.get_current_date()+'.csv'
        self.SI.page_loading(self.driver)
        if not os.path.isfile(self.filename):
            print("Districtwise csv is not downloaded")
            count = count + 1
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                schools = 0
                for row in csv.reader(fin):
                    schools += int(row[0])
                school = self.driver.find_element_by_id("schools").text
                sc = re.sub('\D', "", school)
                if int(sc) != int(schools):
                    print("school count mismatched")
                    count = count + 1
            os.remove(self.filename)
        return  count

    def check_download_csv1(self, setup):
        p = pwd()
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.fname = file_extention()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SI.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        for x in range(int(len(select_district.options))-1, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.SI.page_loading(self.driver)
            for y in range(len(select_block.options)-1,len(select_block.options)):
                select_block.select_by_index(y)
                self.SI.page_loading(self.driver)
                for z in range(1,len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.SI.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value.split(":")
                    nodata = self.driver.find_element_by_id("errMsg").text
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    if len(markers)-1 == 0:
                            print(select_cluster.options[z].text,"does not contains markers on map")
                    else:
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" + self.fname.scmap_clusterwise()+name+'_schools_of_cluster_'+value[1].strip()+'_'+self.SI.get_current_date()+'.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(select_cluster.options[z].text ,"csv file is not downloaded!")
                            count = count+1
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin)
                                data = list(csv_reader)
                                countrecords =len(data)
                                # header = next(csv_reader)
                                # total = 0
                                # for row in csv.reader(fin):
                                #     total += int(row[2])
                                school = self.driver.find_element_by_id("schools").text
                                sc= re.sub('\D', "", school)
                                if int(sc) != int(countrecords)-1:
                                    print(select_block.options[y].text, "schools:", int(countrecords)-1, int(sc), "mismatch found")
                                    count = count + 1
                            os.remove(self.filename)
        return count


    def test_home(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SI.page_loading(self.driver)

        self.driver.find_element_by_id(self.data.Block_button).click()
        self.SI.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        self.SI.page_loading(self.driver)
        count1 = len(dots) - 1

        self.SI.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        self.SI.page_loading(self.driver)
        time.sleep(20)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        self.SI.page_loading(self.driver)
        count2 = len(dots) - 1
        self.SI.page_loading(self.driver)

        self.driver.find_element_by_id(self.data.School_button).click()
        self.SI.page_loading(self.driver)
        time.sleep(30)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        self.SI.page_loading(self.driver)
        count3 = len(dots) - 1
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SI.page_loading(self.driver)
        return count1 , count2 ,count3

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

    def test_mousehover(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SI.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        count = len(markers)-1
        print("Mousehover on each markers..")
        self.SI.test_mouse_over()
        self.SI.page_loading(self.driver)
        return count

    def block_disable(self, setup):
        self.driver = setup
        self.data = Locator_Path
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.SI.Choosedist().select_by_index(1)



