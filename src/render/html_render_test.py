import pytest

from ..render.html_render import render
from ..parser.parser import parse_md_to_ast
from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper

@pytest.mark.parametrize("md_str, expected", [
    ('abc***bold***', '<html><a>abc<strong><em>bold</em></strong></a></html>'),
    ('> abc***bold***', '<html><blockquote>abc<strong><em>bold</em></strong></blockquote></html>'),
])
def test_render_simple(md_str, expected):
    root = parse_md_to_ast(md_str)
    html = render(root)
    print(html)
    assert html == expected
