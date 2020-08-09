import pytest
from link_block import LinkBlock


@pytest.mark.parametrize("content, url, html",
                         [("google",
                           "https://www.google.com",
                           "<a href='https://www.google.com'>google</a>")])
def test_link_render(content, url, html):
    line_block = LinkBlock(content, url)
    assert html == line_block.render()


@pytest.mark.parametrize("content, expected_start, html",
                         [("[google](https://www.google.com)",
                           0,
                           "<a href='https://www.google.com'>google</a>"),
                          ("\\[[google](https://www.google.com)",
                           2,
                           "<a href='https://www.google.com'>google</a>"),
                          ("[google\\]](https://www.google.com)",
                           0,
                           "<a href='https://www.google.com'>google\\]</a>"),
                          ("[google](https://www.google.com\\))",
                           0,
                           "<a href='https://www.google.com\\)'>google</a>"),
                          ("text[google](https://www.google.com)",
                           4,
                           "<a href='https://www.google.com'>google</a>"),
                          ])
def test_link_parse(content, expected_start, html):
    start, end, link_block = LinkBlock.parse(content)
    assert start == expected_start
    assert end == len(content)
    assert link_block is not None
    assert link_block.render() == html


@pytest.mark.parametrize("content", [
    ("\\[google](https://www.google.com)"),
    ("[google\\](https://www.google.com)"),
    ("[google]\\((https://www.google.com)"),
    ("[google]\\(https://www.google.com)"),
    ("[google](https://www.google.com\\)"),
])
def test_link_parse_failed(content):
    start, end, link_block = LinkBlock.parse(content)
    assert start == end == -1
    assert link_block is None
