import re
from functions import extract_markdown_images, extract_markdown_links
from textnode import TextType, Textnode

#        listToCompare = [
#            Textnode("This is text with an ", TextType.TEXT),
#            Textnode(
#                "link",
#                TextType.IMAGE,
#                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
#            ),
#            Textnode(" and another ", TextType.TEXT),
#            Textnode(
#                "second link",
#                TextType.IMAGE,
#                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
#            ),
#        ]
#        node = Textnode(
#            "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#            TextType.TEXT,
#        )

def split_node_images(old_nodes):
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
            prev_image = f"![{image[0]}]({image[1]})"
    return new_nodes

def split_node_links(old_nodes):
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
            text_node = node.text.split(f"[{link[0]}]({link[1]})", 1)
            if len(prev_link) != 0:
                text_node = text_node[0].split(prev_link, 1)
                new_nodes.append(Textnode(text_node[1], TextType.TEXT))
            if len(text_node) != 0 and len(prev_link) == 0:
                new_nodes.append(Textnode(text_node[0], TextType.TEXT))
            new_nodes.append(new_node)
            prev_link = f"[{link[0]}]({link[1]})"
    return new_nodes
