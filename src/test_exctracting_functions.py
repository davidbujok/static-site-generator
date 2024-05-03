import unittest
from functions import *
from splitfunctions import markdown_to_block, split_node_delimiter, split_node_images, split_node_links, split_nodes_delimiter
from textnode import TextType, Textnode


class TestExtractingFunction(unittest.TestCase):

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

    def test_can_split_on_code_multiple_occurances_return_correct_code_type_for_eacg(
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
        result = split_node_images([node])
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
        result = split_node_links([node])
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
        block_two = [ "This is another paragraph with *italic* text and `code` here", \
                    "This is the same paragraph on a new line" ]
        block_three = [ "* This is a list", "* with items" ]
        blocks = markdown_to_block(text)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(type(blocks), list)
        self.assertEqual(blocks[0], ["This is **bolded** paragraph"])
        self.assertEqual(blocks[1], block_two)
        self.assertEqual(blocks[2], block_three)


if __name__ == "__main__":
    unittest.main()
