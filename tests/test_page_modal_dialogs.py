import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_modal_dialogs import PageModalDialogs


@allure.feature('Testing the page modal dialogs')
@allure.story('Testing small modal dialogs')
def test_validate_small_modal(driver):
    page_modal_dialogs = PageModalDialogs(driver, "https://demoqa.com/modal-dialogs")
    with allure.step('Page loading  https://demoqa.com/modal-dialogs'):
        page_modal_dialogs.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_modal_dialogs.call_small_modal() == 'Small Modal'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_small_modal',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page modal dialogs')
@allure.story('Testing large modal dialogs')
def test_validate_large_modal(driver):
    page_modal_dialogs = PageModalDialogs(driver, "https://demoqa.com/modal-dialogs")
    with allure.step('Page loading  https://demoqa.com/modal-dialogs'):
        page_modal_dialogs.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_modal_dialogs.call_large_modal() == 'Large Modal'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_large_modal',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
