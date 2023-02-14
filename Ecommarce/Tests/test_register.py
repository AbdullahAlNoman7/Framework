from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest
import time

# import page
from Pages.Register_page import RegisterPage
from Utils import excel_utils


class RegisterTest(unittest.TestCase):
    global driver

    def test_register(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://automationexercise.com/")

        # excel implement
        file = "G:\\SQA\\Ecommarce\\Data\\Data.xlsx"
        sheet = "Register"

        numbers_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, numbers_of_rows + 1):
            userName_data = excel_utils.read_data(file, sheet, r, 1)
            email_data = excel_utils.read_data(file, sheet, r, 2)
            password_data = excel_utils.read_data(file, sheet, r, 3)
            firstname_data = excel_utils.read_data(file, sheet, r, 4)
            lastname_data = excel_utils.read_data(file, sheet, r, 5)
            company_data = excel_utils.read_data(file, sheet, r, 6)
            address1_data = excel_utils.read_data(file, sheet, r, 7)
            address2_data = excel_utils.read_data(file, sheet, r, 8)
            state_data = excel_utils.read_data(file, sheet, r, 9)
            city_data = excel_utils.read_data(file, sheet, r, 10)
            zipcode_data = excel_utils.read_data(file, sheet, r, 11)
            mobile_data = excel_utils.read_data(file, sheet, r, 12)

            reg_obj = RegisterPage(driver)
            reg_obj.click_singup()
            reg_obj.singup(userName_data, email_data)
            reg_obj.afterClick_singup(password_data, firstname_data, lastname_data, company_data, address1_data,
                                      address2_data, state_data
                                      , city_data, zipcode_data, mobile_data)

        print(driver.title)
        driver.close()
