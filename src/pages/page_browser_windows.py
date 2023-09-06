from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class PageBrowserWindow(BasePage):
    button_new_tab = (By.CSS_SELECTOR, '#tabButton')
    header_new_tab = (By.CSS_SELECTOR, '#sampleHeading')
    button_new_window = (By.CSS_SELECTOR, '#windowButton')
    header_new_window = (By.CSS_SELECTOR, '#sampleHeading')

    def click_button_new_tab(self):
        self.find_element(PageBrowserWindow.button_new_tab).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.find_element(PageBrowserWindow.header_new_tab).text

    def click_button_new_window(self):
        self.find_element(PageBrowserWindow.button_new_window).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.find_element(PageBrowserWindow.header_new_window).text

