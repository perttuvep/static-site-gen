from imagelinkregex import extract_markdown_images, extract_markdown_links
import unittest


class TestRegex(unittest.TestCase):
    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and a image ![text alt](image.jpg)"
        # print(extract_markdown_links(text), "ImageLinkRegex")
