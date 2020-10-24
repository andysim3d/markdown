import re
from .paragraph import Paragraph


class QuoteParagraph(Paragraph):
    """Element decorated by '>'.
    """
    def __init__(self, content, children=None):
        super().__init__(content, children)

    def render(self) -> str:
        return "<blockquote>{}</blockquote>".format(self.content())

    def render_html(self):
        return "<blockquote>{}</blockquote>"
