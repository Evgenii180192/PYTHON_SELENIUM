from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class PageCheckBox(BasePage):
    input_check_box = (By.XPATH, "//span[@class='rct-checkbox']")
    result = (By.XPATH, "//span[text() = 'You have selected :']")

    def click_check_box(self):
        self.find_element(PageCheckBox.input_check_box).click()

    def check_result(self):
        return self.find_element(PageCheckBox.result)
