import pytest
from ..list_paragraph import OrderedList, UnorderedList


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