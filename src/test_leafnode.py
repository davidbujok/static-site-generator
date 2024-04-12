import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_inherited_text_to_html_method(self):

        leaf_node = LeafNode(
            "h3", "subtitle", {"class": "bold", "attributes": "navbar"}
        )
        self.assertEqual(leaf_node.props_to_html(), ' class="bold" attributes="navbar"')

    def test_repr(self):
        leaf_node = LeafNode(
            "h3", "subtitle", {"class": "bold", "attributes": "navbar"}
        )
        self.assertEqual(
            leaf_node.__repr__(),
            "LeafNode: h3 subtitle {'class': 'bold', 'attributes': 'navbar'}",
        )

    def test_if_can_create_tag(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_raise_error_on_empty_value(self):
        node1 = LeafNode("h1")
        self.assertEqual(node1.to_html(), ValueError)

