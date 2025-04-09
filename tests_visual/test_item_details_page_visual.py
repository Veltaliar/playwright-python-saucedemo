import pytest
from playwright.sync_api import expect

from data.PageUrls import PageUrls
from data.Products import Products


PRODUCT = list(Products.PRODUCT_DETAILS.keys())[0]


@pytest.mark.parametrize("product_name", [PRODUCT])
def test_item_details_view(login, inventory_page, item_details_page, product_name, assert_snapshot):
    """Test the item details page view."""
    inventory_page.get_item_name(product_name) \
                  .click()

    expect(item_details_page.page).to_have_url(f"{PageUrls.INVENTORY_ITEM_URL}?id={Products.PRODUCT_DETAILS[product_name]['id']}")
    assert_snapshot(item_details_page.page.screenshot(full_page=True))
