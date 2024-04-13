import unittest

from leafnode import LeafNode
from textnode import TextType, Textnode


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = Textnode("This is a text node", "bold")
        node2 = Textnode("This is a text node", "bold")
        self.assertTrue(node.__eq__(node2))

    def test_if_url_None(self):
        node = Textnode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_not_equal(self):
        node = Textnode("This is a text node", "bold")
        node2 = Textnode("This is a different node", "italic")
        self.assertFalse(node.__eq__(node2))

    def test_raw_text_conversion(self):
        text_node = Textnode("This is a text node", TextType.TEXT)
        self.assertEqual(text_node.text_node_to_html_node(), "This is a text node")

    def test_bold_conversion(self):
        bold_text_node = Textnode("This is a bold node", TextType.BOLD)
        leaf_node = bold_text_node.text_node_to_html_node()
        compare_this_leaf_node = LeafNode("This is a bold node", "b")
        self.assertTrue(leaf_node.__eq__(compare_this_leaf_node))

    def test_italic_conversion(self):
        italic_text_node = Textnode("This is a italic node", TextType.ITALIC)
        leaf_node = italic_text_node.text_node_to_html_node()
        compare_this_leaf_node = LeafNode("This is a italic node", "i")
        self.assertTrue(leaf_node.__eq__(compare_this_leaf_node))

    def test_code_conversion(self):
        code_text_node = Textnode("This is a code node", TextType.CODE)
        leaf_node = code_text_node.text_node_to_html_node()
        compare_this_leaf_node = LeafNode("This is a code node", "code")
        self.assertTrue(leaf_node.__eq__(compare_this_leaf_node))

    def test_link_conversion(self):
        link_text_node = Textnode("This is a link node", TextType.LINK)
        leaf_node = link_text_node.text_node_to_html_node()
        compare_this_leaf_node = LeafNode("This is a link node", "a", {"href": ""})
        self.assertTrue(leaf_node.__eq__(compare_this_leaf_node))

    def test_image_conversion(self):
        image_text_node = Textnode(
            "This is image description", TextType.IMAGE, "https://test.com"
        )
        leaf_node = image_text_node.text_node_to_html_node()
        compare_this_leaf_node = LeafNode(
            "", "img", {"src": "https://test.com", "alt": "This is image description"}
        )
        self.assertTrue(leaf_node.__eq__(compare_this_leaf_node))

    def test_can_split_on_asteriks_return_correct_text_type(self):
        leaf_node = LeafNode("div", "",)
        text_node = Textnode("This is a text with some **boldness** node", TextType.TEXT)
        split = text_node.split_nodes_delimiter(leaf_node, "*", TextType.BOLD)
        self.assertEqual(split[0].text_type, TextType.TEXT)

    def test_can_split_on_asteriks_return_correct_bold_type(self):
        leaf_node = LeafNode("div", "",)
        text_node = Textnode("This is a text with some **boldness** node", TextType.TEXT)
        split = text_node.split_nodes_delimiter(leaf_node, "*", TextType.BOLD)
        self.assertEqual(split[1].text_type, TextType.BOLD)

    def test_can_split_on_code_return_correct_code_type(self):
        leaf_node = LeafNode("div", "",)
        text_node = Textnode("This will be code block `calc = 2+2` node", TextType.TEXT)
        split = text_node.split_nodes_delimiter(leaf_node, "`", TextType.CODE)
        self.assertEqual(split[1].text_type, TextType.CODE)


if __name__ == "__main__":
    unittest.main()
