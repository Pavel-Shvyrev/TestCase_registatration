# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class RegistrationHelper:
    SUBMIT_BUTTON = "button"
    USERNAME_INPUT = "//input[@placeholder='LOGIN']"
    PASSWORD_INPUT = "//input[@placeholder='PASSWORD']"
    DROPDOWN = "//mat-form-field/div"
    USER_DROPDOWN_ITEM = "//span[text() = 'USER']/.."
    ADMIN_DROPDOWN_ITEM = "//span[text() = 'ADMIN']/.."
    CURTAIN = "//div[@class = 'cdk-overlay-container']"
    USERNAME_EXIST_MESSAGE = "//*[text()='THIS USERNAME EXIST']"

    def __init__(self, controller):
        self.controller = controller

    # if the email is already registered, then add characters to the email field
    def check_waring_email_already_in_use(self):
        driver = self.controller.driver
        try:
            driver.find_element(By.XPATH, self.USERNAME_EXIST_MESSAGE).is_displayed()
            return True
        except NoSuchElementException:
            return False
            pass

    def click_registration_button(self):
        driver = self.controller.driver
        driver.find_element(By.CSS_SELECTOR, self.SUBMIT_BUTTON).click()

    def fill_registration_text_areas(self, user):
        driver = self.controller.driver

        # Fill textarea name
        driver.find_element(By.XPATH, self.USERNAME_INPUT).click()
        driver.find_element(By.XPATH, self.USERNAME_INPUT).send_keys(user.name)

        # Fill textarea password
        driver.find_element(By.XPATH, self.PASSWORD_INPUT).click()
        driver.find_element(By.XPATH, self.PASSWORD_INPUT).send_keys(user.password)

    def choose_roles(self):
        driver = self.controller.driver
        driver.find_element(By.XPATH, self.DROPDOWN).click()
        driver.find_element(By.XPATH, self.USER_DROPDOWN_ITEM).click()
        driver.find_element(By.XPATH, self.ADMIN_DROPDOWN_ITEM).click()
        driver.find_element(By.XPATH, self.CURTAIN).click()
