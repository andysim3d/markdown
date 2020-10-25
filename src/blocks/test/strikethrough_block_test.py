import pytest
from src.blocks import StrikethroughBlock


@pytest.mark.parametrize("content, html",
                         [("testing text", "<del>testing text</del>"),
                          ("", "<del></del>")])
def test_strikethrough_render(content, html):
    strikethrough_block = StrikethroughBlock(content)
    assert html == strikethrough_block.render()
