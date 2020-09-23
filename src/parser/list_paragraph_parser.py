import re
from ..blocks import OrderedList, UnorderedList


def parse_ordered_list(content) -> (int, int, 'OrderedList'):
    """Parse a list paragraph, and return (begin, end, OrderedList) if parseable,
    or (-1, -1, None) that no such a element
    """
    pattern = r'^[ ]*\d\.[ ]+(.*)$\n*'
    matches = re.search(pattern, content, re.MULTILINE)
    if matches:
        return (matches.start(), matches.end(), OrderedList(matches.group(1)))
    return (-1, -1, None)


def parse_unordered_list(content) -> (int, int, 'UnorderedList'):
    """
    Parse a list paragraph, and return (begin, end, UnorderedList)
    if parseable, or (-1, -1, None) that no such a element
    """
    pattern = r'^[ ]*(?:\*|\-|\+)[ ]+(.*)$\n*'
    matches = re.search(pattern, content, re.MULTILINE)
    if matches:
        return (matches.start(), matches.end(),
                UnorderedList(matches.group(1)))
    return (-1, -1, None)
