from elements.base_element import BaseElement


class Text(BaseElement):
    def to_have_text(self, param):
        @property
        def type_of(self) -> str:
            return "text"