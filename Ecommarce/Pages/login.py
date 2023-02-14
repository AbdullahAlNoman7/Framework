from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        # click the login/SingUp
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
        password_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        click_login = self.driver.find_element(By.CSS_SELECTOR,".login-form > form[method='post'] > .btn.btn-default")

        # check statement
        expected_title = self.driver.title
        actual_title = "Automation Exercise - Signup / Login"

        if expected_title==actual_title:
            email_field.send_keys(email)
        if expected_title==actual_title:
            password_field.send_keys(password)
        click_login.click()