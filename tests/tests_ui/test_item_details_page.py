
import random
import pytest
from playwright.sync_api import expect

from data.page_urls import PageUrls
from data.products import Products


PRODUCTS = Products.PRODUCT_DETAILS.keys()


@pytest.mark.parametrize("product_name", list(PRODUCTS))
def test_name_navigates_to_item_details(login, inventory_page, item_details_page, product_name):
    """ Test that clicking on the item name navigates to the item details page. """
    inventory_page.get_item_name(product_name) \
                  .click()

    expect(item_details_page.page).to_have_url(f"{PageUrls.INVENTORY_ITEM_URL}?id={Products.PRODUCT_DETAILS[product_name]['id']}")


@pytest.mark.parametrize("product_name", list(PRODUCTS))
def test_image_navigates_to_item_details(login, inventory_page, item_details_page, product_name):
    """ Test that clicking on the item image navigates to the item details page. """
    inventory_page.get_locator_by_name(product_name) \
                  .get_by_role("img", name=product_name) \
                  .click()

    expect(item_details_page.page).to_have_url(f"{PageUrls.INVENTORY_ITEM_URL}?id={Products.PRODUCT_DETAILS[product_name]['id']}")


@pytest.mark.parametrize("product_name", list(PRODUCTS))
def test_item_details_matches_inventory_page(login, inventory_page, item_details_page, product_name):
    """ Test that the item details match the product data. """
    inventory_page.get_item_name(product_name) \
                  .click()

    expect(item_details_page.page).to_have_url(f"{PageUrls.INVENTORY_ITEM_URL}?id={Products.PRODUCT_DETAILS[product_name]['id']}")

    expect(item_details_page.get_item_details_name()).to_have_text(product_name)
    expect(item_details_page.get_item_details_price()).to_have_text(Products.PRODUCT_DETAILS[product_name]["price"])
