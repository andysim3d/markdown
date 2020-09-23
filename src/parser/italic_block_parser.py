import re
from ..blocks import ItalicBlock


def parse_italic_block(content) -> (int, int, 'ItalicBlock'):
    """
    Parse a italic content, and return (begin, end, ItalicBlock)
    if parseable, or (-1, -1, None) that no such a element
    """
    pattern_star = r'(?:^|[^\\])([*])(.*[^\\])([*])'
    pattern_underscore = r'(?:^|[^\\])([_])(.*[^\\])([_])'

    match_star = re.search(pattern_star, content)
    match_underscore = re.search(pattern_underscore, content)

    def _parse_hanlder(match):
        start = match.start(1)
        end = match.end()
        content = match.group(2)
        return (start, end, ItalicBlock(content))

    if match_star:
        return _parse_hanlder(match_star)
    elif match_underscore:
        return _parse_hanlder(match_underscore)
    else:
        return (-1, -1, None)
