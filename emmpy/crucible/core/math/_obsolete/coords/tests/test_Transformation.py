import unittest

from emmpy.crucible.core.math.coords.transformation import Transformation


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Transformation()

    def test_getTransformation(self):
        with self.assertRaises(Exception):
            Transformation.getTransformation(None, None, None)

    def test_getInverseTransformation(self):
        with self.assertRaises(Exception):
            Transformation.getInverseTransformation(None, None, None)

    def test_mxv(self):
        with self.assertRaises(Exception):
            Transformation.mxv(None, None, None)


if __name__ == '__main__':
    unittest.main()
