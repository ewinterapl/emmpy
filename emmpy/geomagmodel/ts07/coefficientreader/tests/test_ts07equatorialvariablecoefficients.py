import unittest

from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatoriallinearcoefficients import (
    Ts07EquatorialLinearCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients import (
    Ts07EquatorialVariableCoefficients
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
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

    def test_getTotalNumberOfParameters(self):
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
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
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
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
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
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
