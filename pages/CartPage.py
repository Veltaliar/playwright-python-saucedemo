import logging
from playwright.sync_api import Page, Locator

from data.PageUrls import PageUrls


class CartPage():
    """ Provides methods to interact with the cart page. """
    def __init__(self, page: Page):
        self.page = page
        self.continue_shopping_button = "button[data-test='continue-shopping']"
        self.checkout_button = "button[data-test='checkout']"
        self.cart_items = "div.cart_item"

    def navigate_to(self) -> "CartPage":
        """ Navigate to the cart page. """
        logging.info("Navigating to the cart page.")
        self.page.goto(PageUrls.CART_URL)
        return self

    def click_continue_shopping(self) -> "CartPage":
        """ Click the continue shopping button. """
        logging.info("Clicking the continue shopping button.")
        self.page.locator(self.continue_shopping_button).click()
        return self

    def click_checkout(self) -> "CartPage":
        """ Click the checkout button. """
        logging.info("Clicking the checkout button.")
        self.page.locator(self.checkout_button).click()
        return self

    # Getters
    def get_cart_items(self) -> Locator:
        """ Get the cart items locator. """
        logging.info("Getting the cart items locator.")
        return self.page.locator(self.cart_items)
