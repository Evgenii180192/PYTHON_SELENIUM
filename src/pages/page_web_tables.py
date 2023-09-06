from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class PageWebTables(BasePage):
    button_add = (By.XPATH, "//button[@id='addNewRecordButton']")
    first_name = (By.XPATH, "//input[@id='firstName']")
    last_name =(By.XPATH, "//input[@id='lastName']")
    email = (By.XPATH, "//input[@id='userEmail']")
    age = (By.XPATH, "//input[@id='age']")
    salary = (By.XPATH, "//input[@id='salary']")
    department = (By.XPATH, "//input[@id='department']")
    button_submit = (By.XPATH, "//button[@id='submit']")
    result_name = (By.XPATH, "//div[@class='rt-td' and text()='Evgenii']")

    def add_user_web_tables(self):
        self.find_element(PageWebTables.button_add).click()
        self.find_element(PageWebTables.first_name).send_keys('Evgenii')
        self.find_element(PageWebTables.last_name).send_keys('Sergejchenko')
        self.find_element(PageWebTables.email).send_keys('sevgeniiv92@mail.ru')
        self.find_element(PageWebTables.age).send_keys(31)
        self.find_element(PageWebTables.salary).send_keys(1400)
        self.find_element(PageWebTables.department).send_keys('Security')
        self.find_element(PageWebTables.button_submit).click()
        return self.find_element(PageWebTables.result_name).text