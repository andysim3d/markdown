import re
from block import Block

class ImgBlock(Block):
    def __init__(self, content, url):
        super().__init__(content)
        self._url = url
    def render(self) -> str:
        return '<img src="{}" alt="{}"> </img>'.format(self._url, self.content())

    @staticmethod
    def parse(content):
        img_pattern = r"(^|[^\\])\!\[(.*[^\\])\][ ]*\((.*[^\\])\)"
        img_match = re.search(img_pattern, content)
        if img_match:
            start = img_match.start()
            if img_match.group(1):
                '''matched non \\! case, move start one step back'''
                start = start + 1
            end = img_match.end()
            url = img_match.group(3)
            alt = img_match.group(2)
            url = url if url else ""
            alt = alt if alt else ""
            return (start, end, ImgBlock(url=url, content=alt))
        return (-1, -1, None)
