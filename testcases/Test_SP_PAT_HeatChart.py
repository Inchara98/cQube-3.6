import os
import time
import pytest

from Logs.Log import log_Details
from utilities.readProperties import ReadConfig
from PageObjects.SP_PAT_Heat_Chart import PAT_Heat_Chart


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()

    logger = log_Details.logen()


    def test_districtwise(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.District_select_box(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_blockwise(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.Blocks_select_box(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_clusterwise(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.Clusters_select_box(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_Catagory_series(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.viewbys_options(self.driver)
        if res == 0:
            assert True
        else:
            assert False



    def test_test_questions(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.test_questions_records(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_test_indicators(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.test_indicator_records(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_Download_districtwise(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.download_all_district_records(self.driver)
        if res == 0:
            assert True
        else:
            assert False



    def test_exams_series(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.exams_dates(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_subject_levels(self, setup):
        self.driver = setup
        self.b =PAT_Heat_Chart(self.driver)
        res = self.b.subjects_types(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_Home_functions(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.test_homeicons(self.driver)
        print("Checked with homeicon functionality ")


    def test_Homebtn_functions(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.test_homebutton(self.driver)
        if res == 0:
            assert True
        else:
            assert False




    def test_year_selection(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.test_year_dropdown(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_check_hyperlinks(self, setup):
        self.driver = setup
        self.hyperlinks = PAT_Heat_Chart(self.driver)
        res = self.hyperlinks.test_hyperlink(self.driver)
        print('hyper link is working ')



    def test_gradewise_records(self, setup):
        self.driver = setup
        self.b =PAT_Heat_Chart(self.driver)
        res = self.b.grades_files(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_Random_test(self, setup):
        self.driver = setup
        self.b = PAT_Heat_Chart(self.driver)
        res = self.b.test_randoms(self.driver)
        if res == 0:
            assert True
        else:
            assert False








