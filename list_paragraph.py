from paragraph import Paragraph


class ListParagraph(Paragraph):
    def __init__(self, content, is_ordered, is_start=None, is_end=None):
        super().__init__(content)
        self._is_ordered = is_ordered
        self._is_start = is_start
        self._is_end = is_end

    def render(self) -> str:
        item = f"<li>{self.content()}</li>"
        if self._is_start is None and self._is_end is None:
            return item
        elif self._is_start:
            return f"<ol>{item}" if self._is_ordered else f"<ul>{item}"
        elif self._is_end:
            return f"{item}</ol>" if self._is_ordered else f"{item}</ul>"


class OrderedList(ListParagraph):
    """Line starting with number
    """

    def __init__(self, content, is_start, is_end):
        super().__init__(content, True, is_start, is_end)


class UnorderedList(ListParagraph):
    """Line starting with '-', '*' or '+'
    """

    def __init__(self, content, is_start, is_end):
        super().__init__(content, False, is_start, is_end)
