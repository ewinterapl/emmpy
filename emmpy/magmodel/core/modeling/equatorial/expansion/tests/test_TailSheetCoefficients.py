import unittest

from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class TestTailSheetCoefficients(unittest.TestCase):

    def test___init__(self):
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        c = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        self.assertAlmostEqual(c.tailSheetSymmetricValues, tailSym)
        self.assertAlmostEqual(c.tailSheetOddValues, tailOdd)
        self.assertAlmostEqual(c.tailSheetEvenValues, tailEven)

    def test_createUnity(self):
        e = TailSheetCoefficients.createUnity(3, 3)
        self.assertAlmostEqual(e.tailSheetSymmetricValues.getCoefficient(1), 1)
        self.assertAlmostEqual(e.tailSheetOddValues.getCoefficient(1, 1), 1)
        self.assertAlmostEqual(e.tailSheetEvenValues.getCoefficient(1, 1), 1)

    def test_createFromArray(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertAlmostEqual(c.tailSheetSymmetricValues.getCoefficient(1), 0)
        self.assertAlmostEqual(c.tailSheetSymmetricValues.getCoefficient(2), 1)
        self.assertAlmostEqual(c.tailSheetOddValues.getCoefficient(1, 1), 2)
        self.assertAlmostEqual(c.tailSheetOddValues.getCoefficient(1, 2), 5)
        self.assertAlmostEqual(c.tailSheetOddValues.getCoefficient(2, 1), 3)
        self.assertAlmostEqual(c.tailSheetOddValues.getCoefficient(2, 2), 6)
        self.assertAlmostEqual(c.tailSheetOddValues.getCoefficient(3, 1), 4)
        self.assertAlmostEqual(c.tailSheetOddValues.getCoefficient(3, 2), 7)
        self.assertAlmostEqual(c.tailSheetEvenValues.getCoefficient(1, 1), 8)
        self.assertAlmostEqual(c.tailSheetEvenValues.getCoefficient(1, 2), 11)
        self.assertAlmostEqual(c.tailSheetEvenValues.getCoefficient(2, 1), 9)
        self.assertAlmostEqual(c.tailSheetEvenValues.getCoefficient(2, 2), 12)
        self.assertAlmostEqual(c.tailSheetEvenValues.getCoefficient(3, 1), 10)
        self.assertAlmostEqual(c.tailSheetEvenValues.getCoefficient(3, 2), 13)

    def test_getTailSheetSymmetricValues(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertAlmostEqual(
            c.getTailSheetSymmetricValues().getCoefficient(1), 0
        )
        self.assertAlmostEqual(
            c.getTailSheetSymmetricValues().getCoefficient(2), 1
        )

    def test_getTailSheetOddValues(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertAlmostEqual(c.getTailSheetOddValues().getCoefficient(1, 1),
                               2)
        self.assertAlmostEqual(c.getTailSheetOddValues().getCoefficient(1, 2),
                               5)
        self.assertAlmostEqual(c.getTailSheetOddValues().getCoefficient(2, 1),
                               3)
        self.assertAlmostEqual(c.getTailSheetOddValues().getCoefficient(2, 2),
                               6)
        self.assertAlmostEqual(c.getTailSheetOddValues().getCoefficient(3, 1),
                               4)
        self.assertAlmostEqual(c.getTailSheetOddValues().getCoefficient(3, 2),
                               7)

    def test_getTailSheetEvenValues(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertAlmostEqual(c.getTailSheetEvenValues().getCoefficient(1, 1),
                               8)
        self.assertAlmostEqual(c.getTailSheetEvenValues().getCoefficient(1, 2),
                               11)
        self.assertAlmostEqual(c.getTailSheetEvenValues().getCoefficient(2, 1),
                               9)
        self.assertAlmostEqual(c.getTailSheetEvenValues().getCoefficient(2, 2),
                               12)
        self.assertAlmostEqual(c.getTailSheetEvenValues().getCoefficient(3, 1),
                               10)
        self.assertAlmostEqual(c.getTailSheetEvenValues().getCoefficient(3, 2),
                               13)

    def test_getAsSingleExpansion(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        e = c.getAsSingleExpansion()
        for i in range(n):
            self.assertAlmostEqual(e.getCoefficient(i + 1), i)

    def test_getNumAzimuthalExpansions(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertEqual(c.getNumAzimuthalExpansions(), na)

    def test_getNumRadialExpansions(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertEqual(c.getNumRadialExpansions(), nr)

    def test_getNumberOfExpansions(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertEqual(c.getNumberOfExpansions(), n)

    def test_toString(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertEqual(
            c.toString(),
            "TailSheetCoefficients [tailSheetSymmetricValues="
            "ArrayCoefficientExpansion1D [array=[0, 1], "
            "getLowerBoundIndex()=1, getUpperBoundIndex()=2], "
            "tailSheetOddValues=ArrayCoefficientExpansion2D "
            "[data=[[2, 5], [3, 6], [4, 7]], getILowerBoundIndex()=1, "
            "getIUpperBoundIndex()=3, getJLowerBoundIndex()=1, "
            "getJUpperBoundIndex()=2], tailSheetEvenValues="
            "ArrayCoefficientExpansion2D [data=[[8, 11], [9, 12], "
            "[10, 13]], getILowerBoundIndex()=1, getIUpperBoundIndex()=3, "
            "getJLowerBoundIndex()=1, getJUpperBoundIndex()=2], "
            "numAzimuthalExpansions=3, numRadialExpansions=2]"
        )

    def test_hashCode(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertEqual(c.hashCode(), 61044674)

    def test_equals(self):
        nr1 = 2
        na1 = 3
        n1 = nr1 + 2*nr1*na1
        a1 = list(range(n1 + 1))
        c1 = TailSheetCoefficients.createFromArray(a1, na1, nr1)
        nr2 = 2
        na2 = 3
        n2 = nr2 + 2*nr2*na2
        a2 = list(range(n2 + 1))
        c2 = TailSheetCoefficients.createFromArray(a2, na2, nr2)
        nr3 = 3
        na3 = 3
        n3 = nr3 + 2*nr3*na3
        a3 = list(range(n3 + 1))
        c3 = TailSheetCoefficients.createFromArray(a3, na3, nr3)
        self.assertTrue(c1.equals(c2))
        self.assertFalse(c1.equals(c3))


if __name__ == '__main__':
    unittest.main()
