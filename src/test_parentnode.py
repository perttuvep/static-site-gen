from parentnode import ParentNode
from leafnode import LeafNode
import unittest


class TestParentNode(unittest.TestCase):
    def test_img(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "bold text"),
                LeafNode("i", "italic text"),
                LeafNode("n", "normal text"),
            ],
        )

        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "bold text"),
                LeafNode("i", "italic text"),
                LeafNode("n", "normal text"),
            ],
        )
        node3 = ParentNode(
            "p",
            [
                LeafNode("a", "link text", {"href": "google.com"}),
                LeafNode("b", "bold text"),
                ParentNode("p", [LeafNode("b", "text bold"), LeafNode("i", "italic")]),
            ],
        )
        self.assertEqual(node, node1)

    # def test_a(self):
    #     node = HTMLNode("a")
    #     node1 = HTMLNode("a")
    #     self.assertEqual(node, node1)


if __name__ == "__main__":
    unittest.main()
