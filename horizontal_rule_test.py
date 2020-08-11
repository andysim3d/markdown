import pytest
from horizontal_rule import HorizontalRule


def test_render():
    horiz_rule = HorizontalRule('')
    assert horiz_rule.render() == '<hr>'


@pytest.mark.parametrize(
    "content, start, end",
    [
        ('***', 0, 3),
        ('____', 0, 4),
        ('-----', 0, 5),
        (' ------', 0, 7),
        ('______ ', 0, 7),
    ]
)
def test_parse(content, start, end):
    (start_index, end_index, hori_rule) = HorizontalRule.parse(content)
    assert start_index == start
    assert end_index == end
    assert hori_rule._content == ''


@pytest.mark.parametrize(
    "content",
    [
        # not match
        ('**'),
        ('*_-'),
        ('\---'),
        ('a___'),
        ('*****a'),
        ('***a**'),
        ('*** ***'),
    ]
)
def test_parse_not_match(content):
    (start_index, end_index, hori_rule) = HorizontalRule.parse(content)
    assert start_index == -1
    assert end_index == -1
    assert hori_rule is None
