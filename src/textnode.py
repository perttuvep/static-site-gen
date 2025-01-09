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
        return f"TextNode({self.text},{self.text_type.value}, {self.url})"

    def textnode_to_htmlnode(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
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
