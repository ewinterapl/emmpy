import unittest

from emmpy.crucible.core.math.vectorfields.scalarfield2d import ScalarField2D


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            ScalarField2D()

    def test_evaluate(self):
        with self.assertRaises(Exception):
            ScalarField2D.evaluate(None, None)


if __name__ == '__main__':
    unittest.main()
