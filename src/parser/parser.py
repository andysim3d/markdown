import sys

from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock

from .bold_parser import parse_bold_block
from .codeblock_parser import parse_code_block
from .fenced_code_block_parser import parse_fenced_code_block
from .header_parser import parse_header_paragraph
from .horizontal_rule_parser import parse_horiontal_rule
from .img_parser import parse_img_block
from .italic_block_parser import parse_italic_block
from .link_block_parser import parse_link_block
from .list_paragraph_parser import parse_ordered_list, parse_unordered_list
from .quote_parser import parse_quote
from .strikethrough_block_parser import parse_strike_through_block

class AbstractParser(object):
    def __init__(self):
        self._parsers = set()

    @property
    def parsers(self):
        return self._parsers

    @parsers.setter
    def parsers(self, new_parsers):
        self._parsers = new_parsers

    def register_parser(self, parser):
        '''
        Register a paragraph parser to self._parsers
        '''
        self._parsers.add(parser)

    def unregister_parser(self, parser):
        '''
        Remove a registered parser
        '''
        if parser in self._parsers:
            self._parsers.remove(parser)

    def parse(self, content):
        raise NotImplementedError("AbstractParser is not implemented.")


class ParagraphParser(AbstractParser):
    def _invoke_parsers(self, parent, content):
        '''
        Invoke all parsers in self._parsers to try to parse the content.
        Return unparsed part.
        '''
        start_index = len(content)
        end_index = len(content)
        final_element = TextParagraph(content)
        for parser in self._parsers:
            begin, end, element = parser(content)
            if begin != 0 and begin < start_index:
                start_index, end_index, final_element = begin, end, element
        if start_index != 0 and start_index != len(content):
            text_paragraph = TextParagraph(content[0, start_index])
            link_parent_and_child(parent, text_paragraph)
        link_parent_and_child(parent, final_element)
        return content[end:]

    def parse(self, content, root=None):
        """
        Parse content into an AST, then return the root node of the tree.

        If the root is not given, new root will created and returned.
        """
        if root is None:
            root = Element(content)
        remain_content = self._invoke_parsers(root, content)
        while remain_content:
            remain_content = self._invoke_parsers(root, remain_content)
        return root


def link_parent_and_child(parent, child):
    child.set_parent(parent)
    parent.add_child(child)


class BlockParser(AbstractParser):
    def _invoke_parsers(self, parent, content):
        start_index = len(content)
        end_index = len(content)
        final_element = TextBlock(content)
        for parser in self._parsers:
            begin, end, element = parser(content)
            if begin != 0 and begin < start_index:
                start_index, end_index, final_element = begin, end, element
        if start_index != 0 and start_index != len(content):
            child = TextBlock(content[0, start_index])
            link_parent_and_child(parent, child)
        link_parent_and_child(parent, final_element)
        return content[end:]

    def parse(self, content, root=None):
        '''
        Parse the content into an AST.

        If the root is not given, will create an Element serving as root node.

        Return the root node.
        '''
        if root is None:
            root = Element(content)
        cur_content = content
        while cur_content:
            cur_content = self._invoke_parsers(root, cur_content)

        for child in root.children():
            if child.nested():
                if not isinstance(child, TextBlock):
                    self.parse(child.content(), child)
            else:
                child.add_child(TextBlock(child.content()))

        return root


def create_paragrah_and_block_parsers():
    p_parser = ParagraphParser()
    b_parser = BlockParser()

    paragraph_functors = [
        parse_header_paragraph,
        parse_horiontal_rule, 
        parse_ordered_list, 
        parse_unordered_list,
        parse_quote,
        parse_fenced_code_block
    ]
    for parser_functor in paragraph_functors:
        p_parser.parsers.append(parser_functor)

    block_element_functors = [
        parse_bold_block,
        parse_italic_block,
        parse_img_block,
        parse_link_block,
        parse_code_block,
        parse_strike_through_block,
    ]
    for parser_functor in block_element_functors:
        b_parser.parsers.append(parser_functor)

    return (p_parser, b_parser)


def parse_md_to_ast(md_content):
    p_parser, b_parser = create_paragrah_and_block_parsers()

    root = p_parser.parse(md_content)
    for child in root.children():
        b_parser.parse(child.content, child)

    return root
