import re
from ..blocks import QuoteParagraph


def parse_quote(content) -> (int, int, 'QuoteParagraph'):
    """Parse a quote content, and return (begin, end, QuoteParagraph) if parseable,
    or (-1, -1, None) that no such a element
    """
    pattern = r'^[ ]*\>[ ]*(.*)$'

    quote_match = re.search(pattern, content)
    if quote_match:
        start = 0
        end = len(content)
        content = quote_match.group(1)
        return (start, end, QuoteParagraph(content))
    return (-1, -1, None)
