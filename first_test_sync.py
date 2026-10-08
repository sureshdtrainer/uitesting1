from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #Open Browser and launch the google.com
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #enter the target URL
    page.goto("https://www.google.com")

    print(page.title())

    #Wait for 3 seconds before closing the browser
    page.wait_for_timeout(3000)

    #Close the browser
    browser.close()