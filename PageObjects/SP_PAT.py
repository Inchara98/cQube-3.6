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


class PATReport:
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
        self.driver.find_element_by_id(self.data.PAT).click()
        time.sleep(5)

    def click_download_icon(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        count =0
        management = self.SP.get_management_selected_option()
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.pat_district()+management+'_all_allGrades__allDistricts_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(markers)-1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                # total = 0
                # schools = 0
                # for row in csv.reader(fin):
                #     total += int(row[2])
                #     schools += int(row[3])
                # students = self.driver.find_element_by_id("students").text
                # res = re.sub('\D', "", students)
                #
                # school = self.driver.find_element_by_id("schools").text
                # sc = re.sub('\D', "", school)
                # if int(res) != total:
                #     print("student count mismatched")
                #     count = count + 1
                # if int(sc) != schools:
                #     print("school count mismatched")
                #     count = count + 1
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched",dots,row_count)
                    count = count + 1
            os.remove(self.filename)
        return count



    def check_with_block_footervalues(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        files = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(self.data.Block_button).click()
        self.SP.page_loading(self.driver)
        marker = self.driver.find_elements_by_class_name(self.data.markers)
        counts = len(marker ) -1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(5)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/"+files.pat_block()+management+'_all_allGrades__allBlocks_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(markers) - 1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return counts , count


    def check_with_cluster_footervalues(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        files = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        self.SP.page_loading(self.driver)
        marker = self.driver.find_elements_by_class_name(self.data.markers)
        counts = len(marker ) -1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(5)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/"+files.pat_block()+management+'_all_allGrades__allClusters_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(markers) - 1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return counts , count

    def check_with_schoolfooters(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(self.data.School_button).click()
        time.sleep(20)
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        dots = len(markers )-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(15)
        p = pwd()
        count = 0
        files= file_extention()
        self.filename = p.get_download_dir() + "/" + files.pat_school()+management+'_all_allGrades__allSchools_'+self.SP.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(markers) - 1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return dots , count

    global student_count


    def block_cluster_schools_footer_info(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)

        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        time.sleep(4)
        schools = self.driver.find_element_by_id('schools').text
        scs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        stds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        attds = re.sub('\D', "", attended)

        print('Expected Footer values : ', scs, stds, attds)
        "********************Block level Records *******************"
        self.driver.find_element_by_id(self.data.Block_button).click()
        self.SP.page_loading(self.driver)

        schools = self.driver.find_element_by_id('schools').text
        bscs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        bstds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        battds = re.sub('\D', "", attended)
        count = 0
        if scs != bscs:
            print('Block level schools count mismatch found', 'fi:' + scs, bscs)
            count = count + 1
        if stds != bstds:
            print('Block level students count mismatch found', stds, bstds)
            count = count + 1
        if attds != battds:
            print('Block level schools count mismatch found', attds, battds)
            count = count + 1
        "********************Cluster level Records *******************"
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        # cal = GetData()
        self.SP.page_loading(self.driver)
        time.sleep(10)
        schools = self.driver.find_element_by_id('schools').text
        cscs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        cstds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        cattds = re.sub('\D', "", attended)
        if scs != cscs:
            print('Cluster level schools count mismatch found', scs, cscs)
            count = count + 1
        if stds != cstds:
            print('Cluster level students count mismatch found', stds, cstds)
            count = count + 1
        if attds != cattds:
            print('Cluster level schools count mismatch found', attds, cattds)
            count = count + 1
        "********************School level Records *******************"
        self.driver.find_element_by_id(self.data.School_button).click()
        # cal = GetData()
        self.SP.page_loading(self.driver)
        time.sleep(10)
        schools = self.driver.find_element_by_id('schools').text
        sscs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        sstds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        sattds = re.sub('\D', "", attended)

        if scs != sscs:
            print('School level schools count mismatch found', scs, sscs)
            count = count + 1
        if stds != sstds:
            print('School level students count mismatch found', stds, sstds)
            count = count + 1
        if attds != sattds:
            print('School level schools count mismatch found', attds, sattds)
            count = count + 1

        return count

    def click_on_blocks_click_on_home_icon(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Block_button).click()
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)



    def click_on_hyperlinks(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        time.sleep(3)
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

    def pat_year_month_firstselected(self):
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        year = year.first_selected_option.text
        month = month.first_selected_option.text
        return year , month


    def check_district(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        time.sleep(3)
        self.year ,self.month = self.SP.pat_year_month_firstselected()
        self.SP.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.SP.page_loading(self.driver)
            value = self.driver.find_element_by_id(self.data.Choose_Dist).get_attribute('value')
            value = value.split(":")
            markers = self.driver.find_elements_by_class_name(self.data.markers)
            time.sleep(3)
            if (len(markers)- 1) == 0 :
                print("District" + select_district.first_selected_option.text +"no data")
                count = count + 1
            else :
                self.driver.find_element_by_id(self.data.Downloads).click()
                time.sleep(4)
                p = pwd()
                file =file_extention()
                self.filename = p.get_download_dir() + "/"+file.pat_districtwise()+management+"_"+self.year+'_'+self.month+'_allGrades__blocks_of_district_'+value[1].strip()+'_'+self.SP.get_current_date()+'.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                    count = count + 1
                else:
                    values = pd.read_csv(self.filename)

                    school = values['Total Schools'].sum()
                    students = values['Total Students'].sum()
                    attend = values['Students Attended'].sum()

                    schools = self.driver.find_element_by_id('schools').text
                    scs = re.sub('\D', '', schools)

                    student = self.driver.find_element_by_id('students').text
                    stds = re.sub('\D', '', student)

                    attended = self.driver.find_element_by_id('studentsAttended').text
                    attds = re.sub('\D', '', attended)
                    print(school,scs,students,stds,attend,attds)

                    if int(scs) != school:
                        print("schools count in footer and csv file records count mismatched", int(scs),
                              int(schools))
                        count = count + 1

                    if int(stds) != students:
                        print("student count in footer and csv file records count mismatched", int(scs),
                              int(schools))
                        count = count + 1

                    if int(attds) != attend:
                        print("Attended count in footer and csv file records count mismatched", int(scs),
                              int(schools))
                        count = count + 1

                os.remove(self.filename)
            return count

    def remove_csv(self):
        os.remove(self.filename)

    def check_district_block_cluster(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.driver.implicitly_wait(50)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        self.SP.page_loading(self.driver)
        self.year ,self.month = self.SP.pat_year_month_firstselected()
        self.fname = file_extention()
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        select_cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
        count = 0
        for x in range(len(select_district.options)-1,len(select_district.options)):
            select_district.select_by_index(x)
            self.SP.page_loading(self.driver)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                self.SP.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.SP.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value.split(":")
                    time.sleep(3)
                    nodata = self.driver.find_element_by_id("errMsg").text
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(3)
                    p = pwd()
                    self.filename = p.get_download_dir() +"/" + self.fname.pat_clusterwise()+management+"_"+self.year+'_'+self.month+'_allGrades__schools_of_cluster_'+value[1].strip()+'_'+self.SP.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                         values = pd.read_csv(self.filename)

                         school = values['Total Schools'].sum()
                         students = values['Total Students'].sum()
                         attend = values['Students Attended'].sum()

                         schools = self.driver.find_element_by_id('schools').text
                         scs = re.sub('\D', '', schools)

                         student = self.driver.find_element_by_id('students').text
                         stds = re.sub('\D', '', student)

                         attended = self.driver.find_element_by_id('studentsAttended').text
                         attds = re.sub('\D', '', attended)

                         print(school,scs,students,stds,attend,attds)

                         if  int(scs) != school:
                             print("schools count in footer and csv file records count mismatched", int(scs),
                                   int(schools))
                             count = count + 1

                         if  int(stds) != students:
                             print("student count in footer and csv file records count mismatched", int(scs),
                                   int(schools))
                             count = count + 1

                         if  int(attds) != attend:
                             print("Attended count in footer and csv file records count mismatched", int(scs),
                                   int(schools))
                             count = count + 1

                    os.remove(self.filename)
            return count


    def check_grade_dropdown_options(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grade =Select(self.driver.find_element_by_id(self.data.Grade))
        counter = len(grade.options)
        for i in range(1,len(grade.options)):
            grade.select_by_index(i)
            print(grade.options[i].text)
            self.SP.page_loading(self.driver)
        return counter

    def click_each_grades(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.driver.implicitly_wait(50)
        count = 0
        p = pwd()
        files = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        grade =Select(self.driver.find_element_by_id(self.data.Grade))
        for i in range(1,len(grade.options)-2):
            grade.select_by_index(i)
            gradename = (grade.options[i].text).strip()
            gradenum = re.sub('\D','',gradename)
            dots = self.driver.find_elements_by_class_name(self.data.markers)
            markers = len(dots)-1
            self.SP.page_loading(self.driver)
            self.driver.find_element_by_id(self.data.Downloads).click()
            time.sleep(3)
            self.filename = p.get_download_dir() + '/'+ files.pat_gradewise()+management.strip()+'_all_Grade '+gradenum.strip()+'__allDistricts_'+self.SP.get_current_date()+'.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('District wise csv file is not downloaded')
                count = count + 1
            else:
                file = open(self.filename)
                read = file.read()
                if grade.options[i].text in read:
                    print(grade.options[i].text ,"is present")
                self.SP.page_loading(self.driver)
            os.remove(self.filename)
        self.SP.page_loading(self.driver)
        return count

    def select_subjects_dropdown(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        grade = Select(self.driver.find_element_by_id(self.data.Grade))
        subjects = Select(self.driver.find_element_by_id(self.data.Subject))
        subcount = len(subjects.options)-1
        files = file_extention()
        for i in range(1,len(grade.options)):
            grade.select_by_index(i)
            self.SP.page_loading(self.driver)
            gradename = grade.options[i].text.strip()
            gradenum = re.sub('\D','',gradename)
            for j in range(len(subjects.options)-1,len(subjects.options)):
                subjects.select_by_index(j)
                self.SP.page_loading(self.driver)
                sub = (subjects.options[j].text).strip()
                if "No data found" in self.driver.page_source:
                    print("No data found ")
                else:
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + '/' + files.pat_gradewise()+management+'_all_Grade '+gradenum.strip()+'_'+sub+'_allDistricts_' + self.SP.get_current_date()+'.csv'
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print('grade wise wise csv file is not downloaded')
                        count = count+1
                    else:
                        file = open(self.filename)
                        read = file.read()
                        if grade.options[j].text in read:
                            print(grade.options[j].text, "is present")
                        self.SP.page_loading(self.driver)
                    os.remove(self.filename)
            return count

    def test_options_times(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        count = len(times.options)
        print(count)
        return count

    def time_over_all(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        p = pwd()
        count =0
        management = self.SP.get_management_selected_option()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        dist =Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        times = Select(self.driver.find_element_by_id('period'))
        for i in range(1,len(times.options)):
            times.select_by_index(i)
            time.sleep(3)
            if 'No data found' in self.driver.page_source:
                print(times.options[i].text,'has no data found')
            else:
                for j in range(1,len(dist.options)-1):
                    dist.select_by_index(j)
                    value = self.driver.find_element_by_id(self.data.Choose_Dist).get_attribute('value')
                    value = value.split(":")

                    time.sleep(2)
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    dots = len(markers) -1
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(4)
                    self.filename = p.get_download_dir() + '/'+ self.fname.pat_districtwise()+management+'_all_allGrades__blocks_of_district_'+value[1].strip()+'_'+self.SP.get_current_date()+'.csv'
                    print(self.filename)
                    time.sleep(2)
                    if os.path.isfile(self.filename) !=True:
                        print( dist.options[i],"district csv file not downloaded ")
                        count = count + 1
                    else:
                        markers = self.driver.find_elements_by_class_name(self.data.markers)
                        dots = len(markers) - 1
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            if int(dots) != row_count:
                                print("Markers and csv file records count mismatched", dots, row_count)
                                count = count + 1
                        os.remove(self.filename)
            return count


    def check_last_30_days(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        times= Select(self.driver.find_element_by_id('period'))
        times.select_by_index(2)
        print(times.first_selected_option.text)
        time.sleep(3)
        schools = self.driver.find_element_by_id('schools').text
        students = self.driver.find_element_by_id('students').text
        attended = self.driver.find_element_by_id('studentsAttended').text

        schol = re.sub('\D', "", schools)
        std = re.sub('\D', "", students)
        attd = re.sub('\D', "", attended)

        print('Expected footer values : ', schol, std, attd)

        print('***************Block level footer values******************')

        self.driver.find_element_by_id(self.data.Block_button).click()
        # cal = GetData()
        if 'No data found' in self.driver.page_source:
            print("NO DATA FOUND")
        else:
            self.SP.page_loading(self.driver)
            time.sleep(5)
            dots = self.driver.find_elements_by_class_name(self.data.markers)
            markers = len(dots) - 1
            if markers == 0:
                print("Block level markers are not present ")
                count = count + 1
            else:
                bschools = self.driver.find_element_by_id('schools').text
                bsch = re.sub('\D', "", bschools)

                bstudents = self.driver.find_element_by_id('students').text
                bstd = re.sub('\D', "", bstudents)

                battended = self.driver.find_element_by_id('studentsAttended').text
                battd = re.sub('\D', "", battended)

                print('after Clicking of block footer values ', bsch, bstd, battd)

                count = 0
                if int(bsch) != int(schol):
                    print('Block level footer mismatch found', int(bsch), int(schol))
                    count = count + 1
                if int(bstd) != int(std):
                    print('Block level footer mismatch found', int(bstd), int(std))
                    count = count + 1
                if int(battd) != int(attd):
                    print('Block level footer mismatch found', int(battd), int(attd))
                    count = count + 1

            print('***************Cluster level footer values******************')

            self.driver.find_element_by_id(self.data.Cluster_button).click()
            # cal = GetData()
            self.SP.page_loading(self.driver)
            time.sleep(10)
            if 'No data found' in self.driver.page_source:
                print("NO DATA FOUND")
            else:
                dots = self.driver.find_elements_by_class_name(self.data.markers)
                dots = len(dots) - 1
                if dots == 0:
                    print("Cluster level markers are not present ")
                    count = count + 1

                cschools = self.driver.find_element_by_id('schools').text
                csch = re.sub('\D', '', cschools)

                cstudents = self.driver.find_element_by_id('students').text
                cstd = re.sub('\D', '', cstudents)

                cattended = self.driver.find_element_by_id('studentsAttended').text
                cattd = re.sub('\D', '', cattended)

                print('after Clicking of cluster footer values ', csch, cstd, cattd)

                if int(csch) != int(schol):
                    print('Cluster level footer mismatch found', int(csch), int(schol))
                    count = count + 1
                if int(cstd) != int(std):
                    print('Cluster level footer mismatch found', int(cstd), int(std))
                    count = count + 1
                if int(cattd) != int(attd):
                    print('Cluster level footer mismatch found', int(cattd), int(attd))
                    count = count + 1

            print('***************School level footer values******************')

            self.driver.find_element_by_id(self.data.School_button).click()
            # cal = GetData()
            self.SP.page_loading(self.driver)
            time.sleep(10)
            if 'No data found' in self.driver.page_source:
                print("NO DATA FOUND")
            else:
                result = self.driver.find_elements_by_class_name(self.data.markers)
                dots = len(result) - 1
                if dots == 0:
                    print("School level markers are not present ")
                    count = count + 1

                sschools = self.driver.find_element_by_id('schools').text
                ssch = re.sub('\D', '', sschools)

                sstudents = self.driver.find_element_by_id('students').text
                sstd = re.sub('\D', '', sstudents)

                sattended = self.driver.find_element_by_id('studentsAttended').text
                sattd = re.sub('\D', '', sattended)

                print('after Clicking of School footer values ', ssch, sstd, sattd)

                if int(ssch) != int(schol):
                    print('School level footer mismatch found', int(ssch), int(schol))
                    count = count + 1
                if int(sstd) != int(std):
                    print('School level footer mismatch found', int(sstd), int(std))
                    count = count + 1
                if int(sattd) != int(attd):
                    print('School level footer mismatch found', int(sattd), int(attd))
                    count = count + 1
        return count

    def check_last_7_days(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        times.select_by_index(3)
        print(times.first_selected_option.text)
        time.sleep(3)
        schools = self.driver.find_element_by_id('schools').text
        students = self.driver.find_element_by_id('students').text
        attended = self.driver.find_element_by_id('studentsAttended').text

        schol = re.sub('\D', "", schools)
        std = re.sub('\D', "", students)
        attd = re.sub('\D', "", attended)

        print('Expected footer values : ', schol, std, attd)

        print('***************Block level footer values******************')

        self.driver.find_element_by_id(self.data.Block_button).click()
        # cal = GetData()
        self.SP.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(self.data.markers)
        markers = len(dots) - 1
        if markers == 0:
            print("Block level markers are not present ")
            count = count + 1
        else:
            bschools = self.driver.find_element_by_id('schools').text
            bsch = re.sub('\D', "", bschools)

            bstudents = self.driver.find_element_by_id('students').text
            bstd = re.sub('\D', "", bstudents)

            battended = self.driver.find_element_by_id('studentsAttended').text
            battd = re.sub('\D', "", battended)

            print('after Clicking of block footer values ', bsch, bstd, battd)

            count = 0
            if int(bsch) != int(schol):
                print('Block level footer mismatch found', int(bsch), int(schol))
                count = count + 1
            if int(bstd) != int(std):
                print('Block level footer mismatch found', int(bstd), int(std))
                count = count + 1
            if int(battd) != int(attd):
                print('Block level footer mismatch found', int(battd), int(attd))
                count = count + 1

            print('***************Cluster level footer values******************')

            self.driver.find_element_by_id(self.data.Cluster_button).click()
            # cal = GetData()
            self.SP.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(dots) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            cschools = self.driver.find_element_by_id('schools').text
            csch = re.sub('\D', '', cschools)

            cstudents = self.driver.find_element_by_id('students').text
            cstd = re.sub('\D', '', cstudents)

            cattended = self.driver.find_element_by_id('studentsAttended').text
            cattd = re.sub('\D', '', cattended)

            print('after Clicking of cluster footer values ', csch, cstd, cattd)

            if int(csch) != int(schol):
                print('Cluster level footer mismatch found', int(csch), int(schol))
                count = count + 1
            if int(cstd) != int(std):
                print('Cluster level footer mismatch found', int(cstd), int(std))
                count = count + 1
            if int(cattd) != int(attd):
                print('Cluster level footer mismatch found', int(cattd), int(attd))
                count = count + 1

            print('***************School level footer values******************')

            self.driver.find_element_by_id(self.data.School_button).click()
            # cal = GetData()
            self.SP.page_loading(self.driver)
            result = self.driver.find_elements_by_class_name(self.data.markers)
            dots = len(result) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            sschools = self.driver.find_element_by_id('schools').text
            ssch = re.sub('\D', '', sschools)

            sstudents = self.driver.find_element_by_id('students').text
            sstd = re.sub('\D', '', sstudents)

            sattended = self.driver.find_element_by_id('studentsAttended').text
            sattd = re.sub('\D', '', sattended)

            print('after Clicking of School footer values ', ssch, sstd, sattd)

            if int(ssch) != int(schol):
                print('School level footer mismatch found', int(ssch), int(schol))
                count = count + 1
            if int(sstd) != int(std):
                print('School level footer mismatch found', int(sstd), int(std))
                count = count + 1
            if int(sattd) != int(attd):
                print('Cluster level footer mismatch found', int(sattd), int(attd))
                count = count + 1
        return count

    def check_last_30_days_districts(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        management = self.SP.get_management_selected_option()
        times.select_by_index(2)
        time.sleep(2)
        timeseries = times.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 30 days ")
        else:
            select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
            count = 0
            for x in range(1, len(select_district.options)):
                select_district.select_by_index(x)
                self.SP.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
                value = value[4:] + '_'
                markers = self.driver.find_elements_by_class_name(self.data.markers)
                if (len(markers) - 1) == 0:
                    print("District " + select_district.first_selected_option.text + " no data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    p = pwd()
                    time.sleep(5)
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_districtwise() +management+'_'+timeseries.lower()+'_allGrades__blocks_of_district_' + value.strip() + self.SP.get_current_date() + '.csv'
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
                        students = self.driver.find_element_by_id("students").text
                        studs = re.sub('\D', "", students)

                        school = self.driver.find_element_by_id("schools").text
                        sc = re.sub('\D', "", school)

                        attend = self.driver.find_element_by_id("studentsAttended").text
                        atd = re.sub('\D', "", attend)

                        print('value on footer', student, schools, attended)
                        print('value on csv file', studs, sc, atd)

                        if int(studs) != int(student):
                            print(
                                "District " + select_district.first_selected_option.text + " student count mismatched",
                                int(studs), int(student))
                            count = count + 1

                        if int(sc) != int(schools):
                            print(
                                "District " + select_district.first_selected_option.text + " school count mismatched",
                                int(sc), int(schools))
                            count = count + 1

                        if int(atd) != int(attended):
                            print(
                                "District " + select_district.first_selected_option.text + " student attended mismatched",
                                int(atd), int(attended))
                            count = count + 1

                os.remove(self.filename)
        return count

    def check_last_7_days_districts(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(self.data.hyper_link).click()
        self.SP.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        times.select_by_index(3)
        management = self.SP.get_management_selected_option()
        timeseries = times.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 7 days ")
        else:
            select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
            for x in range(1, len(select_district.options)):
                select_district.select_by_index(x)
                self.SP.page_loading(self.driver)
                value = self.driver.find_element_by_id(self.data.Choose_Dist).get_attribute('value')
                value = value.split(":")
                values = value[1].strip()
                markers = self.driver.find_elements_by_class_name(self.data.markers)
                if (len(markers) - 1) == 0:
                    print("District " + select_district.first_selected_option.text + " no data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    p = pwd()
                    time.sleep(5)
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_districtwise()+management+'_'+timeseries.lower + '_allGrades__blocks_of_district_' + values+'_' + self.SP.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        # with open(self.filename) as fin:
                        #     csv_reader = csv.reader(fin, delimiter=',')
                        #     header = next(csv_reader)
                        #     student = 0
                        #     schools = 0
                        #     attended = 0
                        #     for row in csv.reader(fin):
                        #         student += int(row[5])
                        #         schools += int(row[7])
                        #         attended += int(row[6])
                        #     print(self.filename, ':', student, schools, attended)
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
                        students = self.driver.find_element_by_id("students").text
                        studs = re.sub('\D', "", students)

                        school = self.driver.find_element_by_id("schools").text
                        sc = re.sub('\D', "", school)

                        attend = self.driver.find_element_by_id("studentsAttended").text
                        atd = re.sub('\D', "", attend)

                        print('value on footer', student, schools, attended)
                        print('value on csv file', studs, sc, atd)

                        if int(studs) != int(student):
                            print(
                                "District " + select_district.first_selected_option.text + " student count mismatched",
                                int(studs), int(student))
                            count = count + 1

                        if int(sc) != int(schools):
                            print(
                                "District " + select_district.first_selected_option.text + " school count mismatched",
                                int(sc), int(schools))
                            count = count + 1

                        if int(atd) != int(attended):
                            print(
                                "District " + select_district.first_selected_option.text + " student attended mismatched",
                                int(atd), int(attended))
                            count = count + 1
                os.remove(self.filename)
        return count


    def check_districts_block(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            self.SP.page_loading(self.driver)
            for y in range(len(select_block.options)-2, len(select_block.options)):
                select_block.select_by_index(y)
                self.SP.page_loading(self.driver)
                value = self.driver.find_element_by_id(self.data.Choose_Block).get_attribute('value')
                value = value[4:]+'_'
                markers = self.driver.find_elements_by_class_name(self.data.markers)
                if len(markers) - 1 == 0:
                    print("District" + select_district.first_selected_option.text +"Block"+ select_block.first_selected_option.text +"No Locators")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id(self.data.Downloads).click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise()+management+'_all_allGrades__clusters_of_block_'+value.strip()+self.SP.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District" + select_district.first_selected_option.text +"Block"+ select_block.first_selected_option.text+"csv is not downloaded")
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
                        os.remove(self.filename)
                return count

    def check_last30days_districts_block(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period =Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ",'_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 30 days ")
        else:
            select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
            select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                self.SP.page_loading(self.driver)
                for y in range(1, len(select_block.options)):
                    select_block.select_by_index(y)
                    self.SP.page_loading(self.driver)
                    value = self.driver.find_element_by_id(self.data.Choose_Block).get_attribute('value')
                    value = value.split(":")
                    values = value[1].strip()
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    if len(markers) - 1 == 0:
                        print("District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Locators")
                        count = count + 1
                    else:
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise()+management+'_'+timeseries+'_allGrades__clusters_of_block_' + values+'_' + self.SP.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1
                    os.remove(self.filename)
        return count

    def check_last7days_districts_block(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        management = self.SP.get_management_selected_option()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 7 days ")
        else:
            select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
            select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                self.SP.page_loading(self.driver)
                for y in range(len(select_block.options)-3, len(select_block.options)):
                    select_block.select_by_index(y)
                    self.SP.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                    value = value.split(":")
                    values = value[1].strip()
                    markers = self.driver.find_elements_by_class_name(self.data.markers)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Locators")
                        count = count + 1
                    else:
                        time.sleep(2)
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(2)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise() + management +"_"+timeseries + '_allGrades__clusters_of_block_' + values+"_"+ self.SP.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1
                    os.remove(self.filename)
        return count

    def check_last30_district_block_cluster(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
            select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
            select_cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                self.SP.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    self.SP.page_loading(self.driver)
                    for z in range(len(select_cluster.options) - 2, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        self.SP.page_loading(self.driver)
                        value = self.driver.find_element_by_id(self.data.Choose_Cluster).get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(self.data.markers)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + self.SP.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1

                            os.remove(self.filename)
        return count


    def check_last7_district_block_cluster(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        count = 0
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
            select_block = Select(self.driver.find_element_by_id(self.data.Choose_Block))
            select_cluster = Select(self.driver.find_element_by_id(self.data.Choose_Cluster))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                self.SP.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    self.SP.page_loading(self.driver)
                    for z in range(len(select_cluster.options) - 2, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        self.SP.page_loading(self.driver)
                        value = self.driver.find_element_by_id(self.data.Choose_Cluster).get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(self.data.markers)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id(self.data.Downloads).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + self.SP.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1

                            os.remove(self.filename)
        return count



    def click_download_icon_of_blocks(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Block_button).click()
        self.SP.page_loading(self.driver)
        marker = self.driver.find_elements_by_class_name(self.data.markers)
        counts = len(marker)-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(5)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.pat_block()
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            print('Block wise csv file is downloaded')
        os.remove(self.filename)
        return counts

    def click_download_icon_of_clusters(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.Cluster_button).click()
        self.SP.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        dots = len(markers)-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(10)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.pat_cluster()
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            print('Cluster wise csv file downloaded')
        os.remove(self.filename)
        return dots

    def click_download_icon_of_schools(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.fname = file_extention()
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        self.driver.find_element_by_id(self.data.School_button).click()
        time.sleep(10)
        markers = self.driver.find_elements_by_class_name(self.data.markers)
        dots = len(markers)-1
        self.driver.find_element_by_id(self.data.Downloads).click()
        time.sleep(15)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.pat_school()
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            print("School wise csv file is downloaded")
        os.remove(self.filename)
        return dots

    def check_dots_on_each_districts(self, setup):
        self.driver = setup
        self.data = Locator_Path()
        self.driver.get(self.baseUrl)
        self.SP = PATReport(self.driver)
        self.SP.login(self.username, self.password)
        self.SP.click_on_state(self.driver)
        self.SP.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id(self.data.Choose_Dist))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.SP.page_loading(self.driver)
            time.sleep(5)
            dots = self.driver.find_elements_by_class_name(self.data.markers)
            if int(len(dots) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "Markers are not found")
                count = count + 1

        return count




