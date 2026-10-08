import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.wait_for_timeout(3000)  # Wait for 3 seconds before closing the page
    page.close()

#first test ase to verify google.com is opening or not and check for title of the page
def test_google_title(page):   
        page.goto("https://www.google.com")
        #assertion to check the title of the page
        assert page.title() == "Google"

def test_orangehrm_title(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert page.title() == "OrangeHRM"
