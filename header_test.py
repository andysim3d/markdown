import pytest
from header import Header


@pytest.mark.parametrize(
    "content, level, html",
    [
        ('title', 1, '<h1> title </h1>'),
        ('another second title', 2 ,'<h2> another second title </h2>'),
        ('title_3',3, '<h3> title_3 </h3>'),
    ]
)
def test_render(content, level, html):
    header = Header(content, level)
    assert html == header.render()  

