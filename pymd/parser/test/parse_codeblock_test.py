import pytest
from ..codeblock_parser import parse_code_block


@pytest.mark.parametrize("content, expected_html, start, end", [
    ('`code`', '<code>code</code>', 0, 6),
    ('a`code`', '<code>code</code>', 1, 7),
    ('abc`cod\`e,`fg', '<code>cod\`e,</code>', 3, 12),
    ('``', '<code></code>', 0, 2),
])
def test_code_parse_success(content, expected_html, start, end):
    start_, end_, code = parse_code_block(content)
    assert start == start_
    assert end == end_
    assert code is not None
    assert expected_html == code.render()


@pytest.mark.parametrize("content", [('`code\`'), ('`cod')])
def test_code_parse_failed(content):
    start, end, code = parse_code_block(content)
    assert start == -1
    assert end == -1
    assert code is None
