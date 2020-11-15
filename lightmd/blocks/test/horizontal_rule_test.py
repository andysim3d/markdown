import pytest
from .. import HorizontalRule


def test_render():
    horiz_rule = HorizontalRule('')
    assert horiz_rule.render() == '<hr>'
