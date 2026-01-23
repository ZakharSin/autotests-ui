from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', 'Create course title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course button')

    @allure.step('Check visible create course toolbar')
    def check_visible(self, is_create_course_disabled: bool = True):
        self.create_course_button.check_disabled()
        if is_create_course_disabled is False:
            self.create_course_button.check_enabled()

    def click_create_course_button(self, index: int):
        self.create_course_button.click(nth=index)