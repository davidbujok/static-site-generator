import itertools
from functions import extract_markdown_images, extract_markdown_links
from textnode import TextType, Textnode


def split_node_delimiter(node, delimiter, text_type):

    new_nodes = []
    if text_type != TextType.TEXT:
        pass

    copy_text = node.text
    if delimiter not in copy_text:
        return [node]

    split_text = copy_text.split(delimiter)
    remove_empty_items = filter(lambda x: len(x) != 0, split_text)
    text_list = list(remove_empty_items)
    for index, text in enumerate(text_list):
        if index % 2 == 0:
            node = Textnode(text, TextType.TEXT)
            new_nodes.append(node)
        else:
            node = Textnode(text, text_type)
            new_nodes.append(node)

    return new_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    processed_nodes = []
    for node in old_nodes:
        new_nodes = split_node_delimiter(node, delimiter, text_type)
        if len(new_nodes):
            processed_nodes.append(new_nodes)
    return processed_nodes


def split_node_images(old_nodes):
    if type(old_nodes) == str:
        old_nodes = Textnode(old_nodes, TextType.TEXT)
        nodes_copy = [old_nodes]
    elif type(old_nodes) == Textnode:
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


def split_node_links(old_nodes):
    if type(old_nodes) == str:
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


def text_to_textnodes(text):

    text = [Textnode(text, TextType.TEXT)]

    bold_texts = split_nodes_delimiter(text, "**", TextType.BOLD)
    italic_texts = split_nodes_delimiter(itertools.chain(*bold_texts), "*", TextType.ITALIC)
    code_blocks = split_nodes_delimiter(itertools.chain(*italic_texts), "`", TextType.CODE)
    images = split_node_images(itertools.chain(*code_blocks))
    nodes_to_return = split_node_links(images)

    return list(nodes_to_return)

def markdown_to_block(markdown):
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
