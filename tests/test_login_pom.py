import pytest
from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage


@pytest.mark.parametrize("username, password", [("Admin", "admin123")])
def test_valid_login(login_page, username, password):
    login_page.login(username, password)
    dashboard_page = DashboardPage(login_page.page)
    dashboard_page.verify_dashboard()


def test_invalid_login(login_page):
    login_page.login("invalid_user", "invalid_pass")
    expect(login_page.page.locator("text=Invalid credentials")).to_be_visible()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "admin123", "Username cannot be empty"),
        ("Admin", "", "Password cannot be empty"),
        ("", "", "Username cannot be empty"),
    ],
)
def test_login_validation_errors(login_page, username, password, expected_error):
    login_page.login(username, password)
    expect(login_page.page.locator(f"text={expected_error}")).to_be_visible()


@pytest.mark.parametrize(
    "username, password",
    [
        ("invalid_user", "invalid_pass"),
        ("Admin", "wrong_password"),
    ],
)
def test_login_invalid_credentials_error_message(login_page, username, password):
    login_page.login(username, password)
    expect(login_page.page.locator("text=Invalid credentials")).to_be_visible()
