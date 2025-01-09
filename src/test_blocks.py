import unittest
from blocks import markdown_to_blocks, block_to_block_type


class TestBlocks(unittest.TestCase):
    # Test with various edge cases
    test_markdown = """Header with tabs\t\t\t
    Header continues here


    Paragraph with spaces   
    still paragraph

    \t\t\t
       
    * List with windows endings\r\n
    * Still list\r\n\r\n
    Last block"""

    blocks = markdown_to_blocks(test_markdown)

    def test_blocks(self):
        text = "# This is a heading \n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\nThis is the first list item in a block\n*This is the second list item in a block\n*Third item"
        markdown_to_blocks(text)

    def test_blocks1(self):
        text = "Text above\n\n\n\nText below"
        markdown_to_blocks(text)

    def test_blocks2(self):
        text = "\n\n# Heading\n\nSome text\n\n"
        markdown_to_blocks(text)

    def test_blocks3(self):
        text = "Text above\n \nText below"
        markdown_to_blocks(text)

    def test_blocks4(self):
        text = "# Heading\nSome inline text with **bold** words *italic* and so on"
        markdown_to_blocks(text)

    def test_block_to_block_type(self):
        # Heading edge cases

        assert block_to_block_type("#######Hello") == "paragraph"  # Too many #'s
        assert block_to_block_type("#NoSpace") == "paragraph"  # Missing space after #
        assert block_to_block_type("### ") == "heading"  # Just #'s and space

        # List edge cases/
        assert block_to_block_type("1. First\n3. Third") == "paragraph"  # Missing 2
        assert (
            block_to_block_type("1.No space") == "paragraph"
        )  # Missing space after dot
        assert (
            block_to_block_type("* Item\n- Item") == "unordered_list"
        )  # Mixed * and -

        # Quote edge cases
        assert block_to_block_type(">No space") == "paragraph"  # Missing space after >
        assert (
            block_to_block_type("> Line\nLine") == "paragraph"
        )  # Not all lines start with >

        # Code block edge cases
        assert block_to_block_type("```\ncode\n``") == "paragraph"  # Incomplete closing
        assert block_to_block_type("```") == "code"  # Empty code block
        assert (
            block_to_block_type("```\n```") == "code"
        )  # Empty code block with newline
