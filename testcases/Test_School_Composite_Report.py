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


    # def test_composite_report(self,setup):
    #     self.logger.info("********************verifying Back_Button Test********************************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.CR = CompositeReport(self.driver)
    #     self.CR.login(self.username, self.password)
    #     a = "Composite Report"
    #     if a in self.driver.page_source:
    #         assert True
    #     else:
    #         assert False


    def test_hyperlink(self,setup):
        self.logger.info("********************verifying Back_Button Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        time.sleep(2)
        expected = "Composite Report for: " + self.state
        print(expected)
        time.sleep(5)
        actual = self.CR.HyperLink()
        time.sleep(2)
        print(actual)
        if expected == actual:
            assert True
            self.logger.info("********************test_hyperLink Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_hyperLink.png")
            self.driver.close()
            self.logger.info("********************test_hyperLink Failed********************************")
            assert False

