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


class CompositeReport:
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

    def login(self, username, password):
        self.data = Locator_Path()
        self.driver.maximize_window()
        self.driver.find_element_by_id(self.data.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(password)
        self.driver.find_element_by_id(self.data.Submit_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.data.cQube_Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.data.Compositereport).click()

    def HyperLink(self):
        self.data = Locator_Path()
        Hyperlink = self.driver.find_element_by_id(self.data.Hyperlink).text
        return Hyperlink

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


    def test_menulist(self,setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.cQube_logo).click()
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.sch_infra).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.data.Compositereport).click()
        self.CR.page_loading(self.driver)

    def test_districtwise(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.fname = file_extention()
        self.driver.implicitly_wait(20)
        management_name = self.CR.get_management_selected_option()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        p =pwd()
        count = 0
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(1)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        self.CR.page_loading(self.driver)
        time.sleep(10)
        self.filename = p.get_download_dir() + "/" + self.fname.sc_district()+management_name+'_allDistricts_'+self.CR.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count + 1
        else:
            print('District level file is downloaded')
            os.remove(self.filename)
        return count

    def test_block(self,setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.driver.implicitly_wait(20)
        self.fname = file_extention()
        management_name = self.CR.get_management_selected_option()
        self.CR.page_loading(self.driver)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(2)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(15)
        count=0
        self.filename = p.get_download_dir() + "/"+ self.fname.sc_block()+management_name+'_allBlocks_'+self.CR.get_current_date()+'.csv'
        print(self.filename)
        self.CR.page_loading(self.driver)
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count +1
        else:
            print('Block level file is downloaded')
            os.remove(self.filename)
        return count


    def test_clusterwise(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.fname = file_extention()
        management_name = self.CR.get_management_selected_option()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(3)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(15)
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.sc_cluster()+management_name+'_allClusters_'+self.CR.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count + 1
        else:
            print('Cluster level file is downloaded')
            os.remove(self.filename)
        return count

    def test_schoolwise(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.fname =file_extention()
        management_name = self.CR.get_management_selected_option()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        try:
            p = pwd()
            District_wise=Select(self.driver.find_element_by_name("downloadType"))
            District_wise.select_by_index(4)
            self.CR.page_loading(self.driver)
            self.driver.find_element_by_id(self.data.Downloads).click()
            self.CR.page_loading(self.driver)
            time.sleep(30)
            self.filename = p.get_download_dir() + "/" + self.fname.sc_school()+management_name+'_allSchools_'+self.CR.get_current_date()+'.csv'
            time.sleep(10)
            count = 0
            if os.path.isfile(self.filename) != True:
                print('File is not downloaded ')
                count = count + 1
            else:
                print('School level file is downloaded')
                os.remove(self.filename)
            return count

        except exceptions.NoSuchElementException:
            print("school wise csv downloaded")

    def navigate_to_composite_infrastructure(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(self.data.menu_icon).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.data.sch_infra).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.data.Compositereport).click()
        time.sleep(3)

    def test_homebtn(self, setup):
        count = 0
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.cQube_logo).click()
        self.CR.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print("Dashboard Page is displayed ")
        else:
            print('cQube logo is not working ')
            count = count + 1
        self.CR.navigate_to_composite_infrastructure()
        self.CR.page_loading(self.driver)
        return count

    def test_tablevalue(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.d_names).click()
        self.CR.page_loading(self.driver)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        self.CR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.d_names).click()
        self.CR.page_loading(self.driver)
        value = self.driver.find_elements_by_xpath("//th[1]")
        for i in value:
            print(i.get_attribute("aria-sort"))


    def remove_csv1(self):
        os.remove(self.filename)

    def check_csv_download1(self, setup):
        p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.fname =file_extention()
        self.driver.implicitly_wait(50)
        management_name = self.CR.get_management_selected_option()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        select_cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
        count = 0
        for x in range(int(len(select_district.options))-1, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.CR.page_loading(self.driver)
            print(select_district.options[x].text)
            for y in range(len(select_block.options)-3, len(select_block.options)):
                select_block.select_by_index(y)
                self.CR.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.CR.page_loading(self.driver)
                    value = self.driver.find_element_by_name('myCluster').get_attribute('value')
                    cvalue = value.split(":")
                    value = cvalue[1].strip()
                    nodata = self.driver.find_element_by_id("errMsg").text
                    if nodata == "No data found":
                        print(select_district.options[x].text,select_block.options[y],select_cluster.options[z].text, "no data found!")
                        count = count + 1
                    else:
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" + self.fname.sc_clusterwise()+management_name+'_schools_of_cluster_'+ value+'_'+self.CR.get_current_date()+".csv"
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(select_cluster.options[z].text,"csv is not downloaded..")
                        else:
                            with open(self.filename) as fin:
                                csv_dict = [row for row in csv.DictReader(self.filename)]
                                if len(csv_dict) == 0:
                                    print(select_district.options[z].text,"does not contain Table records")
                            os.remove(self.filename)
                            self.CR.page_loading(self.driver)
            return  count



    def test_table_data(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        try:
            select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
            count = 0
            for k in range(len(select_district.options) - 5, len(select_district.options)):
                select_district.select_by_index(k)
                self.CR.page_loading(self.driver)
                print(select_district.options[k].text)
                table_data = []

                li2 = self.driver.find_elements_by_xpath('//*[@id="table"]/tbody/tr')
                for x in li2:
                    table_data_rows = x.text
                    table_data_rows = table_data_rows.split()
                    table_data.append(table_data_rows)

                for i in range(len(table_data)):
                    for j in range(len(table_data[i])):
                        if table_data[i][j].isalpha() and table_data[i][j + 1].isalpha():
                            table_data[i][j] = table_data[i][j] + table_data[i][j + 1]

                for x in range(len(table_data)):
                    for y in range(len(table_data[x])):
                        if table_data[x][y].isalpha() and table_data[x][y + 1].isalpha():
                            del (table_data[x][y + 1])
                        break
                df = pd.DataFrame(table_data)
                index = df.index
                number_of_rows = len(index)
                table_data.clear()
                if number_of_rows == 0:
                    count = count + 1
                    print("District" + select_district.first_selected_option.text + "table data not found")
                else:
                    print("Tables having Records...")
        finally:
            print("Records are present...")
        time.sleep(3)
        return count

    def test_xplots(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        try:
            x_axis = Select(self.driver.find_element_by_id(self.data.x))
            y_axis = Select(self.driver.find_element_by_id(self.data.y))
            self.CR.page_loading(self.driver)
            for x in range(1, len(x_axis.options)):
                x_axis.select_by_index(x)
                self.CR.page_loading(self.driver)
            for y in range(1, len(y_axis.options)):
                    y_axis.select_by_index(y)
                    self.CR.page_loading(self.driver)
        except exceptions.NoSuchElementException:
            print("Both x and y axis are selectable ")

    def test_yaxis(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        try:
            y_axis = Select(self.driver.find_element_by_id(self.data.y))
            self.CR.page_loading(self.driver)
            for y in range(1, len(y_axis.options)):
                y_axis.select_by_index(y)
                self.CR.page_loading(self.driver)
        except exceptions.NoSuchElementException:
            print("Both x and y axis are selectable ")


    def test_district(self, setup):
        p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.fname =file_extention()
        management_name = self.CR.get_management_selected_option()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(len(select_district.options)-4, len(select_district.options)):
            select_district.select_by_index(x)
            self.CR.page_loading(self.driver)
            value = self.driver.find_element_by_name('myDistrict').get_attribute("value")
            blkval =value.split(":")
            val = blkval[1].strip()
            nodata = self.driver.find_element_by_id("errMsg").text
            if nodata == "No data found":
                print(select_district.options[x].text, "no data found!")
            else:
                self.driver.find_element_by_id(self.data.Downloads).click()
                time.sleep(3)
                self.filename = p.get_download_dir() + "/" + self.fname.sc_districtwise()+management_name+'_blocks_of_district_'+(val+'_').strip()+self.CR.get_current_date()+'.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print(select_district.options[x].text , " csv file is not downloaded")
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_dict = [row for row in csv.DictReader(self.filename)]
                        if len(csv_dict) == 0:
                            print(select_district.options[x].text,'csv file is empty')
                    os.remove(self.filename)
        return count

    def test_blockwise(self, setup):
        p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.fname =file_extention()
        self.driver.implicitly_wait(60)
        management_name = self.CR.get_management_selected_option()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            self.CR.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                self.CR.page_loading(self.driver)
                value = self.driver.find_element_by_name('myBlock').get_attribute('value')
                cval = value.split(":")
                sval = cval[1].strip()
                nodata = self.driver.find_element_by_id("errMsg").text
                if nodata == "No data found":
                    print(select_block.options[y].text, "no data found!")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + "/" + self.fname.sc_blockwise()+management_name+'_clusters_of_block_'+(sval+'_').strip()+self.CR.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(select_block.options[y].text,"csv file is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_dict = [row for row in csv.DictReader(self.filename)]
                            if len(csv_dict) == 0:
                                print(select_district.options[y].text,"Does not have Table records")
                        os.remove(self.filename)
        return count

    def test_cluster(self, setup):
        p = pwd()
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        self.CR.page_loading(self.driver)
        self.fname =file_extention()
        self.driver.implicitly_wait(60)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.CR.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            self.CR.page_loading(self.driver)
            for y in range(len(select_block.options) - 1, len(select_block.options)):
                select_block.select_by_index(y)
                self.CR.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.CR.page_loading(self.driver)
                    value = self.driver.find_element_by_id(self.data.Choose_Cluster).get_attribute('value')
                    cval = value.split(":")
                    sval = cval[1].strip()
                    nodata = self.driver.find_element_by_id("errMsg").text
                    if nodata == "No data found":
                        print(select_cluster.options[z].text, "no data found!")
                        count = count + 1
                    else:
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" + self.fname.sc_clusterwise()+management+'_schools_of_cluster_'+(sval+'_').strip()+self.CR.get_current_date()+'.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(select_cluster.options[z].text,"csv file is not downloaded")
                            count = count + 1
                        else:
                            with open(self.filename) as fin:
                                csv_dict = [row for row in csv.DictReader(self.filename)]
                                if len(csv_dict) == 0:
                                    print(select_district.options[y].text,"Does not have Table records")
                            os.remove(self.filename)
        return count