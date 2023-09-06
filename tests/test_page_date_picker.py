import allure
from allure_commons.types import AttachmentType
from src.conftest.conftest import driver
from src.errors.errors import AssertError
from src.pages.page_date_picker import PageDatePicker


@allure.feature('Testing the page date picker')
@allure.story('Testing input date element')
def test_validate_filling_date(driver):
    page_date_picker = PageDatePicker(driver, "https://demoqa.com/date-picker")
    with allure.step('Page loading  https://demoqa.com/date-picker'):
        page_date_picker.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_date_picker.filling_date() == "01/18/1992"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_filling_date',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
