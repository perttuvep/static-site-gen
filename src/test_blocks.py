import unittest
from blocks import markdown_to_blocks, block_to_block_type
from markdown_to_html import markdown_to_htmlnode


class TestBlocks(unittest.TestCase):
    #     text = "# This is a heading \n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\nThis is the first list item in a block\n*This is the second list item in a block\n*Third item"
    #     markdown_to_blocks(text)
    #
    def test_blocks1(self):
        with open("static/index.md") as f:
            text = f.read()

        nodes = markdown_to_htmlnode(text)
        nodes.to_html()

    #
    # def test_blocks2(self):
    #     text = "\n\n# Heading\n\nSome text\n\n"
    #     markdown_to_blocks(text)
    #
    # def test_blocks3(self):
    #     text = "Text above\n \nText below"
    #     markdown_to_blocks(text)
    #
    # def test_blocks4(self):
    #     text = "# Heading\nSome inline text with **bold** words *italic* and so on"
    #     markdown_to_blocks(text)
    #
    def test_block_to_block_type(self):
        # Heading edge cases

        # assert block_to_block_type("#######Hello") == "paragraph"  # Too many #'s
        # assert block_to_block_type("#NoSpace") == "paragraph"  # Missing space after #
        # assert block_to_block_type("### ") == "heading"  # Just #'s and space
        #
        # # List edge cases/
        # assert block_to_block_type("1. First\n3. Third") == "paragraph"  # Missing 2
        # assert (
        #     block_to_block_type("1.No space") == "paragraph"

        print(
            "!!!!!",
            block_to_block_type(
                "1. Gandalf\n2. Bilbo\n3. Sam\n4. Glorfindel\n5. Galadriel\n6. Elrond\n7. Thorin\n8. Sauron\n9. Aragorn\n"
            ),
        )
        assert (
            block_to_block_type(
                "1. Gandalf\n2. Bilbo\n3. Sam\n4. Glorfindel\n5. Galadriel\n6. Elrond\n7. Thorin\n8. Sauron\n9. Aragorn\n"
            )
            == "ordered_list"
        )  # Mixed * and -

    #
    #     # Quote edge cases
    #     assert block_to_block_type(">No space") == "paragraph"  # Missing space after >
    #     assert (
    #         block_to_block_type("> Line\nLine") == "paragraph"
    #     )  # Not all lines start with >
    #
    #     # Code block edge cases
    #     assert block_to_block_type("```\ncode\n``") == "paragraph"  # Incomplete closing
    #     assert block_to_block_type("```") == "code"  # Empty code block
    #     assert (
    #         block_to_block_type("```\n```") == "code"
    #     )  # Empty code block with newline
    #
    # def test_md_to_html(self):
    #     text = "1. Gandalf\n2. Bilbo\n3. Sam\n4. Glorfindel\n5. Galadriel\n6. Elrond\n7. Thorin\n8. Sauron\n9. Aragorn\n"
