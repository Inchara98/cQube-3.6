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


    def test_composite_report(self,setup):
        self.logger.info("********************verifying Back_Button Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.CR = CompositeReport(self.driver)
        self.CR.login(self.username, self.password)
        a = "Composite Report"
        if a in self.driver.page_source:
            assert True
        else:
            assert False


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


    def test_dashboard(self, setup):
            self.driver = setup
            self.b = CompositeReport(self.driver)
            self.b.test_menulist(self.driver)
            print("check with dashboard options is working fine ")
            self.b.page_loading(self.driver)
            a = "Composite Report"
            if a in self.driver.page_source:
                assert True
            else:
                assert False

    def test_download_districtwise(self,setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_districtwise(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_download_blockwise(self,setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_block(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_download_clusterwise(self,setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_clusterwise(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_download_schoolwise(self,setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_schoolwise(self.driver)
        if res == 0:
            assert True
        else:
            assert False


    def test_homebutton(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_homebtn(self.driver)
        print("homeicon is working..")
        if res == 0:
            assert True
        else:
            assert False
        self.b.page_loading(self.driver)

    def test_check_orderwise(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        print("Table record order wise..")
        res = self.b.test_tablevalue(self.driver)
        print("checked with orderwise of table data")
        self.b.page_loading(self.driver)

    def test_schools_per_cluster_csv_download1(self, setup):
        self.driver = setup
        self.school = CompositeReport(self.driver)
        result = self.school.check_csv_download1(self.driver)
        if result == 0:
            assert True
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            assert False


    def test_tabledata_districtwise(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_table_data(self.driver)
        if res == 0:
            assert True
            print("District table data is present...")
        else:
            assert False


    def test_plotxvalues(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_xplots(self.driver)
        print("Checked with xaxis values are working..")
        self.b.page_loading(self.driver)

    def test_plotyvalues(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        res = self.b.test_yaxis(self.driver)
        print("Checked with  y axis values are working..")
        self.b.page_loading(self.driver)

    def test_sc_scator_districtwise(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        result = self.b.test_district(self.driver)
        if result == 0:
            assert True
            print("Checked with each district wise records")
        else:
            assert False



    def test_sc_scator_blockwise(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        result = self.b.test_blockwise(self.driver)
        if result == 0:
            assert True
            print("Checked with each Block wise records")
        else:
            assert False


    def test_sc_scator_clockwise(self, setup):
        self.driver = setup
        self.b = CompositeReport(self.driver)
        result = self.b.test_cluster(self.driver)
        if result == 0:
            assert True
            print("Checked with each Cluster wise records")
        else:
            assert False
