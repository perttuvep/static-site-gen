from textnode import TextNode, TextType
from splits import (
    split_nodes_links,
    split_nodes_delimiter,
    split_nodes_images,
    text_to_textnodes,
)
from markdown_to_html import markdown_to_htmlnode


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    markdown_to_htmlnode(text)


main()
