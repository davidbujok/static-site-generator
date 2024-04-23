import unittest
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode


class TestParentNode(unittest.TestCase):

    def test_can_nest_html_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_children_length(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.get_children_length(), 4)

    def test_recursive_node_creation(self):
        nested_node = ParentNode(
            "div",
            [
                LeafNode("b", "I'm nested")
            ],
        )
        main_node = ParentNode(
            "div",
            [
                nested_node,
                LeafNode("b", "Bold text"),
                LeafNode("p", "Normal text"),
            ],
        )
        self.assertEqual(main_node.to_html(), "<div><div><b>I'm nested</b></div><b>Bold text</b><p>Normal text</p></div>")


if __name__ == "__main__":
    unittest.main()
