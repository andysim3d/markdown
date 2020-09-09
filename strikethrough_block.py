import re
from block import Block


class StrikethroughBlock(Block):
    """Element wrapped by '~'
    """

    def __init__(self, content):
        super().__init__(content)

    def render(self) -> str:
        return f"<del>{self.content()}</del>"

    @staticmethod
    def parse(content) -> (int, int, 'StrikethroughBlock'):
        """Parse a strikethrough content, and return (begin, end, StrikethroughBlock) if parseable,
        or (-1, -1, None) that no such a element.
        Behavior on github markdown:
        1) ~a~ or ~~a~~ -> strikethrough
        2) any single ~ is plain text. ~~a~ -> plain text
        3) Once the number of leading ~ > 2, it will be a code block and ignore content.
        """
        pattern = r'(^|[^\\])([~]+)(.*[^~\\])(\\~)*([~]+)'
        wave_match = re.search(pattern, content)
        if wave_match:
            start_wave_num = len(wave_match.group(2))
            end_wave_num = len(wave_match.group(5))

            if start_wave_num <= 2:
                if start_wave_num == end_wave_num:
                    start = wave_match.start()
                    if wave_match.group(1):
                        start += 1
                    end = wave_match.end()
                    content = wave_match.group(3)
                    content += wave_match.group(
                        4) if wave_match.group(4) else ""
                    return (start, end, StrikethroughBlock(content))
            # else: call Code

        return (-1, -1, None)
