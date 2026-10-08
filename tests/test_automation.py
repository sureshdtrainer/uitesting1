import pytest
from playwright.sync_api import sync_playwright

#first test ase to verify google.com is opening or not and check for title of the page
def test_google_title(playwright):
        #Open Browser and launch the google.com
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        #enter the target URL
        page.goto("https://www.google.com")
        #assertion to check the title of the page
        assert page.title() == "Google"
        #Wait for 3 seconds before closing the browser
        page.wait_for_timeout(3000)
        #Close the browser
        browser.close()

def test_orangehrm_title(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert page.title() == "OrangeHRM"
    page.wait_for_timeout(3000)
    browser.close()
