import unittest

from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertAlmostEqual(e.data, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(e.iLowerBoundIndex, 1)
        self.assertEqual(e.jLowerBoundIndex, 1)

    def test_getILowerBoundIndex(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertEqual(e.getILowerBoundIndex(), 1)

    def test_getIUpperBoundIndex(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertEqual(e.getIUpperBoundIndex(), 3)

    def test_getJLowerBoundIndex(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertEqual(e.getJLowerBoundIndex(), 1)

    def test_getJUpperBoundIndex(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertEqual(e.getJUpperBoundIndex(), 3)

    def test_getJUpperBoundIndex(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertEqual(e.getCoefficient(1, 1), 0)

    def test_toString(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertEqual(
            e.toString(),
            "ArrayCoefficientExpansion2D ["
            "data=[[0, 1, 2], [3, 4, 5], [6, 7, 8]], "
            "getILowerBoundIndex()=1, getIUpperBoundIndex()=3, "
            "getJLowerBoundIndex()=1, getJUpperBoundIndex()=3]"
        )

    def test_hashCode(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertEqual(e.hashCode(), 29823)

    def test_hashCode(self):
        e1 = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        e2 = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        e3 = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 2
        )
        self.assertTrue(e1.equals(e2))
        self.assertFalse(e1.equals(e3))


if __name__ == '__main__':
    unittest.main()