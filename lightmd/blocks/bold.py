import re
from .block import Block


class BoldBlock(Block):
    '''
        https://www.markdownguide.org/basic-syntax/#bold
    '''
    def __init__(self, content, children=None):
        super().__init__(content, children)

    def render(self, format_functor):
        rendered_children = []
        for child in self._children:
            rendered_children.append(child.render(format_functor))

        return format_functor(self).format("".join(rendered_children))
