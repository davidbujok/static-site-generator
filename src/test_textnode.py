import unittest

from textnode import Textnode


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

if __name__ == "__main__":
    unittest.main()

