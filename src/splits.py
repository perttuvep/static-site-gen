from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
        else:
            text = node.text
            text = text.split(delimiter)
            if len(text) % 2 == 0:
                raise ValueError("Unclosed delimiter")

            for i in range(0, len(text)):
                if len(text[i]) > 0:
                    out.append(
                        TextNode(text[i], text_type)
                    ) if i % 2 == 1 else out.append(TextNode(text[i], TextType.TEXT))

    return out


def split_nodes_links(old_nodes):
    out = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
        else:
            text = node.text
            regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
            matches = list(re.finditer(regex, text))
            if len(matches) < 1:
                out.append(node)
            else:
                cursor = 0
                for i in range(0, len(matches)):
                    textpart = text[cursor : matches[i].start()]
                    out.append((TextNode(textpart, TextType.TEXT)))
                    linktext = matches[i].group(1)
                    linkurl = matches[i].group(2)
                    out.append((TextNode(linktext, TextType.LINKS, linkurl)))
                    cursor = matches[i].end()
                if len(text[cursor:]) > 0:
                    out.append(TextNode(text[cursor:], TextType.TEXT))
    return out


def split_nodes_images(old_nodes):
    out = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
        else:
            text = node.text
            regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
            matches = list(re.finditer(regex, text))
            if len(matches) < 1:
                out.append(node)
            else:
                cursor = 0
                for i in range(0, len(matches)):
                    textpart = text[cursor : matches[i].start()]
                    out.append((TextNode(textpart, TextType.TEXT)))
                    linktext = matches[i].group(1)
                    linkurl = matches[i].group(2)
                    out.append((TextNode(linktext, TextType.IMAGES, linkurl)))
                    cursor = matches[i].end()
                if len(text[cursor:]) > 0:
                    out.append(TextNode(text[cursor:], TextType.TEXT))
    return out


def text_to_textnodes(text):
    textnodes = [TextNode(text, TextType.TEXT)]
    # NOTE: bold italic code image link
    textnodes = split_nodes_delimiter(textnodes, "**", TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, "*", TextType.ITALIC)
    textnodes = split_nodes_delimiter(textnodes, "`", TextType.CODE)

    textnodes = split_nodes_images(textnodes)
    textnodes = split_nodes_links(textnodes)
    out = []
    for node in textnodes:
        out.append(node)
    return out
