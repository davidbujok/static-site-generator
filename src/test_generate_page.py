import unittest

from generate_page import extract_title, generate_page
from markdownblocks import markdown_to_blocks

class TestGenereteWebPage(unittest.TestCase):

    def test_can_extract_title(self):
        markdown_file = open("markdown_files/test.md")
        blocks = markdown_to_blocks(markdown_file.read())
        markdown_file.close()
        title = extract_title(blocks)
        self.assertEqual(title ," This is new document.")
