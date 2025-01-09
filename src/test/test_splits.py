import unittest
from splits import split_nodes_images, split_nodes_links, split_nodes_delimiter
from textnode import TextType, TextNode


class TestSplitLinks(unittest.TestCase):
    def test_splits(self):
        nodes = [
            TextNode(
                "This is a textnode with a two links [goog](www.google.com)[yt](youtube.com)",
                TextType.TEXT,
            )
        ]
        nodes = split_nodes_links(nodes)
        # print(nodes)

    def test_images(self):
        nodes = []
        nodes = [
            TextNode(
                "Text with ![alt text](image.jpg) and a [link](link.com)", TextType.TEXT
            ),
            TextNode("Text with a ![image](image.bmp)", TextType.TEXT),
        ]

        nodes = split_nodes_images(nodes)

    # delimiter = "*"
    # split_nodes_delimiter(nodes, delimiter, TextType.TEXT)
