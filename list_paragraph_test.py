import pytest
from list_paragraph import OrderedList, UnorderedList


@pytest.mark.parametrize("content, is_start, is_end, html", [
    ("first item", True, None, "<ol><li>first item</li>"),
    ("second item", None, None, "<li>second item</li>"),
    ("last item", None, True, "<li>last item</li></ol>")
])
def test_ordered_render(content, is_start, is_end, html):
    ordered_list = OrderedList(content, is_start, is_end)
    assert html == ordered_list.render()


@pytest.mark.parametrize("content, is_start, is_end, html", [
    ("first item", True, None, "<ul><li>first item</li>"),
    ("second item", None, None, "<li>second item</li>"),
    ("last item", None, True, "<li>last item</li></ul>")
])
def test_unordered_render(content, is_start, is_end, html):
    unordered_list = UnorderedList(content, is_start, is_end)
    assert html == unordered_list.render()
