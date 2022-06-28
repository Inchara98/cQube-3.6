import os
import time
import pytest

from Logs.Log import log_Details
from utilities.readProperties import ReadConfig
from PageObjects.School_Composite import CompositeReport


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()

    logger = log_Details.logen()


    # def test_plotxvalues(self, setup):
    #     self.driver = setup
    #     self.b = CompositeReport(self.driver)
    #     res = self.b.test_xplots(self.driver)
    #     print("Checked with xaxis values are working..")
    #     self.b.page_loading(self.driver)
    #
    # def test_plotyvalues(self, setup):
    #     self.driver = setup
    #     self.b = CompositeReport(self.driver)
    #     res = self.b.test_yaxis(self.driver)
    #     print("Checked with  y axis values are working..")
    #     self.b.page_loading(self.driver)

    # def test_sc_scator_districtwise(self, setup):
    #     self.driver = setup
    #     self.b = CompositeReport(self.driver)
    #     result = self.b.test_district(self.driver)
    #     if result == 0:
    #         assert True
    #         print("Checked with each district wise records")
    #     else:
    #         assert False



    # def test_sc_scator_blockwise(self, setup):
    #     self.driver = setup
    #     self.b = CompositeReport(self.driver)
    #     result = self.b.test_blockwise(self.driver)
    #     if result == 0:
    #         assert True
    #         print("Checked with each Block wise records")
    #     else:
    #         assert False


    def test_sc_scator_clockwise(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        result = self.b.test_cluster(self.driver)
        if result == 0:
            assert True
            print("Checked with each Cluster wise records")
        else:
            assert False
