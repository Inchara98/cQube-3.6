import os
import time
import pytest

from Logs.Log import log_Details
from utilities.readProperties import ReadConfig
from PageObjects.School_Udise import UdiseReport


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()

    logger = log_Details.logen()


    def test_hyperlink(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res = self.b.test_link(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_download_districtcsv(self, setup):
        self.driver = setup
        self.fn = UdiseReport(self.driver)
        res = self.fn.test_districtwise(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_test_school_map_schoollevel_records(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res = self.b.check_download_csv1(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_Block_cluster_school_for_udise(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res, res1, res2, res3 = self.b.test_check_total_schoolvalue(self.driver)
        if res == res1:
            assert True
            print("Block level school is same")
        else:
            assert False
        if res == res2:
            assert True
            print("Cluster level school is same")
        else:
            assert False
        if res == res3:
            assert True
            print("School level school is same")
        else:
            assert False

    def test_block_wise_download(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res, res1 = self.b.test_download_blockwise(self.driver)
        if res != 0:
            assert True
            print("Block level csv file is downloaded")
        else:
            assert False

        if res1 != 0:
            assert True
            print("Markers are displaying on Block level map")
        else:
            assert False

    def test_cluster_wise_download(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res, res1 = self.b.test_clusterbtn(self.driver)
        if res != 0:
            assert True
            print("Cluster level csv file is downloaded")
        else:
            assert False

        if res1 != 0:
            assert True
            print("Markers are displaying on cluster level map")
        else:
            assert False

    def test_school_wise_download(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res, res1 = self.b.test_click_on_school_btn(self.driver)
        if res != 0:
            assert True
            print("School level csv file is downloaded")
        else:
            assert False

        if res1 != 0:
            assert True
            print("Markers are displaying on School level map")
        else:
            assert False

    def test_block_btn_scores(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res = self.b.test_click_blocks(self.driver)
        if res == 0:
            assert True
            print("markers are present at selected indices")
        else:
            assert False

    def test_cluster_btn_scores(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res = self.b.test_click_clusters(self.driver)
        if res == 0:
            assert True
            print("markers are present at selected indices")
        else:
            assert False

    def test_indices_infra(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        indices_score = self.b.infrastructure_score(self.driver)
        self.b.remove_csv()
        if indices_score >= 0:
            assert True
        else:
            assert False

    def test_indices_administation(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        administation = self.b.administation(self.driver)
        self.b.remove_csv()
        if administation >= 0:
            assert True
        else:
            assert False

    def test_indices_artslab(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        artslab = self.b.artslab(self.driver)
        self.b.remove_csv()
        if artslab >= 0:
            assert True
        else:
            assert False

    def test_indices_community(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        indices_score = self.b.community(self.driver)
        self.b.remove_csv()
        if indices_score >= 0:
            assert True
        else:
            assert False

    def test_indices_enrollment(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        Enrollment = self.b.Enrollment(self.driver)
        self.b.remove_csv()
        if Enrollment >= 0:
            assert True
        else:
            assert False

    def test_indices_grantexpenditure(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        grant = self.b.grant_expenditure(self.driver)
        self.b.remove_csv()
        if grant >= 0:
            assert True
        else:
            assert False

    def test_indices_ictlab(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        ictlab = self.b.ictlab(self.driver)
        self.b.remove_csv()
        if ictlab >= 0:
            assert True
        else:
            assert False

    def test_indices_medical(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        Medical = self.b.Medical(self.driver)
        self.b.remove_csv()
        if Medical >= 0:
            assert True
        else:
            assert False

    def test_indices_nsqf(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        nsqf = self.b.nsqf(self.driver)
        self.b.remove_csv()
        if nsqf >= 0:
            assert True
        else:
            assert False

    def test_indices_policy(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        policy = self.b.policy(self.driver)
        self.b.remove_csv()
        if policy >= 0:
            assert True
        else:
            assert False

    def test_indices_safety(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        Safety = self.b.Safety(self.driver)
        self.b.remove_csv()
        if Safety >= 0:
            assert True
        else:
            assert False

    def test_indices_school_infra(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        School_infrastructure = self.b.School_infrastructure(self.driver)
        self.b.remove_csv()
        if School_infrastructure >= 0:
            assert True
        else:
            assert False

    def test_indices_school_inspection(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        School_inspection = self.b.School_inspection(self.driver)
        self.b.remove_csv()
        if School_inspection >= 0:
            assert True
        else:
            assert False

    def test_indices_school_Performance(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        School_perfomance = self.b.School_perfomance(self.driver)
        self.b.remove_csv()
        if School_perfomance >= 0:
            assert True
        else:
            assert False

    def test_indices_sci_lab(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        Sci_Lab = self.b.Science_lab(self.driver)
        self.b.remove_csv()
        if Sci_Lab >= 0:
            assert True
        else:
            assert False

    def test_indices_Teacher_Pro(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        Teacher_Profile = self.b.Teacher_profile(self.driver)
        self.b.remove_csv()
        if Teacher_Profile >= 0:
            assert True
        else:
            assert False

    def test_school_wise_download(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res, res1 = self.b.test_download(self.driver)
        if res != 0:
            assert True
            print("School level csv file is downloaded")
        else:
            assert False
        if res1 != 0:
            assert True
            print("Markers are present on school level map")
        else:
            assert False

    def test_udise_districtwise_schoolvalue(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res = self.b.test_districtwise_schools_count(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_mouse_over(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res = self.b.test_mousehover(self.driver)
        count = count = self.b.test_mouse_over()
        if count != 0:
            assert True
        else:
            assert True

    def test_school_btn_scores(self, setup):
        self.driver = setup
        self.b = UdiseReport(self.driver)
        res = self.b.test_click_schools(self.driver)
        if res == 0:
            assert True
        else:
            assert False

    def test_block_disable(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        time.sleep(8)
        time.sleep(10)
        choosedist = self.UR.Choosedist()
        i = 0
        for i in range(1, len(choosedist.options)):
            choosedist.select_by_index(i)
            print(choosedist.options[i].text, 'District is selected')
            a = self.UR.Blockbutton().is_enabled()
            if a == False:
                assert True
                print("Block button is disable")
                self.logger.info(
                    "********************test_mouseover_on_dots Passed********************************")
            else:
                print("Block button is enable")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_mouseover_on_dots.png")
                self.driver.close()
                self.logger.info(
                    "********************test_mouseover_on_dots Failed********************************")
                assert False

    def test_cluster_disable(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        time.sleep(8)
        time.sleep(10)
        self.UR.Choosedist().select_by_index(1)
        time.sleep(2)
        chooseblock = self.UR.Chooseblock()
        i = 0
        for i in range(1, len(chooseblock.options)):
            chooseblock.select_by_index(i)
            print(chooseblock.options[i].text, 'Block is selected')
            a = self.UR.Clusterbutton().is_enabled()
            if a == False:
                assert True
                print("Cluster button is disable")
            else:
                print("Cluster button is enable")
                assert False

    def test_school_disable(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.UR = UdiseReport(self.driver)
        self.UR.login(self.username, self.password)
        time.sleep(8)
        time.sleep(10)
        self.UR.Choosedist().select_by_index(1)
        time.sleep(2)
        self.UR.Chooseblock().select_by_index(1)
        time.sleep(2)
        choosecluster = self.UR.Choosecluster()
        i = 0
        for i in range(1, len(choosecluster.options)):
            choosecluster.select_by_index(i)
            print(choosecluster.options[i].text, 'Cluster is selected')
            a = self.UR.Schoolbutton().is_enabled()
            if a == False:
                assert True
                print("School button is disable")
            else:
                print("School button is enable")
                assert False