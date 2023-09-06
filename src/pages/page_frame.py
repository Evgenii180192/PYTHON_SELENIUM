from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class PageFrame(BasePage):
    frame_title = (By.XPATH, "//h1[@id='sampleHeading']")

    def switch_to_frame_one(self):
        Wait(self.driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#frame1")))
        return self.find_element(PageFrame.frame_title).text

    def switch_to_frame_two(self):
        self.remove_footer()
        self.scroll_page()
        Wait(self.driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#frame2")))
        return self.find_element(PageFrame.frame_title).text
