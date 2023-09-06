import allure
from allure_commons.types import AttachmentType
from src.conftest.conftest import driver
from src.errors.errors import AssertError
from src.pages.page_upload import PageUpload


@allure.feature('Testing the page upload')
@allure.story('Testing check upload file')
def test_validate_upload_file(driver):
    page_upload = PageUpload(driver, "https://demoqa.com/upload-download")
    with allure.step('Page loading  https://demoqa.com/upload-download'):
        page_upload.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_upload.upload_file() == r"C:\fakepath\Новый текстовый документ.txt"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_upload_file',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
