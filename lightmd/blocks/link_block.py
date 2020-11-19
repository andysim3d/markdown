import re
from .block import Block


class LinkBlock(Block):
    def __init__(self, content, url, children=None):
        super().__init__(content, children)
        self._url = url

    def url(self):
        return self._url
