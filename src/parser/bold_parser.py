import re
from ..blocks import BoldBlock


def parse_bold_block(content):
    '''
    Input: a text content
    Output: a tuple (int, int, BoldBlock)
        [0]: start index,
        [1]: end index,
        [2]: created class,

    Note, the index of start and end follow the convention of [start, end)

    Return (-1, -1, None) if no such match found.
    '''
    pattern = \
        r'(?:^|[^\\])(([*_]{2,})((?:\\(?:\*|_|\\))*(?:.*[^*_\\])(?:\\(?:\*|_|\\))*)([*_]{2,}))'  # pylint: disable=line-too-long
    matches = re.search(pattern, content)
    if matches:
        head_asterisks_num = len(matches.group(2))
        tail_asterisks_num = len(matches.group(4))
        start_index = matches.start(1)
        end_index = matches.end()

        bold_content = ""
        for i in range(3, 4):
            bold_content += matches.group(i) if matches.group(i) else ""

        # follow the trigger convention of Github
        # as long as head or tail has three asterisks, it's bold and italic
        if ((head_asterisks_num == 3 or tail_asterisks_num == 3)
                and head_asterisks_num + tail_asterisks_num >= 6):
            # match Bold and Italic first
            # ***test*** -> *test* -> pass to ItatlicBlock()
            head_remain = max(head_asterisks_num - 2, 0)
            tail_remain = max(tail_asterisks_num - 2, 0)
            bold_content = '*' * head_remain + bold_content + '*' * tail_remain
            return (start_index, end_index, BoldBlock(content=bold_content))
        elif head_asterisks_num >= 2 and tail_asterisks_num >= 2:
            # match bold without italic
            diff = head_asterisks_num - tail_asterisks_num
            if diff >= 0:
                bold_content = '*' * diff + bold_content
            else:
                bold_content = bold_content + '*' * -diff
            return (start_index, end_index, BoldBlock(content=bold_content))

    return (-1, -1, None)
