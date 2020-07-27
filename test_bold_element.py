from bold_element import BoldElement
import pytest


@pytest.mark.parametrize(
    "content, html",
    [
        ('**bold text**', '<strong>bold text</strong>'),
        ('**This is ** a test **!**', '<strong>This is </strong> a test <strong>!</strong>'),
        ('********', '<strong></strong><strong></strong>'),
        ('******', '<strong></strong>**'),
    ]
)
def test_render(content, html):
    bold = BoldElement(content)
    assert html == bold.render() 