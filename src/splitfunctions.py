import re
from functions import extract_markdown_images, extract_markdown_links
from textnode import TextType, Textnode

def split_nodes_delimiter(old_nodes, delimiter, text_type): 

    if text_type != TextType.TEXT:
        pass

    copy_text = old_nodes.text
    split_text = copy_text.split(delimiter)
    remove_empty_items = filter(lambda x: len(x) != 0, split_text)
    text_list = list(remove_empty_items)
    new_nodes = []

    for index, text in enumerate(text_list):
        if index % 2 == 0:
            node = Textnode(text, TextType.TEXT)
            new_nodes.append(node)
        else:
            node = Textnode(text, text_type)
            new_nodes.append(node)

    return new_nodes

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
        if images is None:
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
        if links is None:
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
    extracted_nodes = []
    text = Textnode(text, TextType.TEXT)

    bold_texts = split_nodes_delimiter(text, "**", TextType.BOLD)
    if len(bold_texts) > 0:
        for index in range(len(bold_texts) - 1):
            extracted_nodes.append(bold_texts[index])

    italic_texts = split_nodes_delimiter([bold_texts[0], bold_texts[-1]], "*", TextType.ITALIC)
    if len(italic_texts) > 0:
        for index in range(len(italic_texts) - 1):
            extracted_nodes.append(bold_texts[index])

    code_blocks = split_nodes_delimiter(italic_texts[-1], "`", TextType.CODE)
    if len(code_blocks) > 0:
        for index in range(len(code_blocks) - 1):
            extracted_nodes.append(code_blocks[index])

    images = split_node_images(code_blocks[-1])
    if len(images) > 0:
        for index in range(len(images) - 1):
            extracted_nodes.append(images[index])

    if len(images) > 0:
        links = split_node_links(images[-1])
        if len(links) > 0:
            for index in range(len(links)):
                extracted_nodes.append(links[index])
    return extracted_nodes
    
