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
        leafnodes.append(n.textnode_to_htmlnode())
    return leafnodes


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

        elif blocktype == "heading":
            num_hashes = len(block) - len(block.lstrip("#"))
            nodes.append(
                ParentNode(f"h{num_hashes}", leafnode_from_text(block.lstrip("# ")))
            )

        elif blocktype == "ordered_list":
            tmpnodes = []
            for line in lines:
                tmpnodes.append(
                    ParentNode("li", leafnode_from_text(line.lstrip("1234567890. ")))
                )
            node = ParentNode("ol", tmpnodes)
            nodes.append(node)

        elif blocktype == "unordered_list":
            tmpnodes = []
            for line in lines:
                tmpnodes.append(
                    ParentNode(
                        "li",
                        leafnode_from_text(line.replace("* ", "").replace("- ", "")),
                    )
                )
            node = ParentNode("ul", tmpnodes)
            nodes.append(node)

        elif blocktype == "code":
            node = ParentNode(
                "pre", [ParentNode("code", leafnode_from_text(block.strip("`")))]
            )

            nodes.append(node)

        elif blocktype == "quote":
            node = ParentNode("blockquote", leafnode_from_text(block.lstrip("> ")))

            nodes.append(node)
    return ParentNode("div", nodes)
