import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_frame import PageFrame


@allure.feature('Testing the page frame')
@allure.story('Testing switch to frame one')
def test_validate_switch_to_frame_one(driver):
    page_frame = PageFrame(driver, "https://demoqa.com/frames")
    with allure.step('Page loading  https://demoqa.com/frames'):
        page_frame.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_frame.switch_to_frame_one() == "This is a sample page"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_switch_to_frame_one',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page frame')
@allure.story('Testing switch to frame two')
def test_validate_switch_to_frame_two(driver):
    page_frame = PageFrame(driver, "https://demoqa.com/frames")
    with allure.step('Page loading  https://demoqa.com/frames'):
        page_frame.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_frame.switch_to_frame_two() == "This is a sample page"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_switch_to_frame_two',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)

