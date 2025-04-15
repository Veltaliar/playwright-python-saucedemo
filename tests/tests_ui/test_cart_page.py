import random
import pytest
from playwright.sync_api import expect

from data.PageUrls import PageUrls
from data.Products import Products


PRODUCTS = random.sample(list(Products.PRODUCT_DETAILS.keys()), 2)


def test_continue_shopping_button(login, cart_page):
    """ Test the functionality of the continue shopping button on the cart page. """
    cart_page.navigate_to() \
             .click_continue_shopping()

    expect(cart_page.page).to_have_url(PageUrls.INVENTORY_URL)


@pytest.mark.xfail(reason="Bug on website: Checkout should not be possible without items.")
def test_checkout_without_items(login, cart_page):
    """ Test the functionality of the checkout button when there are no items in the cart. """
    cart_page.navigate_to() \
             .click_checkout()

    expect(cart_page.page).to_have_url(PageUrls.CART_URL)


def test_cart_blank_by_default(login, cart_page):
    """ Test that the cart is blank by default. """
    cart_page.navigate_to()

    expect(cart_page.get_cart_items()).to_have_count(0)


def test_cart_items_visible(login, inventory_page, cart_page, add_item_to_cart):
    """ Test that the items in the cart are visible. """
    inventory_page.navigate_to()

    for product in PRODUCTS:
        add_item_to_cart(product)

    cart_page.navigate_to()
    expect(cart_page.get_cart_items()).to_have_count(len(PRODUCTS))


def test_checkout_with_items(login, inventory_page, cart_page, add_item_to_cart):
    """ Test the functionality of the checkout button when there are items in the cart. """
    inventory_page.navigate_to()

    for product in PRODUCTS:
        add_item_to_cart(product)

    cart_page.navigate_to() \
             .click_checkout()

    expect(cart_page.page).to_have_url(PageUrls.CHECKOUT_URL_STEP1)
