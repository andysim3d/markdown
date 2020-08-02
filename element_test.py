import unittest
import pytest
from element import QuoteParagraph, TextBlock, ImgBlock, \
                    ItalicBlock, UnorderedParagraph, LinkBlock, \
                    StrikethroughBlock

class TestStringMethods(unittest.TestCase):

    def test_text_render(self):

        h1 = TextBlock("test")
        self.assertEqual(h1.render(), "test")

    def test_quote_render(self):
        qp = QuoteParagraph("abc")
        self.assertEqual(qp.render(), "<blockquote> abc </blockquote>")
        self.assertEqual(QuoteParagraph("<html> rand tag </html>").render(), "<blockquote> <html> rand tag </html> </blockquote>")


    def test_img_render(self):
        ib = ImgBlock("test image", "https://google.com/imagea")
        self.assertEqual(ib.render(), "<img src='https://google.com/imagea' alt='test image'> </img>")

@pytest.mark.parametrize("content, html", [
    ( "testing text", "<em>testing text</em>" ),
    ( "", "<em></em>")
])
def test_italic_render(content, html):
    ib = ItalicBlock(content)
    assert html == ib.render()

@pytest.mark.parametrize("content, isStart, isEnd, html", [
    ( "first item", True, None, "<ul><li>first item</li>" ),
    ( "second item", None, None, "<li>second item</li>" ),
    ( "last item", None, True, "<li>last item</li></ul>" )
])
def test_unordered_render(content, isStart, isEnd, html):
    up = UnorderedParagraph(content, isStart, isEnd)
    assert html == up.render()

@pytest.mark.parametrize("content, url, html", [
    ( "google", "https://www.google.com", "<a href='https://www.google.com'>google</a>")
])
def test_link_render(content, url, html):
    lb = LinkBlock(content, url)
    assert html == lb.render()

@pytest.mark.parametrize("content, html", [
    ( "testing text", "<del>testing text</del>"),
    ( "", "<del></del>")
])
def test_strikethrough_render(content, html):
    sb = StrikethroughBlock(content)
    assert html == sb.render()

if __name__ == '__main__':
    unittest.main()
