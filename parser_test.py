# pylint: skip-file
import pytest

from parser import ParagraphParser, BlockParser,\
    create_paragraph_parsers, create_block_parsers
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


@pytest.mark.parametrize("content, expected", [
    ("# Test", [Header("Test")]),
    (r"""Test
----
Test""", [TextParagraph("Test\n"), HorizontalRule(""), TextParagraph("\nTest")]),
    (r"""1. List1
2. List2
>content""", [OrderedList("List1"), OrderedList("List2"), QuoteParagraph("content")]),
])
def test_paragraph_parser(content, expected):
    paragraph_parser = create_paragraph_parsers()
    root = paragraph_parser.parse(content)
    children = root.children()
    assert len(expected) == len(children)
    for i in range(len(children)):
        assert isinstance(expected[i], type(children[i]))
        assert expected[i].content() == children[i].content()

@pytest.mark.parametrize("content, expected", [
    ("testing", [TextBlock("testing")]),
    ("![test](testurl)", [ImgBlock("test", "testurl")]),
    ("*testing*[test](testurl)", [ItalicBlock("testing"), LinkBlock("test", "testurl")]),
])
def test_block_parser(content, expected):
    block_parser = create_block_parsers()
    root = block_parser.parse(content)
    children = root.children()
    assert len(expected) == len(children)
    for i in range(len(children)):
        assert isinstance(expected[i], type(children[i]))
        assert expected[i].content() == children[i].content()

def test_nested_block_parser():
    block_parser = create_block_parsers()
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
