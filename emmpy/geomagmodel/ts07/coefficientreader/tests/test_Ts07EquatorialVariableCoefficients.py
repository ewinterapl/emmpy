import unittest

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatoriallinearcoefficients import (
    Ts07EquatorialLinearCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients import (
    Ts07EquatorialVariableCoefficients
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        coeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        pdynDependentCoeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        na = 3
        nr = 2
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )
        # Single thickness
        c = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        self.assertIsNotNone(c)
        # List of thicknesses
        c = Ts07EquatorialVariableCoefficients(
            [1, 2], 1, 2, 3, [ts07elc, ts07elc]
        )
        self.assertIsNotNone(c)

    def test_getTwistParam(self):
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        coeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        pdynDependentCoeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        na = 3
        nr = 2
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )
        c = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        self.assertAlmostEqual(c.getTwistParam(), 3)

    def test_getLinearCoeffs(self):
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        coeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        pdynDependentCoeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        na = 3
        nr = 2
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )
        c = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        # self.assertTrue(c.getLinearCoeffs()[0].equals(ts07elc))

    def test_getTotalNumberOfParameters(self):
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        coeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        pdynDependentCoeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        na = 3
        nr = 2
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )
        c = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        np = 2*(nr + 2*nr*na) + 1 + 3
        self.assertEqual(c.getTotalNumberOfParameters(), np)

    def test_getTotalNumberOfLinearParameters(self):
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        coeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        pdynDependentCoeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        na = 3
        nr = 2
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )
        c = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        np = 2*(nr + 2*nr*na)
        self.assertEqual(c.getTotalNumberOfLinearParameters(), np)

    def test_getTotalNumberOfNonLinearParameters(self):
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        coeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        pdynDependentCoeffs = TailSheetCoefficients(tailSym, tailOdd, tailEven)
        na = 3
        nr = 2
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )
        c = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        np = 4
        self.assertEqual(c.getTotalNumberOfNonLinearParameters(), np)


if __name__ == '__main__':
    unittest.main()
