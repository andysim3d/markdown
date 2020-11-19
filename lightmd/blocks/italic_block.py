import re
from .block import Block


class ItalicBlock(Block):
    """Element wrapped by '*' or '_'
    """
    def __init__(self, content, children=None):
        super().__init__(content, children)
