import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_progress_bar import PageProgressBar


@allure.feature('Testing the page progress bar')
@allure.story('Testing check value progress bar')
def test_validate_value_progress_bar(driver):
    page_progress_bar = PageProgressBar(driver, "https://demoqa.com/progress-bar")
    with allure.step('Page loading  https://demoqa.com/progress-bar'):
        page_progress_bar.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_progress_bar.check_value_progress_bar() == 50
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_value_progress_bar',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
