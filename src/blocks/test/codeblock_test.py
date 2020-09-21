import pytest
from ..codeblock import CodeBlock


@pytest.mark.parametrize("content, html", [
    ('print(hello world)', '<code>print(hello world)</code>'),
    ('print(hello `Andy`)', '<code>print(hello `Andy`)</code>'),
])
def test_render(content, html):
    fcb = CodeBlock(content)
    assert html == fcb.render()