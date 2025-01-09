from blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from splits import (
    split_nodes_delimiter,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes,
)
from textnode import TextType, TextNode


def leafnode_from_text(text):
    leafnodes = []
    textnodes = text_to_textnodes(text)

    for n in textnodes:
        leafnodes.append(n.textnode_to_html())


def strip_n_chars(s, n, char):
    """Remove at most n of char from the start of s."""
    for _ in range(n):
        if s[0] == char:
            s = s[1:]
        else:
            break
    return s


def markdown_to_htmlnode(markdown_text_input):
    blocks = markdown_to_blocks(markdown_text_input)
    nodes = []

    for block in blocks:
        lines = block.split("\n")

        blocktype = block_to_block_type(block)

        if blocktype == "paragraph":
            nodes.append(ParentNode("p", leafnode_from_text(block)))

        if blocktype == "heading":
            num_hashes = len(block) - len(block.lstrip("#"))
            nodes.append(
                ParentNode(
                    f"h{num_hashes}", leafnode_from_text(strip_n_chars(block, 6, "#"))
                )
            )

        if blocktype == "ordered_list":
            tmpnodes = []
            for line in lines:
                tmpnodes.append(
                    ParentNode("li", leafnode_from_text(line.lstrip("123457890. ")))
                )
            node = ParentNode("ol", tmpnodes)
            nodes.append(node)

        if blocktype == "unordered_list":
            tmpnodes = []
            for line in lines:
                tmpnodes.append(
                    ParentNode("li", leafnode_from_text(line.lstrip("*- ")))
                )
            node = ParentNode("ul", tmpnodes)
            nodes.append(node)

        if blocktype == "code":
            node = ParentNode(
                "pre", [ParentNode("code", leafnode_from_text(block.strip("`")))]
            )

            nodes.append(node)

        if blocktype == "quote":
            node = LeafNode("blockquote", block.lstrip("> "))
