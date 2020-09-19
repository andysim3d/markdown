import pytest

from parser import ParagraphParser, BlockParser
from block import TextBlock
from bold import BoldBlock
from italic_block import ItalicBlock
from img import ImgBlock
from link_block import LinkBlock
from codeblock import CodeBlock
from fenched_code_block import FenchedCodeBlock
from strikethrough_block import StrikethroughBlock

from header import Header
from horizontal_rule import HorizontalRule
from list_paragraph import ListParagraph
from quote import QuoteParagraph

@pytest.fixture(scope="module")
def create_paragraph_parsers():
    PARAGRAPH_ELEMENTS = [
        Header,
        HorizontalRule,
        ListParagraph,
        QuoteParagraph
    ]
    parsers = []
    for element in PARAGRAPH_ELEMENTS:
        parser = element.parse
        parsers.append(parser)
    
    return parsers

@pytest.mark.parametrize("content, expected", [
    ("# Test", [Header("Test")]),
    ("Test\n----\nTest", [TextBlock("Test"), HorizontalRule("----"), TextBlock("Test")]),
    ("# Title\n1. List1\n2. List2\n>content", [Header("Title"), ListParagraph("List1"), \
                                                ListParagraph("List2"), QuoteParagraph("content")]),
])
def test_paragraph_parser(create_paragraph_parsers, content, expected):
    parsers = create_paragraph_parsers
    paragraph_parser = ParagraphParser()
    for p in parsers:
        paragraph_parser.register_parser(p)

    root = paragraph_parser.parse(content)
    children = root.children()
    assert len(expected) == len(children)
    for i in range(len(children)):
        assert type(expected[i]) == type(children[i]) 
        assert expected[i].content() == children[i].content()


@pytest.fixture(scope="module")
def create_block_parsers():
    BLOCK_ELEMENTS = [
        BoldBlock,
        ItalicBlock,
        ImgBlock,
        LinkBlock,
        CodeBlock,
        FenchedCodeBlock,
        StrikethroughBlock
    ]
    parsers = []
    for element in BLOCK_ELEMENTS:
        parser = element.parse
        parsers.append(parser)
    
    return parsers

@pytest.mark.parametrize("content, expected", [
    ("testing",             [TextBlock("testing")]),
    ("*testing*",           [ItalicBlock("testing")]),
    ("![test](testurl)",    [ImgBlock("test", "testurl")]),
    ("*testing*[test](testurl)", [ItalicBlock("testing"), LinkBlock("test", "testurl")]),
])
def test_block_parser(create_block_parsers, content, expected):
    parsers = create_block_parsers
    block_parser = BlockParser()
    for p in parsers:
        block_parser.register_parser(p)
    
    root = block_parser.parse(content)
    children = root.children()
    assert len(expected) == len(children)
    for i in range(len(children)):
        assert type(expected[i]) == type(children[i])
        assert expected[i].content() == children[i].content()