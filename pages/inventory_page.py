import logging
from playwright.sync_api import Page, Locator

from data.page_urls import PageUrls


class InventoryPage():
    """ Provides methods to interact with the inventory page. """
    def __init__(self, page: Page):
        self.page = page
        self.burger_menu = "button[id='react-burger-menu-btn']"
        self.burger_menu_close = "button[id='react-burger-cross-btn']"
        self.all_items_link = "a[data-test='inventory-sidebar-link']"
        self.about_link = "a[data-test='about-sidebar-link']"
        self.logout_link = "a[data-test='logout-sidebar-link']"
        self.reset_app_link = "a[data-test='reset-sidebar-link']"
        self.cart_link = "a[data-test='shopping-cart-link']"
        self.cart_badge = "span[class='shopping_cart_badge']"
        self.sort_dropdown = "select[data-test='product-sort-container']"
        self.product_items = "div.inventory_item"
        self.item_name = "div[data-test='inventory-item-name']"
        self.item_image = "div.inventory_details_img_container img"

    def navigate_to(self) -> "InventoryPage":
        """ Navigate to the inventory page. """
        logging.info("Navigating to the inventory page.")
        self.page.goto(PageUrls.INVENTORY_URL)
        return self

    def open_burger_menu(self) -> "InventoryPage":
        """ Open the burger menu. """
        logging.info("Opening the burger menu.")
        self.page.locator(self.burger_menu).click()
        return self

    def close_burger_menu(self) -> "InventoryPage":
        """ Close the burger menu. """
        logging.info("Closing the burger menu.")
        self.page.locator(self.burger_menu_close).click()
        return self

    def click_logout_button(self) -> "InventoryPage":
        """ Click the logout button in the burger menu. """
        logging.info("Logging out.")
        self.page.locator(self.logout_link).click()
        return self

    def click_cart_icon(self) -> "InventoryPage":
        """ Navigate to the shopping cart. """
        logging.info("Navigating to the shopping cart.")
        self.page.locator(self.cart_link).click()
        return self

    def select_sort_option(self, value: str):
        """ Select a sorting option from the dropdown. """
        self.page.locator(self.sort_dropdown).select_option(value)

    # Getters
    def get_burger_menu(self) -> Locator:
        """ Get the burger menu locator. """
        logging.info("Getting burger menu locator.")
        return self.page.locator(self.burger_menu)

    def get_close_burger_menu_button(self) -> Locator:
        """ Get the close burger menu button locator. """
        logging.info("Getting close burger menu locator.")
        return self.page.locator(self.burger_menu_close)

    def get_all_items_link(self) -> Locator:
        """ Get the all items link locator. """
        logging.info("Getting all items link locator.")
        return self.page.locator(self.all_items_link)

    def get_about_link(self) -> Locator:
        """ Get the about link locator. """
        logging.info("Getting about link locator.")
        return self.page.locator(self.about_link)

    def get_logout_link(self) -> Locator:
        """ Get the logout link locator. """
        logging.info("Getting logout link locator.")
        return self.page.locator(self.logout_link)

    def get_reset_app_link(self) -> Locator:
        """ Get the reset app link locator. """
        logging.info("Getting reset app link locator.")
        return self.page.locator(self.reset_app_link)

    def get_cart_badge(self) -> Locator:
        """ Get the cart badge locator. """
        logging.info("Getting cart badge locator.")
        return self.page.locator(self.cart_badge)

    def get_locator_by_name(self, name: str) -> Locator:
        """ Get the product item locator by name. """
        logging.info("Getting product item locator by name: %s", name)
        return self.get_product_items().filter(has_text=name)

    def get_item_name(self, filter_text: str) -> Locator:
        """ Get the item name locator with a specific text. """
        logging.info("Getting item name locator.")
        return self.page.locator(self.item_name).filter(has_text=filter_text)

    def get_product_items(self) -> Locator:
        """ Get the product items locator. """
        logging.info("Getting product items locator.")
        return self.page.locator(self.product_items)

    def get_sort_dropdown(self) -> Locator:
        """ Get the sort dropdown locator. """
        logging.info("Getting sort dropdown locator.")
        return self.page.locator(self.sort_dropdown)

    def get_sort_dropdown_options(self) -> Locator:
        """ Get the sort dropdown options locator. """
        logging.info("Getting sort dropdown options.")
        return self.page.locator(f"{self.sort_dropdown} option")

    def get_product_image(self) -> Locator:
        """ Get the product image locator. """
        logging.info("Getting product image locator.")
        return self.page.locator(self.item_image)
