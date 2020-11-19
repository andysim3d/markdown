from .element import Element


class Paragraph(Element):
    def __init__(self, content, children=None):
        super().__init__(content, children)


class TextParagraph(Paragraph):
    def __init__(self, content, children=None):
        super().__init__(content, children)
