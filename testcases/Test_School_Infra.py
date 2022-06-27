import os
import time
import pytest

from Logs.Log import log_Details
from utilities.readProperties import ReadConfig
from PageObjects.School_Infra import SchoolInfra


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    state = ReadConfig.getState()

    logger = log_Details.logen()


    @pytest.mark.smoke
    def test_Back_Button(self,setup):
        self.logger.info("********************verifying Back_Button Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username,self.password)
        self.SI.Backbutton().click()
        time.sleep(5)
        a = self.driver.current_url
        if a == "https://demo4cqube.tibilprojects.com/#/home":
            assert True
            self.driver.close()
            self.logger.info("********************test_Back_Button Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_Back_Button.png")
            self.driver.close()
            self.logger.info("********************test_Back_Button Failed********************************")
            assert False

    def test_logout(self,setup):
        self.logger.info("********************verifying Back_Button Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(3)
        self.SI.logout().click()
        a = self.driver.current_url
        if a == "https://demo4cqube.tibilprojects.com/#/signin":
            assert True
            self.driver.close()
            self.logger.info("********************test_Logout Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_Logout.png")
            self.driver.close()
            self.logger.info("********************test_Logout Failed********************************")
            assert False


    def test_InfraMap(self,setup):
        self.logger.info("********************verifying Back_Button Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(10)
        self.SI.InfraMap().click()
        b = "Report on Infrastructure access by location for:"
        if b in self.driver.page_source:
            assert True
            self.driver.close()
            self.logger.info("********************test_InfraMap Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_InfraMap.png")
            self.driver.close()
            self.logger.info("********************test_InfraMap Failed********************************")
            assert False



    def test_HyperLink(self,setup):
        self.logger.info("********************verifying Hyperlink Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(5)
        self.SI.InfraMap().click()
        time.sleep(5)
        expected = "Report on Infrastructure access by location for: " + self.state
        actual = self.SI.HyperLink()
        if expected == actual:
            assert True
            self.driver.close()
            self.logger.info("********************test_HyperLink Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_HyperLink.png")
            self.driver.close()
            self.logger.info("********************test_HyperLink Failed********************************")
            assert False


    def test_click_on_block(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        res1, res2 = self.b.test_Block_button(self.driver)
        if res1 != 0:
            assert True
            print('Markers are present on map ')
            self.logger.info("********************test_click_on_block Passed********************************")
        else:
            print("Markers are not present in the map ")
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_block.png")
            self.logger.info("********************test_click_on_block Failed********************************")
            assert False
        if res2 == True:
            assert True
            print('Block wise csv file downloaded...')
            self.logger.info("********************test_click_on_block Passed********************************")
        else:
            print("Block wise csv file not downloaded...")
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_block.png")
            self.driver.close()
            self.logger.info("********************test_click_on_block Failed********************************")
            assert False


    def test_click_on_cluster(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        res1, res2 = self.b.test_Cluster_button(self.driver)
        if res1 != 0:
            assert True
            print('Markers are present on map ')
            self.logger.info("********************test_click_on_cluster Passed********************************")
        else:
            print("Markers are not present in the map ")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_cluster.png")
            self.logger.info("********************test_click_on_block Failed********************************")
            assert False
        if res2 == True:
            assert True
            print('Cluster wise csv file downloaded...')
            self.logger.info("********************test_click_on_cluster Passed********************************")
        else:
            print("Cluster wise csv file not downloaded...")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_cluster.png")
            self.driver.close()
            self.logger.info("********************test_click_on_cluster Failed********************************")
            assert False


    def test_click_on_school(self,setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        res1, res2 = self.b.test_School_button(self.driver)
        if res1 != 0:
            assert True
            print('Markers are present on map ')
            self.logger.info("********************test_click_on_school Passed********************************")
        else:
            print("Markers are not present in the map ")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_cluster.png")
            self.logger.info("********************test_click_on_school Failed********************************")
            assert False
        if res2 == True:
            assert True
            print('School wise csv file downloaded...')
            self.logger.info("********************test_click_on_school Passed********************************")
        else:
            print("School wise csv file not downloaded...")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_cluster.png")
            self.driver.close()
            self.logger.info("********************test_click_on_school Failed********************************")
            assert False

    def test_no_of_schools(self,setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        r, r1, r2, r3 = self.b.test_check_total_schoolvalue(self.driver)
        if int(r) == int(r1):
            assert True
            self.logger.info("********************test_no_of_schools Passed********************************")
            print("No of school in block level is matching")
        else:
            print("No of school in block level is not matching")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_no_of_schools.png")
            self.logger.info("********************test_no_of_schools Failed********************************")
            assert False
        if int(r) == int(r2):
            assert True
            print("No of school in cluster level is matching")
            self.logger.info("********************test_no_of_schools Passed********************************")
        else:
            print("No of school in cluster level is not matching")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_no_of_schools.png")
            self.logger.info("********************test_no_of_schools Failed********************************")
            assert False
        if int(r) == int(r3):
            assert True
            print("No of school in school level is matching")
            self.logger.info("********************test_click_on_school Passed********************************")
        else:
            print("No of school in school level is not matching")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_cluster.png")
            self.logger.info("********************test_click_on_school Failed********************************")
            self.driver.close()
            assert False
        self.b.page_loading(self.driver)
        print("checked with comapared with footer values ")

    def test_click_on_block_cluster_school(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        res1, res2 = self.b.test_Block_button(self.driver)
        if res1 != 0:
            assert True
            print('Markers are present on map ')
            self.logger.info("********************test_click_on_block_cluster_school Passed********************************")
        else:
            print("Markers are not present in the map ")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_block_cluster_school.png")
            self.logger.info("********************test_click_on_block_cluster_school Failed********************************")
            assert False
        if res2 == True:
            assert True
            print('Block wise csv file downloaded...')
            self.logger.info("********************test_click_on_block_cluster_school Passed********************************")
        else:
            print("Block wise csv file not downloaded...")
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_block_cluster_school.png")
            self.driver.close()
            self.logger.info("********************test_click_on_block_cluster_school Failed********************************")
            assert False



    def test_infrascore(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        infra_score = self.b.infra_score_dropdown(self.driver)
        self.b.remove_csv()
        if infra_score >= 0:
            assert True
            print("Passed")
            self.logger.info(
                "********************test_infrascore Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_infrascore.png")
            self.driver.close()
            self.logger.info(
                "********************test_infrascore Failed********************************")
            assert False

    def test_access_to_toilet(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        AccessToToilet = self.b.Access_to_toilet(self.driver)
        self.b.remove_csv()
        if AccessToToilet >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_access_to_toilet Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_access_to_toilet.png")
            self.driver.close()
            self.logger.info(
                "********************test_access_to_toilet Failed********************************")
            assert False


    def test_access_to_water(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        AccessToWater = self.b.Access_to_water(self.driver)
        self.b.remove_csv()
        if AccessToWater >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_access_to_water Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_access_to_water.png")
            self.driver.close()
            self.logger.info(
                "********************test_access_to_water Failed********************************")
            assert False

    def test_boy_toilet(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        boy_toilet = self.b.Boys_toilet_percentage(self.driver)
        self.b.remove_csv()
        if boy_toilet >= 0:
            assert True
            print("Passed")
            self.logger.info(
                "********************test_boy_toilet Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_boy_toilet.png")
            self.driver.close()
            self.logger.info(
                "********************test_boy_toilet Failed********************************")
            assert False


    def test_drinking_water(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        drinking_water = self.b.drinking_water(self.driver)
        self.b.remove_csv()
        if drinking_water >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_drinking_water Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_drinking_water.png")
            self.driver.close()
            self.logger.info(
                "********************test_drinking_water Failed********************************")
            assert False

    def test_Electricity(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        Electricity = self.b.Electricity(self.driver)
        self.b.remove_csv()
        if Electricity >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_Electricity Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_Electricity.png")
            self.driver.close()
            self.logger.info(
                "********************test_Electricity Failed********************************")
            assert False

    def test_girls_toilet(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        girls_toilet = self.b.girls_toilet(self.driver)
        self.b.remove_csv()
        if girls_toilet >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_girls_toilet Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_girls_toilet.png")
            self.driver.close()
            self.logger.info(
                "********************test_girls_toilet Failed********************************")
            assert False

    def test_handpump(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        Handpump = self.b.Handpump(self.driver)
        self.b.remove_csv()
        if Handpump >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_handpump Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_handpump.png")
            self.driver.close()
            self.logger.info(
                "********************test_handpump Failed********************************")
            assert False


    def test_handwash(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        Handwash = self.b.Handwash(self.driver)
        self.b.remove_csv()
        if Handwash >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_handwash Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_handwash.png")
            self.driver.close()
            self.logger.info(
                "********************test_handwash Failed********************************")
            assert False

    def test_library(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        Library = self.b.Library(self.driver)
        self.b.remove_csv()
        if Library >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_library Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_library.png")
            self.driver.close()
            self.logger.info(
                "********************test_library Failed********************************")
            assert False


    def test_solar_panel(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        Solar_panel = self.b.Solar_panel(self.driver)
        self.b.remove_csv()
        if Solar_panel >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_solar_panel Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_solar_panel.png")
            self.driver.close()
            self.logger.info(
                "********************test_solar_panel Failed********************************")
            assert False


    def test_tapwater(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        Tapwater = self.b.Tapwater(self.driver)
        self.b.remove_csv()
        if Tapwater >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_tapwater Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_tapwater.png")
            self.driver.close()
            self.logger.info(
                "********************test_tapwater Failed********************************")
            assert False


    def test_toilet(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        Toilet = self.b.Toilet(self.driver)
        self.b.remove_csv()
        if Toilet >= 0:
            assert True
            print("passed")
            self.logger.info(
                "********************test_toilet Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_toilet.png")
            self.driver.close()
            self.logger.info(
                "********************test_toilet Failed********************************")
            assert False


    def test_infrascores_dropdown(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        res = self.b.test_infrascores(self.driver)
        if res != 0:
            assert True
            print("checked with infra scores options")
            self.logger.info(
                "********************test_infrascores_dropdown Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_infrascores_dropdown.png")
            self.driver.close()
            self.logger.info(
                "********************test_infrascores_dropdown Failed********************************")
            assert False

    def test_districtwise_download(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        res = self.b.test_download(self.driver)
        if res == 0:
            assert True
            self.logger.info(
                "********************test_districtwise_download Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_districtwise_download.png")
            self.driver.close()
            self.logger.info(
                "********************test_districtwise_download Failed********************************")
            assert False

    def test_schools_per_cluster_csv_download1(self, setup):
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        result = self.b.check_download_csv1(self.driver)
        if result == 0:
            assert True
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
            self.logger.info(
                "********************test_schools_per_cluster_csv_download1 Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_schools_per_cluster_csv_download1.png")
            self.driver.close()
            self.logger.info(
                "********************test_schools_per_cluster_csv_download1 Failed********************************")
            assert False

    def test_click_on_home(self, setup):
        print("check with footer values")
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        c1, c2, c3 = self.b.test_home(self.driver)
        if c1 != 0:
            assert True
            print("Records are present on the map")
            self.logger.info(
                "********************test_click_on_home Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_home.png")
            self.logger.info(
                "********************test_click_on_home Failed********************************")
            assert False
        if c2 != 0:
            assert True
            print("Records are present on the map")
            self.logger.info(
                "********************test_click_on_home Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_home.png")
            self.logger.info(
                "********************test_click_on_home Failed********************************")
            assert False
        if c3 != 0:
            assert True
            print("Records are present on the map")
            self.logger.info(
                "********************test_click_on_home Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_click_on_home.png")
            self.driver.close()
            self.logger.info(
                "********************test_click_on_home Failed********************************")
            assert False


    def test_mouseover_on_dots(self, setup):
        print("mouseover on markers present on map")
        self.driver = setup
        self.b = SchoolInfra(self.driver)
        res = self.b.test_mousehover(self.driver)
        count = self.b.test_mouse_over()
        if count != 0:
            assert True
            print("markers present in map")
            self.logger.info(
                "********************test_mouseover_on_dots Passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_mouseover_on_dots.png")
            self.driver.close()
            self.logger.info(
                "********************test_mouseover_on_dots Failed********************************")
            assert False

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
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.SI.Choosedist().select_by_index(1)
        time.sleep(2)
        chooseblock = self.SI.Chooseblock()
        i = 0
        for i in range(1,len(chooseblock.options)):
            chooseblock.select_by_index(i)
            print(chooseblock.options[i].text, 'Block is selected')
            a = self.SI.Clusterbutton().is_enabled()
            if a == False:
                assert True
                print("Cluster button is disable")
            else:
                print("Cluster button is enable")
                assert False

    def test_school_disable(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.SI = SchoolInfra(self.driver)
        self.SI.login(self.username, self.password)
        time.sleep(8)
        self.SI.InfraMap().click()
        time.sleep(10)
        self.SI.Choosedist().select_by_index(1)
        time.sleep(2)
        self.SI.Chooseblock().select_by_index(1)
        time.sleep(2)
        choosecluster = self.SI.Choosecluster()
        i = 0
        for i in range(1,len(choosecluster.options)):
            choosecluster.select_by_index(i)
            print(choosecluster.options[i].text, 'Cluster is selected')
            a = self.SI.Schoolbutton().is_enabled()
            if a == False:
                assert True
                print("School button is disable")
            else:
                print("School button is enable")
                assert False






        










