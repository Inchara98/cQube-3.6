from selenium import webdriver
from Locators.Locators import Locator_Path

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.textbox_username_id)
        return a

    def setPassword(self):
        self.data = Locator_Path()
        b = self.driver.find_element_by_id(self.data.textbox_password_id)
        return b

    def loginbutton(self):
        self.data = Locator_Path()
        c = self.driver.find_element_by_id(self.data.Submit_button)
        return c

    def cQubeDashboard(self):
        self.data = Locator_Path()
        Dashboard = self.driver.find_element_by_id(self.data.cQube_Dashboard)
        return Dashboard

    def logout(self):
        self.data = Locator_Path()
        Logout = self.driver.find_element_by_id(self.data.logout)
        return Logout




