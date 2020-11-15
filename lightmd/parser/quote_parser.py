import re
from ..blocks import QuoteParagraph


def parse_quote(content) -> (int, int, 'QuoteParagraph'):
    """Parse a quote content, and return (begin, end, QuoteParagraph)
    if parseable, or (-1, -1, None) that no such a element
    """
    pattern = r'^[ ]*\>[ ]*(.*)$\n?'

    quote_match = re.search(pattern, content, re.MULTILINE)
    if quote_match:
        start = quote_match.start()
        end = quote_match.end()
        content = quote_match.group(1)
        return (start, end, QuoteParagraph(content))
    return (-1, -1, None)
