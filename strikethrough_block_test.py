import pytest
from strikethrough_block import StrikethroughBlock
@pytest.mark.parametrize("content, html", [
    ( "testing text", "<del>testing text</del>"),
    ( "", "<del></del>")
])
def test_strikethrough_render(content, html):
    sb = StrikethroughBlock(content)
    assert html == sb.render()

if __name__ == '__main__':
    unittest.main()