import unittest

from copy_content import copy_content

class TestCopyFunction(unittest.TestCase):

    def test_path_exist(self):
        path = copy_content()
        self.assertEqual(path, "/home/arch/repos/static-site-generator/static")




