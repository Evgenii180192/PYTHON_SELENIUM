from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class PageRadioButton(BasePage):
    radio_button_yes = (By.XPATH, "//label[@for='yesRadio']")
    radio_button_impressive = (By.XPATH, "//label[@for='impressiveRadio']")
    text_result = (By.XPATH, "//span[@class='text-success']")

    def click_radio_button_yes(self):
        self.find_element(PageRadioButton.radio_button_yes).click()
        return self.find_element(PageRadioButton.text_result).text

    def click_radio_button_impressive(self):
        self.find_element(PageRadioButton.radio_button_impressive).click()
        return self.find_element(PageRadioButton.text_result).text
