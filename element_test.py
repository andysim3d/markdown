import unittest
from element import QuoteParagraph, TextBlock, ImgBlock
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

if __name__ == '__main__':
    unittest.main()
