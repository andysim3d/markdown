import re
import typing
from paragraph import Paragraph

class Header(Paragraph):
    def __init__(self, content, level=1):
        super().__init__(content)
        assert level > 0 and level <= 6
        self._level = level

    def render(self):
        return "<h{0}>{1}</h{0}>".format(self._level, self.content())



def parser(content: typing.Text) -> (int, int, Header):
    header_pattern = r"^([ ]*)(#+)([ ]*)(.+)$"
    def _parse(content):
        header = re.search(header_pattern, content)
        if header:
            header_num = len(header.group(2))
            if header_num > 6:
                return None
            header_content = header.group(4)
            return Header(level=header_num, content=header_content)
        return None
    header = _parse(content)
    if header:
        return 0, len(content), header
    return (-1, -1, None)
