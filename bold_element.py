from element import Element
import re

class BoldElement(Element):

    def _render(self):
        pattern = re.compile(r'[*]{2}(.*?)[*]{2}')
        rendered = pattern.sub(r'<strong>\1</strong>', self.content())
        return rendered


        