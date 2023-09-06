from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class PageAlert(BasePage):
    first_button_click_me = (By.XPATH, "//button[@id='alertButton']")
    second_button_click_me = (By.CSS_SELECTOR, "#timerAlertButton")
    third_button_click_me = (By.CSS_SELECTOR, "#confirmButton")
    text_result = (By.CSS_SELECTOR, "#confirmResult")
    fours_button_click_me = (By.CSS_SELECTOR, "#promtButton")
    text_result_prompt = (By.CSS_SELECTOR, "#promptResult")

    def click_first_button_click_me(self):
        self.find_element(PageAlert.first_button_click_me).click()
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert

    def click_second_button_click_me(self):
        self.find_element(PageAlert.second_button_click_me).click()
        Wait(self.driver, timeout=6).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert

    def click_third_button_click_me(self):
        self.find_element(PageAlert.third_button_click_me).click()
        self.driver.switch_to.alert.accept()
        return self.find_element(PageAlert.text_result).text

    def click_fours_button_click_me(self):
        self.find_element(PageAlert.fours_button_click_me).click()
        self.driver.switch_to.alert.send_keys('Hello')
        self.driver.switch_to.alert.accept()
        return self.find_element(PageAlert.text_result_prompt).text


