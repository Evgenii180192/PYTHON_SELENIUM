from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as es


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_browser(self):
        self.driver.get(self.url)

    def find_element(self, locator, timeout=3):
        return Wait(self.driver, timeout).until(es.visibility_of_element_located(locator))

    def find_elements(self, locator, timeout=3):
        return Wait(self.driver, timeout).until(es.visibility_of_all_elements_located(locator))

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove()")
        self.driver.execute_script('document.getElementById("fixedban").style.display = "none"')

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, 350);")
