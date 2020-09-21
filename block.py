from element import Element

class Block(Element):
    def __init__(self, content):
        super().__init__(content)

class TextBlock(Block):
    """Pure text block"""
    def __init__(self, content):
        super().__init__(content)

    def render(self):
        return str(self._content)
