import pytest
from link_block import LinkBlock

@pytest.mark.parametrize("content, url, html", [
    ( "google", "https://www.google.com", "<a href='https://www.google.com'>google</a>")
])
def test_link_render(content, url, html):
    lb = LinkBlock(content, url)
    assert html == lb.render()