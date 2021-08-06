import unittest

from emmpy.crucible.core.math.vectorfields.vectorfields import (
    VectorFields
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            VectorFields()

    def test_add(self):
        pass

    def test_addAll(self):
        pass

    def test_negate(self):
        pass

    def test_scale(self):
        pass

    def test_scaleLocation(self):
        pass

    def test_multiply(self):
        pass

    def test_cross(self):
        pass

    def test_compose(self):
        pass

    def test_unitize(self):
        pass

    def test_unitizeZero(self):
        pass

    def test_rotate(self):
        pass

    def test_offset(self):
        pass

    def filter(self):
        pass

    def test_withCache(self):
        with self.assertRaises(Exception):
            VectorFields.withCache(None, None)


if __name__ == '__main__':
    unittest.main()
