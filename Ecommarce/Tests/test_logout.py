from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest
import time

# import page
from Pages.logout import LogOutPage
from Pages.login import LoginPage


class LogOut(unittest.TestCase):
    global driver

    def test_logout(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://automationexercise.com/")

        # login object
        login_obj = LoginPage(driver)
        login_obj.login("sagor@gmail.com", "123@456")
        # logout object
        logout_obj = LogOutPage(driver)
        time.sleep(2)
        print(driver.title)
        logout_obj.logout()
