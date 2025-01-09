from markdown_to_html import markdown_to_htmlnode

with open("static/index.md") as f:
    md = f.read()

    print(markdown_to_htmlnode(md))
