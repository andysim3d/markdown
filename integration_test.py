import os
import glob
import pytest

import lightmd.parser as parser
from lightmd import render_html


def test():
    for file in os.listdir("./md_to_html"):
        if file.endswith(".md"):
            full_path = (os.path.join(os.getcwd(), "md_to_html", file))
            parsed_html = ""
            with open(full_path, 'r') as md_file:
                content = md_file.read()
                root = parser.parse_md_to_ast(content)
                parsed_html = render_html(root)
            with open(full_path.replace(".md", ".html"), 'r') as html_file:
                html_content = html_file.read()
                assert html_content == parsed_html
