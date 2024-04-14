import re

from textnode import TextType, Textnode

def extract_markdown_images(text):
    copy_text = text
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", copy_text)
    return matches
        
def extract_markdown_links(text):
    copy_text = text
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", copy_text)
    return matches

def split_node_images(old_nodes):
    nodes_copy = old_nodes
    new_nodes = []
    for node in nodes_copy:
        images = extract_markdown_images(node.text)
        if images is None:
            new_nodes.append(node)
            continue
        for image in images:
            new_node = Textnode(image[0], TextType.IMAGE, image[1])
            new_nodes.append(new_node)
    return new_nodes
