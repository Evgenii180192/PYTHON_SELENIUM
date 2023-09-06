from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class PageUpload(BasePage):
    input_upload_file = (By.XPATH, "//input[@id='uploadFile']")
    text_result = (By.XPATH, "//p[@id='uploadedFilePath']")

    def upload_file(self):
        self.find_element(PageUpload.input_upload_file).send_keys(r"D:\Новый текстовый документ.txt")
        return self.find_element(PageUpload.text_result).text
