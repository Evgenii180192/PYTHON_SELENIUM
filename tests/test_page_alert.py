import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.pages.page_alert import PageAlert
from src.errors.errors import AssertError


@allure.feature('Testing the page alert')
@allure.story('Testing the first alert element')
def test_validate_click_first_button_click_me(driver):
    page_alert = PageAlert(driver, "https://demoqa.com/alerts")
    with allure.step('Page loading  https://demoqa.com/alerts'):
        page_alert.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_alert.click_first_button_click_me() == 'You clicked a button'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_first_button_click_me',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page alert')
@allure.story('Testing the second alert element')
def test_validate_click_second_button_click_me(driver):
    page_alert = PageAlert(driver, "https://demoqa.com/alerts")
    with allure.step('Page loading  https://demoqa.com/alerts'):
        page_alert.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_alert.click_second_button_click_me() == 'This alert appeared after 5 seconds'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_second_button_click_me',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page alert')
@allure.story('Testing the third alert element')
def test_validate_click_third_button_click_me(driver):
    page_alert = PageAlert(driver, "https://demoqa.com/alerts")
    with allure.step('Page loading  https://demoqa.com/alerts'):
        page_alert.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_alert.click_third_button_click_me() == 'You selected Ok'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_third_button_click_me',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page alert')
@allure.story('Testing the fours alert element')
def test_validate_click_fours_button_click_me(driver):
    page_alert = PageAlert(driver, "https://demoqa.com/alerts")
    with allure.step('Page loading  https://demoqa.com/alerts'):
        page_alert.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_alert.click_fours_button_click_me() == 'You entered Hello'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_fours_button_click_me',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
