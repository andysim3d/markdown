import re
from .paragraph import Paragraph


class ListParagraph(Paragraph):
    def __init__(self, content, is_ordered):
        super().__init__(content)
        self._is_ordered = is_ordered

    def render(self) -> str:
        return f"<li>{self.content()}</li>"


class OrderedList(ListParagraph):
    """Line starting with number
    """

    def __init__(self, content):
        super().__init__(content, True)


class UnorderedList(ListParagraph):
    """Line starting with '-', '*' or '+'
    """

    def __init__(self, content):
        super().__init__(content, False)
