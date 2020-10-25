import re
from .block import Block


class ImgBlock(Block):
    def __init__(self, content, url, children=None):
        super().__init__(content, children)
        self._url = url

    def nested(self):
        ''' Img Block should not has child '''
        return False

    def url(self):
        return self._url

    def render(self) -> str:
        return '<img src="{}" alt="{}"> </img>'.format(self._url,
                                                       self.content())
