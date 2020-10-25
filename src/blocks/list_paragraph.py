import re
from .paragraph import Paragraph


class ListParagraph(Paragraph):
    def __init__(self, content, is_ordered, indent, children=None):
        super().__init__(content, children)
        self._is_ordered = is_ordered
        self._indent = indent

    def render(self) -> str:
        return f"<li>{self.content()}</li>"

    def is_ordered(self):
        return self._is_ordered

    @property
    def indent(self):
        return self._indent

    @indent.setter
    def indent(self, val):
        self._indent = val


class ListWrapper(Paragraph):
    def __init__(self, content, is_ordered, indent=0):
        super().__init__(None)
        self._children = content if content else []
        self._is_ordered = is_ordered
        self._indent = indent

    def is_ordered(self):
        return self._is_ordered

    @property
    def indent(self):
        return self._indent

    @indent.setter
    def indent(self, val):
        self._indent = val

    def render(self) -> str:
        rendered_children = "\n".join((i.render() for i in self._children))
        if self._is_ordered:
            return f"<ol>{rendered_children}</ol>"
        else:
            return f"<ul>{rendered_children}</ul>"


class OrderedList(ListParagraph):
    """Line starting with number
    """

    def __init__(self, content, indent=0):
        super().__init__(content, True, indent)


class UnorderedList(ListParagraph):
    """Line starting with '-', '*' or '+'
    """

    def __init__(self, content, indent=0):
        super().__init__(content, False, indent)
