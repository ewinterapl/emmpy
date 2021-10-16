import unittest

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
)


class TestBuilder(unittest.TestCase):

    def test_createExpansionFromArray(self):
        # 2 args - list + firstExpansionNumber
        e = CoefficientExpansions.createExpansionFromArray([0, 1, 2], 1)
        self.assertIsInstance(e, ArrayCoefficientExpansion1D)
        # 3 args - list + firstI,JexpansionNumber
        e = CoefficientExpansions.createExpansionFromArray(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1)
        self.assertIsInstance(e, ArrayCoefficientExpansion2D)

    def test_add(self):
        e1 = CoefficientExpansions.createExpansionFromArray(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1
        )
        e2 = CoefficientExpansions.createExpansionFromArray(
            [[2, 3, 4], [5, 6, 7], [8, 9, 0]], 1, 1
        )
        e3 = CoefficientExpansions.add(e1, e2)
        self.assertEqual(e3.iLowerBoundIndex, 1)
        self.assertEqual(e3.iUpperBoundIndex, 3)
        self.assertEqual(e3.jLowerBoundIndex, 1)
        self.assertEqual(e3.jUpperBoundIndex, 3)
        self.assertAlmostEqual(e3.getCoefficient(1, 1), 3)
        self.assertAlmostEqual(e3.getCoefficient(1, 2), 5)
        self.assertAlmostEqual(e3.getCoefficient(1, 3), 7)
        self.assertAlmostEqual(e3.getCoefficient(2, 1), 9)
        self.assertAlmostEqual(e3.getCoefficient(2, 2), 11)
        self.assertAlmostEqual(e3.getCoefficient(2, 3), 13)
        self.assertAlmostEqual(e3.getCoefficient(3, 1), 15)
        self.assertAlmostEqual(e3.getCoefficient(3, 2), 17)
        self.assertAlmostEqual(e3.getCoefficient(3, 3), 9)


if __name__ == "__main__":
    unittest.main()
