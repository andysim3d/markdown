import re
from ..blocks import OrderedList, UnorderedList


def replace_leading_tabs(content, leading_len) -> str:
    # replace tab with 4 spaces
    return content[:leading_len].replace('\t', 4 * ' ') + content[leading_len:]


def parse_ordered_list(content) -> (int, int, 'OrderedList'):
    """Parse a list paragraph, and return (begin, end, OrderedList) if parseable,
    or (-1, -1, None) that no such a element
    """
    pattern = r'^([ \t]*)\d\.[ ]+.*$\n*'
    matches = re.search(pattern, content, re.MULTILINE)
    if matches:
        new_content = replace_leading_tabs(content, len(matches.group(1)))
        new_pattern = r'^([ ]*)\d\.[ ]+(.*)$\n*'
        new_matches = re.search(new_pattern, new_content, re.MULTILINE)
        return (
            new_matches.start(), new_matches.end(), OrderedList(
                new_matches.group(2), len(new_matches.group(1))))
    return (-1, -1, None)


def parse_unordered_list(content) -> (int, int, 'UnorderedList'):
    """
    Parse a list paragraph, and return (begin, end, UnorderedList)
    if parseable, or (-1, -1, None) that no such a element
    """
    pattern = r'^([ \t]*)(?:\*|\-|\+)[ ]+.*$\n*'
    matches = re.search(pattern, content, re.MULTILINE)
    if matches:
        new_content = replace_leading_tabs(content, len(matches.group(1)))
        new_pattern = r'^([ ]*)(?:\*|\-|\+)[ ]+(.*)$\n*'
        new_matches = re.search(new_pattern, new_content, re.MULTILINE)
        return (new_matches.start(), new_matches.end(),
                UnorderedList(new_matches.group(2), len(new_matches.group(1))))
    return (-1, -1, None)
