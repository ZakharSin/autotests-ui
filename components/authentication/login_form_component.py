from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.login_password_input = page.get_by_test_id('login-form-password-input').locator('input')

    def check_visible(self):
        expect(self.login_email_input).to_be_visible()
        expect(self.login_password_input).to_be_visible()

    def fill(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)