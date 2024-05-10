from src.custom_types import TextType
from src.leafnode import LeafNode


class Textnode:
    def __init__(self, text, TextType, url=None):
        self.text = text
        self.text_type = TextType
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"Text: {self.text} Type: {self.text_type} Url:{self.url}"

    def text_node_to_html_node(self):
        if self.text_type not in TextType:
            return ValueError
        if self.text_type == TextType.TEXT:
            return self.text
        if self.text_type == TextType.BOLD:
            return LeafNode(self.text, "b")
        if self.text_type == TextType.ITALIC:
            return LeafNode(self.text, "i")
        if self.text_type == TextType.CODE:
            return LeafNode(self.text, "code")
        if self.text_type == TextType.IMAGE:
            return LeafNode("", "img", {"src": self.url, "alt": self.text})
        if self.text_type == TextType.LINK:
            return LeafNode(self.text, "a", {"href": ""})
