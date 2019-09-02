# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.registration import RegistrationHelper


class Controller:

    def __init__(self, browser_dir):
        self.driver = webdriver.Firefox(executable_path=browser_dir)
        self.driver.implicitly_wait(10)
        #self.driver.set_window_size(1900, 1020)
        self.vars = {}
        self.registration = RegistrationHelper(self)
        self.session = SessionHelper(self)

    def open_login_page(self):
        self.driver.get("https://rc.dev.avanpos.com/signin")

    # teardown
    def stop_driver(self):
        self.driver.quit()
