import re
from .block import Block


class ItalicBlock(Block):
    """Element wrapped by '*' or '_'
    """
    def __init__(self, content):
        super().__init__(content)

    def render(self) -> str:
        return f"<em>{self.content()}</em>"
