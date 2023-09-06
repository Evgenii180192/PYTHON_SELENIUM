from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class PageDynamicProperties(BasePage):
    visible_button = (By.XPATH, "//button[@id='visibleAfter']")

    def wait_visible_button(self):
        try:
            Wait(self.driver, 5).until(EC.visibility_of_element_located(PageDynamicProperties.visible_button))
        except Exception:
            raise ValueError('The element did not appear on the page')
        return self.find_element(PageDynamicProperties.visible_button).text
