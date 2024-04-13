from htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):

        super().__init__(value, tag, None, props)

    def __repr__(self):
        return f"LeafNode: {self.tag} {self.value} {self.props}"

    def __eq__(self, other):
        return (
            self.value == other.value
            and self.tag == other.tag
            and self.props == other.props
        )

    def to_html(self):
        if self.value is None:
            return ValueError
        if self.tag is None:
            return self.value

        if self.props is not None:
            attributes = self.props_to_html()
            new_tag = f"<{self.tag}{attributes}>{self.value}</{self.tag}>"
            return new_tag
        else:
            new_tag = f"<{self.tag}>{self.value}</{self.tag}>"
            return new_tag
