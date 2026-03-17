from playwright.sync_api import sync_playwright, expect
from tools.routes import AppRoute
from config import settings

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
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

    # Новая сессия
with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    # Переходим на страницу Courses
    page.goto(AppRoute.COURSES)

    # Проверка наличия и текста заголовка "Courses"
    courses_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_be_visible()

    # Проверка наличия иконки
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    # Проверка наличия и текста "There is no results"
    no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_visible()

    # Проверка наличия и текста "Results from the load test pipeline will be displayed here"
    results_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_text).to_be_visible()