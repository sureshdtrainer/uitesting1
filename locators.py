from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #Open Browser and launch the google.com
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #enter the target URL
    page.goto("https://demo.automationtesting.in/Index.html")

    #Locators for email text box
    #by id
    #by class
    #CSS selectors

    emailtextbox = page.wait_for_selector("#email")
    emailtextbox.fill("test123@email.com")

    #Click the next button
    button = page.wait_for_selector("#enterimg")
    button.click()

    print(page.title())


    #Wait for 3 seconds before closing the browser
    page.wait_for_timeout(3000)

    #Close the browser
    browser.close()