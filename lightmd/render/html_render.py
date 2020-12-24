import re
from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper


def get_html_format(node):
    # Root
    if type(node) is Element:
        return "<html>{}</html>"
    # Paragraph
    if isinstance(node, HorizontalRule):
        style_class = get_style_class("hr")
        return f"<hr{style_class}>"
    if isinstance(node, FencedCodeBlock):
        style_class = get_style_class("code")
        return f"<code{style_class}>{{}}</code>"
    if isinstance(node, HeaderParagraph):
        level = node.level()
        style_class = get_style_class(f"h{level}")
        return f"<h{level}{style_class}>{{}}</h{level}>"

    _format = ""
    if isinstance(node, TextParagraph):
        style_class = get_style_class("p")
        _format = f"<p{style_class}>{{}}</p>"
    if isinstance(node, ListWrapper):
        if node.is_ordered():
            style_class = get_style_class("ol")
            _format = f"<ol{style_class}>{{}}</ol>"
        else:
            style_class = get_style_class("ul")
            _format = f"<ul{style_class}>{{}}</ul>"
    if isinstance(node, QuoteParagraph):
        style_class = get_style_class("blockquote")
        _format = f"<blockquote{style_class}>{{}}</blockquote>"

    # Block
    if isinstance(node, TextBlock):
        return "{}"
    if isinstance(node, ImgBlock):
        style_class = get_style_class("img")
        return f'<img src="{node.url()}" alt="{node.content()}"{style_class}>'
    if isinstance(node, LinkBlock):
        style_class = get_style_class("href")
        return f'<a href="{node.url()}"{style_class}>{node.content()}</a>'
    if isinstance(node, CodeBlock):
        style_class = get_style_class("code")
        return f"<code{style_class}>{{}}</code>"

    if isinstance(node, ListParagraph):
        style_class = get_style_class("li")
        _format = f"<li{style_class}>{{}}</li>"
    if isinstance(node, BoldBlock):
        style_class = get_style_class("strong")
        _format = f"<strong{style_class}>{{}}</strong>"
    if isinstance(node, ItalicBlock):
        style_class = get_style_class("em")
        _format = f"<em{style_class}>{{}}</em>"
    if isinstance(node, StrikethroughBlock):
        style_class = get_style_class("del")
        _format = f"<del{style_class}>{{}}</del>"
    if isinstance(node, QuoteParagraph):
        style_class = get_style_class("blockquote")
        _format = f"<blockquote{style_class}>{{}}</blockquote>"

    return _format


def render(root, css_path=None):
    # print(HTML_FORMAT[HorizontalRule])
    global STYLE_MAP
    STYLE_MAP = parse_css(css_path)
    return root.render(get_html_format)


def parse_css(css_path):
    """parse css and return a global STYLE_MAP
       which key is the element and value is the class name
    """
    if css_path is None:
        return {}

    #pylint: disable=invalid-name
    STYLE_MAP = {}
    with open(css_path, "r") as file:
        pattern = r"^(.*)\.([^\s]*)(?:\s)*{$"
        for line in file.readlines():
            match = re.search(pattern, line)
            if match:
                element_name = match.group(1) if match.group(1) else "all"
                if STYLE_MAP.get(element_name):
                    STYLE_MAP[element_name] = f"{STYLE_MAP.get(element_name)} {match.group(2)}"
                else:
                    STYLE_MAP[element_name] = match.group(2)

    return STYLE_MAP


def get_style_class(element_name):
    class_name = STYLE_MAP.get(element_name, "")
    apply_all = STYLE_MAP.get("all")
    if apply_all:
        class_name = f"{apply_all} {class_name}" if class_name else apply_all
    return f' class="{class_name}"' if class_name else ""
