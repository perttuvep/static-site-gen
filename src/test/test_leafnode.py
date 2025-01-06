import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_a(self):
        node = LeafNode(
            "a", "link text here", {"href": "www.google.com", "target": "blank"}
        )
        node1 = LeafNode(
            "a", "link text here", {"href": "www.google.com", "target": "blank"}
        )
        self.assertEqual(node, node1)

    def test_to_html(self):
        node = LeafNode(
            "a", "link text here", {"href": "www.google.com", "target": "blank"}
        )

    # def test_a(self):
    #    node =
    #    node1 =
    #    self.assertEqual(node,node1)


if __name__ == "__main__":
    unittest.main()
