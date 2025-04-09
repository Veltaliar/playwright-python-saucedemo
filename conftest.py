import pytest
from playwright.sync_api import expect

from data.ValidCredentials import ValidCredentials
from data.PageUrls import PageUrls

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.ItemDetailsPage import ItemDetailsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
def browser_context_args(browser_name):
    if browser_name == "chromium":
        return {
            "args": [
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--disable-software-rasterizer",
                "--no-sandbox",
                "--font-render-hinting=none",
                "--force-device-scale-factor=1",
                "--disable-lcd-text"
            ],
        }
    return {}


@pytest.fixture
def login_page(page):
    """ Fixture to initialize the LoginPage. """
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    """ Fixture to initialize the InventoryPage. """
    return InventoryPage(page)


@pytest.fixture
def item_details_page(page):
    """ Fixture to initialize the ItemDetailsPage. """
    return ItemDetailsPage(page)


@pytest.fixture
def cart_page(page):
    """ Fixture to initialize the CartPage. """
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    """ Fixture to initialize the CheckoutPage. """
    return CheckoutPage(page)


@pytest.fixture
def login(login_page, inventory_page):
    """ Fixture to log in to the application before each test. And log out after the test. """
    login_page.navigate_to() \
              .enter_username(ValidCredentials.STANDARD_USER) \
              .enter_password(ValidCredentials.PASSWORD) \
              .click_login_button()
    expect(login_page.page).to_have_url(PageUrls.INVENTORY_URL)

    yield

    inventory_page.navigate_to() \
                  .open_burger_menu() \
                  .click_logout_button()
    expect(login_page.page).to_have_url(f"{PageUrls.BASE_URL}/")


@pytest.fixture
def add_item_to_cart(inventory_page):
    """ Fixture to add an item to the cart. """
    def _add_item(product_name):
        inventory_page.get_locator_by_name(product_name) \
                      .get_by_role("button", name="Add to cart") \
                      .click()
    return _add_item
