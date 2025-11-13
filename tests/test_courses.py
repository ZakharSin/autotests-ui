import pytest
from playwright.sync_api import Page, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

    # Переходим на страницу courses
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка наличия и текста заголовка "Courses"
    courses_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_be_visible()

    # Проверка наличия иконки
    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    # Проверка наличия и текста "There is no results"
    no_results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_visible()

    # Проверка наличия и текста "Results from the load test pipeline will be displayed here"
    results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_text).to_be_visible()