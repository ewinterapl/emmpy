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

    def test_negate(self):
        e = CoefficientExpansions.createExpansionFromArray(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)
        en = CoefficientExpansions.negate(e)
        self.assertEqual(en.iLowerBoundIndex, 1)
        self.assertEqual(en.iUpperBoundIndex, 3)
        self.assertEqual(en.jLowerBoundIndex, 1)
        self.assertEqual(en.jUpperBoundIndex, 3)
        self.assertAlmostEqual(en.getCoefficient(1, 1), -1)
        self.assertAlmostEqual(en.getCoefficient(1, 2), -2)
        self.assertAlmostEqual(en.getCoefficient(1, 3), -3)
        self.assertAlmostEqual(en.getCoefficient(2, 1), -4)
        self.assertAlmostEqual(en.getCoefficient(2, 2), -5)
        self.assertAlmostEqual(en.getCoefficient(2, 3), -6)
        self.assertAlmostEqual(en.getCoefficient(3, 1), -7)
        self.assertAlmostEqual(en.getCoefficient(3, 2), -8)
        self.assertAlmostEqual(en.getCoefficient(3, 3), -9)

    def test_createUnity(self):
        eu = CoefficientExpansions.createUnity(1, 3, 1, 3)
        self.assertEqual(eu.iLowerBoundIndex, 1)
        self.assertEqual(eu.iUpperBoundIndex, 3)
        self.assertEqual(eu.jLowerBoundIndex, 1)
        self.assertEqual(eu.jUpperBoundIndex, 3)
        self.assertAlmostEqual(eu.getCoefficient(1, 1), 1)
        self.assertAlmostEqual(eu.getCoefficient(1, 2), 1)
        self.assertAlmostEqual(eu.getCoefficient(1, 3), 1)
        self.assertAlmostEqual(eu.getCoefficient(2, 1), 1)
        self.assertAlmostEqual(eu.getCoefficient(2, 2), 1)
        self.assertAlmostEqual(eu.getCoefficient(2, 3), 1)
        self.assertAlmostEqual(eu.getCoefficient(3, 1), 1)
        self.assertAlmostEqual(eu.getCoefficient(3, 2), 1)
        self.assertAlmostEqual(eu.getCoefficient(3, 3), 1)

    def test_scale(self):
        e = CoefficientExpansions.createExpansionFromArray(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)
        es = CoefficientExpansions.scale(e, 2)
        self.assertEqual(es.iLowerBoundIndex, 1)
        self.assertEqual(es.iUpperBoundIndex, 3)
        self.assertEqual(es.jLowerBoundIndex, 1)
        self.assertEqual(es.jUpperBoundIndex, 3)
        self.assertAlmostEqual(es.getCoefficient(1, 1), 2)
        self.assertAlmostEqual(es.getCoefficient(1, 2), 4)
        self.assertAlmostEqual(es.getCoefficient(1, 3), 6)
        self.assertAlmostEqual(es.getCoefficient(2, 1), 8)
        self.assertAlmostEqual(es.getCoefficient(2, 2), 10)
        self.assertAlmostEqual(es.getCoefficient(2, 3), 12)
        self.assertAlmostEqual(es.getCoefficient(3, 1), 14)
        self.assertAlmostEqual(es.getCoefficient(3, 2), 16)
        self.assertAlmostEqual(es.getCoefficient(3, 3), 18)

    def test_createConstant(self):
        e = CoefficientExpansions.createConstant(1, 3, 99)
        self.assertEqual(e.firstExpansionNumber, 1)
        self.assertEqual(e.lastExpansionNumber, 3)
        self.assertAlmostEqual(e.getCoefficient(1), 99)
        self.assertAlmostEqual(e.getCoefficient(2), 99)
        self.assertAlmostEqual(e.getCoefficient(3), 99)
        e = CoefficientExpansions.createConstant(1, 3, 1, 3, 99)
        self.assertEqual(e.iLowerBoundIndex, 1)
        self.assertEqual(e.iUpperBoundIndex, 3)
        self.assertEqual(e.jLowerBoundIndex, 1)
        self.assertEqual(e.jUpperBoundIndex, 3)
        self.assertAlmostEqual(e.getCoefficient(1, 1), 99)
        self.assertAlmostEqual(e.getCoefficient(1, 2), 99)
        self.assertAlmostEqual(e.getCoefficient(1, 3), 99)
        self.assertAlmostEqual(e.getCoefficient(2, 1), 99)
        self.assertAlmostEqual(e.getCoefficient(2, 2), 99)
        self.assertAlmostEqual(e.getCoefficient(2, 3), 99)
        self.assertAlmostEqual(e.getCoefficient(3, 1), 99)
        self.assertAlmostEqual(e.getCoefficient(3, 2), 99)
        self.assertAlmostEqual(e.getCoefficient(3, 3), 99)

    def test_add(self):
        e1 = CoefficientExpansions.createExpansionFromArray([1, 2, 3], 1)
        e2 = CoefficientExpansions.createExpansionFromArray([4, 5, 6], 1)
        e3 = CoefficientExpansions.add(e1, e2)
        self.assertEqual(e3.firstExpansionNumber, 1)
        self.assertEqual(e3.lastExpansionNumber, 3)
        self.assertAlmostEqual(e3.getCoefficient(1), 5)
        self.assertAlmostEqual(e3.getCoefficient(2), 7)
        self.assertAlmostEqual(e3.getCoefficient(3), 9)
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
