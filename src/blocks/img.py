import re
from .block import Block

class ImgBlock(Block):
    def __init__(self, content, url):
        super().__init__(content)
        self._url = url

    def nested(self):
        ''' Img Block should not has child '''
        return False

    def render(self) -> str:
        return '<img src="{}" alt="{}"> </img>'.format(self._url, self.content())
