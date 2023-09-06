import allure
from allure_commons.types import AttachmentType

from src.conftest.conftest import driver
from src.errors.errors import AssertError
from src.pages.page_links import PageLinks


@allure.feature('Testing the page links')
@allure.story('Testing following link home')
def test_validate_following_link_home(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.following_link_home() == "https://demoqa.com/"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_following_link_home',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing following link home foalt')
def test_validate_following_link_home_foalt(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.following_link_home() == "https://demoqa.com/"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_following_link_home_foalt',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing following link created')
def test_validate_link_created(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.click_link_created() == "Link has responded with staus 201 and status text Created"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_link_created',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing following link no content')
def test_validate_link_no_content(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.click_link_no_content() == "Link has responded with staus 204 and status text No Content"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_link_no_content',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing following link moved')
def test_validate_link_moved(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.click_link_moved() == ("Link has responded with staus 301 and status text Moved "
                                                     "Permanently")
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_link_moved',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing link bad request')
def test_validate_link_bad_request(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.click_link_bad_request() == ("Link has responded with staus 400 and status text Bad "
                                                           "Request")
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_link_bad_request',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing link unauthorized')
def test_validate_link_unauthorized(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.click_link_unauthorized() == ("Link has responded with staus 401 and status text "
                                                            "Unauthorized")
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_link_unauthorized',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing link forbidden')
def test_validate_link_forbidden(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.click_link_forbidden() == "Link has responded with staus 403 and status text Forbidden"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_link_forbidden',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)


@allure.feature('Testing the page links')
@allure.story('Testing link forbidden')
def test_validate_link_not_found(driver):
    page_links = PageLinks(driver, "https://demoqa.com/links")
    with allure.step('Page loading  https://demoqa.com/links'):
        page_links.open_browser()
    try:
        with allure.step('Checking whether the expected result matches the actual.'):
            assert page_links.click_link_not_found() == "Link has responded with staus 404 and status text Not Found"
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name='validate_link_not_found',
                      attachment_type=AttachmentType.PNG)
        raise AssertionError(AssertError.Error.value)
