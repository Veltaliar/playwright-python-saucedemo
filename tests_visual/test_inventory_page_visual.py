import sys
import pytest
from playwright.sync_api import expect

from data.PageUrls import PageUrls
from data.ValidCredentials import ValidCredentials


@pytest.mark.parametrize("valid_login_test_data", [
    {"username": ValidCredentials.STANDARD_USER, "password": ValidCredentials.PASSWORD},
    {"username": ValidCredentials.ERROR_USER, "password": ValidCredentials.PASSWORD},
    pytest.param({"username": ValidCredentials.PERFORMANCE_GLITCH_USER, "password": ValidCredentials.PASSWORD}, marks=pytest.mark.xfail),
    pytest.param({"username": ValidCredentials.PROBLEM_USER, "password": ValidCredentials.PASSWORD}, marks=pytest.mark.xfail),
    pytest.param({"username": ValidCredentials.VISUAL_USER, "password": ValidCredentials.PASSWORD}, marks=pytest.mark.xfail),
])
def test_inventory_page_view_visual(login_page, inventory_page, valid_login_test_data, assert_snapshot):
    """Test the inventory page view."""
    login_page.navigate_to() \
              .enter_username(valid_login_test_data["username"]) \
              .enter_password(valid_login_test_data["password"]) \
              .click_login_button()

    expect(inventory_page.page).to_have_url(f"{PageUrls.INVENTORY_URL}")

    browser_name = inventory_page.page.context.browser.browser_type.name
    operating_system = sys.platform
    assert_snapshot(inventory_page.page.screenshot(full_page=True), threshold=0.02, name=f"inventory_page[{browser_name}][{operating_system}].png")
