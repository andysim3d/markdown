import pytest
from codeblock import CodeBlock


@pytest.mark.parametrize("content, html", [
    ('print(hello world)', '<code>print(hello world)</code>'),
    ('print(hello `Andy`)', '<code>print(hello `Andy`)</code>'),
])
def test_render(content, html):
    fcb = CodeBlock(content)
    assert html == fcb.render()


@pytest.mark.parametrize("content, expected_html, start, end", [
    ('`code`', '<code>code</code>', 0, 6),
    ('a`code`', '<code>code</code>', 1, 7),
    ('abc`cod\`e,`fg', '<code>cod\`e,</code>', 3, 12),
    ('``', '<code></code>', 0, 2),
])
def test_code_parse_success(content, expected_html, start, end):
    start_, end_, code = CodeBlock.parse(content)
    assert start == start_
    assert end == end_
    assert code is not None
    assert expected_html == code.render()


@pytest.mark.parametrize("content", [('`code\`'), ('`cod')])
def test_code_parse_failed(content):
    start, end, code = CodeBlock.parse(content)
    assert start == -1
    assert end == -1
    assert code is None
