import re
from .block import Block


class StrikethroughBlock(Block):
    """Element wrapped by '~'
    """

    def __init__(self, content):
        super().__init__(content)

    def render(self) -> str:
        return f"<del>{self.content()}</del>"
