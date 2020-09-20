import sys
from element import Element
from paragraph import TextParagraph
from block import TextBlock


class AbstractParser(object):
    def __init__(self):
        self._parsers = dict()

    @property
    def parsers(self):
        return list(self._parsers)

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
        if parser in self._parsers.keys():
            del self._parsers[parser]

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
            if begin != -1 and begin < start_index:
                start_index, end_index, final_element = begin, end, element
        if start_index > 0 and start_index != len(content):
            text_paragraph = TextParagraph(content[:start_index])
            link_parent_and_child(parent, text_paragraph)
        link_parent_and_child(parent, final_element)
        return content[end_index:]

    def parse(self, content, root=None):
        """
        Parse content into an AST, then return the root node of the tree.

        If the root is not given, new root will created and returned.
        """
        if root is None:
            root = Element(None)
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

        for child in root.children():
            if not isinstance(child, TextBlock):
                self.parse(child.content(), child)

        return root
