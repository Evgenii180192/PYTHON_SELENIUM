from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class PageModalDialogs(BasePage):
    button_small_modal = (By.CSS_SELECTOR, "#showSmallModal")
    small_modal_title = (By.CSS_SELECTOR, "#example-modal-sizes-title-sm")
    button_close_small_modal = (By.CSS_SELECTOR, "#closeSmallModal")
    button_large_modal = (By.CSS_SELECTOR, "#showLargeModal")
    large_modal_title = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    button_close_large_modal = (By.CSS_SELECTOR, "#closeLargeModal")

    def call_small_modal(self):
        self.find_element(PageModalDialogs.button_small_modal).click()
        text = self.find_element(PageModalDialogs.small_modal_title).text
        self.find_element(PageModalDialogs.button_close_small_modal).click()
        return text

    def call_large_modal(self):
        self.find_element(PageModalDialogs.button_large_modal).click()
        text = self.find_element(PageModalDialogs.large_modal_title).text
        self.find_element(PageModalDialogs.button_close_large_modal).click()
        return text
