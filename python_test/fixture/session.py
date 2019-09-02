# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, contrl):
        self.contrl = contrl

    def login(self, user):
        driver = self.contrl.driver
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").send_keys(user.email)
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys(user.password)
        driver.find_element(By.CSS_SELECTOR, ".full").click()

    def logout(self):
        driver = self.contrl.driver
        try:
            driver.find_element(By.CSS_SELECTOR, ".icon-logout").click()
        except:
            # click button accessibly
            driver.find_element(By.CSS_SELECTOR, ".middle").click()
            # click exit button
            driver.find_element(By.CSS_SELECTOR, ".icon-logout").click()

