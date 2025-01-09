def markdown_to_blocks(text):
    return [block.strip() for block in text.split("\n\n") if block.strip()]


def block_to_block_type(inblock):
    blocktype = "paragraph"
    blocks = inblock.split("\n")
    text = "".join(inblock)
    num_hashes = len(text) - len(text.lstrip("#"))
    print("--!!!", inblock, "!!!---")

    if all((block.startswith("- ") or block.startswith("* ")) for block in blocks):
        blocktype = "unordered_list"

    elif all(block.startswith(f"{i+1}. ") for i, block in enumerate(blocks)):
        blocktype = "ordered_list"

    elif all(block.startswith("> ") for block in blocks):
        blocktype = "quote"

    elif (
        text.startswith("#")
        and text.lstrip("#").startswith(" ")
        and "\n" not in text
        and 1 <= num_hashes <= 6
    ):
        blocktype = "heading"

    elif text.startswith("```") and text.endswith("```"):
        blocktype = "code"

    return blocktype
