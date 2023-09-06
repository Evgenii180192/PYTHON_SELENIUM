import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_form import PageForm


@allure.feature('Testing the page form')
@allure.story('Testing filling form')
def test_validate_filling_form(driver):
    page_form = PageForm(driver, "https://demoqa.com/automation-practice-form")
    with allure.step('Page loading  https://demoqa.com/automation-practice-form'):
        page_form.open_browser()
    user = page_form.filling_form()
    result = page_form.form_result()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert f'{user.first_name} {user.last_name}' == result[0]
            assert user.email == result[1]
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_filling_form',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
