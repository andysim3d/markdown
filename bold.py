import re
from block import Block

class BoldBlock(Block):
    '''
        https://www.markdownguide.org/basic-syntax/#bold
    '''
    def _render(self):
        return '<strong>{}</strong>'.format(self.content())

    @staticmethod
    def parse(content):
        '''
        Input: a text content
        Output: a tuple (int, int, BoldBlock)
            [0]: start index,
            [1]: end index,
            [2]: created class,

        Note, the index of start and end follow the convention of [start, end)

        Return (-1, -1, None) if no such match found.
        '''
        pattern = r'([*]+)(.*?)([*]+)'
        matches = re.search(pattern, content)
        if matches:
            head_asterisks_num = len(matches.group(1))
            tail_asterisks_num = len(matches.group(3))
            start_index = matches.start(1)
            end_index = matches.end(3)

            # follow the trigger convention of Github
            # as long as head or tail has three asterisks, it's bold and italic
            if (head_asterisks_num == 3 or tail_asterisks_num == 3) and \
                head_asterisks_num+tail_asterisks_num >= 6:
                # match Bold and Italic first
                # ***test*** -> *test* -> pass to ItatlicBlock()
                head_remain = max(head_asterisks_num - 2, 0)
                tail_remain = max(tail_asterisks_num - 2, 0)
                bold_content = '*' * head_remain + matches.group(2) + '*' * tail_remain
                return (
                    start_index,
                    end_index,
                    BoldBlock(content=bold_content)
                )
            elif head_asterisks_num >= 2 and tail_asterisks_num >= 2:
                # match bold without italic
                diff = head_asterisks_num - tail_asterisks_num
                if diff >= 0:
                    bold_content = '*' * diff + matches.group(2)
                else:
                    bold_content = matches.group(2) + '*' * -diff
                return (
                    start_index,
                    end_index,
                    BoldBlock(content=bold_content)
                )
        return (-1, -1, None)
