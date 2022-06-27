import os
import time
import pytest

from PageObjects.LoginPage import LoginPage
from Logs.Log import log_Details
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    usernameBlank = ReadConfig.getusernameBlank()
    passwordBlank = ReadConfig.getPasswordBlank()
    usernamewrong = ReadConfig.getusernamewrong()
    passwordwrong = ReadConfig.getpasswordwrong()

    logger = log_Details.logen()



    @pytest.mark.smoke
    def test_Login(self,setup):
        self.logger.info("********************verifying LoginPage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.username)
        password = self.lp.setPassword()
        password.send_keys(self.password)
        self.lp.loginbutton().click()
        time.sleep(7)
        a = self.driver.current_url
        if a == "https://demo4cqube.tibilprojects.com/#/home":
            assert True
            self.driver.close()
            self.logger.info("********************Test LoginPage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_Login.png")
            self.driver.close()
            self.logger.info("********************LoginPage Test Failed********************************")
            assert False


    def test_Login1(self,setup):
        self.logger.info("********************verifying LoginPage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.username)
        password = self.lp.setPassword()
        password.send_keys(self.passwordBlank)
        submit = self.lp.loginbutton().is_enabled()
        time.sleep(20)
        if submit == False:
            assert True
            self.driver.close()
            self.logger.info("********************Test LoginPage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots/" + "test_Login1.png")
            self.logger.info("********************LoginPage Test Failed********************************")
            self.driver.close()
            assert False

    def test_Login2(self,setup):
        self.logger.info("********************verifying LoginPage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.usernameBlank)
        password = self.lp.setPassword()
        password.send_keys(self.password)
        submit = self.lp.loginbutton().is_enabled()
        time.sleep(20)
        if submit == False:
            assert True
            self.driver.close()
            self.logger.info("********************Test LoginPage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots/" + "test_Login2.png")
            self.logger.info("********************LoginPage Test Failed********************************")
            self.driver.close()
            assert False


    def test_Login3(self,setup):
        self.logger.info("********************verifying LoginPage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.usernameBlank)
        password = self.lp.setPassword()
        password.send_keys(self.passwordBlank)
        submit = self.lp.loginbutton().is_enabled()
        time.sleep(20)
        if submit == False:
            assert True
            self.driver.close()
            self.logger.info("********************Test LoginPage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots/" + "test_Login3.png")
            self.logger.info("********************LoginPage Test Failed********************************")
            self.driver.close()
            assert False


    def test_Login4(self,setup):
        self.logger.info("********************verifying LoginPage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.usernamewrong)
        password = self.lp.setPassword()
        password.send_keys(self.password)
        self.lp.loginbutton().click()
        time.sleep(5)
        a = "please check user name and password"
        if a in self.driver.page_source:
            assert True
            self.driver.close()
            self.logger.info("********************Test LoginPage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots/" + "test_Login4.png")
            self.logger.info("********************LoginPage Test Failed********************************")
            self.driver.close()
            assert False

    def test_Login5(self,setup):
        self.logger.info("********************verifying LoginPage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.username)
        password = self.lp.setPassword()
        password.send_keys(self.passwordwrong)
        self.lp.loginbutton().click()
        time.sleep(5)
        a = "please check user name and password"
        if a in self.driver.page_source:
            assert True
            self.driver.close()
            self.logger.info("********************Test LoginPage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots/" + "test_Login5.png")
            self.logger.info("********************LoginPage Test Failed********************************")
            self.driver.close()
            assert False

    def test_Login6(self,setup):
        self.logger.info("********************verifying LoginPage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.usernamewrong)
        password = self.lp.setPassword()
        password.send_keys(self.passwordwrong)
        self.lp.loginbutton().click()
        time.sleep(5)
        a = "please check user name and password"
        if a in self.driver.page_source:
            assert True
            self.driver.close()
            self.logger.info("********************Test LoginPage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots/" + "test_Login6.png")
            self.logger.info("********************LoginPage Test Failed********************************")
            self.driver.close()
            assert False


    def test_Dashboard_button(self,setup):
        self.logger.info("********************verifying test_Dashboard_button ********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.username)
        password = self.lp.setPassword()
        password.send_keys(self.password)
        self.lp.loginbutton().click()
        time.sleep(5)
        self.lp.cQubeDashboard().click()
        time.sleep(5)
        a = self.driver.current_url
        if a == "https://demo4cqube.tibilprojects.com/#/dashboard/infrastructure-dashboard":
            assert True
            self.driver.close()
            self.logger.info("********************test_Dashboard_button Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/cQube-3.6/Screenshots" + "test_Dashboard_button.png")
            self.driver.close()
            self.logger.info("********************test_Dashboard_button Failed********************************")
            assert False

    def test_Logout(self,setup):
        self.logger.info("********************verifying test_Dashboard_button ********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        username = self.lp.setUserName()
        username.send_keys(self.username)
        password = self.lp.setPassword()
        password.send_keys(self.password)
        self.lp.loginbutton().click()
        time.sleep(5)
        self.lp.logout().click()
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

