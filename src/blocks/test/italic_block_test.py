import pytest
from ..italic_block import ItalicBlock


@pytest.mark.parametrize("content, html",
                         [("testing text", "<em>testing text</em>"),
                          ("", "<em></em>")])
def test_italic_render(content, html):
    italic_block = ItalicBlock(content)
    assert html == italic_block.render()
