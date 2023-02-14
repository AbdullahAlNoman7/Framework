import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Pages.login_page_HRM import LoginPage
from Utils import excel_utlis


class LoginTest(unittest.TestCase):
    global driver

    def test_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        # Excel implementation
        file = "G:\\SQA\\Framework\\Data\\Data.xlsx"
        sheet = 'Sheet1'

        number_of_rows = excel_utlis.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utlis.read_data(file, sheet, r, 1)
            password = excel_utlis.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_orange(username, password)

        driver.close()
