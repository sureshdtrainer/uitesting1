import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.parametrize("username, password", [("Admin", "admin123")])
def test_valid_login(login_page, username, password):
    login_page.login(username,password)
    dashboard_page = DashboardPage(login_page.page)
    dashboard_page.verify_dashboard()
