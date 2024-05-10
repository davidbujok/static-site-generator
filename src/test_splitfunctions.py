import unittest

from src.custom_types import TextType
from src.splitfunctions import split_node_delimiter
from src.textnode import Textnode


class TestSplitFunction(unittest.TestCase):
    def test_can_split_on_code_multiple_occurances_return_correct_code_type_for_each(
        self,
    ):
        text_node = Textnode(
            "This will be code block `calc = 2+2` node and another one `multi = 2*2`",
            TextType.TEXT,
        )
        split = split_node_delimiter(text_node, "`", TextType.CODE)
        self.assertEqual(split[1].text_type, TextType.CODE)
        self.assertEqual(split[1].text, "calc = 2+2")
        self.assertEqual(split[3].text_type, TextType.CODE)
        self.assertEqual(split[3].text, "multi = 2*2")

    def test_can_split_on_asteriks_return_correct_text_type(self):
        text_node = Textnode(
            "This is a text with some **boldness** node", TextType.TEXT
        )
        split = split_node_delimiter(text_node, "*", TextType.BOLD)
        self.assertEqual(split[0].text_type, TextType.TEXT)

    def test_can_split_on_asteriks_return_correct_bold_type(self):
        text_node = Textnode(
            "This is a text with some **boldness** node", TextType.TEXT
        )
        split = split_node_delimiter(text_node, "*", TextType.BOLD)
        self.assertEqual(split[1].text_type, TextType.BOLD)

    def test_can_split_on_code_return_correct_code_type(self):
        text_node = Textnode("This will be code block `calc = 2+2` node", TextType.TEXT)
        split = split_node_delimiter(text_node, "`", TextType.CODE)
        self.assertEqual(split[1].text_type, TextType.CODE)
