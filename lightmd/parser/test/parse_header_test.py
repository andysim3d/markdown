import pytest
from ..header_parser import parse_header_paragraph
from ...render.html_render import get_html_format


@pytest.mark.parametrize("content, expected_html",
                         [('  ### abc', '<h3>abc</h3>'),
                          (' # ababa# bbba', '<h1>ababa# bbba</h1>'),
                          ('#ttt', '<h1>ttt</h1>')])
def test_header_parse_success(content, expected_html):
    start, end, header = parse_header_paragraph(content)
    assert start == 0
    assert end == len(content)
    assert header is not None
    assert expected_html == get_html_format(header).format(header.content())


@pytest.mark.parametrize("content", [('####### ababa# bbba'), ('ttt')])
def test_header_parse_failed(content):
    start, end, header = parse_header_paragraph(content)
    assert start == -1
    assert end == -1
    assert header is None
