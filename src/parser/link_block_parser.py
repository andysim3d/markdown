import re
from ..blocks import LinkBlock


def parse_link_block(content) -> (int, int, 'LinkBlock'):
    """Parse a link content, and return (begin, end, LinkBlock) if parseable,
    or (-1, -1, None) that no such a element
    """
    pattern = r'(^|[^\\])\[(.*[^\\])\]\((.*[^\\])\)'

    link_match = re.search(pattern, content)
    if link_match:
        start = link_match.start()
        if link_match.group(1):
            # escape case
            start += 1
        end = link_match.end()
        url = link_match.group(3)
        content = link_match.group(2)
        url = url if url else ""
        content = content if content else ""
        return (start, end, LinkBlock(content, url))
    return (-1, -1, None)
