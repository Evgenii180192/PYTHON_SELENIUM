from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class PageDatePicker(BasePage):
    select_date = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
    month = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    month_january = (By.XPATH, "//option[@value='0']")
    year = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    year_1992 = (By.XPATH, "//option[@value='1992']")
    number = (
        By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--018 react-datepicker__day--weekend']")

    def filling_date(self):
        self.find_element(PageDatePicker.select_date).click()
        self.find_element(PageDatePicker.month).click()
        self.find_element(PageDatePicker.month_january).click()
        self.find_element(PageDatePicker.year).click()
        self.find_element(PageDatePicker.year_1992).click()
        self.find_element(PageDatePicker.number).click()
        return self.find_element(PageDatePicker.select_date).get_attribute("value")
