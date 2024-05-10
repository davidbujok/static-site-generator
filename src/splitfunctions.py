from src.custom_types import TextType
from src.textnode import Textnode


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
    """Split any given list of nodes on any given delimiter"""
    processed_nodes = []
    for node in old_nodes:
        new_nodes = split_node_delimiter(node, delimiter, text_type)
        if len(new_nodes):
            processed_nodes.append(new_nodes)
    return processed_nodes
