import re
from ..blocks import HorizontalRule


def parse_horiontal_rule(content):
    '''
    Input: a text content
    Output: a tuple (int, int, HorizontalRule)
        [0]: start index,
        [1]: end index,
        [2]: created class,
    Note, the index of start and end follow the convention of [start, end)
    Return (-1, -1, None) if no such match found.
    '''
    pattern = r'^[^\S\r\n]*(\*{3,}|-{3,}|_{3,})[^\S\r\n]*$\n?'
    matches = re.search(pattern, content, re.MULTILINE)
    if matches:
        return (matches.start(), matches.end(), HorizontalRule(''))
    else:
        return (-1, -1, None)
