import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class PageButtons(BasePage):
    button_double_click = (By.XPATH, "//button[text()='Double Click Me']")
    text_after_double_click = (By.XPATH, "//p[@id='doubleClickMessage']")
    button_right_click = (By.XPATH, "//button[@id='rightClickBtn']")
    text_after_right_click = (By.XPATH, "//p[@id='rightClickMessage']")
    button_click = (By.XPATH, "//button[text()='Click Me']")
    text_after_left_click = (By.XPATH, "//p[@id='dynamicClickMessage']")

    def double_click(self):
        action = ActionChains(self.driver)
        double_click = self.find_element(PageButtons.button_double_click)
        action.double_click(double_click).perform()
        return self.find_element(PageButtons.text_after_double_click).text

    def right_click(self):
        action = ActionChains(self.driver)
        right_click = self.find_element(PageButtons.button_right_click)
        action.context_click(right_click).perform()
        return self.find_element(PageButtons.text_after_right_click).text

    def left_click(self):
        self.find_element(PageButtons.button_click).click()
        return self.find_element(PageButtons.text_after_left_click).text
