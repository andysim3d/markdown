import re
from paragraph import Paragraph

class HorizontalRule(Paragraph):
    '''
        https://www.markdownguide.org/basic-syntax/#horizontal-rules
    '''

    def nested(self):
        ''' Horizontal Rule has no child '''
        return False

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
        pattern = r'^\s*(\*{3,}|-{3,}|_{3,})\s*$'
        matches = re.search(pattern, content, re.MULTILINE)
        if matches:
            return (matches.start(1), matches.end(1), HorizontalRule(''))
        else:
            return (-1, -1, None)
