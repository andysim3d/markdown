import pytest
from .. import OrderedList, UnorderedList, ListWrapper


@pytest.mark.parametrize("content, html",
                         [("first item", "<li>first item</li>"),
                          (" second item", "<li> second item</li>")])
def test_ordered_render(content, html):
    ordered_list = OrderedList(content)
    assert html == ordered_list.render()


@pytest.mark.parametrize("content, html",
                         [("first item", "<li>first item</li>"),
                          ("second item ", "<li>second item </li>")])
def test_unordered_render(content, html):
    unordered_list = UnorderedList(content)
    assert html == unordered_list.render()


@pytest.mark.parametrize("content, ordered, html", [
    ([OrderedList("first item")], True, "<ol><li>first item</li></ol>"),
    ([OrderedList("second item")], False, "<ul><li>second item</li></ul>"),
    ([OrderedList("first item"),
      OrderedList("second item")
      ], False, "<ul><li>first item</li>\n<li>second item</li></ul>"),
])
def test_list_wrapper_render(content, ordered, html):
    list_wrapper = ListWrapper(content, is_ordered=ordered)
    assert html == list_wrapper.render()
