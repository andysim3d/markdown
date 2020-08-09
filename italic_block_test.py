import pytest
from italic_block import ItalicBlock


@pytest.mark.parametrize("content, html", [
    ("testing text", "<em>testing text</em>"),
    ("", "<em></em>")
])
def test_italic_render(content, html):
    italic_block = ItalicBlock(content)
    assert html == italic_block.render()


@pytest.mark.parametrize("content, html", [
    ("*testing text*", "<em>testing text</em>"),
    ("_testing text_", "<em>testing text</em>"),
    ("*testing text**", "<em>testing text*</em>")
])
def test_italic_parse(content, html):
    start, end, italic_block = ItalicBlock.parse(content)
    assert 0 == start
    assert len(content) == end
    assert italic_block is not None
    assert html == italic_block.render()

@pytest.mark.parametrize("content", [
    ("*testing text"),
    ("*testing text_"),
    ("\\*testing text*"),
])
def test_italic_parse_failed(content):
    start, end, italic_block = ItalicBlock.parse(content)
    assert -1 == start == end
    assert italic_block is None
