import pytest
from ..bold_parser import parse_bold_block


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
        ('**test***', 0, 9, 'test*'),
        # with escape match
        (r"\***test**", 2, 10, 'test'),
        (r"**\*test**", 0, 10, r'\*test'),
        (r"**test\***", 0, 10, r'test\*'),
        (r"**test**\*", 0, 8, 'test'),
        (r'**\test**', 0, 9, r'\test'),
        (r'**te\st**', 0, 9, r'te\st'),
        (r'**test\\**', 0, 10, r'test\\'),
        # Alternative
        ('__test__', 0, 8, 'test'),
        ('*_test_*', 0, 8, 'test'),
        ('___test___', 0, 10, '*test*'),
        ('__*test*__', 0, 10, '*test*'),
        ('*__test__*', 0, 10, '*test*'),
        ('**_test_**', 0, 10, '*test*'),
        ('_**test**_', 0, 10, '*test*'),
        # Alternative with escape match
        (r"\___test__", 2, 10, 'test'),
        (r"__\_test__", 0, 10, r'\_test'),
        (r"__test\___", 0, 10, r'test\_'),
        (r"__test__\_", 0, 8, 'test'),
        # Double back-slash case
        (r"**test\\***", 0, 11, r'test\\*'),
        # Complicated escape with alternative
        (r"\*\_**\_\*test\*\_**", 4, 20, r'\_\*test\*\_'),
        (r"\_\*abc**abc**", 7, 14, 'abc'),
        (r"\*\\\_**\\\_\*test\*\_\\**", 6, 26, r'\\\_\*test\*\_\\'),
    ]
)
def test_parse(content, start, end, sub_content):
    (start_index, end_index, bold_block) = parse_bold_block(content)
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
        # with escape match
        (r"\**test**"),
        (r"*\*test**"),
        (r"*test\**"),
        (r"*test*\*"),
    ]
)
def test_parse_not_match(content):
    (start_index, end_index, bold_block) = parse_bold_block(content)
    assert start_index == -1
    assert end_index == -1
    assert bold_block is None
