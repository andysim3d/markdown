# pylint: skip-file
import pytest

from ..parser import ParagraphParser, BlockParser,\
    create_paragraph_parsers, create_block_parsers
from ...blocks import *


@pytest.mark.parametrize("content, expected", [
    ("# Test", [HeaderParagraph("Test")]),
    (r"""Test
----
Test""",
     [TextParagraph("Test"),
      HorizontalRule(""),
      TextParagraph("Test")]),
    (r"""
      
      
      
      
bala
>test
This is a 
text paragraph""", [TextParagraph(""),TextParagraph("bala"), QuoteParagraph("test"), TextParagraph("This is a text paragraph")]),
(r"""1. List1
2. List2
>content
1. List3
- List4
""", [ListWrapper([OrderedList("List1"),OrderedList("List2")], True), QuoteParagraph("content"), 
        ListWrapper([OrderedList("List3")], True), ListWrapper([OrderedList("List4")], False)]),
(r""">a
>b""", [QuoteParagraph("a\nb")]),
(r""">a

>b""", [QuoteParagraph("a"), TextParagraph(""), QuoteParagraph("b")]),
(r"""1. List1
   - subList1
       - subList2
""", [ListWrapper([OrderedList("List1"), ListWrapper([UnorderedList("subList1"), ListWrapper([UnorderedList("subList2")], False)], False)], True)]),
(r"""1. List1
   - subList1
   - subList2
2. List2
""", [ListWrapper([OrderedList("List1"), ListWrapper([UnorderedList("subList1"), UnorderedList("subList2")], False), OrderedList("List2")], True)]),
(r"""1. List1
    - subList1
2. List2
    - subList2
""", [ListWrapper([OrderedList("List1"), ListWrapper([UnorderedList("subList1")], False), OrderedList("List2"), ListWrapper([UnorderedList("subList2")], False)], True)]),
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
