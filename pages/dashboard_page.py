from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_heading = page.locator(
            "h6:has-text('Dashboard')"
        )

    def verify_dashboard(self):
        expect(self.dashboard_heading).to_be_visible()

    def get_page_title(self):
        return self.page.title()


