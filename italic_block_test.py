import pytest
from italic_block import ItalicBlock

@pytest.mark.parametrize("content, html", [
    ( "testing text", "<em>testing text</em>" ),
    ( "", "<em></em>")
])
def test_italic_render(content, html):
    ib = ItalicBlock(content)
    assert html == ib.render()