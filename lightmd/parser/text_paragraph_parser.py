# r"(^.+(\n?))+(\n)?"

import re
import os
from ..blocks import TextParagraph


def parse_text_pargraph(content) -> (int, int, 'TextParagraph'):
    """Parse a text paragraph content, and return (begin, end,
    TextParagraph) if parseable,
    or (-1, -1, None) that no such a element.
    """
    pattern = r"(^.+(\n?))+(\n)?"
    paragraph_match = re.search(pattern, content, re.MULTILINE)
    if paragraph_match:
        full_text = paragraph_match.group(0).replace(
            os.linesep, "")  # remove all newline in one text paragraph.
        start = paragraph_match.start()
        end = paragraph_match.end()
        return (start, end, TextParagraph(full_text))
    return (-1, -1, None)


def parse_empty_newlines(content) -> (int, int, 'None'):
    """
    Parse multiple empty line. If match, return start and end of continous empty lines.
    or -1, -1, None.
    """
    pattern = r"(\s*\n)+"
    empty_line_match = re.search(pattern, content, re.MULTILINE)
    if empty_line_match and empty_line_match.start() == 0:
        return (empty_line_match.start(), empty_line_match.end(), None)
    return -1, -1, None
