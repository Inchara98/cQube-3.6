import os
import time
import pytest

from PageObjects.School_Infra import SchoolInfra
from Logs.Log import log_Details
from filenames import file_extention
from get_dir import pwd
from utilities.readProperties import ReadConfig





class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()
    logger = log_Details.logen()



    def test_block_disable(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        choosedist = self.SI.Choosedist()
        i = 0
        for i in range(1,len(choosedist.options)):
            choosedist.select_by_index(i)
            print(choosedist.options[i].text, 'District is selected')
            a = self.SI.Blockbutton().is_enabled()
            if a == False:
                assert True
                print("Block button is disable")
            else:
                print("Block button is enable")
                self.driver.close()
                assert False

    # def test_cluster_disable(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.SI = SchoolInfra(self.driver)
    #     self.SI.login(self.username, self.password)
    #     time.sleep(8)
    #     self.SI.InfraMap().click()
    #     time.sleep(10)
    #     self.SI.Choosedist().select_by_index(1)
    #     time.sleep(2)
    #     chooseblock = self.SI.Chooseblock()
    #     i = 0
    #     for i in range(1,len(chooseblock.options)):
    #         chooseblock.select_by_index(i)
    #         print(chooseblock.options[i].text, 'Block is selected')
    #         a = self.SI.Clusterbutton().is_enabled()
    #         if a == False:
    #             assert True
    #             print("Cluster button is disable")
    #         else:
    #             print("Cluster button is enable")
    #             assert False
    #
    # def test_school_disable(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.SI = SchoolInfra(self.driver)
    #     self.SI.login(self.username, self.password)
    #     time.sleep(8)
    #     self.SI.InfraMap().click()
    #     time.sleep(10)
    #     self.SI.Choosedist().select_by_index(1)
    #     time.sleep(2)
    #     self.SI.Chooseblock().select_by_index(1)
    #     time.sleep(2)
    #     choosecluster = self.SI.Choosecluster()
    #     i = 0
    #     for i in range(1,len(choosecluster.options)):
    #         choosecluster.select_by_index(i)
    #         print(choosecluster.options[i].text, 'Cluster is selected')
    #         a = self.SI.Schoolbutton().is_enabled()
    #         if a == False:
    #             assert True
    #             print("School button is disable")
    #         else:
    #             print("School button is enable")
    #             assert False

    # def test_cluster_disable(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.SI = SchoolInfra(self.driver)
    #     self.SI.login(self.username, self.password)
    #     time.sleep(8)
    #     self.SI.InfraMap().click()
    #     time.sleep(10)
    #     self.SI.Choosedist().select_by_index(1)
    #     time.sleep(2)
    #     self.SI.Chooseblock().select_by_index(1)
    #     time.sleep(3)
    #     a = self.SI.Clusterbutton().is_enabled()
    #     if a == False:
    #         assert True
    #         print("Cluster button is disable")
    #     else:
    #         print("Cluster button is enable")
    #         assert False
    #
    #
    # def test_school_disable(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.SI = SchoolInfra(self.driver)
    #     self.SI.login(self.username, self.password)
    #     time.sleep(8)
    #     self.SI.InfraMap().click()
    #     time.sleep(10)
    #     self.SI.Choosedist().select_by_index(1)
    #     time.sleep(3)
    #     self.SI.Chooseblock().select_by_index(1)
    #     time.sleep(3)
    #     self.SI.Choosecluster().select_by_index(1)
    #     time.sleep(2)
    #     a = self.SI.Schoolbutton().is_enabled()
    #     if a == False:
    #         assert True
    #         print("School button is disable")
    #     else:
    #         print("School button is enable")
    #         assert False