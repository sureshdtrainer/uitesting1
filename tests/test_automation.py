import pytest
from playwright.sync_api import sync_playwright, expect

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


@pytest.mark.parametrize("username, password", [("Admin", "admin123")])
def test_success_orangehr_login(page, username, password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    page.wait_for_selector('//input[@name="username"]').fill(username)
    page.wait_for_selector('//input[@placeholder="Password"]').fill(password)
    page.wait_for_selector('//button[@type="submit"]').click()

    page.wait_for_timeout(2000)
    # CSS selector by class (.)
    dashboard_breadcrumb = page.wait_for_selector(
        '.oxd-topbar-header-breadcrumb-module')
    dashboard_name = dashboard_breadcrumb.text_content()
    print("Dashboard name:", dashboard_name)
    assert "Dashboard" == dashboard_name


@pytest.mark.parametrize('username,password', [('testuser1', 'testpwd1'), ('testuser2', 'testpwd2')])
def test_invalid_orangehrm_login(page, username, password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_selector('//input[@name="username"]').fill(username)
    page.wait_for_selector('//input[@placeholder="Password"]').fill(password)
    page.wait_for_selector('//button[@type="submit"]').click()

    page.wait_for_timeout(2000)

    error = page.wait_for_selector('//div[@role="alert"]//p').text_content()
    assert "Invalid credentials" == error



    

