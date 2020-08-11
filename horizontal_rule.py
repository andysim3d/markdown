import re
from paragraph import Paragraph

class HorizontalRule(Paragraph):
    '''
        https://www.markdownguide.org/basic-syntax/#horizontal-rules
    '''
    def _render(self):
        return '<hr>'

    @staticmethod
    def parse(content):
        '''
        Input: a text content
        Output: a tuple (int, int, HorizontalRule)
            [0]: start index,
            [1]: end index,
            [2]: created class,
        Note, the index of start and end follow the convention of [start, end)
        Return (-1, -1, None) if no such match found.
        '''
        pattern = r'^ *(?:\*{3,}|-{3,}|_{3,}) *$'
        matches = re.search(pattern, content, re.MULTILINE)
        if matches:
            return (matches.start(), matches.end(), HorizontalRule(''))
        else:
            return (-1, -1, None)
