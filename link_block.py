from block import Block

class LinkBlock(Block):
    def __init__(self, content, url):
        super().__init__(content)
        self._url = url
    
    def render(self) -> str:
        return f"<a href='{self._url}'>{self.content()}</a>"