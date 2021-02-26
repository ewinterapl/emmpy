import unittest

from emmpy.templates.interfacetemplate import InterfaceTemplate


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            InterfaceTemplate()


if __name__ == '__main__':
    unittest.main()
