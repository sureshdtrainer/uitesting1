from playwright.sync_api import Page


class LoginPage:


    def __init__(self, page: Page):
        self.page = page


        # Locators
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")


    def navigate(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )


    def enter_username(self, username):
        self.username.fill(username)


    def enter_password(self, password):
        self.password.fill(password)


    def click_login(self):
        self.login_button.click()


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
