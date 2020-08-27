import sys
from paragraph import TextParagraph


class AbstractParser(object):
    def __init__(self):
        self._parsers = set()

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
    def __init__(self):
        super().__init__()
        self._paragraphs = []

    def parse(self, content):
        '''
        Invoke all parsers in self._parsers to try to parse the content.
        Return unparsed part.
        '''
        index = len(content)
        end = len(content)
        final_element = TextParagraph(content)
        for parser in self._parsers:
            beg, en, element = parser(content)
            if beg != 0 and beg < index:
                index, end, final_element = beg, en, element
        if index != 0 and index != len(content):
            self._paragraphs.append(TextParagraph(content[0, index]))
        self._paragraphs.append(final_element)
        return content[end:]


class BlockParser(AbstractParser):
    def __init__(self):
        super().__init__()
        self._blocks = []

    def parse(self, content):
        '''
        Invoke all parsers in self._parsers to try to parse the content.
        Return unparsed part.
        '''
        # TODO: implement it.