def markdown_to_blocks(text):
    return [block.strip() for block in text.split("\n\n") if block.strip()]


def block_to_block_type(inblock):
    blocktype = "paragraph"
    blocks = "".join(inblock).split("\n")
    text = "".join(inblock)
    num_hashes = len(text) - len(text.lstrip("#"))
    order = False

    for i in range(0, len(blocks)):
        if blocks[i].startswith(f"{i}. "):
            order = True
        else:
            order = False

    if all((block.startswith("- ") or block.startswith("* ")) for block in blocks):
        blocktype = "unordered_list"

    elif all(block.startswith("> ") for block in blocks):
        blocktype = "quote"

    elif order:
        blocktype = "ordered"

    elif (
        text.startswith("#")
        and text.lstrip("#").startswith(" ")
        and "\n" not in text
        and 1 <= num_hashes <= 6
    ):
        blocktype = "heading"

    elif "".join(inblock).startswith("```") and "".join(inblock).endswith("```"):
        blocktype = "code"

    return blocktype
