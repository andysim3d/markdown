class Element(object):
    """Super class for any objects"""
    def __init__(self, content):
        self._content = content # text content 
        self._children = []
        self._parent = None

    def render(self):
        """render self as html format"""
        return self._render()

    def content(self):
        return self._content

    def children(self):
        return self._children
        
    def inner_text(self):
        "inner text or nested elements as string format"
        return str(self._content)

    def _render(self):
        pass

    def nested(self):
        """Could this element hold other elements inside, True for yes.
        """
        return False

class Paragraph(Element):
    def __init__(self, content):
        super().__init__(content)

    def nested(self):
        """All paragraph elements probably contains children.
        """
        return True

class Block(Element):
    def __init__(self, content):
        super().__init__(content)

    def nested(self):
        """All paragraph elements probably contains children.
        """
        return False
    
    def children(self):
        return None

class TextBlock(Block):
    """Pure text block"""
    def __init__(self, content):
        super().__init__(content)

    def render(self):
        return str(self._content)

class QuoteParagraph(Paragraph):
    """Element decorated by '>'.
    """
    def __init__(self, content):
        super().__init__(content)

    def render(self) -> str:
        return "<blockquote> {} </blockquote>".format(self.inner_text())

class ImgBlock(Block):
    def __init__(self, content, url):
        super().__init__(content)
        self._url = url
    def render(self) -> str:
        return "<img src='{}' alt='{}'> </img>".format(self._url, self.inner_text())

class ItalicBlock(Block):
    """Element wrapped by '*' or '_'
    """
    def __init__(self, content):
        super().__init__(content)
    
    def render(self) -> str:
        return f"<em>{self.inner_text()}</em>"

class UnorderedParagraph(Paragraph):
    """Line starting with '-', '*' or '+'
    """
    def __init__(self, content, isStart=None, isEnd=None):
        super().__init__(content)
        self._isStart = isStart
        self._isEnd = isEnd
    
    def render(self) -> str:
        item = f"<li>{self.inner_text()}</li>"
        if self._isStart == None and self._isEnd == None:
            return item
        elif self._isStart:
            return f"<ul>{item}"
        elif self._isEnd:
            return f"{item}</ul>"

class LinkBlock(Block):
    def __init__(self, content, url):
        super().__init__(content)
        self._url = url
    
    def render(self) -> str:
        return f"<a href='{self._url}'>{self.inner_text()}</a>"

class StrikethroughBlock(Block):
    """Element wrapped by '~'
    """
    def __init__(self, content):
        super().__init__(content)
    
    def render(self) -> str:
        return f"<del>{self.inner_text()}</del>"