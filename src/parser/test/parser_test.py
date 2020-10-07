# pylint: skip-file
import pytest

from ..parser import ParagraphParser, BlockParser,\
    create_paragraph_parsers, create_block_parsers
from ...blocks import *
# from block import TextBlock
# from bold import BoldBlock
# from italic_block import ItalicBlock
# from img import ImgBlock
# from link_block import LinkBlock
# from codeblock import CodeBlock
# from fenched_code_block import FenchedCodeBlock
# from strikethrough_block import StrikethroughBlock

# from paragraph import TextParagraph
# from header import Header
# from horizontal_rule import HorizontalRule
# from list_paragraph import OrderedList, UnorderedList
# from quote import QuoteParagraph


@pytest.mark.parametrize("content, expected", [
    ("# Test", [HeaderParagraph("Test")]),
    (r"""Test
----
Test""",
     [TextParagraph("Test"),
      HorizontalRule(""),
      TextParagraph("Test")]),
    (r"""1. List1
2. List2
>content""",
     [OrderedList("List1"),
      OrderedList("List2"),
      QuoteParagraph("content")]),
    (r"""
      
      
      
      
bala
>test
This is a 
text paragraph""", [TextParagraph(""),TextParagraph("bala"), QuoteParagraph("test"), TextParagraph("This is a text paragraph")]),
(r""">a
>b""", [QuoteParagraph("a\nb")]),
(r""">a

>b""", [QuoteParagraph("a"), TextParagraph(""), QuoteParagraph("b")])
])
def test_paragraph_parser(content, expected):
    paragraph_parser = create_paragraph_parsers()
    root = paragraph_parser.parse(content)
    children = root.children
    assert len(expected) == len(children)
    for i in range(len(children)):
        assert isinstance(expected[i], type(children[i]))
        assert expected[i].content() == children[i].content()


@pytest.mark.parametrize("content, expected", [
    ("testing", [TextBlock("testing")]),
    ("![test](testurl)", [ImgBlock("test", "testurl")]),
    ("*testing*[test](testurl)",
     [ItalicBlock("testing"),
      LinkBlock("test", "testurl")]),
])
def test_block_parser(content, expected):
    block_parser = create_block_parsers()
    root = block_parser.parse(content)
    children = root.children
    assert len(expected) == len(children)
    for i in range(len(children)):
        assert isinstance(expected[i], type(children[i]))
        assert expected[i].content() == children[i].content()


def test_nested_block_parser():
    block_parser = create_block_parsers()
    content = "***abc***"
    expected = {
        0: BoldBlock("*abc*"),
        1: ItalicBlock("abc"),
        2: TextBlock("abc")
    }
    root = block_parser.parse(content)
    print(root.render())
    cur = root.children
    idx = 0
    while not cur:
        assert isinstance(expected[idx], type(cur[0]))
        assert expected[idx].content() == cur[0].content()
        cur = cur[0].children
        idx += 1
