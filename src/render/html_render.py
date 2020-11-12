from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper


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
