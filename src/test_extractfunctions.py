import unittest

from src.custom_types import BlockType, TextType
from src.extractfunctions import (
    extract_block_type,
    extract_images,
    extract_links,
    extract_markdown_images,
    extract_markdown_links,
    extract_markdown_to_blocks,
)
from src.textnode import Textnode


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
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) yet another ![third image](https://mortgage.pogleapis.com/manult/sets/556cxdx.png)",
            TextType.TEXT,
        )
        listToCompare = [
            Textnode("This is text with an ", TextType.TEXT),
            Textnode(
                "image",
                TextType.IMAGE,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            Textnode(" and another ", TextType.TEXT),
            Textnode(
                "second image",
                TextType.IMAGE,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
            Textnode(" yet another ", TextType.TEXT),
            Textnode(
                "third image",
                TextType.IMAGE,
                "https://mortgage.pogleapis.com/manult/sets/556cxdx.png",
            ),
        ]
        result = extract_images([node])
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].text, "This is text with an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "image")
        self.assertEqual(
            result[1].url,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
        )
        self.assertEqual(result[2].text, " and another ")
        self.assertEqual(result[3].text, "second image")
        self.assertEqual(
            result[3].url,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
        )
        self.assertEqual(result[4].text, " yet another ")
        self.assertEqual(result[5].text, "third image")
        self.assertEqual(
            result[5].url, "https://mortgage.pogleapis.com/manult/sets/556cxdx.png"
        )
        self.assertEqual(result, listToCompare)

    def test_can_extract_links_from_node(self):
        node = Textnode(
            "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) yet another [third link](https://mortgage.pogleapis.com/manult/sets/556cxdx.png)",
            TextType.TEXT,
        )
        listToCompare = [
            Textnode("This is text with an ", TextType.TEXT),
            Textnode(
                "link",
                TextType.LINK,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            Textnode(" and another ", TextType.TEXT),
            Textnode(
                "second link",
                TextType.LINK,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
            Textnode(" yet another ", TextType.TEXT),
            Textnode(
                "third link",
                TextType.LINK,
                "https://mortgage.pogleapis.com/manult/sets/556cxdx.png",
            ),
        ]
        result = extract_links([node])
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].text, "This is text with an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "link")
        self.assertEqual(
            result[1].url,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
        )
        self.assertEqual(result[2].text, " and another ")
        self.assertEqual(result[3].text, "second link")
        self.assertEqual(
            result[3].url,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
        )
        self.assertEqual(result[4].text, " yet another ")
        self.assertEqual(result[5].text, "third link")
        self.assertEqual(
            result[5].url, "https://mortgage.pogleapis.com/manult/sets/556cxdx.png"
        )
        self.assertEqual(result, listToCompare)

    def test_can_extract_markdown_block(self):

        text = """This is **bolded** paragraph

                  This is another paragraph with *italic* text and `code` here
                  This is the same paragraph on a new line

                  * This is a list
                  * with items"""
        block_two = [
            "This is another paragraph with *italic* text and `code` here",
            "This is the same paragraph on a new line",
        ]
        block_three = ["* This is a list", "* with items"]
        blocks = extract_markdown_to_blocks(text)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(type(blocks), list)
        self.assertEqual(blocks[0], ["This is **bolded** paragraph"])
        self.assertEqual(blocks[1], block_two)
        self.assertEqual(blocks[2], block_three)

    def test_can_return_images_and_links(self):
        testing_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) there is more text"
        text_to_convert = Textnode(testing_text, TextType.TEXT)
        images = extract_images(testing_text)
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

    def test_can_extract_block_type_from_block(self):
        text = """#### Heading

                  This is another paragraph with *italic* text and `code` here
                  This is the same paragraph on a new line

                  '''
                  import unittest
                  class TestBlock():
                  '''

                  * This is a list
                  * with items

                  100. This is a ordered list
                  1. This is a ordered list
                  2. with some items"""
        block_two = [
            "This is another paragraph with *italic* text and `code` here",
            "This is the same paragraph on a new line",
        ]
        block_three = ["* This is a list", "* with items"]
        blocks = extract_markdown_to_blocks(text)
        heading_blocks = extract_block_type(blocks[0])
        text_block = extract_block_type(blocks[1])
        code_block = extract_block_type(blocks[2])
        bullet_block = extract_block_type(blocks[3])
        number_list_block = extract_block_type(blocks[4])
        self.assertEqual(heading_blocks.name, BlockType.HEADING.name)
        self.assertEqual(text_block.name, BlockType.PARAGRAPH.name)
        self.assertEqual(code_block.name, BlockType.CODE.name)
        self.assertEqual(bullet_block.name, BlockType.UNORDERED_LIST.name)
        self.assertEqual(number_list_block.name, BlockType.ORDERED_LIST.name)


if __name__ == "__main__":
    unittest.main()
