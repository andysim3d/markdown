import pytest
from ..img import ImgBlock


@pytest.mark.parametrize("content, url, html", [
    ('test image', "https://google.com/imagea",
     '<img src="https://google.com/imagea" alt="test image"> </img>'),
])
def test_render(content, url, html):
    img = ImgBlock(content, url)
    assert html == img.render()
