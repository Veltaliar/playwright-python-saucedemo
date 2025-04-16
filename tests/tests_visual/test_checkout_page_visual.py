from playwright.sync_api import expect

from data.page_urls import PageUrls
from data.products_data import Products
from data.error_messages import ErrorMessages


PRODUCT = list(Products.PRODUCT_DETAILS.keys())[0]
FIRST_NAME = "John"
LAST_NAME = "Doe"
ZIP_CODE = "12345"


def test_blank_checkout_form_visual(login, checkout_page, assert_snapshot):
    """ Test the visual appearance of the blank checkout form. """
    checkout_page.navigate_to()
    expect(checkout_page.page).to_have_url(PageUrls.CHECKOUT_URL_STEP1)
    assert_snapshot(checkout_page.page.screenshot(full_page=True))


def test_checkout_form_firstname_required_visual(login, checkout_page, assert_snapshot):
    """ Test the visual appearance of the checkout form with first name required error. """
    checkout_page.navigate_to() \
                 .click_continue()
    expect(checkout_page.get_error_message()).to_have_text(ErrorMessages.FIRST_NAME_REQUIRED_ERROR)
    assert_snapshot(checkout_page.page.screenshot(full_page=True))


def test_checkout_form_lastname_required_visual(login, checkout_page, assert_snapshot):
    """ Test the visual appearance of the checkout form with last name required error. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .click_continue()
    expect(checkout_page.get_error_message()).to_have_text(ErrorMessages.LAST_NAME_REQUIRED_ERROR)
    assert_snapshot(checkout_page.page.screenshot(full_page=True))


def test_checkout_form_zipcode_required_visual(login, checkout_page, assert_snapshot):
    """ Test the visual appearance of the checkout form with zip code required error. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .click_continue()
    expect(checkout_page.get_error_message()).to_have_text(ErrorMessages.ZIP_CODE_REQUIRED_ERROR)
    assert_snapshot(checkout_page.page.screenshot(full_page=True))


def test_overview_with_item_visual(login, checkout_page, add_item_to_cart, assert_snapshot):
    """ Test the visual appearance of the checkout overview page with an item. """
    add_item_to_cart(PRODUCT)
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .fill_zip_code(ZIP_CODE) \
                 .click_continue()
    expect(checkout_page.page).to_have_url(PageUrls.CHECKOUT_URL_STEP2)
    assert_snapshot(checkout_page.page.screenshot(full_page=True))


def test_order_submited_visual(login, checkout_page, assert_snapshot):
    """ Test the visual appearance of the order submission page. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .fill_zip_code(ZIP_CODE) \
                 .click_continue() \
                 .click_finish()
    expect(checkout_page.page).to_have_url(PageUrls.CHECKOUT_URL_STEP3)
    assert_snapshot(checkout_page.page.screenshot(full_page=True))
