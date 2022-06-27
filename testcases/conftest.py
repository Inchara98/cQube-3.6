from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
@pytest.fixture()

# def setup(browser):
#     chromeOptions = Options()
#     chromeOptions.add_experimental_option("prefs",
#                                           {"download.default_directory": "/home/inchara/PycharmProjects/cQube-3.6/Downloads/"})
#     chromeOptions.add_argument("--window-size=3860,2160")
#     # chromeOptions.add_argument('--headless')
#     chromeOptions.add_argument('--no-sandbox')
#     chromeOptions.add_argument('--disable-gpu')
#     if browser == 'chrome':
#         driver = webdriver.Chrome(executable_path="/home/inchara/PycharmProjects/cQube-3.6/driver/chromedriver",
#                                   chrome_options=chromeOptions)
#         print("Launching chrome browser.......")
#         return driver
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(executable_path="/home/inchara/PycharmProjects/PDS/driver/geckodriver")
#         print("Launching firefox browser.......")
#         return driver
def setup():
    chromeOptions = Options()
    chromeOptions.add_experimental_option("prefs",
                                          {"download.default_directory": "/home/inchara/PycharmProjects/cQube-3.6/Downloads/"})
    chromeOptions.add_argument("--window-size=3860,2160")
    # chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="/home/inchara/PycharmProjects/cQube-3.6/driver/chromedriver", chrome_options=chromeOptions)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report #############
#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'cQube'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Inchara'


#It is hook for delete/modify Environment info to Html Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)


