import re
from paragraph import Paragraph


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

    @staticmethod
    def parse(content) -> (int, int, 'OrderedList'):
        """Parse a list paragraph, and return (begin, end, OrderedList) if parseable,
        or (-1, -1, None) that no such a element
        """
        pattern = r'^[ ]*\d\.[ ]+(.*)$'
        matches = re.search(pattern, content)
        if matches:
            return (
                matches.start(),
                matches.end(),
                OrderedList(
                    matches.group(1)))
        return (-1, -1, None)


class UnorderedList(ListParagraph):
    """Line starting with '-', '*' or '+'
    """

    def __init__(self, content):
        super().__init__(content, False)

    @staticmethod
    def parse(content) -> (int, int, 'UnorderedList'):
        """Parse a list paragraph, and return (begin, end, UnorderedList) if parseable,
        or (-1, -1, None) that no such a element
        """
        pattern = r'^[ ]*(?:\*|\-|\+)[ ]+(.*)$'
        matches = re.search(pattern, content)
        if matches:
            return (
                matches.start(),
                matches.end(),
                UnorderedList(
                    matches.group(1)))
        return (-1, -1, None)
