# markdown

[![Build Status](https://travis-ci.org/andysim3d/markdown.svg?branch=master)](https://travis-ci.org/andysim3d/markdown)

![Upload Python Package](https://github.com/andysim3d/markdown/workflows/Upload%20Python%20Package/badge.svg)
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
    parsed_content = lightmd.parse_md_to_ast(md_file.read())
    ## Render to HTML
    rendered_html = lightmd.render_html(parsed_content)
    ## Render to HTML with custom css style
    rendered_html = lightmd.render_html(parsed_content, "/path/to/css_style.css")
```

## Dev onboarding

### Install Python 3.7

For Mac OS:

```
brew install python@3.7
```

For Windows User:

```
choco install python --version=3.7
```

### Create Virtual Enviroment

run following command to install pipenv

```
pip install pipenv
```

Restart your command-line console, run following command:

```
cd [project dir]
pipenv shell
```

Install all dependencies

```
pipenv install
```
