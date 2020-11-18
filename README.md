# markdown
[![Build Status](https://travis-ci.org/andysim3d/markdown.svg?branch=master)](https://travis-ci.org/andysim3d/markdown)

A learn-motivated markdown parser. 

Supports all standard md elements. 

## Sample use case:

Install:
```
pip install lightmd
```

Parse md.

```python
import lightmd

with open("your.md", "r") as md_file:
    ## Parse content
    parsed_content = lightmd.parse_md_to_ast(md_file) 
    ## Render to HTML
    rendered_html = lightmd.render_html(parsed_content)
    ## Render to HTML with custom css style
    rendered_html = lightmd.render_html(parsed_content, "css_style.css")
```

