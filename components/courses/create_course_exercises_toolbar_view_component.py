from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Exercises title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create exercise button')

    @allure.step('Check visible create course toolbar view "{index}"')
    def check_visible(self, index: int):
        self.exercises_title.check_visible(nth=index)
        self.create_exercise_button.check_visible(nth=index)

    def click_create_exercise_button(self, index:int):
        self.create_exercise_button.click(nth=index)