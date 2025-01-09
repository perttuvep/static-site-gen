from typing import Text
import unittest

from textnode import TextNode, TextType, split_nodes_delimiter
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_default(self):
        node = TextNode("text", TextType.TEXT)
        node1 = TextNode("text", TextType.TEXT)
        self.assertEqual(node, node1)

    def test_diff_text(self):
        node1 = TextNode("text", TextType.TEXT)
        node = TextNode("text", TextType.TEXT)
        self.assertEqual(node, node1)
        node2 = TextNode("boop", TextType.LINKS, "www.google.com")
        node2 = TextNode.textnode_to_htmlnode(node2)
        node3 = LeafNode("a", "boop", {"href": "www.google.com"})
        self.assertEqual(node2, node3)

    def test_delim(self):
        nodes = [
            TextNode(
                "Text with **bold text** and *italic* text and `code` text",
                TextType.TEXT,
            )
        ]
        nodes = split_nodes_delimiter(nodes, "**", TextType.TEXT)
        nodes = split_nodes_delimiter(nodes, "*", TextType.TEXT)
        nodes = split_nodes_delimiter(nodes, "`", TextType.TEXT)


if __name__ == "__main__":
    unittest.main()
