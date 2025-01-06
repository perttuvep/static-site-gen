from enum import Enum
from typing import Text
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if vars(self) == vars(other):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def textnode_to_html(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, value=self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.IMAGES:
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case TextType.LINKS:
                return LeafNode("a", self.text, {"href": self.url})
            case _:
                raise ValueError("Unknown TextType")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_text_type = None
    if delimiter == "**":
        new_text_type = TextType.BOLD
    elif delimiter == "*":
        new_text_type = TextType.ITALIC

    elif delimiter == "`":
        new_text_type = TextType.CODE
    #
    outnodes = []
    for node in old_nodes:
        nodetext = node.text
        print(nodetext)

        if delimiter == "`" or "**" and node.text_type == TextType.TEXT:
            while nodetext.find(delimiter) != -1:
                firstpos = 0
                firstpos = nodetext.find(delimiter, firstpos, len(nodetext))
                secondpos = nodetext.find(delimiter, firstpos + 1, len(nodetext))
                print(
                    f"firstpos == {firstpos}   secondpos == {secondpos} {nodetext[firstpos+1:secondpos]}"
                )

                if nodetext[:firstpos] != "":
                    outnodes.append(TextNode(nodetext[:firstpos], TextType.TEXT))

                if nodetext[firstpos + 1 : secondpos] != "":
                    outnodes.append(
                        TextNode(nodetext[firstpos + 1 : secondpos], new_text_type)
                    )
                nodetext = nodetext[secondpos + 1 :]
            if nodetext != "":
                outnodes.append(TextNode(nodetext, TextType.TEXT))

        elif delimiter == "*" and node.text_type == TextType.TEXT:
            while nodetext.find(delimiter) != -1:
                firstpos = 0
                firstpos = nodetext.find(delimiter, firstpos, len(nodetext))
                while (nodetext[firstpos + 1] == "*") or nodetext.find(
                    delimiter, firstpos + 1, len(nodetext) == -1
                ):
                    firstpos = nodetext.find(delimiter, firstpos + 1, len(nodetext))
                if nodetext[:firstpos] != "":
                    outnodes.append(TextNode(nodetext[:firstpos], TextType.TEXT))

                secondpos = nodetext.find(delimiter, firstpos + 1, len(nodetext))

                if nodetext[firstpos + 1 : secondpos] != "":
                    outnodes.append(
                        TextNode(nodetext[firstpos + 1 : secondpos], new_text_type)
                    )
                nodetext = nodetext[secondpos + 1 :]
            if nodetext != "":
                outnodes.append(TextNode(nodetext, TextType.TEXT))

    return outnodes
