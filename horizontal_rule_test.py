from horizontal_rule import HorizontalRule
import pytest

def test_render():
    hr = HorizontalRule('')
    assert '<hr>' == hr.render() 