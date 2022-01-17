import unittest

from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class TestTailSheetCoefficients(unittest.TestCase):

    def test___init__(self):
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1
        )
        c = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        self.assertIs(c.tailSheetSymmetricValues, tailSym)
        self.assertIs(c.tailSheetOddValues, tailOdd)
        self.assertIs(c.tailSheetEvenValues, tailEven)

    def test_createUnity(self):
        e = TailSheetCoefficients.createUnity(3, 3)
        self.assertAlmostEqual(e.tailSheetSymmetricValues[1], 1)
        self.assertAlmostEqual(e.tailSheetOddValues[1, 1], 1)
        self.assertAlmostEqual(e.tailSheetEvenValues[1, 1], 1)

    def test_createFromArray(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertAlmostEqual(c.tailSheetSymmetricValues[0], 0)
        self.assertAlmostEqual(c.tailSheetSymmetricValues[1], 1)
        self.assertAlmostEqual(c.tailSheetOddValues[0, 1], 2)
        self.assertAlmostEqual(c.tailSheetOddValues[0, 2], 5)
        self.assertAlmostEqual(c.tailSheetOddValues[1, 1], 3)
        self.assertAlmostEqual(c.tailSheetOddValues[1, 2], 6)
        self.assertAlmostEqual(c.tailSheetOddValues[2, 1], 4)
        self.assertAlmostEqual(c.tailSheetOddValues[2, 2], 7)
        self.assertAlmostEqual(c.tailSheetEvenValues[0, 1], 8)
        self.assertAlmostEqual(c.tailSheetEvenValues[0, 2], 11)
        self.assertAlmostEqual(c.tailSheetEvenValues[1, 1], 9)
        self.assertAlmostEqual(c.tailSheetEvenValues[1, 2], 12)
        self.assertAlmostEqual(c.tailSheetEvenValues[2, 1], 10)
        self.assertAlmostEqual(c.tailSheetEvenValues[2, 2], 13)

    def test_getAsSingleExpansion(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        e = c.getAsSingleExpansion()
        for i in range(n):
            self.assertAlmostEqual(e[i], i)

    def test_getNumberOfExpansions(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        self.assertEqual(c.getNumberOfExpansions(), n)


if __name__ == '__main__':
    unittest.main()
