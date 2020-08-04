from paragraph import Paragraph

class ListParagraph(Paragraph):
    def __init__(self, content, isOrdered, isStart=None, isEnd=None):
        super().__init__(content)
        self._isOrdered = isOrdered
        self._isStart = isStart
        self._isEnd = isEnd
    
    def render(self) -> str:
        item = f"<li>{self.content()}</li>"
        if self._isStart == None and self._isEnd == None:
            return item
        elif self._isStart:
            return f"<ol>{item}" if self._isOrdered else f"<ul>{item}"
        elif self._isEnd:
            return f"{item}</ol>" if self._isOrdered else f"{item}</ul>" 

class OrderedList(ListParagraph):
    """Line starting with number
    """
    def __init__(self, content, isStart, isEnd):
        super().__init__(content, True, isStart, isEnd)

class UnorderedList(ListParagraph):
    """Line starting with '-', '*' or '+'
    """
    def __init__(self, content, isStart, isEnd):
        super().__init__(content, False, isStart, isEnd)