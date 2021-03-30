import unittest

from emmpy.crucible.core.math.vectorfields.scalarfield import ScalarField


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            ScalarField()

    def test_evaluate(self):
        with self.assertRaises(Exception):
            ScalarField.evaluate(None, None)


if __name__ == '__main__':
    unittest.main()
