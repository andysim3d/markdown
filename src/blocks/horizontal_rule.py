import re
from .paragraph import Paragraph


class HorizontalRule(Paragraph):
    '''
        https://www.markdownguide.org/basic-syntax/#horizontal-rules
    '''
    def nested(self):
        ''' Horizontal Rule has no child '''
        return False

    def _render(self):
        return '<hr>'
