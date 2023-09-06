from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class PageNestedFrames(BasePage):
    frame_title = (By.XPATH, "//body")

    def switch_to_frame_outer(self):
        self.remove_footer()
        Wait(self.driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#frame1")))
        return self.find_element(PageNestedFrames.frame_title).text

    def switch_to_frame_inner(self):
        self.remove_footer()
        Wait(self.driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#frame1")))
        Wait(self.driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")))
        return self.find_element(PageNestedFrames.frame_title).text

