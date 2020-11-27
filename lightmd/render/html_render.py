from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper


<<<<<<< HEAD
def render(root, css_path=None):
    rendered_child = []
    for paragraph in root.children:
        rendered_child.append(_render_a_paragraph(paragraph))
    if css_path:
        rendered_child.insert(0, f'<head>\n<link rel="stylesheet" href="{css_path}">\n</head>')
    return "<html>{}</html>".format("\n".join(rendered_child))


def _render_a_paragraph(paragraph):
    if isinstance(paragraph, HorizontalRule):
        return "<hr/>"
    if isinstance(paragraph, FencedCodeBlock):
        return "<code>{}</code>".format(paragraph.content())
    if isinstance(paragraph, HeaderParagraph):
        return "<h{0}>{1}</h{0}>".format(paragraph.level(), paragraph.content())
=======
def get_html_format(node):
    # Root
    if type(node) is Element:
        return "<html>{}</html>"
    # Paragraph
    if isinstance(node, HorizontalRule):
        return "<hr>"
    if isinstance(node, FencedCodeBlock):
        return "<code>{}</code>"
    if isinstance(node, HeaderParagraph):
        return "<h{level}>{{}}</h{level}>".format(level=node.level())
>>>>>>> cab5ed3301697a3b633c8842c25ad5dd842fb20f

    _format = ""
    if isinstance(node, TextParagraph):
        _format = "<p>{}</p>"
    if isinstance(node, ListWrapper):
        if node.is_ordered():
            _format = "<ol>{}</ol>"
        else:
            _format = "<ul>{}</ul>"
    if isinstance(node, QuoteParagraph):
        _format = "<blockquote>{}</blockquote>"

    # Block
    if isinstance(node, TextBlock):
        return '{}'
    if isinstance(node, ImgBlock):
        return '<img src="{0}" alt="{1}">'.format(node.url(), node.content())
    if isinstance(node, LinkBlock):
        return '<a href="{0}">{1}</a>'.format(node.url(), node.content())
    if isinstance(node, CodeBlock):
        return "<code>{}</code>"

    if isinstance(node, ListParagraph):
        _format = "<li>{}</li>"
    if isinstance(node, BoldBlock):
        _format = "<strong>{}</strong>"
    if isinstance(node, ItalicBlock):
        _format = "<em>{}</em>"
    if isinstance(node, StrikethroughBlock):
        _format = "<del>{}</del>"
    if isinstance(node, QuoteParagraph):
        _format = "<blockquote>{}</blockquote>"

    return _format

def render(root):
    #print(HTML_FORMAT[HorizontalRule])
    return root.render(get_html_format)
