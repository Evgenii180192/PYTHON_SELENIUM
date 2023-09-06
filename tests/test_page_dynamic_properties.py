import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_dynamic_properties import PageDynamicProperties


@allure.feature('Testing the page dynamic properties')
@allure.story('Testing visible element')
def test_validate_visible_element_page(driver):
    page_dynamic_properties = PageDynamicProperties(driver, "https://demoqa.com/dynamic-properties")
    with allure.step('Page loading  https://demoqa.com/dynamic-properties'):
        page_dynamic_properties.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_dynamic_properties.wait_visible_button() == "Visible After 5 Seconds"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_visible_element_page',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
