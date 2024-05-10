import unittest

from src.custom_types import TextType
from src.extractfunctions import extract_images, extract_links, extract_text_nodes
from src.splitfunctions import split_node_delimiter
from src.textnode import Textnode


class TestTextToTextNode(unittest.TestCase):

    def test_can_return_links(self):
        testing_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) there is more text"
        text_to_convert = Textnode(testing_text, TextType.TEXT)
        images = extract_images(text_to_convert)
        self.assertEqual(len(images), 3)
        self.assertEqual(
            images[0].text,
            "This is **text** with an *italic* word and a `code block` and an ",
        )
        self.assertEqual(images[0].text_type, TextType.TEXT)
        self.assertEqual(images[1].text, "image")
        self.assertEqual(images[1].text_type, TextType.IMAGE)
        self.assertEqual(
            images[1].url,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
        )
        self.assertEqual(
            images[2].text, " and a [link](https://boot.dev) there is more text"
        )
        links = extract_links(images[-1])
        self.assertEqual(len(links), 3)
        self.assertEqual(links[0].text, " and a ")
        self.assertEqual(links[0].text_type, TextType.TEXT)
        self.assertEqual(links[1].text, "link")
        self.assertEqual(links[1].text_type, TextType.LINK)
        self.assertEqual(links[1].url, "https://boot.dev")
        self.assertEqual(links[2].text, " there is more text")

    def test_can_return_list_of_nodes(self):
        testing_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) there is more text"
        nodes = extract_text_nodes(testing_text)
        self.assertEqual(len(nodes), 11)
        self.assertEqual(type(nodes), list)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)
        self.assertEqual(nodes[4].text, " word and a ")
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[6].text_type, TextType.TEXT)
        self.assertEqual(nodes[6].text, " and an ")
        self.assertEqual(nodes[7].text_type, TextType.IMAGE)
        self.assertEqual(
            nodes[7].url,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
        )
        self.assertEqual(nodes[8].text_type, TextType.TEXT)
        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[9].text_type, TextType.LINK)
        self.assertEqual(nodes[9].url, "https://boot.dev")
        self.assertEqual(nodes[10].text_type, TextType.TEXT)
        self.assertEqual(nodes[10].text, " there is more text")

    def test_can_return_list_of_nodes_second_test(self):
        testing_text = "This is *italic* with an **bold** word  and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) there is more text and a `code block`"
        nodes = extract_text_nodes(testing_text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[3].text_type, TextType.BOLD)
        self.assertEqual(nodes[3].text, "bold")
        self.assertEqual(nodes[6].text, " and a ")
        self.assertEqual(nodes[7].url, "https://boot.dev")
        self.assertEqual(nodes[9].text_type, TextType.CODE)
        self.assertEqual(nodes[9].text, "code block")
        self.assertEqual(nodes[9].text, "code block")


if __name__ == "__main__":
    unittest.main()
