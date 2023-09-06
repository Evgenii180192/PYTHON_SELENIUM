import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_radio_button import PageRadioButton


@allure.feature('Testing the page radio button')
@allure.story('Testing check click radio button yes')
def test_validate_click_radio_button_yes(driver):
    page_radio_button = PageRadioButton(driver, "https://demoqa.com/radio-button")
    with allure.step('Page loading  https://demoqa.com/progress-bar'):
        page_radio_button.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_radio_button.click_radio_button_yes() == 'Yes'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_radio_button_yes',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page radio button')
@allure.story('Testing check click radio button impressive')
def test_validate_click_radio_button_impressive(driver):
    page_radio_button = PageRadioButton(driver, "https://demoqa.com/radio-button")
    with allure.step('Page loading  https://demoqa.com/progress-bar'):
        page_radio_button.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_radio_button.click_radio_button_impressive() == 'Impressive'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_radio_button_impressive',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
