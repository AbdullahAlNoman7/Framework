from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time


class RegisterPage(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_singup(self):
        # click the login/SingUp
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    def singup(self, name, email):
        time.sleep(5)
        # locate username and email input field
        userName_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Name']")
        email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
        singUp = self.driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")

        # check statement
        expected_title = self.driver.title
        actual_title_false = "Automation Exercise"
        actual_title = "Automation Exercise - Signup / Login"

        # check condition
        self.assertNotEqual(expected_title, actual_title_false)
        try:
            userName_field.clear()
            userName_field.send_keys(name)
        except:
            print("assert error for name field..")
        self.assertTrue(expected_title, actual_title)
        try:
            email_field.clear()
            email_field.send_keys(email)
        except:
            print("Email field error..")

        singUp.send_keys(Keys.RETURN)

    def afterClick_singup(self, password, firstName, lastName, company, address1, address2, state, city, zipcode,
                          mobileNumber):

        # locate account information
        title_filed_mr = self.wait.until(EC.presence_of_element_located((By.ID, "uniform-id_gender1")))
        password_field = self.driver.find_element(By.XPATH, "/html//input[@id='password']")

        # DOB
        days_field = self.driver.find_element(By.NAME, "days")
        month_field = self.driver.find_element(By.ID, "months")
        years_field = self.driver.find_element(By.ID, "years")

        # Address Information locate
        firstName_field = self.driver.find_element(By.ID, "first_name")
        lastName_field = self.driver.find_element(By.ID, "last_name")
        company_field = self.driver.find_element(By.ID, "company")
        address1_field = self.driver.find_element(By.NAME, "address1")
        address2_field = self.driver.find_element(By.NAME, "address2")
        country_field = self.driver.find_element(By.ID, "country")
        state_field = self.driver.find_element(By.ID, "state")
        city_field = self.driver.find_element(By.ID, "city")
        zipcode_field = self.driver.find_element(By.ID, "zipcode")
        mobileNumber_field = self.driver.find_element(By.ID, "mobile_number")
        clcik_create_account = self.driver.find_element(By.XPATH,"//button[normalize-space()='Create Account']")

        # condition check
        expected_title = self.driver.find_element(By.XPATH, "//b[normalize-space()='Enter Account Information']").text
        actual_title = "Enter Account Information"

        # enter all data field and check condition

        if title_filed_mr.is_displayed() and title_filed_mr.is_enabled() == True:
            title_filed_mr.click()
        self.assertTrue(expected_title, actual_title)
        password_field.send_keys(password)
        time.sleep(2)
        # DOB
        days_select = Select(days_field)
        for all_days in days_select.options:
            # print("Days ...", all_days.text)
            if all_days.text == "7":
                all_days.click()
                break
        time.sleep(2)
        months_select = Select(month_field)
        for all_months in months_select.options:
            # print("Months ...", all_months.text)
            if all_months.text == "April":
                all_months.click()
                break
        time.sleep(2)
        years_select = Select(years_field)
        for all_years in years_select.options:
            # print("Months ...", all_years.text)
            if all_years.text == "2020":
                all_years.click()
                break
        time.sleep(2)

        # address information entery
        if firstName_field.is_displayed():
            try:
                firstName_field.send_keys(firstName)
            except:
                print("Logical error firstName...")

        self.assertNotEqual(expected_title, actual_title, "Not matched..")
        try:
            lastName_field.send_keys(lastName)
        except:
            print("Logical error lastName...")

        if not company_field.is_selected():
            company_field.send_keys(company)
        else:
            print("Logical error company...")

        address1_field.clear()
        address1_field.send_keys(address1)
        address2_field.clear()
        address2_field.send_keys(address2)

        country_select = Select(country_field)
        for all_country in country_select.options:
            # print("Days ...", all_days.text)
            if all_country.text == "New Zealand":
                all_country.click()
                break

        state_field.send_keys(state)
        city_field.send_keys(city)
        zipcode_field.send_keys(zipcode)
        mobileNumber_field.send_keys(mobileNumber)
        clcik_create_account.click()
