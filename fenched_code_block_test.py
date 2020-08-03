from fenched_code_block import FenchedCodeBlock
import pytest


@pytest.mark.parametrize(
    "content, html",
    [
        ('print(hello world)', '<code>print(hello world)</code>'),
        ('print(hello `Andy`)', '<code>print(hello `Andy`)</code>'), # ability to escape backticks
    ]
)
def test_render(content, html):
    fcb = FenchedCodeBlock(content)
    assert html == fcb.render() 