from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest
import time

# import login page
from Pages.login import LoginPage
from Utils import excel_utils


class LoginTest(unittest.TestCase):
    global driver

    def test_login(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://automationexercise.com/")

        # excel implement
        file = "G:\\SQA\\Ecommarce\\Data\\Data.xlsx"
        sheet = "Login"
        numbers_of_rows = excel_utils.get_row_count(file,sheet)

        for r in range(2,numbers_of_rows+1):
            email_filed_data = excel_utils.read_data(file,sheet,r,1)
            password_field_data = excel_utils.read_data(file,sheet,r,2)

            lg_obg = LoginPage(driver)
            lg_obg.login(email_filed_data,password_field_data)

        print(driver.title)
