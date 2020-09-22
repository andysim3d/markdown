import pytest
from ..quote import QuoteParagraph


@pytest.mark.parametrize("content, html", [
    (r'abc', r"<blockquote>abc</blockquote>"),
    (r'<html> rand tag </html>',
     r"<blockquote><html> rand tag </html></blockquote>"),
])
def test_render(content, html):
    quote = QuoteParagraph(content)
    assert html == quote.render()