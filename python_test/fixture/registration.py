# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class RegistrationHelper:

    def __init__(self, contrl):
        self.contrl = contrl

    # if the email is already registered, then add characters to the email field
    def check_waring_email_already_in_use(self, user):
        driver = self.contrl.driver
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/form/div[5]/p/a[1]").is_displayed()
            return True
        except:
            return False
            pass

    def compare_registration_message(self):
        driver = self.contrl.driver
        text_message = driver.find_element(By.XPATH,
                                           "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[4]/p[1]").text
        print (text_message)
        return text_message == str("Мы отправили письмо на указанную электронную почту. Для того, чтобы завершить регистрацию, перейдите по ссылке в письме. Ссылка будет работать 24 часа")

    def click_registration_button(self):
        driver = self.contrl.driver
        driver.find_element(By.CSS_SELECTOR, ".button").click()

    def fill_registration_textareas(self, user):
        driver = self.contrl.driver
        # Fill textarea company
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").send_keys(user.company_name)
        # Fill textarea name
        driver.find_element(By.NAME, "name").click()
        driver.find_element(By.NAME, "name").send_keys(user.user_name)
        # Fill textarea surname
        driver.find_element(By.NAME, "surname").click()
        driver.find_element(By.NAME, "surname").send_keys(user.user_surname)
        # Fill textarea phone number
        driver.find_element(By.NAME, "phone").click()
        driver.find_element(By.NAME, "phone").send_keys(user.phone)
        # Fill textarea email
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").send_keys(user.email)
        # Fill textarea password
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys(user.password)

    def go_to_reg_page(self):
        driver = self.contrl.driver
        driver.find_element(By.CSS_SELECTOR, ".link-action:nth-child(2)").click()
