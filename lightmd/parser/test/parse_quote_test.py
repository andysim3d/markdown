import pytest
from ..quote_parser import parse_quote
from ...render.html_render import get_html_format


@pytest.mark.parametrize("content, html",
                         [(r"> test", r"<blockquote>test</blockquote>"),
                          (r"  >test", r"<blockquote>test</blockquote>"),
                          (r""">a""", r"<blockquote>a</blockquote>"),
                          (r">", r"<blockquote></blockquote>")])
def test_quote_parse(content, html):
    start, end, quote_para = parse_quote(content)
    assert start == 0
    assert quote_para is not None
    assert html == get_html_format(quote_para).format(quote_para.content())


@pytest.mark.parametrize("content", [
    (r"\\> a"),
    (r"\> a"),
])
def test_quote_parse_failed(content):
    start, end, quote_para = parse_quote(content)
    assert -1 == start == end
    assert quote_para is None
