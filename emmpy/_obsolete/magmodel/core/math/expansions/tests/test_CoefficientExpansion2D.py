import unittest

from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)


class TestBuilder(unittest.TestCase):
    pass

    def test_toArray(self):
        pass

    def test_iSize(self):
        pass

    def test_jSize(self):
        pass

    def test_getILowerBoundIndex(self):
        with self.assertRaises(Exception):
            CoefficientExpansion2D.getILowerBoundIndex(None)

    def test_getIUpperBoundIndex(self):
        with self.assertRaises(Exception):
            CoefficientExpansion2D.getIUpperBoundIndex(None)

    def test_getJLowerBoundIndex(self):
        with self.assertRaises(Exception):
            CoefficientExpansion2D.getILowerBoundIndex(None)

    def test_getJUpperBoundIndex(self):
        with self.assertRaises(Exception):
            CoefficientExpansion2D.getIUpperBoundIndex(None)

    def test_getCoefficient(self):
        with self.assertRaises(Exception):
            CoefficientExpansion2D.getCoefficient(None, 0, 0)


if __name__ == '__main__':
    unittest.main()
