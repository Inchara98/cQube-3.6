import os
import time
import pytest

from Logs.Log import log_Details
from utilities.readProperties import ReadConfig
from PageObjects.SP_PAT import PATReport


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()

    logger = log_Details.logen()


    def test_DistrictwiseCsv(self, setup):
        self.driver = setup
        self.cls = PATReport(self.driver)
        func = self.cls.click_download_icon(self.driver)
        if func == 0:
            assert True
            print('Downloading district level csv file is working')
        else:
            assert False


    def test_blockbutton_footers(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res1, res2 = self.b.check_with_block_footervalues(self.driver)
        if res1 != 0:
            assert True
        else:
            assert False

        if res2 == 0:
            assert True
        else:
            assert False



    def test_clusterbutton_footers(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res1, res2 = self.b.check_with_cluster_footervalues(self.driver)
        if res1 != 0:
            assert True
        else:
            assert False

        if res2 == 0:
            assert True
        else:
            assert False


    def test_schoolbutton_footers(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res1, res2 = self.b.check_with_schoolfooters(self.driver)
        if res1 != 0:
            assert True
        else:
            assert False

        if res2 == 0:
            assert True
        else:
            assert False

    def test_TotalStudentsSchools(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res1,res2,res3,res4,res5,res6,res7,res8 = self.b.block_cluster_schools_footer_info(self.driver)
        if int(res1) == int(res3):
            assert True
            print("Block level student info is matching")
        else:
            assert False

        if int(res2) == int(res4):
            assert True
            print("Block level school info is matching")
        else:
            assert False

        if int(res1) == int(res5):
            assert True
            print("Cluster level student info is matching")
        else:
            assert False

        if int(res2) == int(res6):
            assert True
            print("Cluster level school info is matching")
        else:
            assert False

        if int(res1) == int(res7):
            assert True
            print("School level student info is matching")
        else:
            assert False

        if int(res2) == int(res8):
            assert True
            print("School level school info is matching")
        else:
            assert False

    def test_Homeicon(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.click_on_blocks_click_on_home_icon(self.driver)
        print('Home icon is working')

    def test_check_hyperlinks(self,setup):
        self.driver = setup
        self.hyperlinks = PATReport(self.driver)
        result1, result2, choose_dist = self.hyperlinks.click_on_hyperlinks(self.driver)
        if result1 == False and result2 == False and choose_dist == "Choose a District":
            assert True
            print("hyperlinks are working")
        else:
            assert False

    def test_each_district(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.check_district(self.driver)
        if res == 0:
            assert True
            print('Districtwise records are working fine')
        else:
            assert False

    def test_district_block_clusterwise(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.check_district_block_cluster(self.driver)
        if res == 0:
            assert True
            print('School level records are working fine')
        else:
            assert False

    def test_periodic_grades(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.check_grade_dropdown_options(self.driver)
        if res != 0:
            assert True
            print("checking with each grades")
        else:
            assert False

    def test_grades_downloadfile(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.click_each_grades(self.driver)
        if res == 0:
            assert True
            print("checking with each grades with download functionality")
        else:
            assert False

    def test_grades_subjects(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.select_subjects_dropdown(self.driver)
        if res == 0:
            assert True
            print("checking with each grades with subjects")
        else:
            assert False

    def test_timeseries_pat(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.test_options_times(self.driver)
        if res != 0:
            assert True
            print("checking with time period options ")
        else:
            assert False

    def test_timeseries_with_downloading(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.time_over_all(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_click_on_blocks_cluster_schools(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last_30_days(self.driver)
        if result == 0:
            assert True
        else:
            assert False

    def test_click_on_blocks_cluster_schools_7days(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last_7_days(self.driver)
        if result != 0:
            assert True
        else:
            assert False

    def test_last30_districts(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last_30_days_districts(self.driver)
        if result == 0:
            assert True
        else:
            assert False

    def test_last7days_districts(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last_7_days_districts(self.driver)
        if result == 0:
            assert True
        else:
            assert False

    def test_district_blockwise(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.check_districts_block(self.driver)
        if res != 0:
          assert True
          print('Blockwise records are working fine')
        else:
          assert False


    def test_last30days_district_blockwise_clusterwise(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last30days_districts_block(self.driver)
        if result == 0:
            assert True
        else:
            assert False


    def test_last30_district_blockwise_clusterwise(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last30_district_block_cluster(self.driver)
        if result == 0:
            assert True
         #   print("Schools per cluster csv download report is working on selection of each district,block and cluster The footer value of no of schools and no of students are equals to downloaded file")
        else:
            assert False

    def test_last7days_district_blockwise_clusterwise(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last7days_districts_block(self.driver)
        if result == 0:
            assert True
            #print("District csv file is downloaded")
        else:
            assert False

    def test_last7_district_blockwise_clusterwise(self, setup):
        self.driver = setup
        self.block = PATReport(self.driver)
        result = self.block.check_last7_district_block_cluster(self.driver)
        if result == 0:
            assert True
            #print("Schools per cluster csv download report is working on selection of each district,block and cluster The footer value of no of schools and no of students are equals to downloaded file")
        else:
            assert False

    def test_district_blockwise(self, setup):
        self.driver = setup
        self.b = PATReport(self.driver)
        res = self.b.check_districts_block(self.driver)
        if res != 0:
          assert True
          print('Blockwise records are working fine')
        else:
          assert False

