import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_slider import PageSlider


@allure.feature('Testing the page radio slider')
@allure.story('Testing check to change value slider')
def test_validate_change_value_slider(driver):
    page_slider = PageSlider(driver, "https://demoqa.com/slider")
    with allure.step('Page loading  https://demoqa.com/slider'):
        page_slider.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_slider.check_value_slider() == '50'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_change_value_slider',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)