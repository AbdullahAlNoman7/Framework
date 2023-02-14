from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time


class AddProduct:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_product(self):
        # click product
        self.driver.find_element(By.XPATH, "//a[@href='/products']").click()
        # click men and filter
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Men']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Tshirts']").click()

    def view_product(self):
        self.driver.find_element(By.CSS_SELECTOR, "[href='\/product_details\/2']").click()
