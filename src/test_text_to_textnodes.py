import unittest

from splitfunctions import split_node_images, split_node_links, split_nodes_delimiter, text_to_textnodes
from textnode import TextType, Textnode

class TestTextToTextNode(unittest.TestCase):

    def test_can_return_links(self):
        testing_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) there is more text"
        text_to_convert = Textnode(testing_text, TextType.TEXT)
        bold_texts = split_nodes_delimiter(text_to_convert, "**", TextType.BOLD)
        self.assertEqual(len(bold_texts), 3)
        self.assertEqual(bold_texts[0].text, "This is ")
        self.assertEqual(bold_texts[0].text_type, TextType.TEXT)
        self.assertEqual(bold_texts[1].text, "text")
        self.assertEqual(bold_texts[1].text_type, TextType.BOLD)
        italic_texts = split_nodes_delimiter(bold_texts[-1], "*", TextType.ITALIC)
        self.assertEqual(len(italic_texts), 3)
        self.assertEqual(italic_texts[0].text, " with an ")
        self.assertEqual(italic_texts[0].text_type, TextType.TEXT)
        self.assertEqual(italic_texts[1].text, "italic")
        self.assertEqual(italic_texts[1].text_type, TextType.ITALIC)
        code_blocks = split_nodes_delimiter(italic_texts[-1], "`", TextType.CODE)
        self.assertEqual(len(code_blocks), 3)
        self.assertEqual(code_blocks[0].text, " word and a ")
        self.assertEqual(code_blocks[0].text_type, TextType.TEXT)
        self.assertEqual(code_blocks[1].text, "code block")
        self.assertEqual(code_blocks[1].text_type, TextType.CODE)
        images = split_node_images(code_blocks[-1])
        self.assertEqual(len(images), 3)
        self.assertEqual(images[0].text, " and an ")
        self.assertEqual(images[0].text_type, TextType.TEXT)
        self.assertEqual(images[1].text, "image")
        self.assertEqual(images[1].text_type, TextType.IMAGE)
        self.assertEqual(images[1].url, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        self.assertEqual(images[2].text, " and a [link](https://boot.dev) there is more text")
        links = split_node_links(images[-1])
        self.assertEqual(len(links), 3)
        self.assertEqual(links[0].text, " and a ")
        self.assertEqual(links[0].text_type, TextType.TEXT)
        self.assertEqual(links[1].text, "link")
        self.assertEqual(links[1].text_type, TextType.LINK)
        self.assertEqual(links[1].url, "https://boot.dev")
        self.assertEqual(links[2].text, " there is more text")
