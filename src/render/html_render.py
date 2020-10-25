from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper


def render(root):
    rendered_child = []
    for paragraph in root.children:
        rendered_child.append(_render_a_paragraph(paragraph))
    return "<html>{}</html>".format("\n".join(rendered_child))


def _render_a_paragraph(paragraph):
    if isinstance(paragraph, HorizontalRule):
        return "<hr/>"
    if isinstance(paragraph, FencedCodeBlock):
        return "<code>{}</code>".format(paragraph.content())
    if isinstance(paragraph, HeaderParagraph):
        return "<h{0}>{1}</h{0}>".format(paragraph.level(), paragraph.content())

    _format = ""
    if isinstance(paragraph, TextParagraph):
        _format = "<p>{}</p>"
    if isinstance(paragraph, ListWrapper):
        if paragraph.is_ordered():
            _format = "<ol>\n{}</ol>"
        else:
            _format = "<ul>\n{}</ul>"
    if isinstance(paragraph, QuoteParagraph):
        _format = "<blockquote>{}</blockquote>"
    rendered_content = []
    for element in paragraph.children:
        rendered_content.append(_render_a_element(element))
    return _format.format("".join(rendered_content))


def _render_a_element(element):
    _format = ""
    if isinstance(element, TextBlock):
        return element.content()
    if isinstance(element, ImgBlock):
        return "<img src={} alt={}/>".format(element.url(), element.content())
    if isinstance(element, LinkBlock):
        return "<a herf={0}>{1}</a>".format(element.url(), element.content())
    if isinstance(element, CodeBlock):
        return "<code>{}</code>".format(element.content())

    if isinstance(element, ListParagraph):
        _format = "<li>{}</li>\n"
    if isinstance(element, BoldBlock):
        _format = "<strong>{}</strong>"
    if isinstance(element, ItalicBlock):
        _format = "<em>{}</em>"
    if isinstance(element, StrikethroughBlock):
        _format = "<del>{}</del>"
    if isinstance(element, QuoteParagraph):
        _format = "<blockquote>{}</blockquote>"

    return _format.format("".join(
        [_render_a_element(i) for i in element.children]))
