# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class LoginHelper:
    GO_TO_REG_PAGE_BUTTON = "//div[@class='ToDoList']/button[text() = 'SIGN UP']"
    USERNAME_INPUT = "//input[@placeholder='LOGIN']"
    PASSWORD_INPUT = "//input[@placeholder='PASSWORD']"
    ENTER_BUTTON = "//div[@class='ToDoList']/button[text() = 'ENTER']"

    def __init__(self, controller):
        self.controller = controller

    def login(self, user):
        driver = self.controller.driver
        driver.find_element(By.XPATH, self.USERNAME_INPUT).click()
        driver.find_element(By.XPATH, self.USERNAME_INPUT).send_keys(user.name)
        driver.find_element(By.XPATH, self.PASSWORD_INPUT).click()
        driver.find_element(By.XPATH, self.PASSWORD_INPUT).send_keys(user.password)
        driver.find_element(By.XPATH, self.ENTER_BUTTON).click()

    def check_if_login_was_successful(self):
        driver = self.controller.driver
        assert "/todo" in driver.current_url

    def go_to_reg_page(self):
        driver = self.controller.driver
        driver.find_element(By.XPATH, self.GO_TO_REG_PAGE_BUTTON).click()
