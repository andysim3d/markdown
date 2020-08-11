import pytest
from fenched_code_block import FenchedCodeBlock


@pytest.mark.parametrize(
    "content, html",
    [
        ('print(hello world)', '<code>print(hello world)</code>'),
        ('print(hello `Andy`)', '<code>print(hello `Andy`)</code>'), # ability to escape backticks
    ]
)
def test_render(content, html):
    fcb = FenchedCodeBlock(content, None)
    assert html == fcb.render()


@pytest.mark.parametrize(
    "content, start, end, language, sub_content",
    [
        # No language, single line
        (
            '''
```
print(hello)
```
            ''',
            1, 21, None,
            'print(hello)'
        ),
        # With Valid language(Case insensitive), multiple line
        (
            '''
```Python
print(hello)
a = b + c
print(world)
```
            ''',
            1, 50, 'python',
            'print(hello)\na = b + c\nprint(world)'
        ),
        # Invalid language(Case insensitive)
        (
            '''
```Andy
print(hello)
```
            ''',
            1, 25, None,
            'print(hello)'
        ),
        # Allowed white space before backticks
        (
            '''
   ```     Java
print(hello)
   ```
            ''',
            4, 36, 'java',
            'print(hello)'
        ),
        # starting backticks more than ending ones
        (
            '''
``````html
print(hello)
```''',
            1, 28, 'html',
            'print(hello)\n```'
        ),
        # starting backticks less than ending ones
        (
            '''
```c++
print(hello)
`````
            ''',
            1, 26, 'c++',
            'print(hello)'
        ),
    ]
)
def test_parse(content, start, end, language, sub_content):
    (start_index, end_index, fcb) = FenchedCodeBlock.parse(content)
    assert start_index == start
    assert end_index == end
    assert fcb._language == language
    assert fcb._content == sub_content



@pytest.mark.parametrize(
    "content",
    [
        # more than 3 white space before backticks
        (
            '''
    ```python
print(hello)
    ```
            '''
        ),
        # not enough backticks
        (
            '''
``python
print(hello)
```
            '''
        ),
    ]
)
def test_parse_not_match(content):
    (start_index, end_index, fcb) = FenchedCodeBlock.parse(content)
    assert start_index == -1
    assert end_index == -1
    assert fcb is None
