import allure
from allure_commons.types import AttachmentType
from src.conftest.conftest import driver
from src.errors.errors import AssertError
from src.pages.page_nested_frames import PageNestedFrames


@allure.feature('Testing the page nested frames')
@allure.story('Testing switch to frame outer')
def test_validate_switch_to_frame_outer(driver):
    page_nested_frame = PageNestedFrames(driver, "https://demoqa.com/nestedframes")
    with allure.step('Page loading  https://demoqa.com/nestedframes'):
        page_nested_frame.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_nested_frame.switch_to_frame_outer() == 'Parent frame'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_switch_to_frame_outer',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page nested frames')
@allure.story('Testing switch to frame inner')
def test_validate_switch_to_frame_inner(driver):
    page_nested_frame = PageNestedFrames(driver, "https://demoqa.com/nestedframes")
    with allure.step('Page loading  https://demoqa.com/nestedframes'):
        page_nested_frame.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_nested_frame.switch_to_frame_inner() == 'Child Iframe'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_switch_to_frame_inner',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
