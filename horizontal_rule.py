from paragraph import Paragraph

class HorizontalRule(Paragraph):
    '''
        https://www.markdownguide.org/basic-syntax/#horizontal-rules
    '''
    def _render(self):
        return '<hr>'
