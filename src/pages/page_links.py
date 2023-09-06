from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class PageLinks(BasePage):
    text_link_result = (By.XPATH, "//p[@id='linkResponse']")
    link_home = (By.XPATH, "//a[@id='simpleLink']")
    link_home_FOalt = (By.XPATH, "//a[@id='dynamicLink']")
    link_created = (By.XPATH, "//a[@id='created']")
    link_no_content = (By.XPATH, "//a[@id='no-content']")
    link_moved = (By.XPATH, "//a[@id='moved']")
    link_bad_request = (By.XPATH, "//a[@id='bad-request']")
    link_unauthorized = (By.XPATH, "//a[@id='unauthorized']")
    link_forbidden = (By.XPATH, "//a[@id='forbidden']")
    link_not_found = (By.XPATH, "//a[@id='invalid-url']")

    def following_link_home(self):
        self.find_element(PageLinks.link_home).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.driver.current_url
        return current_url

    def following_link_home_foalt(self):
        self.find_element(PageLinks.link_home_FOalt).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.driver.current_url
        return current_url

    def click_link_created(self):
        self.find_element(PageLinks.link_created).click()
        self.scroll_page()
        return self.find_element(PageLinks.text_link_result).text

    def click_link_no_content(self):
        self.find_element(PageLinks.link_no_content).click()
        self.scroll_page()
        return self.find_element(PageLinks.text_link_result).text

    def click_link_moved(self):
        self.find_element(PageLinks.link_moved).click()
        self.scroll_page()
        return self.find_element(PageLinks.text_link_result).text

    def click_link_bad_request(self):
        self.scroll_page()
        self.find_element(PageLinks.link_bad_request).click()
        return self.find_element(PageLinks.text_link_result).text

    def click_link_unauthorized(self):
        self.scroll_page()
        self.find_element(PageLinks.link_unauthorized).click()
        return self.find_element(PageLinks.text_link_result).text

    def click_link_forbidden(self):
        self.scroll_page()
        self.find_element(PageLinks.link_forbidden).click()
        return self.find_element(PageLinks.text_link_result).text

    def click_link_not_found(self):
        self.scroll_page()
        self.find_element(PageLinks.link_not_found).click()
        return self.find_element(PageLinks.text_link_result).text
