from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper

def render(root):
    return _dfs(root)

def _dfs(node):
    if isinstance(node, TextBlock):
        return node.content()

    rendered_child = []
    print(type(node), node.children)
    for child in node.children:
        rendered_child.append(_dfs(child))

    return node.render_html().format(''.join(rendered_child))
