import sys
from collections import OrderedDict


from ..blocks import Element, TextParagraph, TextBlock, HeaderParagraph, \
    HorizontalRule, ListParagraph, QuoteParagraph, BoldBlock, ItalicBlock, \
    ImgBlock, LinkBlock, CodeBlock, FencedCodeBlock, StrikethroughBlock, ListWrapper

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
from .text_paragraph_parser import parse_empty_newlines, parse_text_pargraph


class AbstractParser(object):
    def __init__(self):
        self._parsers = OrderedDict()

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
        self._parsers[parser] = 0

    def unregister_parser(self, parser):
        '''
        Remove a registered parser
        '''
        if parser in self._parsers:
            del self._parsers[parser]

    def parse(self, content):
        raise NotImplementedError("AbstractParser is not implemented.")


class ParagraphParser(AbstractParser):
    def __init__(self):
        super().__init__()
        self._default = None

    def default_parser(self, parser):
        self._default = parser

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
            if begin != -1 and begin < start_index:
                start_index, end_index, final_element = begin, end, element
        if start_index > 0:
            # try to eliminate empty lines
            begin, end, _ = parse_empty_newlines(content)
            if begin == 0:
                ## put an empty text paragraph to avoid paragraph merge.
                start_index, end_index, final_element = begin, end, TextParagraph(
                    "")
                ## put an empty text paragraph to avoid paragraph merge.
            else:
                start_index, end_index, final_element = self._default(
                    content[:start_index])
        final_element = self._post_parse_merge_quote(parent, final_element)
        tmp_parent = self._post_parse_merge_list(parent, final_element)
        link_parent_and_child(tmp_parent, final_element)
        return content[end_index:]

    def _post_parse_merge_quote(self, parent, new_element):
        """
        After parse, merge merabele paragraph.
        For instance,
        ">a
         >b
        "
        will be merged with one QuoteBlock.
        """
        if (parent.children and isinstance(new_element, QuoteParagraph)
                and isinstance(parent.children[-1], QuoteParagraph)):
            content = "\n".join((
                parent.children[-1].content(),
                new_element.content(),
            ))
            parent.children.pop(-1)
            return QuoteParagraph(content)
        else:
            return new_element

    def _post_parse_merge_list(self, parent, new_element):
        """
        After parse, merge mergable list element and apply indentations
        """
        if isinstance(new_element, ListParagraph):
            new_element_indent = new_element.indent
            prev_list_element = self._find_prev_list_element(parent, new_element_indent)
            if prev_list_element.children:
                if (isinstance(prev_list_element.children[-1], ListWrapper)
                        and prev_list_element.children[-1].is_ordered()
                        == new_element.is_ordered()):
                    return prev_list_element.children[-1]
            virtual_list = ListWrapper([], new_element.is_ordered(), new_element_indent)
            link_parent_and_child(prev_list_element, virtual_list)
            return prev_list_element.children[-1]
        return parent

    def _find_prev_list_element(self, parent, indent):
        cur = parent
        while cur.children and hasattr(cur.children[-1], 'indent'):
            diff = indent - cur.children[-1].indent
            if diff < 1:
                return cur
            cur = cur.children[-1]
        return cur

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
    child.parent = parent
    parent.add_child(child)


class BlockParser(AbstractParser):
    def _invoke_parsers(self, parent, content):
        start_index = len(content)
        end_index = len(content)
        final_element = TextBlock(content)
        for parser in self._parsers:
            begin, end, element = parser(content)
            if begin != -1 and begin < start_index:
                start_index, end_index, final_element = begin, end, element
        if start_index > 0 and start_index != len(content):
            child = TextBlock(content[:start_index])
            link_parent_and_child(parent, child)
        link_parent_and_child(parent, final_element)
        return content[end_index:]

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
        for child in root.children:
            if (not isinstance(child, TextBlock)) and child.nested():
                self.parse(child.content(), child)
        return root


def create_paragraph_parsers():
    p_parser = ParagraphParser()
    paragraph_functors = [
        parse_header_paragraph, parse_horiontal_rule, parse_ordered_list,
        parse_unordered_list, parse_quote, parse_fenced_code_block
    ]
    for func in paragraph_functors:
        p_parser.register_parser(func)

    p_parser.default_parser(parse_text_pargraph)
    return p_parser


def create_block_parsers():
    b_parser = BlockParser()
    block_functors = [
        parse_bold_block, parse_italic_block, parse_img_block,
        parse_link_block, parse_code_block, parse_strike_through_block,
        parse_quote
    ]
    for func in block_functors:
        b_parser.register_parser(func)

    return b_parser


def parse_md_to_ast(md_content):
    p_parser = create_paragraph_parsers()
    b_parser = create_block_parsers()

    root = p_parser.parse(md_content)
    for child in root.children:
        b_parser.parse(child.content(), child)

    return root
