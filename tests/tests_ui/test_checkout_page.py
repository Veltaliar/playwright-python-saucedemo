import random
from playwright.sync_api import expect

from data.page_urls import PageUrls
from data.error_messages import ErrorMessages
from data.products_data import Products


PRODUCTS = random.sample(list(Products.PRODUCT_DETAILS.keys()), 3)
FIRST_NAME = "John"
LAST_NAME = "Doe"
ZIP_CODE = "12345"


def test_checkout_form_firstname_required(login, checkout_page):
    """ Test to ensure that the first name field is required. """
    checkout_page.navigate_to() \
                 .click_continue()
    expect(checkout_page.get_error_message()).to_have_text(ErrorMessages.FIRST_NAME_REQUIRED_ERROR)


def test_checkout_form_lastname_required(login, checkout_page):
    """ Test to ensure that the last name field is required. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .click_continue()
    expect(checkout_page.get_error_message()).to_have_text(ErrorMessages.LAST_NAME_REQUIRED_ERROR)


def test_checkout_form_zipcode_required(login, checkout_page):
    """ Test to ensure that the zip code field is required. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .click_continue()
    expect(checkout_page.get_error_message()).to_have_text(ErrorMessages.ZIP_CODE_REQUIRED_ERROR)


def test_cancel_form_button_functionality(login, checkout_page):
    """ Test to ensure that the cancel button works correctly. """
    checkout_page.navigate_to() \
                 .click_cancel()

    expect(checkout_page.page).to_have_url(PageUrls.CART_URL)


def test_continue_button_functionality(login, checkout_page):
    """ Test to ensure that the continue button works correctly. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .fill_zip_code(ZIP_CODE) \
                 .click_continue()

    expect(checkout_page.page).to_have_url(PageUrls.CHECKOUT_URL_STEP2)


def test_cancel_overview_button_functionality(login, checkout_page):
    """ Test to ensure that the cancel button works correctly on the overview page. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .fill_zip_code(ZIP_CODE) \
                 .click_continue() \
                 .click_cancel()

    expect(checkout_page.page).to_have_url(PageUrls.INVENTORY_URL)


def test_overview_page_items_visible(login, checkout_page, inventory_page, add_item_to_cart):
    """ Test to ensure that the items are visible on the overview page. """
    inventory_page.navigate_to()

    for product in PRODUCTS:
        add_item_to_cart(product)

    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .fill_zip_code(ZIP_CODE) \
                 .click_continue()

    expect(checkout_page.get_overview_items()).to_have_count(len(PRODUCTS))


def test_finish_button_functionality(login, checkout_page):
    """ Test to ensure that the finish button works correctly. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .fill_zip_code(ZIP_CODE) \
                 .click_continue() \
                 .click_finish()

    expect(checkout_page.page).to_have_url(PageUrls.CHECKOUT_URL_STEP3)


def test_back_home_button_functionality(login, checkout_page):
    """ Test to ensure that the back home button works correctly. """
    checkout_page.navigate_to() \
                 .fill_first_name(FIRST_NAME) \
                 .fill_last_name(LAST_NAME) \
                 .fill_zip_code(ZIP_CODE) \
                 .click_continue() \
                 .click_finish() \
                 .click_back_home()

    expect(checkout_page.page).to_have_url(PageUrls.INVENTORY_URL)
