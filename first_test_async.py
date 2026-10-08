import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Open Browser and launch the google.com
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Enter the target URL
        await page.goto("https://www.google.com")

        print(await page.title())

        # Wait for 3 seconds before closing the browser
        await page.wait_for_timeout(3000)

        # Close the browser
        await browser.close()

# Run the main function
asyncio.run(main())