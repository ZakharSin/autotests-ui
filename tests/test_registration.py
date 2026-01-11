import pytest

from pages.registration_page import RegistrationPage  # Импортируем RegistrationPage
from pages.dashboard_page import DashboardPage # Импортируем DashboardPage

@pytest.mark.registration
@pytest.mark.regression

def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_login_form("user.name@gmail.com", "username", "password")
    registration_page.click_registration_button()
    dashboard_page.dashboard_toolbar_view.check_visible()