import re
from block import Block


class ItalicBlock(Block):
    """Element wrapped by '*' or '_'
    """

    def __init__(self, content):
        super().__init__(content)

    def render(self) -> str:
        return f"<em>{self.content()}</em>"

    @staticmethod
    def parse(content) -> (int, int, 'ItalicBlock'):
        """Parse a italic content, and return (begin, end, ItalicBlock) if parseable,
        or (-1, -1, None) that no such a element
        """
        pattern_star = r'(^|[^\\])([*])(.*[^\\])([*])'
        pattern_underscore = r'(^|[^\\])([_])(.*[^\\])([_])'

        match_star = re.search(pattern_star, content)
        match_underscore = re.search(pattern_underscore, content)

        def _parse_hanlder(match):
            start = match.start()
            if match.group(1):
                # escape case
                start += 1
            end = match.end()
            content = match.group(3)
            return (start, end, ItalicBlock(content))

        if match_star:
            return _parse_hanlder(match_star)
        elif match_underscore:
            return _parse_hanlder(match_underscore)
        else:
            return (-1, -1, None)
