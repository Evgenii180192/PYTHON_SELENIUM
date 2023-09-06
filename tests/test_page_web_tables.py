import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError

from src.pages.page_web_tables import PageWebTables


@allure.feature('Testing the page web tables')
@allure.story('Testing check add user web tables')
def test_validate_add_user_web_tables(driver):
    page_web_tables = PageWebTables(driver, "https://demoqa.com/webtables")
    with allure.step('Page loading  https://demoqa.com/webtables'):
        page_web_tables.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_web_tables.add_user_web_tables() == 'Evgenii'
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_add_user_web_tables',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
