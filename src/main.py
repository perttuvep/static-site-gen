from os.path import isdir, isfile
from posixpath import dirname
from textnode import TextNode, TextType
from splits import (
    text_to_textnodes,
)
from markdown_to_html import markdown_to_htmlnode
import shutil
import os


def main():
    copy_to_pub("static/", "public")
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"

    generate_pages_recursive(os.path.abspath("static"), "template.html", "public")


def copy_to_pub(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for file in os.listdir(src):
        if os.path.isfile(os.path.join(src, file)):
            shutil.copy(os.path.join(src, file), os.path.join(dst, file))
        elif os.path.isdir(os.path.join(src, file)):
            copy_to_pub(os.path.join(src, file), os.path.join(dst, file))


def extract_title(markdown):
    with open(markdown) as f:
        textmd = f.read()
    title = "Not found!"
    lines = textmd.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
    if title == "Not found!":
        raise ValueError("Header not found")
    return title


#
# def generate_page(from_path, template_path, dest_path):
#     print(f"Generating page from {from_path} to {dest_path} using {template_path}")
#
#     with open(from_path) as f:
#         mdfile = f.read()
#     with open(template_path) as f:
#         contenttemplate = f.read()
#
#     node = markdown_to_htmlnode(mdfile)
#     out = node.to_html()
#     title = extract_title(from_path)
#     print(title, out)
#
#     outputhtml = contenttemplate.replace("{{ Title }}", title).replace(
#         "{{ Content }}", out
#     )
#     destdir = os.path.abspath(dest_path)
#
#     if not os.path.exists(os.path.dirname(destdir)):
#         os.makedirs(os.path.dirname(destdir))
#         print("yo")
#     with open(dest_path, "w") as out:
#         out.write(outputhtml)
#         print(f"wrote to {dest_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    with open(template_path) as f:
        contenttemplate = f.read()
    print(
        f"Entering {dir_path_content} with {template_path} as template and outputting to {dest_dir_path}"
    )
    for entry in os.listdir(dir_path_content):
        if ".md" == os.path.splitext(entry)[1]:
            with open(os.path.join(dir_path_content, entry)) as f:
                md = f.read()
            node = markdown_to_htmlnode(md)
            out = node.to_html()
            title = extract_title(os.path.join(dir_path_content, entry))
            html = contenttemplate.replace("{{ Title }}", title).replace(
                "{{ Content }}", out
            )
            if not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path)
            outputfilename = entry.replace(".md", ".html")

            with open(os.path.join(dest_dir_path, outputfilename), "w") as outfile:
                outfile.write(html)
        if os.path.isdir(os.path.join(dir_path_content, entry)):
            print(f"calling {os.path.join(dir_path_content,entry)}")
            generate_pages_recursive(
                os.path.join(dir_path_content, entry),
                template_path,
                os.path.join(dest_dir_path, entry),
            )
        else:
            print(entry, "WTF")


main()
