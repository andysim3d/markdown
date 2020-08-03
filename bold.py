from block import Block

class BoldBlock(Block):
    '''
        https://www.markdownguide.org/basic-syntax/#bold
    '''
    def _render(self):
        return '<strong>{}</strong>'.format(self.content())


        