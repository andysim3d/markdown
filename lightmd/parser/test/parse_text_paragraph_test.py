import pytest
from ..text_paragraph_parser import parse_text_pargraph, parse_empty_newlines
from ...blocks.paragraph import TextParagraph


@pytest.mark.parametrize(
    "content, expected_start, expected_end, expected_obj", [
        (r"""testing text""", 0, 12, TextParagraph("testing text")),
        (r"""abc
def
g
""", 0, 10, TextParagraph("abcdefg")),
        (r"""abc
def
g

higk
""", 0, 11, TextParagraph("abcdefg")),
    ])
def test_text_paragraph_parse(content, expected_start, expected_end,
                              expected_obj):
    start, end, text_paragraph = parse_text_pargraph(content)
    assert expected_start == start
    assert expected_end == end
    assert text_paragraph is not None
    assert expected_obj == text_paragraph


@pytest.mark.parametrize("content, expected_start, expected_end", [
    (r"""



""", 0, 4),
    (r"""

""", 0, 2),
    (r"""
""", 0, 1),
])
def test_multiple_line_parse(content, expected_start, expected_end):
    start, end, _ = parse_empty_newlines(content)
    assert expected_start == start
    assert expected_end == end


@pytest.mark.parametrize("content", [
    (r""""""),
])
def test_multiple_line_parse_failed(content):
    start, end, _ = parse_empty_newlines(content)
    assert -1 == start
    assert -1 == end
