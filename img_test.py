import pytest
from img import ImgBlock


@pytest.mark.parametrize("content, url, html", [
    ('test image', "https://google.com/imagea",
     '<img src="https://google.com/imagea" alt="test image"> </img>'),
])
def test_render(content, url, html):
    img = ImgBlock(content, url)
    assert html == img.render()


@pytest.mark.parametrize("content, expected_html, start, end", [

    ('![abc](such a url)', '<img src="such a url" alt="abc"> </img>', 0,
     18),
    ('![abc](such a url\))', '<img src="such a url\)" alt="abc"> </img>', 0,
     20),
    ('![abc\]](such a url\))', '<img src="such a url\)" alt="abc\]"> </img>',
     0, 22),
    ('d![abc\]](such a url\))', '<img src="such a url\)" alt="abc\]"> </img>',
     1, 23),
    ('dd![abc\]](such a url\))', '<img src="such a url\)" alt="abc\]"> </img>',
     2, 24),
])
def test_img_parse_success(content, expected_html, start, end):
    start_, end_, img = ImgBlock.parse(content)
    assert start == start_
    assert end == end_
    assert img is not None
    assert expected_html == img.render()


@pytest.mark.parametrize("content",
                         [('\![abc](such a url\))'),
                          ('![abc](such a url\)'), '![abc\](such a url)'])
def test_img_parse_failed(content):
    start, end, img = ImgBlock.parse(content)
    assert start == -1
    assert end == -1
    assert img is None