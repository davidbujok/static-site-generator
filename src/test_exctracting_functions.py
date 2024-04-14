import unittest
from functions import *

class TestExtractingFunction(unittest.TestCase):

    def test_can_extract_images(self):
        image_text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        to_be_extracted = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        data = extract_markdown_images(image_text)
        self.assertEqual(data, to_be_extracted)

    def test_can_extracts_links(self):
        link_text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        data = extract_markdown_links(link_text)
        to_be_extracted = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(data, to_be_extracted)

        

