import unittest
from functions import *
from textnode import TextType, Textnode


class TestExtractingFunction(unittest.TestCase):

    def test_can_extract_images(self):
        image_text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        to_be_extracted = [
            (
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            (
                "another",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
            ),
        ]
        data = extract_markdown_images(image_text)
        self.assertEqual(data, to_be_extracted)

    def test_can_extracts_links(self):
        link_text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        data = extract_markdown_links(link_text)
        to_be_extracted = [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another"),
        ]
        self.assertEqual(data, to_be_extracted)

    def test_can_extract_nodes(self):
        node = Textnode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT,
        )
        compare_node1 = Textnode(
            "image",
            TextType.IMAGE,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
        )
        compare_node2 = Textnode(
            "second image",
            TextType.IMAGE,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
        )
        result = split_node_images([node])
        self.assertEqual(result[0], compare_node1)
        self.assertEqual(result[1], compare_node2)
