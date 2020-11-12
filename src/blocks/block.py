from .element import Element


class Block(Element):
    def __init__(self, content, children=None):
        super().__init__(content, children)

    def render(self, format_functor):
        return format_functor(self).format(self.content())


class TextBlock(Block):
    """Pure text block"""
    def __init__(self, content, children=None):
        super().__init__(content, children)

    def nested(self):
        return False
