import pytest
from bold import BoldBlock


@pytest.mark.parametrize(
    "content, html",
    [
        ('bold text', '<strong>bold text</strong>'),
        ('', '<strong></strong>'),
    ]
)
def test_render(content, html):
    bold = BoldBlock(content)
    assert html == bold.render()


@pytest.mark.parametrize(
    "content, start, end, sub_content",
    [
        # Bold and Italic (Either head or tail has 3 asterisks and total asterisks > 6)
        ('***test***', 0, 10, '*test*'),
        ('****test***', 0, 11, '**test*'),
        ('***test****', 0, 11, '*test**'),
        ('*****test***', 0, 12, '***test*'),
        ('***test*****', 0, 12, '*test***'),
        # Bold only (Otherwise from above, head and tail has at least 2 asterisks)
        ('**test**', 0, 8, 'test'),
        ('***test**', 0, 9, '*test'),
        ('**test***', 0, 9, 'test*')
    ]
)
def test_parse(content, start, end, sub_content):
    (start_index, end_index, bold_block) = BoldBlock.parse(content)
    assert start_index == start
    assert end_index == end
    assert bold_block._content == sub_content


@pytest.mark.parametrize(
    "content",
    [
        # not match
        ('test'),
        ('*test'),
        ('*test*'),
        ('*test**'),
        ('**test*'),
        ('*_test_*'),
    ]
)
def test_parse_not_match(content):
    (start_index, end_index, bold_block) = BoldBlock.parse(content)
    assert start_index == -1
    assert end_index == -1
    assert bold_block is None
