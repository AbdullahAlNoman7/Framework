import time

from selenium.webdriver.common.by import By


class LoginPage:

    global drive
    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        user_name_field = self.driver.find_element(By.NAME, "username")
        user_name_field.send_keys(username)
        time.sleep(2)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        time.sleep(2)

        login_button = self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
        login_button.click()
