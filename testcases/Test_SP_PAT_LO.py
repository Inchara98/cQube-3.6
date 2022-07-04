import os
import time
import pytest

from Logs.Log import log_Details
from utilities.readProperties import ReadConfig
from PageObjects.SP_PAT_LO import PAT_LO


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()

    logger = log_Details.logen()


    def test_Catagory_series(self, setup):
        self.driver = setup
        self.b =PAT_LO(self.driver)
        res = self.b.viewbys_options(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_test_questions(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.test_questions_records(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_test_indicator(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.test_indicator_records(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_Download_districtwise(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.download_all_district_records(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_exams_series(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.exams_dates(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_subject_levels(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.subjects_types(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_Home_functions(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.test_homeicons(self.driver)


    def test_Homebtn_functions(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.test_homebutton(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_year_selection(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.test_year_dropdown(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_districtwise(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.District_select_box(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_Blockwise(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.Block_select_box(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_Clusterwise(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.Clusters_select_box(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_grade_files(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.grades_files(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_grade_files(self, setup):
        self.driver = setup
        self.b = PAT_LO(self.driver)
        res = self.b.test_randoms(self.driver)
        if res == 0:
            assert True
        else:
            assert False