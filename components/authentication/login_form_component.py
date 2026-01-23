from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
import allure

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_email_input = Input(page,'login-form-email-input', 'Email')
        self.login_password_input = Input(page, 'login-form-password-input', 'Password')

    @allure.step("Check visible login form")
    def check_visible(self):
        self.login_email_input.check_visible()
        self.login_password_input.check_visible()

    @allure.step("Fill login form")
    def fill(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)