import random
import pytest
from playwright.sync_api import expect

from data.PageUrls import PageUrls
from data.Products import Products


PRODUCTS = Products.PRODUCT_DETAILS.keys()


@pytest.fixture
def open_burger_menu(inventory_page):
    """ Fixture to open the burger menu before each test. """
    inventory_page.open_burger_menu()
    expect(inventory_page.get_close_burger_menu_button()).to_be_visible()


@pytest.fixture
def remove_item_from_cart(inventory_page):
    """ Fixture to remove an item from the cart. """
    def _remove_item(product_name):
        inventory_page.get_locator_by_name(product_name) \
                      .get_by_role("button", name="Remove") \
                      .click()
    return _remove_item


def test_all_items_link_visible_in_burger_menu(login, inventory_page, open_burger_menu):
    """ Test that the all items link is visible in the burger menu. """
    expect(inventory_page.get_all_items_link()).to_be_visible()


def test_about_link_visible_in_burger_menu(login, inventory_page, open_burger_menu):
    """ Test that the about link is visible in the burger menu. """
    expect(inventory_page.get_about_link()).to_be_visible()


def test_logout_link_visible_in_burger_menu(login, inventory_page, open_burger_menu):
    """ Test that the logout link is visible in the burger menu. """
    expect(inventory_page.get_logout_link()).to_be_visible()


def test_reset_app_link_visible_in_burger_menu(login, inventory_page, open_burger_menu):
    """ Test that the reset app link is visible in the burger menu. """
    expect(inventory_page.get_reset_app_link()).to_be_visible()


def test_close_burger_menu(login, inventory_page, open_burger_menu):
    """ Test that the burger menu closes correctly. """
    inventory_page.close_burger_menu()
    expect(inventory_page.get_close_burger_menu_button()).not_to_be_visible()
    expect(inventory_page.get_all_items_link()).not_to_be_visible()
    expect(inventory_page.get_about_link()).not_to_be_visible()
    expect(inventory_page.get_logout_link()).not_to_be_visible()
    expect(inventory_page.get_reset_app_link()).not_to_be_visible()
    expect(inventory_page.get_burger_menu()).to_be_visible()


@pytest.mark.parametrize("product_name", random.sample(list(PRODUCTS), 2))
def test_cart_badge_increase(login, inventory_page, product_name, add_item_to_cart):
    """ Test that the cart badge increases when an item is added to the cart. """
    add_item_to_cart(product_name)

    expect(inventory_page.get_cart_badge()).to_have_text("1")


def test_cart_badge_decreases(login, inventory_page, add_item_to_cart, remove_item_from_cart):
    """ Test that the cart badge decreases when an item is removed from the cart. """
    product_count = len(PRODUCTS)

    for product_name in PRODUCTS:
        add_item_to_cart(product_name)

    for product_name in PRODUCTS:
        remove_item_from_cart(product_name)
        product_count -= 1
        if product_count == 0:
            expect(inventory_page.get_cart_badge()).not_to_be_visible()
        else:
            expect(inventory_page.get_cart_badge()).to_have_text(str(product_count))


@pytest.mark.parametrize("product_name", random.sample(list(PRODUCTS), 2))
def test_cart_badge_disappears(login, inventory_page, product_name, add_item_to_cart, remove_item_from_cart):
    """ Test that the cart badge disappears when the last item is removed from the cart. """
    add_item_to_cart(product_name)
    remove_item_from_cart(product_name)

    expect(inventory_page.get_cart_badge()).not_to_be_visible()


@pytest.mark.parametrize("product_name", random.sample(list(PRODUCTS), 2))
def test_add_button_changes_to_remove(login, inventory_page, product_name, add_item_to_cart):
    """ Test that the add button changes to remove when an item is added to the cart. """
    add_item_to_cart(product_name)
    item = inventory_page.get_locator_by_name(product_name)

    expect(item.get_by_role("button", name="Remove")).to_be_visible()


@pytest.mark.parametrize("product_name", random.sample(list(PRODUCTS), 2))
def test_remove_button_changes_to_add(login, inventory_page, product_name, add_item_to_cart, remove_item_from_cart):
    """ Test that the remove button changes to add when an item is removed from the cart. """
    add_item_to_cart(product_name)
    remove_item_from_cart(product_name)
    item = inventory_page.get_locator_by_name(product_name)

    expect(item.get_by_role("button", name="Add to cart")).to_be_visible()


@pytest.mark.parametrize("product_name", random.sample(list(PRODUCTS), 1))
def test_added_items_persist_through_page_reload(login, inventory_page, product_name, add_item_to_cart):
    """ Test that added items persist through page reload. """
    add_item_to_cart(product_name)
    item = inventory_page.get_locator_by_name(product_name)
    inventory_page.page.reload()

    expect(item.get_by_role("button", name="Remove")).to_be_visible()


@pytest.mark.parametrize("sort_option, key_func, reverse", [
    ("az", lambda x: x, False),
    ("za", lambda x: x, True),
    ("lohi", lambda x: float(str(Products.PRODUCT_DETAILS[x]["price"]).replace("$", "")), False),
    ("hilo", lambda x: float(str(Products.PRODUCT_DETAILS[x]["price"]).replace("$", "")), True),
])
def test_sort_items(login, inventory_page, sort_option, key_func, reverse):
    """ Test the sorting functionality of the inventory page. """
    inventory_page.select_sort_option(sort_option)
    expected_order = sorted(PRODUCTS, key=key_func, reverse=reverse)
    items = inventory_page.get_product_items()
    displayed_names = [items.nth(i).locator(inventory_page.item_name).inner_text() for i in range(items.count())]

    assert displayed_names == expected_order, f"Sorting failed for option '{sort_option}'"


def test_go_to_cart(login, inventory_page, cart_page):
    """ Test the functionality of the go to cart button. """
    inventory_page.click_cart_icon()

    expect(cart_page.page).to_have_url(PageUrls.CART_URL)