import re
from block import Block

SUPPORTED_LANGUAGE = {
    'c',
    'c++',
    'java',
    'python',
    'javascript',
    'golang',
    'c#',
    'html',
    'css',
}

class FenchedCodeBlock(Block):
    '''
        https://www.markdownguide.org/extended-syntax/#fenced-code-blocks
        https://www.markdownguide.org/basic-syntax/#escaping-backticks

        Use triple-backticks(```) to indicate a code block.
        To escape backticks in the code block, use double-backticks(``).
    '''

    def __init__(self, content, language):
        super().__init__(content)
        self._language = language

    def _render(self):
        return '<code>{}</code>'.format(self.content())


    @staticmethod
    def parse(content):
        '''
        Input: a text content
        Output: a tuple (int, int, FenchedCodeBlock)
            [0]: start index,
            [1]: end index,
            [2]: created class,
        Note, the index of start and end follow the convention of [start, end)
        Return (-1, -1, None) if no such match found.

        Convention as Github Markdown Parser:
            1) Use more than 3 back-ticks in its own line to represent fenches
            2) support indicating different language after the starting back-ticks
            3) allow at most three spaces before back-ticks
            4) allow any number of spaces after back-ticks
            5) if the ending back-ticks are less than the starting ones,
               all the remaining content would be in a code block.
        '''
        pattern = r'^ {0,3}(`{3,}) *([^\n]*)\s+(((?:.|\n)*)\n {0,3}(`{3,})\s*(.|\n)*)$'
        matches = re.search(pattern, content, re.MULTILINE)
        if matches:

            language = None
            if matches.group(2) and str(matches.group(2)).lower() in SUPPORTED_LANGUAGE:
                language = str(matches.group(2)).lower()

            num_starting = matches.group(1)
            num_ending = matches.group(5)
            if num_starting > num_ending:
                return (
                    matches.start(1),
                    matches.end(3),
                    FenchedCodeBlock(matches.group(3), language)
                )
            else:
                return (
                    matches.start(1),
                    matches.end(5),
                    FenchedCodeBlock(matches.group(4), language)
                )
        else:
            return (-1, -1, None)
