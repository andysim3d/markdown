import pytest
from .. import BoldBlock


@pytest.mark.parametrize("content, html", [
    ('bold text', '<strong>bold text</strong>'),
    ('', '<strong></strong>'),
])
def test_render(content, html):
    bold = BoldBlock(content)
    assert html == bold.render()
