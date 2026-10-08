import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page):
    from pages.login_page import LoginPage

    login_page = LoginPage(page)
    login_page.navigate()

    return login_page
