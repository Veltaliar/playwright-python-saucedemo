import logging
from playwright.sync_api import Page, Locator

from data.PageUrls import PageUrls


class ItemDetailsPage():
    """ Provides methods to interact with the item details page. """
    def __init__(self, page: Page):
        self.page = page
        self.item_details_name = "div.inventory_details_name"
        self.item_details_price = "div.inventory_details_price"

    def navigate_to(self, product_id) -> "ItemDetailsPage":
        """ Navigate to the item details page. """
        logging.info("Navigating to the item details page.")
        self.page.goto(f"{PageUrls.INVENTORY_ITEM_URL}?id={product_id}")
        return self

    # Getters
    def get_item_details_name(self) -> Locator:
        """ Get the item details name locator. """
        logging.info("Getting item details name text.")
        return self.page.locator(self.item_details_name)

    def get_item_details_price(self) -> Locator:
        """ Get the item details price locator. """
        logging.info("Getting item details price locator.")
        return self.page.locator(self.item_details_price)
