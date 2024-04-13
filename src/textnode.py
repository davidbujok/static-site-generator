from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    TEXT   = "text"
    BOLD   = "bold"
    ITALIC = "italic"
    CODE   = "code"
    LINK   = "link"
    IMAGE  = "image"

class Textnode:

    def __init__(self, text, TextType, url=None):

        self.text = text
        self.text_type = TextType
        self.url = url

    def __eq__(self, other):
        return(
                self.text_type == other.text_type and
                self.text == other.text and
                self.url == other.url
        )

    def __repr__(self) -> str:
        return f"Text: {self.text} Type: {self.text_type} Url:{self.url}"

    def text_node_to_html_node(self):
        if self.text_type not in TextType:
            return ValueError

        if self.text_type == TextType.TEXT:
            return self.text;

        if self.text_type == TextType.BOLD:
            return LeafNode(self.text, "b")

        if self.text_type == TextType.ITALIC:
            return LeafNode(self.text, "i")

        if self.text_type == TextType.CODE:
            return LeafNode(self.text, "code")

        if self.text_type == TextType.LINK:
            return LeafNode(self.text, "a", {"href": ""})

        if self.text_type == TextType.IMAGE:
            return LeafNode("", "img", {"src": self.url, "alt": self.text})

    def split_nodes_delimiter(self, old_nodes, delimiter, text_type): 

        if self.text_type != TextType.TEXT:
            pass

        copy_text = self.text
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
