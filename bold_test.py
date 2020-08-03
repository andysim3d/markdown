from bold import BoldBlock
import pytest


@pytest.mark.parametrize(
    "content, html",
    [
        ('bold text', '<strong>bold text</strong>'),
        ('', '<strong></strong>'),
    ]
)
def test_render(content, html):
    bold = BoldBlock(content)
    assert html == bold.render() 