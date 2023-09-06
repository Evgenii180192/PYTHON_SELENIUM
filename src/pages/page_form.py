import os
import time
from random import randint

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.generator.generator import generator_user, generator_file
from src.pages.base_page import BasePage


class PageForm(BasePage):
    first_name = (By.XPATH, "//input[@id='firstName']")
    last_name = (By.XPATH, "//input[@id='lastName']")
    email = (By.XPATH, "//input[@id='userEmail']")
    gender = (By.XPATH, f"//label[@for='gender-radio-{randint(1, 3)}']")
    mobile_number = (By.XPATH, "//input[@id='userNumber']")
    subject = (By.CSS_SELECTOR, '#subjectsInput')
    hobbies = (By.XPATH, f"//label[@for='hobbies-checkbox-{randint(1, 3)}']")
    picture = (By.CSS_SELECTOR, '#uploadPicture')
    current_address = (By.XPATH, "//textarea[@id='currentAddress']")
    button_submit = (By.XPATH, "//button[@id='submit']")
    table_result = (By.XPATH, "//div[@class='table-responsive']//td[2]")

    def filling_form(self):
        user = generator_user()
        file = generator_file()
        self.remove_footer()
        self.find_element(PageForm.first_name).send_keys(user.first_name)
        self.find_element(PageForm.last_name).send_keys(user.last_name)
        self.find_element(PageForm.email).send_keys(user.email)
        self.scroll_page()
        self.find_element(PageForm.gender).click()
        self.find_element(PageForm.mobile_number).send_keys('1234567891')
        subject = self.find_element(PageForm.subject)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)
        self.find_element(PageForm.hobbies).click()
        self.find_element(PageForm.picture).send_keys(file)
        os.remove(file)
        self.find_element(PageForm.current_address).send_keys('Sviridova 28/56')
        self.find_element(PageForm.button_submit).click()
        return user

    def form_result(self):
        result_list = self.find_elements(PageForm.table_result)
        result_text = [i.text for i in result_list]
        return result_text
