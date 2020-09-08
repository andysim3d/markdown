import pytest
from parser import ParagraphParser, BlockParser
from block import TextBlock
from bold import BoldBlock
from italic_block import ItalicBlock
from img import ImgBlock
from link_block import LinkBlock


@pytest.fixture(scope="module")
def create_block_parsers():
    # some examples, will add more later
    BLOCK_ELEMENTS = [
        BoldBlock,
        ItalicBlock,
        ImgBlock,
        LinkBlock,
    ]
    parsers = []
    for element in BLOCK_ELEMENTS:
        parser = element.parse
        parsers.append(parser)
    
    return parsers

@pytest.mark.parametrize("content, expected_root", [
    ("testing", TextBlock("testing"))
])
def test_block_parser(create_block_parsers, content, expected_root):
    parsers = create_block_parsers
    block_parser = BlockParser()
    for p in parsers:
        block_parser.register_parser(p)

    assert expected_root == block_parser.parse(content)