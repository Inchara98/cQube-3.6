import os
import time
import pytest

from Logs.Log import log_Details
from utilities.readProperties import ReadConfig
from PageObjects.SP_SAT import SATReport


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()

    logger = log_Details.logen()


    def test_schoolwise_cv_download(self, setup):
        self.driver = setup
        self.csv = SATReport(self.driver)
        result = self.csv.click_download_icon_of_schools(self.driver)
        if result == "File Downloaded":
            assert True
        else:
            assert False

    def test_click_on_blocks(self, setup):
        self.driver = setup
        self.block = SATReport(self.driver)
        result = self.block.check_markers_on_block_map(self.driver)
        if len(result) - 1 != 0:
            assert True
        else:
            assert False

    def test_click_on_blocks_cluster_schools(self, setup):
        self.driver = setup
        self.block = SATReport(self.driver)
        result = self.block.check_last_30_days(self.driver)
        if result == 0:
            assert True
        else:
            assert False


    def test_click_on_clusters(self,setup):
        self.driver = setup
        self.cluster = SATReport(self.driver)
        result = self.cluster.check_markers_on_clusters_map(self.driver)
        if  len(result) - 1 != 0:
            assert True
        else:
            assert False


    def test_click_on_schools(self, setup):
        self.driver = setup
        self.school = SATReport(self.driver)
        result = self.school.check_markers_on_school_map(self.driver)
        if len(result)-1 != 0:
            assert True
        else:
            assert False




    def test_check_hyperlinks(self, setup):
        self.driver = setup
        self.hyperlinks = SATReport(self.driver)
        result1, result2, choose_dist = self.hyperlinks.click_on_hyperlinks(self.driver)
        if result1 == False and result2 == False and choose_dist == "Choose a District":
            assert True
            print("hyperlinks are working")
        else:
            assert False


    def test_districtwise_csv_download(self, setup):
        self.driver = setup
        self.csv = SATReport(self.driver)
        result = self.csv.click_download_icon_of_district(self.driver)
        if result != "Mismatch found at footer values":
            print("District wise csv report download is working")
            assert True
        else:
            assert False

    def test_blockwise_csv_download(self, setup):
        self.driver = setup
        self.csv = SATReport(self.driver)
        result = self.csv.click_download_icon_of_blocks(self.driver)
        if result != "File Not Downloaded":
            assert True
            print("Block wise csv report download is working")
        else:
            assert False

    def test_clusterwise_csv_download(self,setup):
        self.driver = setup
        self.csv = SATReport(self.driver)
        result = self.csv.click_download_icon_of_clusters(self.driver)
        if result != "File Not Downloaded":
           assert True
        else:
            assert False




    def test_gradewise_csv_downloading(self, setup):
        self.driver = setup
        self.tc = SATReport(self.driver)
        res = self.tc.check_grade_dropdown_options(self.driver)
        if res != 0:
            assert True
            print("Checked with grade options in sat map report")
        else:
            assert False

    def test_each_grade(self, setup):
        self.driver = setup
        self.fun = SATReport(self.driver)
        res1 = self.fun.click_each_grades(self.driver)
        if res1 == 0:
            assert True
        else:
            assert False



    def test_subjectwise_csv_downloading(self,setup):
        self.driver = setup
        self.tc = SATReport(self.driver)
        res = self.tc.select_subjects_dropdown(self.driver)
        if res == 0:
            assert True
            print("Subjectwise file is downloading")
        else:
            assert False


    def test_choose_district(self, setup):
        self.driver = setup
        self.dist = SATReport(self.driver)
        result = self.dist.check_district(self.driver)
        if result == 0:
            assert True
            print("Block per district csv report download is working")
            print("on selection of each district")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            assert False

    def test_choose_district_block(self, setup):
        self.driver = setup
        self.block = SATReport(self.driver)
        result = self.block.check_districts_block(self.driver)
        if result == 0:
            assert True
            print("Cluster per block csv report download is working")
            print("on selection of each district and block")
        else:
            assert False

    def test_choose_district_block_cluster(self, setup):
        self.driver = setup
        self.schools = SATReport(self.driver)
        result = self.schools.check_district_block_cluster(self.driver)
        if result == 0:
            assert True
            print("School per Cluster csv report download is working")
            print("on selection of each district, block and cluster")
        else:
            assert False

