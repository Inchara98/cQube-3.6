import configparser
import os
import time

config=configparser.RawConfigParser()
config.read("/home/inchara/PycharmProjects/cQube-3.6/Configurations/config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info', 'baseUrl')
        return url

    @staticmethod
    def getUserID():
        username = config.get('common_info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def getusernameBlank():
        usernameBlank = config.get('common_info', 'usernameBlank')
        return usernameBlank

    @staticmethod
    def getPasswordBlank():
        passwordBlank = config.get('common_info', 'passwordBlank')
        return passwordBlank

    @staticmethod
    def getusernamewrong():
        usernamewrong = config.get('common_info', 'usernamewrong')
        return usernamewrong

    @staticmethod
    def getpasswordwrong():
        passwordwrong = config.get('common_info', 'passwordwrong')
        return passwordwrong

    @staticmethod
    def getState():
        State = config.get('common_info', 'State')
        return State

    # def get_driver(self):
    #     options = webdriver.ChromeOptions()
    #     prefs = {'download.default_directory': self.p.get_download_dir()}
    #     options.add_experimental_option('prefs', prefs)
    #     options.add_argument("--window-size=3860,2160")
    #     options.add_argument('--headless')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-gpu')
    #     self.driver = webdriver.Chrome(options=options, executable_path=self.p.get_driver_path())
    #     self.driver.set_window_size(3860, 2160)
    #     print('window size :',self.driver.get_window_size())
    #     print("Current session is {}".format(self.driver.session_id))
    #     return self.driver

