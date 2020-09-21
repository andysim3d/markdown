import pytest
from ..horizontal_rule_parser import parse_horiontal_rule


@pytest.mark.parametrize("content, start, end", [('***', 0, 3), ('____', 0, 4),
                                                 ('-----', 0, 5),
                                                 (' ------', 1, 7),
                                                 ('______ ', 0, 6),
                                                 ('''


-----

''', 3, 8)])
def test_parse(content, start, end):
    (start_index, end_index, hori_rule) = parse_horiontal_rule(content)
    assert start_index == start
    assert end_index == end
    assert hori_rule._content == ''


@pytest.mark.parametrize(
    "content",
    [
        # not match
        ('**'),
        ('*_-'),
        (r'\---'),
        ('a___'),
        ('*****a'),
        ('***a**'),
        ('*** ***'),
    ])
def test_parse_not_match(content):
    (start_index, end_index, hori_rule) = parse_horiontal_rule(content)
    assert start_index == -1
    assert end_index == -1
    assert hori_rule is None
