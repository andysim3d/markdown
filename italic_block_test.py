import pytest
from italic_block import ItalicBlock


@pytest.mark.parametrize("content, html", [
    ("testing text", "<em>testing text</em>"),
    ("", "<em></em>")
])
def test_italic_render(content, html):
    italic_block = ItalicBlock(content)
    assert html == italic_block.render()


@pytest.mark.parametrize("content, expected_start, expected_end, html", [
    ("*testing text*", 0, 14, "<em>testing text</em>"),
    ("_testing text_", 0, 14, "<em>testing text</em>"),
    ("*testing text**", 0, 15, "<em>testing text*</em>"),
    ("*_testing text_*", 0, 16, "<em>_testing text_</em>"), # the final output is <em>testing text</em>
    (r"\_*testing text\_*", 2, 18, r"<em>testing text\_</em>"),
    (r"\**testing text*", 2, 16, "<em>testing text</em>"),
    (r"\**testing text*\*", 2, 16, "<em>testing text</em>"),
    (r"*\*testing text*\*", 0, 16, r"<em>\*testing text</em>")
])
def test_italic_parse(content, expected_start, expected_end, html):
    start, end, italic_block = ItalicBlock.parse(content)
    assert start == expected_start
    assert end == expected_end
    assert italic_block is not None
    assert html == italic_block.render()


@pytest.mark.parametrize("content", [
    ("*testing text"),
    ("*testing text_"),
    (r"\*testing text*"),
    (r"\*testing text\*"),
    (r"\**testing text\*")
])
def test_italic_parse_failed(content):
    start, end, italic_block = ItalicBlock.parse(content)
    assert start == end == -1
    assert italic_block is None
