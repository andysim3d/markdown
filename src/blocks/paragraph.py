from .element import Element


class Paragraph(Element):
    def __init__(self, content):
        super().__init__(content)


class TextParagraph(Paragraph):
    def __init__(self, content):
        super().__init__(content)
