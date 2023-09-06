from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class PageSlider(BasePage):
    slider = (By.XPATH, "//input[@class='range-slider range-slider--primary']")
    slider_value = (By.CSS_SELECTOR, "#sliderValue")

    def check_value_slider(self):
        for i in range(25, 50):
            self.find_element(PageSlider.slider).send_keys(Keys.ARROW_RIGHT)
        return self.find_element(PageSlider.slider_value).get_attribute("value")



