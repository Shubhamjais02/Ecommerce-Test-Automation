from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.login_heading = page.get_by_text(
            "Login to your account"
        )

        self.email_input = page.locator("input[data-qa='login-email']")
        self.password_input = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")
        
        self.login_error = page.get_by_text(
            "Your email or password is incorrect!"
        )

    def verify_login_page(self):
        expect(self.login_heading).to_be_visible()
    
    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_error(self):
        expect(self.login_error).to_be_visible()