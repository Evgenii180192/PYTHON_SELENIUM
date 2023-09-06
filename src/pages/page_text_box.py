from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class PageTextBox(BasePage):
    full_name = (By.XPATH, "//input[@id='userName']")
    email = (By.XPATH, "//input[@id='userEmail']")
    current_address = (By.XPATH, "//textarea[@id='currentAddress']")
    permanent_address = (By.XPATH, "//textarea[@id='permanentAddress']")
    submit = (By.XPATH, "//button[@id='submit']")
    result_block = (By.XPATH, "//div[@class='border col-md-12 col-sm-12']")
    result_name = (By.XPATH, "//p[@id='name']")
    result_email = (By.XPATH, "//p[@id='email']")
    result_current_address = (By.XPATH, "//p[@id='currentAddress']")
    result_permanent_address = (By.XPATH, "//p[@id='permanentAddress']")

    def filling_inputs(self):
        self.find_element(PageTextBox.full_name).send_keys('Evgenii')
        self.find_element(PageTextBox.email).send_keys('sevgeniiv92@mail.ru')
        self.find_element(PageTextBox.current_address).send_keys('Republic of Belarus, Gomel')
        self.scroll_page()
        self.find_element(PageTextBox.permanent_address).send_keys('Sviridova 28/56')
        self.find_element(PageTextBox.submit).click()

    def check_visible_block_border(self):
        return self.find_element(PageTextBox.result_block)

    def check_value_name_block_border(self):
        return self.find_element(PageTextBox.result_name)

    def check_value_email_block_border(self):
        return self.find_element(PageTextBox.result_email)
