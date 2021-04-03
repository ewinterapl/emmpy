import unittest

from emmpy.crucible.core.designpatterns.builder import Builder


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Builder()

    def test_build(self):
        with self.assertRaises(Exception):
            Builder.build(None)


if __name__ == '__main__':
    unittest.main()
