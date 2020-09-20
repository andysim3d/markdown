from element import Element

class Paragraph(Element):
    def __init__(self, content):
        super().__init__(content)

    def nested(self):
        """All paragraph elements probably contains children.
        """
        return True

class TextParagraph(Paragraph):
    pass
