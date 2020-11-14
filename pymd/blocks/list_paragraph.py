import re
from .paragraph import Paragraph


class ListParagraph(Paragraph):
    def __init__(self, content, is_ordered, children=None):
        super().__init__(content, children)
        self._is_ordered = is_ordered

    def render(self) -> str:
        return f"<li>{self.content()}</li>"

    def is_ordered(self):
        return self._is_ordered


class ListWrapper(Paragraph):
    def __init__(self, content, is_ordered):
        super().__init__(None)
        self._children = content if content else []
        self._is_ordered = is_ordered

    def is_ordered(self):
        return self._is_ordered

    def render(self) -> str:
        rendered_children = "\n".join((i.render() for i in self._children))
        if self._is_ordered:
            return f"<ol>{rendered_children}</ol>"
        else:
            return f"<ul>{rendered_children}</ul>"


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
