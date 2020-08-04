import pytest
from header import Header, parser

@pytest.mark.parametrize(
    "content, level, html",
    [
        ('title', 1, '<h1> title </h1>'),
        ('another second title', 2, '<h2> another second title </h2>'),
        ('title_3', 3, '<h3> title_3 </h3>'),
    ]
)
def test_render(content, level, html):
    header = Header(content, level)
    assert html == header.render()  

@pytest.mark.parametrize(
    "content, expected_html",
    [
        ('  ### abc', '<h3>abc</h3>'),
        (' # ababa# bbba', '<h1>ababa# bbba</h1>'),
        ('#ttt', '<h1>ttt</h1>')
    ]
)
def test_header_parse_success(content, expected_html):
    start, end, header = parser(content)
    assert start == 0
    assert end == len(content)
    assert header is not None
    assert expected_html == header.render()

@pytest.mark.parametrize(
    "content",
    [
        ('####### ababa# bbba'),
        ('ttt')
    ]
)
def test_header_parse_failed(content):
    start, end, header = parser(content)
    assert start == -1
    assert end == -1
    assert header is None
