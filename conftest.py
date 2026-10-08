import pytest
from playwright.sync_api import Page
from datetime import datetime


@pytest.fixture
def login_page(page: Page):
    from pages.login_page import LoginPage

    login_page = LoginPage(page)
    login_page.navigate()

    return login_page

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{now}.html"
