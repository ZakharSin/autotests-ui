from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Проверка наличия поле email
    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    # Проверка наличия поля пароль
    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()

    # Проверка наличия кнопки Login
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    # Находим ссылку и нажимаем на нее
    registration_link = page.get_by_test_id("login-page-registration-link")
    registration_link.click()

    # Проверка наличия кнопки Email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    # Проверка наличия элемента Password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    # Проверка наличия элемента Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()