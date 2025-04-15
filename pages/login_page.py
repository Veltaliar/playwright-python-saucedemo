import logging
from playwright.sync_api import Page, Locator

from data.page_urls import PageUrls


class LoginPage():
    """ Provides methods to interact with the login page. """
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input[name='user-name']"
        self.password_input = "input[name='password']"
        self.login_button = "input[name='login-button']"
        self.error_message = "h3[data-test='error']"

    def navigate_to(self) -> "LoginPage":
        """ Navigate to the login page. """
        logging.info("Navigating to the login page.")
        self.page.goto(f"{PageUrls.BASE_URL}/")
        return self

    def enter_username(self, username) -> "LoginPage":
        """ Enter the username in the username input field. """
        logging.info("Entering username: %s", username)
        self.page.locator(self.username_input).fill(username)
        return self

    def enter_password(self, password) -> "LoginPage":
        """ Enter the password in the password input field. """
        logging.info("Entering password.")
        self.page.locator(self.password_input).fill(password)
        return self

    def click_login_button(self) -> "LoginPage":
        """ Click the login button. """
        logging.info("Clicking the login button.")
        self.page.locator(self.login_button).click()
        return self

    # Getters
    def get_error_message(self) -> Locator:
        """ Get the error message locator. """
        logging.info("Retrieving the error message.")
        return self.page.locator(self.error_message)
