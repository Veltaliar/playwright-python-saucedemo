from playwright.sync_api import expect

from data.page_urls import PageUrls
from data.products import Products


PRODUCT = list(Products.PRODUCT_DETAILS.keys())[0]


def test_empty_cart_visual(login, cart_page, assert_snapshot):
    """ Test the visual appearance of an empty cart. """
    cart_page.navigate_to()
    expect(cart_page.page).to_have_url(PageUrls.CART_URL)
    assert_snapshot(cart_page.page.screenshot(full_page=True))


def test_cart_with_item_visual(login, cart_page, assert_snapshot, add_item_to_cart):
    """ Test the visual appearance of the cart with an item. """
    add_item_to_cart(PRODUCT)
    cart_page.navigate_to()
    expect(cart_page.page).to_have_url(PageUrls.CART_URL)
    assert_snapshot(cart_page.page.screenshot(full_page=True))
