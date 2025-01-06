import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_default(self):
        node = TextNode("text", TextType.NORMAL)
        node1 = TextNode("text", TextType.NORMAL)
        self.assertEqual(node, node1)

    def test_diff_text(self):
        node1 = TextNode("text", TextType.NORMAL)
        node = TextNode("text", TextType.NORMAL)
        self.assertEqual(node, node1)


if __name__ == "__main__":
    unittest.main()

