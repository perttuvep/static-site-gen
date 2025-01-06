import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_img(self):
        node = HTMLNode("img", "example.jpg")
        node1 = HTMLNode("img", "example.jpg")
        self.assertEqual(node, node1)

    def test_a(self):
        node = HTMLNode("a")
        node1 = HTMLNode("a")
        self.assertEqual(node, node1)


if __name__ == "__main__":
    unittest.main()
