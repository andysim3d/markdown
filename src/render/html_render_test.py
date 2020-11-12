import pytest

from ..render.html_render import render, get_html_format
from ..parser.parser import parse_md_to_ast
from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper, \
    OrderedList, UnorderedList


@pytest.mark.parametrize("md_str, expected", [
    ('abc***bold***', '<html><p>abc<strong><em>bold</em></strong></p></html>'),
    ('> abc***bold***',
     '<html><blockquote>abc<strong><em>bold</em></strong></blockquote></html>'
     ),
])
def test_render_simple(md_str, expected):
    root = parse_md_to_ast(md_str)
    html = render(root)
    # print("root: ", root)
    print("root.children: ", root.children)
    print("root.children[0].children: ", root.children[0].children)
    print("root.children[0].children[1].children: ", root.children[0].children[1].children)
    print("root.children[0].children[1].children[0].children: ", root.children[0].children[1].children[0].children)

    # print("HTML: ", html)
    # print("=========!!!!!!!!!!==========")
    assert html == expected



# Test each element HTML render

@pytest.mark.parametrize("content, html, children", [
    ('bold text', '<strong>bold text</strong>', [TextBlock('bold text')]),
    ('', '<strong></strong>', [TextBlock('')]),
])
def test_bold_render(content, html, children):
    bold = BoldBlock(content, children=children)
    assert html == bold.render(get_html_format)

@pytest.mark.parametrize("content, html", [
    ('print(hello world)', '<code>print(hello world)</code>'),
    ('print(hello `Andy`)', '<code>print(hello `Andy`)</code>'),
])
def test_code_render(content, html):
    fcb = CodeBlock(content)
    assert html == fcb.render(get_html_format)

@pytest.mark.parametrize(
    "content, language, html",
    [
        # No lanugage
        ('print(hello world)', None,
         '<pre class="prettyprint"><code>print(hello world)</code></pre>'),
        # valid language, ability to escape backticks
        (
            'print(hello `Andy`)',
            'py',
            '<pre class="prettyprint lang-py"><code>print(hello `Andy`)</code></pre>'  # pylint: disable=line-too-long
        )
    ])
def test_fenched_code_render(content, language, html):
    fcb = FencedCodeBlock(content, language)
    assert html == fcb.render(get_html_format)

@pytest.mark.parametrize("content, level, html, children", [
    ('title', 1, '<h1>title</h1>', [TextBlock('title')]),
    (
        'another second title',
        2,
        '<h2>another second title</h2>',
        [TextBlock('another second title')]
    ),
    ('title_3', 3, '<h3>title_3</h3>', [TextBlock('title_3')]),
])
def test_header_render(content, level, html, children):
    header = HeaderParagraph(content, level, children=children)
    assert html == header.render(get_html_format)

def test_horizontal_rule_render():
    horiz_rule = HorizontalRule('')
    assert horiz_rule.render(get_html_format) == '<hr>'

@pytest.mark.parametrize("content, url, html", [
    ('test image', "https://google.com/imagea",
     '<img src="https://google.com/imagea" alt="test image">'),
])
def test_img_render(content, url, html):
    img = ImgBlock(content, url)
    assert html == img.render(get_html_format)

@pytest.mark.parametrize("content, html",
                         [("testing text", "<em>testing text</em>"),
                          ("", "<em></em>")])
def test_italic_render(content, html):
    italic_block = ItalicBlock(content)
    assert html == italic_block.render(get_html_format)

@pytest.mark.parametrize("content, url, html",
                         [("google", "https://www.google.com",
                           '<a href="https://www.google.com">google</a>')])
def test_link_render(content, url, html):
    line_block = LinkBlock(content, url)
    assert html == line_block.render(get_html_format)

@pytest.mark.parametrize("content, html, children",
                         [("first item", "<li>first item</li>", [TextBlock('first item')]),
                          (" second item", "<li> second item</li>", [TextBlock(' second item')])])
def test_ordered_render(content, html, children):
    ordered_list = OrderedList(content, children=children)
    assert html == ordered_list.render(get_html_format)


@pytest.mark.parametrize("content, html, children",
                         [("first item", "<li>first item</li>", [TextBlock('first item')]),
                          (" second item", "<li> second item</li>", [TextBlock(' second item')])])
def test_unordered_render(content, html, children):
    unordered_list = UnorderedList(content, children=children)
    assert html == unordered_list.render(get_html_format)


@pytest.mark.parametrize("content, ordered, html", [
    (
        [OrderedList("first item", children=[TextBlock("first item")])],
        True,
        "<ol><li>first item</li></ol>"
    ),
    (
        [OrderedList("second item", children=[TextBlock("second item")])],
        False,
        "<ul><li>second item</li></ul>"
    ),
    ([OrderedList("first item", children=[TextBlock("first item")]),
      OrderedList("second item", children=[TextBlock("second item")])
      ], False, "<ul><li>first item</li><li>second item</li></ul>"),
])
def test_list_wrapper_render(content, ordered, html):
    list_wrapper = ListWrapper(content, is_ordered=ordered)
    assert html == list_wrapper.render(get_html_format)

@pytest.mark.parametrize("content, html, children", [
    (r'abc', r"<blockquote>abc</blockquote>", [TextBlock('abc')]),
    (r'<html> rand tag </html>',
     r"<blockquote><html> rand tag </html></blockquote>", [TextBlock('<html> rand tag </html>')]),
])
def test_quote_render(content, html, children):
    quote = QuoteParagraph(content, children=children)
    assert html == quote.render(get_html_format)

@pytest.mark.parametrize("content, html",
                         [("testing text", "<del>testing text</del>"),
                          ("", "<del></del>")])
def test_strikethrough_render(content, html):
    strikethrough_block = StrikethroughBlock(content)
    assert html == strikethrough_block.render(get_html_format)
