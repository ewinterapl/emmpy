import unittest

from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)


class TestBuilder(unittest.TestCase):

    def test_toArray(self):
        pass

    def test_size(self):
        pass

    def test_getUpperBoundIndex(self):
        with self.assertRaises(Exception):
            CoefficientExpansion1D.getUpperBoundIndex(None)

    def test_getLowerBoundIndex(self):
        with self.assertRaises(Exception):
            CoefficientExpansion1D.getLowerBoundIndex(None)

    def test_getCoefficient(self):
        with self.assertRaises(Exception):
            CoefficientExpansion1D.getCoefficient(None, 0)


if __name__ == '__main__':
    unittest.main()
