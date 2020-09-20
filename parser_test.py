# pylint: skip-file
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

from paragraph import TextParagraph
from header import Header
from horizontal_rule import HorizontalRule
from list_paragraph import OrderedList, UnorderedList
from quote import QuoteParagraph


@pytest.fixture(scope="module")
def create_paragraph_parsers():
    PARAGRAPH_ELEMENTS = [
        Header,
        HorizontalRule,
        OrderedList,
        UnorderedList,
        QuoteParagraph
    ]
    parsers = []
    for element in PARAGRAPH_ELEMENTS:
        parser = element.parse
        parsers.append(parser)

    return parsers


@pytest.mark.parametrize("content, expected", [
    ("# Test", [Header("Test")]),
    (r"""Test
----
Test""", [TextParagraph("Test"), HorizontalRule("----"), TextParagraph("Test")]),
    (r"""1. List1
2. List2
>content""", [OrderedList("List1"), OrderedList("List2"), QuoteParagraph("content")]),
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
        assert isinstance(expected[i], type(children[i]))
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
    ("testing", [TextBlock("testing")]),
    ("![test](testurl)", [ImgBlock("test", "testurl")]),
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
        assert isinstance(expected[i], type(children[i]))
        assert expected[i].content() == children[i].content()


def test_nested_block_parser(create_block_parsers):
    parsers = create_block_parsers
    block_parser = BlockParser()
    for p in parsers:
        block_parser.register_parser(p)

    content = "***abc***"
    expected = {
        1: BoldBlock("*abc*"),
        2: ItalicBlock("abc"),
        3: TextBlock("abc")
    }
    root = block_parser.parse(content)
    cur = root.children()
    idx = 1
    while len(cur) != 0:
        assert isinstance(expected[idx], type(cur[0]))
        assert expected[idx].content() == cur[0].content()
        cur = cur[0].children()
        idx += 1
