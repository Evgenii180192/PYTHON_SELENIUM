import allure
from allure_commons.types import AttachmentType
from src.conftest.conftest import driver
from src.errors.errors import AssertError
from src.pages.page_buttons import PageButtons


@allure.feature('Testing the page buttons')
@allure.story('Testing the button double click element')
def test_validate_double_click(driver):
    page_buttons = PageButtons(driver, "https://demoqa.com/buttons")
    with allure.step('Page loading  https://demoqa.com/buttons'):
        page_buttons.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_buttons.double_click() == 'You have done a double click'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_double_click',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page buttons')
@allure.story('Testing the button right click element')
def test_validate_right_click(driver):
    page_buttons = PageButtons(driver, "https://demoqa.com/buttons")
    with allure.step('Page loading  https://demoqa.com/buttons'):
        page_buttons.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_buttons.right_click() == 'You have done a right click'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_right_click',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page buttons')
@allure.story('Testing the button left click element')
def test_validate_left_click(driver):
    page_buttons = PageButtons(driver, "https://demoqa.com/buttons")
    with allure.step('Page loading  https://demoqa.com/buttons'):
        page_buttons.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_buttons.left_click() == 'You have done a dynamic click'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_left_click',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
