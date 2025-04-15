import pytest
from playwright.sync_api import expect

from data.PageUrls import PageUrls
from data.ErrorMessages import ErrorMessages
from data.ValidCredentials import ValidCredentials
from data.InvalidCredentials import InvalidCredentials


@pytest.mark.parametrize("invalid_login_test_data", [
    {"username": InvalidCredentials.EMPTY_USERNAME, "password": InvalidCredentials.EMPTY_PASSWORD, "expected_error": ErrorMessages.USERNAME_REQUIRED_ERROR},
    {"username": InvalidCredentials.INVALID_USERNAME, "password": InvalidCredentials.EMPTY_PASSWORD, "expected_error": ErrorMessages.PASSWORD_REQUIRED_ERROR},
    {"username": InvalidCredentials.INVALID_USERNAME, "password": InvalidCredentials.INVALID_PASSWORD, "expected_error": ErrorMessages.INVALID_CREDENTIALS_ERROR},
    {"username": InvalidCredentials.LOCKED_OUT_USER, "password": ValidCredentials.PASSWORD, "expected_error": ErrorMessages.USER_LOCKED_OUT_ERROR},
])
def test_invalid_login(login_page, invalid_login_test_data):
    """ Test invalid login with various credentials. """
    login_page.navigate_to() \
              .enter_username(invalid_login_test_data["username"]) \
              .enter_password(invalid_login_test_data["password"]) \
              .click_login_button()

    expect(login_page.get_error_message()).to_have_text(invalid_login_test_data["expected_error"])


@pytest.mark.parametrize("valid_login_test_data", [
    {"username": ValidCredentials.STANDARD_USER, "password": ValidCredentials.PASSWORD},
    {"username": ValidCredentials.PROBLEM_USER, "password": ValidCredentials.PASSWORD},
    {"username": ValidCredentials.PERFORMANCE_GLITCH_USER, "password": ValidCredentials.PASSWORD},
    {"username": ValidCredentials.VISUAL_USER, "password": ValidCredentials.PASSWORD},
    {"username": ValidCredentials.ERROR_USER, "password": ValidCredentials.PASSWORD},
])
def test_valid_login(login_page, valid_login_test_data):
    """ Test valid login with various credentials. """
    login_page.navigate_to() \
              .enter_username(valid_login_test_data["username"]) \
              .enter_password(valid_login_test_data["password"]) \
              .click_login_button()

    expect(login_page.page).to_have_url(PageUrls.INVENTORY_URL)


@pytest.mark.parametrize("unauthenticated_pages", [
    {"url": PageUrls.INVENTORY_URL, "excepted_error": ErrorMessages.INVENTORY_ACCESS_DENIED_ERROR},
    {"url": PageUrls.CART_URL, "excepted_error": ErrorMessages.CART_ACCESS_DENIED_ERROR},
    {"url": PageUrls.CHECKOUT_URL_STEP1, "excepted_error": ErrorMessages.CHECKOUT_STEP1_ACCESS_DENIED_ERROR},
    {"url": PageUrls.CHECKOUT_URL_STEP2, "excepted_error": ErrorMessages.CHECKOUT_STEP2_ACCESS_DENIED_ERROR},
    {"url": PageUrls.CHECKOUT_URL_STEP3, "excepted_error": ErrorMessages.CHECKOUT_STEP3_ACCESS_DENIED_ERROR},
])
def test_page_access_without_login(login_page, unauthenticated_pages):
    """ Test access to pages without login. """
    login_page.navigate_to() \
              .page.goto(unauthenticated_pages["url"])

    expect(login_page.get_error_message()).to_have_text(unauthenticated_pages["excepted_error"])
