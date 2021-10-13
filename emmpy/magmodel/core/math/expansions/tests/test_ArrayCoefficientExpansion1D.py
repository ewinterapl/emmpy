import unittest

from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        ArrayCoefficientExpansion1D([0], 0)

    # def test_getLowerBoundIndex(self):
    #     c = ArrayCoefficientExpansion1D([0], 0)
    #     self.assertEqual(c.getLowerBoundIndex(), 0)

    def test_getUpperBoundIndex(self):
        c = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        self.assertEqual(c.getUpperBoundIndex(), 4)

    def test_getCoefficient(self):
        c = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 3.3], 1)
        self.assertAlmostEqual(c.getCoefficient(2), 1.1)


if __name__ == '__main__':
    unittest.main()
