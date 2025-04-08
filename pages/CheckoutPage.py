import logging
from playwright.sync_api import Page, Locator

from data.PageUrls import PageUrls


class CheckoutPage:
    """ Provides methods to interact with the checkout page. """
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = "input[data-test='firstName']"
        self.last_name_input = "input[data-test='lastName']"
        self.zip_code_input = "input[data-test='postalCode']"
        self.continue_button = "input[data-test='continue']"
        self.cancel_button = "button[data-test='cancel']"
        self.error_message = "h3[data-test='error']"
        self.finish_button = "button[data-test='finish']"
        self.back_home_button = "button[data-test='back-to-products']"
        self.overview_items = "div.cart_item"

    def navigate_to(self) -> "CheckoutPage":
        """ Navigates to the checkout page. """
        logging.info("Navigating to the checkout page.")
        self.page.goto(PageUrls.CHECKOUT_URL_STEP1)
        return self

    def fill_first_name(self, first_name: str) -> "CheckoutPage":
        """ Fills in the first name field. """
        logging.info("Filling in the first name: %s", first_name)
        self.page.locator(self.first_name_input).fill(first_name)
        return self

    def fill_last_name(self, last_name: str) -> "CheckoutPage":
        """ Fills in the last name field. """
        logging.info("Filling in the last name: %s", last_name)
        self.page.locator(self.last_name_input).fill(last_name)
        return self

    def fill_zip_code(self, zip_code: str) -> "CheckoutPage":
        """ Fills in the zip code field. """
        logging.info("Filling in the zip code: %s", zip_code)
        self.page.locator(self.zip_code_input).fill(zip_code)
        return self

    def click_continue(self) -> "CheckoutPage":
        """ Clicks the continue button. """
        logging.info("Clicking the continue button.")
        self.page.locator(self.continue_button).click()
        return self

    def click_cancel(self) -> "CheckoutPage":
        """ Clicks the cancel button. """
        logging.info("Clicking the cancel button.")
        self.page.locator(self.cancel_button).click()
        return self

    def click_finish(self) -> "CheckoutPage":
        """ Clicks the finish button. """
        logging.info("Clicking the finish button.")
        self.page.locator(self.finish_button).click()
        return self

    def click_back_home(self) -> "CheckoutPage":
        """ Clicks the back home button. """
        logging.info("Clicking the back home button.")
        self.page.locator(self.back_home_button).click()
        return self

    def get_error_message(self) -> Locator:
        """ Retrieves the error message. """
        logging.info("Retrieving the error message.")
        return self.page.locator(self.error_message)

    def get_overview_items(self) -> Locator:
        """ Retrieves the overview items. """
        logging.info("Retrieving the overview items.")
        return self.page.locator(self.overview_items)
