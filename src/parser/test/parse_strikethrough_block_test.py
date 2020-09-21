import pytest
from ..strikethrough_block_parser import parse_strike_through_block


@pytest.mark.parametrize("content, expected_start, expected_end, html", [
    ("~testing text~", 0, 14, "<del>testing text</del>"),
    (r"~\~testing text~", 0, 16, r"<del>\~testing text</del>"),
    ("~~testing text~~", 0, 16, "<del>testing text</del>"),
    (r"\~~testing text~", 2, 16, "<del>testing text</del>"),
    (r"~testing text~\~", 0, 14, "<del>testing text</del>"),
    (r"~testing text\~~", 0, 16, r"<del>testing text\~</del>"),
    (r"\~~~testing text~~", 2, 18, "<del>testing text</del>"),
    (r"\~\~~testing text~\~", 4, 18, "<del>testing text</del>"),
])
def test_strikethrough_parse(content, expected_start, expected_end, html):
    start, end, strikethrough_block = parse_strike_through_block(content)
    assert expected_start == start
    assert expected_end == end
    assert strikethrough_block is not None
    assert html == strikethrough_block.render()


@pytest.mark.parametrize("content", [
    ("~test"),
    (r"\~test~"),
    ("~~test"),
    ("~~test~"),
    (r"~~test\~~"),
    (r"~~test~\~"),
    (r"\~~test~~"),
    ("~~~test~~~"),
    ("~~~test")
])
def test_strikethrough_parse_failed(content):
    start, end, strikethrough_block = parse_strike_through_block(content)
    assert -1 == start == end
    assert strikethrough_block is None
