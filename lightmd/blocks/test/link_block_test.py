import pytest
from .. import LinkBlock


@pytest.mark.parametrize("content, url, html",
                         [("google", "https://www.google.com",
                           "<a href='https://www.google.com'>google</a>")])
def test_link_render(content, url, html):
    line_block = LinkBlock(content, url)
    assert html == line_block.render()
