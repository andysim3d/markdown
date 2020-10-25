import re
from .paragraph import Paragraph


class FencedCodeBlock(Paragraph):
    '''
        https://www.markdownguide.org/extended-syntax/#fenced-code-blocks
        https://www.markdownguide.org/basic-syntax/#escaping-backticks

        Use triple-backticks(```) to indicate a code block.
        To escape backticks in the code block, use double-backticks(``).

        Support language hightlighting by using Goolge's code-prettify:
        https://github.com/googlearchive/code-prettify
    '''
    def __init__(self, content, language=None, children=None):
        super().__init__(content, children)
        self._language = language

    def nested(self):
        '''Fenched Code Block should not hold child except TextBlock '''
        return False

    def _render(self):
        code_tag = '<code>{}</code>'.format(self.content())
        if not self._language:
            return '<pre class="prettyprint">{}</pre>'.format(code_tag)
        else:
            return '<pre class="prettyprint lang-{0}">{1}</pre>'.format(
                self._language, code_tag)
