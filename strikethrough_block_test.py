import pytest
from strikethrough_block import StrikethroughBlock


@pytest.mark.parametrize("content, html", [
    ("testing text", "<del>testing text</del>"),
    ("", "<del></del>")
])
def test_strikethrough_render(content, html):
    strikethrough_block = StrikethroughBlock(content)
    assert html == strikethrough_block.render()


@pytest.mark.parametrize("content, expected_start, expected_end, html", [
    ("~testing text~", 0, 14, "<del>testing text</del>"),
    ("~~testing text~~", 0, 16, "<del>testing text</del>"),
    ("\\~~testing text~", 2, 16, "<del>testing text</del>"),
    ("~testing text~\\~", 0, 14, "<del>testing text</del>"),
    ("~testing text\\~~", 0, 16, "<del>testing text\\~</del>"),
])
def test_strikethrough_parse(content, expected_start, expected_end, html):
    start, end, strikethrough_block = StrikethroughBlock.parse(content)
    assert expected_start == start
    assert expected_end == end
    assert strikethrough_block is not None
    assert html == strikethrough_block.render()


@pytest.mark.parametrize("content", [
    ("~test"),
    ("~~test"),
    ("~~test~"),
    ("~~~test~~~"),
    ("~~~test")
])
def test_strikethrough_parse_failed(content):
    start, end, strikethrough_block = StrikethroughBlock.parse(content)
    assert -1 == start == end
    assert strikethrough_block is None
