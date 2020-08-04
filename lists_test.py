import pytest
from lists import OrderedList, UnorderedList

@pytest.mark.parametrize("content, isStart, isEnd, html", [
    ( "first item", True, None, "<ol><li>first item</li>" ),
    ( "second item", None, None, "<li>second item</li>" ),
    ( "last item", None, True, "<li>last item</li></ol>" )
])
def test_ordered_render(content, isStart, isEnd, html):
    up = OrderedList(content, isStart, isEnd)
    assert html == up.render()

@pytest.mark.parametrize("content, isStart, isEnd, html", [
    ( "first item", True, None, "<ul><li>first item</li>" ),
    ( "second item", None, None, "<li>second item</li>" ),
    ( "last item", None, True, "<li>last item</li></ul>" )
])
def test_unordered_render(content, isStart, isEnd, html):
    up = UnorderedList(content, isStart, isEnd)
    assert html == up.render()