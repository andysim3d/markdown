import pytest
from ..list_paragraph_parser import parse_ordered_list, parse_unordered_list


@pytest.mark.parametrize("content, expected_start, expected_end, expected_indent, html",
                         [("1. first item", 0, 13, 0, "<li>first item</li>"),
                          ("1.  first item", 0, 14, 0, "<li>first item</li>"),
                          ("  1. first item", 0, 15, 2, "<li>first item</li>")])
def test_ordered_parse(content, expected_start, expected_end, expected_indent, html):
    start, end, ordered_list = parse_ordered_list(content)
    assert expected_start == start
    assert expected_end == end
    assert ordered_list is not None
    assert expected_indent == ordered_list.indent
    assert html == ordered_list.render()


@pytest.mark.parametrize("content", [
    ("not a list"),
    (r"1\. first item"),
    ("1 first item"),
    ("1.first item"),
    ("1, first item"),
    ("aa1. first item"),
])
def test_ordered_parse_failed(content):
    start, end, ordered_list = parse_ordered_list(content)
    assert start == end == -1
    assert ordered_list is None


@pytest.mark.parametrize("content, expected_start, expected_end, expected_indent, html",
                         [("* first item", 0, 12, 0, "<li>first item</li>"),
                          ("- first item", 0, 12, 0, "<li>first item</li>"),
                          ("+ first item", 0, 12, 0, "<li>first item</li>"),
                          (" - first item", 0, 13, 1, "<li>first item</li>"),
                          (r"- \-first item", 0, 14, 0, r"<li>\-first item</li>")]
                         )
def test_unordered_parse(content, expected_start, expected_end, expected_indent, html):
    start, end, unordered_list = parse_unordered_list(content)
    assert expected_start == start
    assert expected_end == end
    assert unordered_list is not None
    assert expected_indent == unordered_list.indent
    assert html == unordered_list.render()


@pytest.mark.parametrize("content", [
    ("not a list"),
    (r"-first item"),
    (r"\-first item"),
    (r"\-- first item"),
    ("aa- first item"),
])
def test_unordered_parse_failed(content):
    start, end, unordered_list = parse_unordered_list(content)
    assert start == end == -1
    assert unordered_list is None
