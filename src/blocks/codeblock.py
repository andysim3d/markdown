import re
from typing import Text
from .block import Block


class CodeBlock(Block):
    '''
        https://www.markdownguide.org/extended-syntax/#fenced-code-blocks
        https://www.markdownguide.org/basic-syntax/#escaping-backticks

        Use backticks(`) to indicate a code block.
    '''
    def nested(self):
        ''' Code Block should not hold child except TextBlock '''
        return False

    def _render(self):
        return '<code>{}</code>'.format(self.content())
