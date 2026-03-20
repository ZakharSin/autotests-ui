import pytest
from playwright.sync_api import Playwright, Page
from tools.routes import AppRoute
from config import settings

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        base_url=settings.get_base_url()
    )
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    # Переходим на страницу входа
    page.goto(AppRoute.REGISTRATION)

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    # Заполняем поле password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    # Нажимаем на кнопку registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')
    browser.close()

pytest_plugins = ("fixtures.pages", "fixtures.browser", "fixtures.allure")