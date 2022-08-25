import unittest

from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class TestTailSheetCoefficients(unittest.TestCase):

    def test___init__(self):
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
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
        self.assertAlmostEqual(c.tailSheetOddValues[0, 0], 2)
        self.assertAlmostEqual(c.tailSheetOddValues[1, 0], 3)
        self.assertAlmostEqual(c.tailSheetOddValues[2, 0], 4)
        self.assertAlmostEqual(c.tailSheetOddValues[0, 1], 5)
        self.assertAlmostEqual(c.tailSheetOddValues[1, 1], 6)
        self.assertAlmostEqual(c.tailSheetOddValues[2, 1], 7)
        self.assertAlmostEqual(c.tailSheetEvenValues[0, 0], 8)
        self.assertAlmostEqual(c.tailSheetEvenValues[1, 0], 9)
        self.assertAlmostEqual(c.tailSheetEvenValues[2, 0], 10)
        self.assertAlmostEqual(c.tailSheetEvenValues[0, 1], 11)
        self.assertAlmostEqual(c.tailSheetEvenValues[1, 1], 12)
        self.assertAlmostEqual(c.tailSheetEvenValues[2, 1], 13)

    def test_getAsSingleExpansion(self):
        nr = 2
        na = 3
        n = nr + 2*nr*na
        a = list(range(n + 1))
        c = TailSheetCoefficients.createFromArray(a, na, nr)
        e = c.getAsSingleExpansion()
        for i in range(n):
            self.assertAlmostEqual(e[i], i)


if __name__ == '__main__':
    unittest.main()
