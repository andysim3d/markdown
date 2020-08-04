import pytest
from quote import QuoteParagraph

@pytest.mark.parametrize(
    "content, html",
    [
        ('abc', "<blockquote> abc </blockquote>"),
        ('<html> rand tag </html>', "<blockquote> <html> rand tag </html> </blockquote>"),
    ]
)
def test_render(content, html):
    quote = QuoteParagraph(content)
    assert html == quote.render()
