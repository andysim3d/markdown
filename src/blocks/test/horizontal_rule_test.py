import pytest
from ..horizontal_rule import HorizontalRule


def test_render():
    horiz_rule = HorizontalRule('')
    assert horiz_rule.render() == '<hr>'
