import re
from typing import Text
from ..blocks import CodeBlock, TextBlock


def parse_code_block(content: Text):
    '''
    Parse a text content, and return (begin, end, Element) if parseable,
    or (-1, -1, None) that no such a element
    '''
    code_pattern = r"(^`|[^\\]`)([^\n]*[^\\])*`"
    code_match = re.search(code_pattern, content)
    if code_match:
        start = code_match.start()
        if code_match.group(1) != "`":
            '''matched non \\` case, move start one step back'''
            start = start + 1
        end = code_match.end()
        code_str = code_match.group(2) if code_match.group(2) else ""
        return (start, end, CodeBlock(code_str))
    return (-1, -1, None)
