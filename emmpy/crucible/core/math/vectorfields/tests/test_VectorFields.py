import unittest

from emmpy.crucible.core.math.vectorfields.vectorfields import (
    VectorFields
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            VectorFields()

    def test_scale(self):
        pass


if __name__ == '__main__':
    unittest.main()
