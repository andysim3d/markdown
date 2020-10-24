from .element import Element


class Block(Element):
    def __init__(self, content, children=None):
        super().__init__(content, children)


class TextBlock(Block):
    """Pure text block"""
    def __init__(self, content, children=None):
        super().__init__(content, children)

    def render(self):
        return str(self._content)

    def render_html(self):
        return str(self._content)

    def nested(self):
        return False
