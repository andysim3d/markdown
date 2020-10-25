import re
import typing
from .paragraph import Paragraph


class HeaderParagraph(Paragraph):
    def __init__(self, content, level=1, children=None):
        super().__init__(content, children)
        assert level > 0 and level <= 6
        self._level = level

    def level(self):
        return self._level

    def render(self):
        return "<h{0}>{1}</h{0}>".format(self._level, self.content())
