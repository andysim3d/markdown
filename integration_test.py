import os
import glob
import src.parser.parser as parser
import src.render.html_render as render
import pytest


def test():
    for file in os.listdir("./md_to_html"):
        if file.endswith(".md"):
            full_path = (os.path.join(os.getcwd(), "md_to_html", file))
            parsed_html = ""
            with open(full_path, 'r') as r:
                content = r.read()
                root = parser.parse_md_to_ast(content)
                parsed_html = render.render(root)
            with open(full_path.replace(".md", ".html"), 'r') as r:
                content = r.read()
                assert content == parsed_html