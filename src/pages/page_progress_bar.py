import time

from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class PageProgressBar(BasePage):
    button_start = (By.CSS_SELECTOR, "#startStopButton")
    result = (By.XPATH, "//div[@class='progress-bar bg-info']")

    def check_value_progress_bar(self):
        self.find_element(PageProgressBar.button_start).click()
        time.sleep(5)
        text = self.find_element(PageProgressBar.result).get_attribute('aria-valuenow')
        if text == '50%':
            self.find_element(PageProgressBar.button_start).click()
        result = text.replace("%", '')
        return int(result)
