from paragraph import Paragraph

class Header(Paragraph):
    def __init__(self, content, level = 1):
        super().__init__(content)
        assert level > 0 and level <= 6
        self._level = level
    
    def render(self):
        return "<h{0}> {1} </h{0}>".format(self._level, self.content())
