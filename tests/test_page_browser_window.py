import allure
from allure_commons.types import AttachmentType
from src.conftest.conftest import driver
from src.pages.page_browser_windows import PageBrowserWindow
from src.errors.errors import AssertError


@allure.feature('Testing the page browser window')
@allure.story('Testing the new tab element')
def test_validate_click_button_new_tab(driver):
    page_browser_window = PageBrowserWindow(driver, "https://demoqa.com/browser-windows")
    with allure.step('Page loading  https://demoqa.com/browser-windows'):
        page_browser_window.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_browser_window.click_button_new_tab() == 'This is a sample page'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_button_new_tab',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page browser window')
@allure.story('Testing the new window element')
def test_validate_click_button_new_window(driver):
    page_browser_window = PageBrowserWindow(driver, "https://demoqa.com/browser-windows")
    with allure.step('Page loading https://demoqa.com/browser-windows'):
        page_browser_window.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_browser_window.click_button_new_window() == 'This is a sample pag'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_click_button_new_window',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
