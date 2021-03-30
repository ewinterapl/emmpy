import unittest

from emmpy.crucible.crust.vectorfieldsij.scalarfieldspatialderivative import (
    ScalarFieldIJSpatialDerivative
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            ScalarFieldIJSpatialDerivative()

    def test_differentiateFDi(self):
        with self.assertRaises(Exception):
            ScalarFieldIJSpatialDerivative.differentiateFDi(None, None)

    def test_differentiateFDj(self):
        with self.assertRaises(Exception):
            ScalarFieldIJSpatialDerivative.differentiateFDj(None, None)


if __name__ == '__main__':
    unittest.main()
