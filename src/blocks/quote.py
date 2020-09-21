import re
from .paragraph import Paragraph
class QuoteParagraph(Paragraph):
    """Element decorated by '>'.
    """
    def __init__(self, content):
        super().__init__(content)

    def render(self) -> str:
        return "<blockquote>{}</blockquote>".format(self.content())
