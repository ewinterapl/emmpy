import unittest

from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
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

    def test_invert(self):
        e = CoefficientExpansions.createExpansionFromArray([1, 2, 3], 1)
        ei = CoefficientExpansions.invert(e)
        self.assertEqual(ei.getLowerBoundIndex(), 1)
        self.assertEqual(ei.getUpperBoundIndex(), 3)
        self.assertAlmostEqual(ei.getCoefficient(1), 1)
        self.assertAlmostEqual(ei.getCoefficient(2), 1/2)
        self.assertAlmostEqual(ei.getCoefficient(3), 1/3)

    def test_negate(self):
        e = CoefficientExpansions.createExpansionFromArray([1, 2, 3], 1)
        en = CoefficientExpansions.negate(e)
        self.assertEqual(en.getLowerBoundIndex(), 1)
        self.assertEqual(en.getUpperBoundIndex(), 3)
        self.assertAlmostEqual(en.getCoefficient(1), -1)
        self.assertAlmostEqual(en.getCoefficient(2), -2)
        self.assertAlmostEqual(en.getCoefficient(3), -3)
        e = CoefficientExpansions.createExpansionFromArray(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)
        en = CoefficientExpansions.negate(e)
        self.assertEqual(en.getILowerBoundIndex(), 1)
        self.assertEqual(en.getIUpperBoundIndex(), 3)
        self.assertEqual(en.getJLowerBoundIndex(), 1)
        self.assertEqual(en.getJUpperBoundIndex(), 3)
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
        eu = CoefficientExpansions.createUnity(1, 3)
        self.assertEqual(eu.getLowerBoundIndex(), 1)
        self.assertEqual(eu.getUpperBoundIndex(), 3)
        self.assertAlmostEqual(eu.getCoefficient(1), 1)
        self.assertAlmostEqual(eu.getCoefficient(2), 1)
        self.assertAlmostEqual(eu.getCoefficient(3), 1)
        eu = CoefficientExpansions.createUnity(1, 3, 1, 3)
        self.assertEqual(eu.getILowerBoundIndex(), 1)
        self.assertEqual(eu.getIUpperBoundIndex(), 3)
        self.assertEqual(eu.getJLowerBoundIndex(), 1)
        self.assertEqual(eu.getJUpperBoundIndex(), 3)
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
        e = CoefficientExpansions.createExpansionFromArray([1, 2, 3], 1)
        es = CoefficientExpansions.scale(e, 2)
        self.assertEqual(es.getLowerBoundIndex(), 1)
        self.assertEqual(es.getUpperBoundIndex(), 3)
        self.assertAlmostEqual(es.getCoefficient(1), 2)
        self.assertAlmostEqual(es.getCoefficient(2), 4)
        self.assertAlmostEqual(es.getCoefficient(3), 6)
        e = CoefficientExpansions.createExpansionFromArray(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)
        es = CoefficientExpansions.scale(e, 2)
        self.assertEqual(es.getILowerBoundIndex(), 1)
        self.assertEqual(es.getIUpperBoundIndex(), 3)
        self.assertEqual(es.getJLowerBoundIndex(), 1)
        self.assertEqual(es.getJUpperBoundIndex(), 3)
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
        self.assertEqual(e.getLowerBoundIndex(), 1)
        self.assertEqual(e.getUpperBoundIndex(), 3)
        self.assertAlmostEqual(e.getCoefficient(1), 99)
        self.assertAlmostEqual(e.getCoefficient(2), 99)
        self.assertAlmostEqual(e.getCoefficient(3), 99)
        e = CoefficientExpansions.createConstant(1, 3, 1, 3, 99)
        self.assertEqual(e.getILowerBoundIndex(), 1)
        self.assertEqual(e.getIUpperBoundIndex(), 3)
        self.assertEqual(e.getJLowerBoundIndex(), 1)
        self.assertEqual(e.getJUpperBoundIndex(), 3)
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
        self.assertEqual(e3.getLowerBoundIndex(), 1)
        self.assertEqual(e3.getUpperBoundIndex(), 3)
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
        self.assertEqual(e3.getILowerBoundIndex(), 1)
        self.assertEqual(e3.getIUpperBoundIndex(), 3)
        self.assertEqual(e3.getJLowerBoundIndex(), 1)
        self.assertEqual(e3.getJUpperBoundIndex(), 3)
        self.assertAlmostEqual(e3.getCoefficient(1, 1), 3)
        self.assertAlmostEqual(e3.getCoefficient(1, 2), 5)
        self.assertAlmostEqual(e3.getCoefficient(1, 3), 7)
        self.assertAlmostEqual(e3.getCoefficient(2, 1), 9)
        self.assertAlmostEqual(e3.getCoefficient(2, 2), 11)
        self.assertAlmostEqual(e3.getCoefficient(2, 3), 13)
        self.assertAlmostEqual(e3.getCoefficient(3, 1), 15)
        self.assertAlmostEqual(e3.getCoefficient(3, 2), 17)
        self.assertAlmostEqual(e3.getCoefficient(3, 3), 9)

    def test_createNullExpansion(self):
        e = CoefficientExpansions.createNullExpansion(1, 1, 3)
        with self.assertRaises(Exception):
            e.getCoefficient(1, 1)

    def test_convertTo1D(self):
        e2 = CoefficientExpansions.createExpansionFromArray(
            [[2, 3, 4], [5, 6, 7], [8, 9, 0]], 1, 1
        )
        e1 = CoefficientExpansions.convertTo1D(e2, 1)
        self.assertEqual(e1.getLowerBoundIndex(), 1)
        self.assertEqual(e1.getUpperBoundIndex(), 9)
        self.assertAlmostEqual(e1.getCoefficient(1), 2)
        self.assertAlmostEqual(e1.getCoefficient(2), 3)
        self.assertAlmostEqual(e1.getCoefficient(3), 4)
        self.assertAlmostEqual(e1.getCoefficient(4), 5)
        self.assertAlmostEqual(e1.getCoefficient(5), 6)
        self.assertAlmostEqual(e1.getCoefficient(6), 7)
        self.assertAlmostEqual(e1.getCoefficient(7), 8)
        self.assertAlmostEqual(e1.getCoefficient(8), 9)
        self.assertAlmostEqual(e1.getCoefficient(9), 0)

    def test_convertTo2D(self):
        e1 = CoefficientExpansions.createExpansionFromArray(
            [0, 1, 2, 3, 4, 5, 6, 7, 8], 1
        )
        e2 = CoefficientExpansions.convertTo2D(e1, 1, 3, 1, 3)
        self.assertEqual(e2.getILowerBoundIndex(), 1)
        self.assertEqual(e2.getIUpperBoundIndex(), 3)
        self.assertEqual(e2.getJLowerBoundIndex(), 1)
        self.assertEqual(e2.getJUpperBoundIndex(), 3)
        self.assertAlmostEqual(e2.getCoefficient(1, 1), 0)
        self.assertAlmostEqual(e2.getCoefficient(1, 2), 1)
        self.assertAlmostEqual(e2.getCoefficient(1, 3), 2)
        self.assertAlmostEqual(e2.getCoefficient(2, 1), 3)
        self.assertAlmostEqual(e2.getCoefficient(2, 2), 4)
        self.assertAlmostEqual(e2.getCoefficient(2, 3), 5)
        self.assertAlmostEqual(e2.getCoefficient(3, 1), 6)
        self.assertAlmostEqual(e2.getCoefficient(3, 2), 7)
        self.assertAlmostEqual(e2.getCoefficient(3, 3), 8)

    def test_concat(self):
        e1 = CoefficientExpansions.createExpansionFromArray([0, 1, 2, 3], 1)
        e2 = CoefficientExpansions.createExpansionFromArray([4, 5, 6, 7, 8], 1)
        e3 = CoefficientExpansions.concat(e1, e2)
        self.assertEqual(e3.getLowerBoundIndex(), 1)
        self.assertEqual(e3.getUpperBoundIndex(), 9)
        self.assertAlmostEqual(e3.getCoefficient(1), 0)
        self.assertAlmostEqual(e3.getCoefficient(2), 1)
        self.assertAlmostEqual(e3.getCoefficient(3), 2)
        self.assertAlmostEqual(e3.getCoefficient(4), 3)
        self.assertAlmostEqual(e3.getCoefficient(5), 4)
        self.assertAlmostEqual(e3.getCoefficient(6), 5)
        self.assertAlmostEqual(e3.getCoefficient(7), 6)
        self.assertAlmostEqual(e3.getCoefficient(8), 7)
        self.assertAlmostEqual(e3.getCoefficient(9), 8)


if __name__ == '__main__':
    unittest.main()
