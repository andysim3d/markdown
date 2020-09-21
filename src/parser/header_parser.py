import re
import typing
from ..blocks import HeaderParagraph


def parse_header_paragraph(content):
    """
    Parse a text content, and return (begin, end, Element) if parseable,
    or (-1, -1, None) that no such a element
    """
    header_pattern = r"^([ ]*)(#+)([ ]*)(.+)$"

    def _parse(content):
        header = re.search(header_pattern, content)
        if header:
            header_num = len(header.group(2))
            if header_num > 6:
                return None
            header_content = header.group(4)
            return HeaderParagraph(level=header_num, content=header_content)
        return None

    header = _parse(content)
    if header:
        return 0, len(content), header
    return (-1, -1, None)
