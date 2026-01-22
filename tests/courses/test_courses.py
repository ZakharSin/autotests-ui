import allure
import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.check_visible_create_course_form(title="", description="", estimated_time="", max_score='0', min_score='0')
        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('C:/Users/Пользователь/Documents/GitHub/autotests-ui/testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.fill_create_course_form(title='Playwright', description='2 weeks', estimated_time='Playwright', max_score='10', min_score='10')
        create_course_page.click_create_course_button()

        courses_list_page.toolbar_view.check_visible(index=0)
        courses_list_page.course_view.check_visible(index=0, title='Playwright', estimated_time='Playwright', max_score='10', min_score='10')

    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible(index=0)
        courses_list_page.check_visible_empty_view()

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.fill_create_course_form(title='Playwright', description='2 weeks', estimated_time='Playwright', max_score='10', min_score='10')
        create_course_page.image_upload_widget.upload_preview_image('C:/Users/Пользователь/Documents/GitHub/autotests-ui/testdata/files/image.png')
        create_course_page.click_create_course_button()
        courses_list_page.toolbar_view.check_visible(index=0)
        courses_list_page.course_view_menu.click_edit(index=0)
        create_course_page.fill_create_course_form(title='playwright', description='1 week', estimated_time='playwright', max_score='11', min_score='11')
        create_course_page.click_create_course_button()
        courses_list_page.course_view.check_visible(index=0, title='playwright', estimated_time='playwright', max_score='11', min_score='11')