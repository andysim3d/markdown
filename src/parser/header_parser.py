import re
import typing
from ..blocks import HeaderParagraph


def parse_header_paragraph(content):
    """
    Parse a text content, and return (begin, end, Element) if parseable,
    or (-1, -1, None) that no such a element
    """
    header_pattern = r"^([ ]*)(#+)([ ]*)(.+)$"

    header = re.search(header_pattern, content, re.MULTILINE)
    if header:
        header_num = len(header.group(2))
        if header_num > 6:
            return (-1, -1, None)
        header_content = header.group(4)
        return (header.start(), header.end(),
                HeaderParagraph(level=header_num, content=header_content))
    return (-1, -1, None)
