from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea
class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'Course title input')
        self.create_course_estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Estimated time input')

        self.create_course_description_textarea = Textarea(page, 'create-course-form-description-input', 'Description textarea')
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score input')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score input')

    @allure.step('Check visible create course form "{index}"')
    def check_visible(self, index: int):
        self.create_course_title_input.check_visible(nth=index)
        self.create_course_description_textarea.check_visible(nth=index)
        self.create_course_estimated_time_input.check_visible(nth=index)
        self.create_course_max_score_input.check_visible(nth=index)
        self.create_course_min_score_input.check_visible(nth=index)

    @allure.step("Fill create course form")
    def fill(self, title: str, description: str, max_score: str, min_score: str, estimated_time: str):
        self.create_course_title_input.fill(title)
        self.create_course_description_textarea.fill(description)
        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_max_score_input.fill(max_score)
        self.create_course_min_score_input.fill(min_score)