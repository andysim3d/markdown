import pytest
from ..fenced_code_block import FencedCodeBlock


@pytest.mark.parametrize(
    "content, language, html",
    [
        # No lanugage
        ('print(hello world)', None,
         '<pre class="prettyprint"><code>print(hello world)</code></pre>'),
        # valid language, ability to escape backticks
        ('print(hello `Andy`)', 'py',
         '<pre class="prettyprint lang-py"><code>print(hello `Andy`)</code></pre>'  # pylint: disable=line-too-long
         )
    ])
def test_render(content, language, html):
    fcb = FencedCodeBlock(content, language)
    assert html == fcb.render()
