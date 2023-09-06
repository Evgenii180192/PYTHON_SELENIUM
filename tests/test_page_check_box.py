import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_check_box import PageCheckBox


@allure.feature('Testing the page check box')
@allure.story('Testing click check box element')
def test_validate_click_check_box(driver):
    page_check_box = PageCheckBox(driver, "https://demoqa.com/checkbox")
    with allure.step('Page loading  https://demoqa.com/checkbox'):
        page_check_box.open_browser()
    page_check_box.click_check_box()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_check_box.check_result().text == 'You have selected :'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_check_box',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
