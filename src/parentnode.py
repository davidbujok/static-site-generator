from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):

    def __init__(self, tag, children,  props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            return ValueError
        if self.get_children_length() == 0:
            return ValueError("ParentNode needs at leat one children")

        new_tag = ""
        if self.props is not None:
            attributes = self.props_to_html()
            new_tag = f"<{self.tag}{attributes}>"
        else:
            new_tag = f"<{self.tag}>"

        for node in self.children:
            new_tag += node.to_html()

        new_tag += f"</{self.tag}>"

        return new_tag
