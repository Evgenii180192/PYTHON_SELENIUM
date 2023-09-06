import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_text_box import PageTextBox


@allure.feature('Testing the page text box')
@allure.story('Testing check block border')
def test_validate_block_border(driver):
    text_box_page = PageTextBox(driver, "https://demoqa.com/text-box")
    with allure.step('Page loading  https://demoqa.com/text-box'):
        text_box_page.open_browser()
    with allure.step('Filling form'):
        text_box_page.filling_inputs()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert text_box_page.check_visible_block_border().is_displayed()
            assert text_box_page.check_value_name_block_border().text == 'Name:Evgenii'
            assert text_box_page.check_value_email_block_border().text == 'Email:sevgeniiv92@mail.ru'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_block_border',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)



