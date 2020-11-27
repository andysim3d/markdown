import pytest
from ..img_parser import parse_img_block
from ...render.html_render import get_html_format


@pytest.mark.parametrize("content, expected_html, start, end", [
    ('![abc](such a url)', '<img src="such a url" alt="abc">', 0, 18),
    ('![abc](such a url\))', '<img src="such a url\)" alt="abc">', 0,
     20),
    ('![abc\]](such a url\))', '<img src="such a url\)" alt="abc\]">',
     0, 22),
    ('d![abc\]](such a url\))', '<img src="such a url\)" alt="abc\]">',
     1, 23),
    ('dd![abc\]](such a url\))', '<img src="such a url\)" alt="abc\]">',
     2, 24),
])
def test_img_parse_success(content, expected_html, start, end):
    start_, end_, img = parse_img_block(content)
    assert start == start_
    assert end == end_
    assert img is not None
    assert expected_html == img.render(get_html_format)


@pytest.mark.parametrize("content",
                         [('\![abc](such a url\))'),
                          ('![abc](such a url\)'), '![abc\](such a url)'])
def test_img_parse_failed(content):
    start, end, img = parse_img_block(content)
    assert start == -1
    assert end == -1
    assert img is None
