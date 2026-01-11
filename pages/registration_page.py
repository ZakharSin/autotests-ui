from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form_component = RegistrationFormComponent(page)
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_login_form(self, email: str, username: str, password: str):
        self.registration_form_component.check_visible()
        self.registration_form_component.fill(email, username, password)

    def click_registration_button(self):
        self.registration_button.click()