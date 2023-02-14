from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest
import time

# implement add product page
from Pages.add_product_page import AddProduct
from Pages.login import LoginPage


class TestAddProduct(unittest.TestCase):
    global driver

    def test_add_product(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://automationexercise.com/")

        # login object
        login_obj = LoginPage(driver)
        login_obj.login("sagor@gmail.com", "123@456")

        # add product object
        add_product_obj = AddProduct(driver)
        add_product_obj.add_product()
        add_product_obj.view_product()
