import itertools
import re

from custom_types import BlockType
from splitfunctions import split_nodes_delimiter
from src.textnode import Textnode, TextType


def extract_markdown_images(text):
    copy_text = text
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", copy_text)
    return matches


def extract_markdown_links(text):
    copy_text = text
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", copy_text)
    return matches


def extract_images(old_nodes):
    if isinstance(old_nodes, str):
        old_nodes = Textnode(old_nodes, TextType.TEXT)
        nodes_copy = [old_nodes]
    elif isinstance(old_nodes, Textnode):
        nodes_copy = [old_nodes]
    else:
        nodes_copy = old_nodes
    new_nodes = []
    prev_image = ""
    for node in nodes_copy:
        images = extract_markdown_images(node.text)
        if not len(images):
            new_nodes.append(node)
            continue
        for image in images:
            new_node = Textnode(image[0], TextType.IMAGE, image[1])
            text_node = node.text.split(f"![{image[0]}]({image[1]})")
            if len(prev_image) != 0:
                text_node = text_node[0].split(prev_image, 1)
                new_nodes.append(Textnode(text_node[1], TextType.TEXT))
            if len(text_node) != 0 and len(prev_image) == 0:
                new_nodes.append(Textnode(text_node[0], TextType.TEXT))
            new_nodes.append(new_node)
            if len(images) == 1:
                new_nodes.append(Textnode(text_node[1], TextType.TEXT))
            prev_image = f"![{image[0]}]({image[1]})"
    return new_nodes


def extract_links(old_nodes):
    if isinstance(old_nodes, str):
        old_nodes = Textnode(old_nodes, TextType.TEXT)
        nodes_copy = [old_nodes]
    elif type(old_nodes) == Textnode:
        nodes_copy = [old_nodes]
    else:
        nodes_copy = old_nodes
    new_nodes = []
    prev_link = ""
    for node in nodes_copy:
        links = extract_markdown_links(node.text)
        if not len(links):
            new_nodes.append(node)
            continue
        for link in links:
            new_node = Textnode(link[0], TextType.LINK, link[1])
            text_node = node.text.split(f"[{link[0]}]({link[1]})")
            if len(prev_link) != 0:
                text_node = text_node[0].split(prev_link, 1)
                new_nodes.append(Textnode(text_node[1], TextType.TEXT))
            if len(text_node) != 0 and len(prev_link) == 0:
                new_nodes.append(Textnode(text_node[0], TextType.TEXT))
            new_nodes.append(new_node)
            if len(links) == 1:
                new_nodes.append(Textnode(text_node[1], TextType.TEXT))
            prev_link = f"[{link[0]}]({link[1]})"
    return new_nodes


def extract_markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    block = []
    blocks = []
    for line in lines:
        if len(line) > 0:
            block.append(line.strip())
        else:
            blocks.append(block)
            block = []
    if len(block) > 0:
        blocks.append(block)
    return blocks


def extract_text_nodes(text):
    text = [Textnode(text, TextType.TEXT)]
    bold_texts = split_nodes_delimiter(text, "**", TextType.BOLD)
    italic_texts = split_nodes_delimiter(
        itertools.chain(*bold_texts), "*", TextType.ITALIC
    )
    code_blocks = split_nodes_delimiter(
        itertools.chain(*italic_texts), "`", TextType.CODE
    )
    images = extract_images(itertools.chain(*code_blocks))
    nodes_to_return = extract_links(images)
    return list(nodes_to_return)


def extract_block_type(block):
    count = 0
    heading_level = 0
    re_numbers = re.compile(r"^[0-9]*.\s")
    stripped_txt = block[0].lstrip()
    while block[0][count] == "#":
        heading_level += 1
        count += 1

    if heading_level > 0:
        return BlockType.HEADING

    while count < len(block[0]) and block[0][count] == "'":
        count += 1

    if count == 3 and heading_level == 0:
        closing_block = block[-1][-3:]
        if closing_block == "'''":
            return BlockType.CODE

    if stripped_txt[0:2] == "* " or stripped_txt[0:2] == "- ":
        return BlockType.UNORDERED_LIST
    if re_numbers.match(block[0]):
        return BlockType.ORDERED_LIST

    while count < len(block):
        if block[count][0] != "<":
            break
        if count == len(block) - 1:
            return BlockType.QUOTE
        count += 1
    return BlockType.PARAGRAPH
