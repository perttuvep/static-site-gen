import re
from textnode import TextType


def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"  # mine
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"  # correct
    matches = re.findall(regex, text)
    out = []
    for match in matches:
        out.append(match)
    return out


def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"  # mine
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"  # correct
    matches = re.findall(regex, text)
    out = []
    for match in matches:
        out.append(match)
    return out
