from block import Block

class FenchedCodeBlock(Block):
    '''
        https://www.markdownguide.org/extended-syntax/#fenced-code-blocks
        https://www.markdownguide.org/basic-syntax/#escaping-backticks

        Use triple-backticks(```) to indicate a code block.
        To escape backticks in the code block, use double-backticks(``).
    '''

    def _render(self):
        return '<code>{}</code>'.format(self.content())
