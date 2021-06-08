import unittest

from emmpy.geomagmodel.ts07.coefficientreader.ts07equatoriallinearcoefficients import (
    Ts07EquatorialLinearCoefficients
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
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
        c = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )
        self.assertTrue(c.coeffs is coeffs)
        self.assertTrue(c.pdynDependentCoeffs is pdynDependentCoeffs)
        self.assertEqual(c.numAzimuthalExpansions, na)
        self.assertEqual(c.numRadialExpansions, nr)

    def test_create(self):
        sym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        symPdynDependent = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        aOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aOddPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEvenPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        na = 4
        nr = 4
        c = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        self.assertIsNotNone(c)

    def test_getNumAzimuthalExpansions(self):
        sym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        symPdynDependent = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        aOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aOddPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEvenPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        na = 4
        nr = 4
        c = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        self.assertEqual(c.getNumAzimuthalExpansions(), na)

    def test_getNumRadialExpansions(self):
        sym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        symPdynDependent = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        aOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aOddPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEvenPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        na = 4
        nr = 4
        c = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        self.assertEqual(c.getNumRadialExpansions(), nr)

    def test_getCoeffs(self):
        sym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        symPdynDependent = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        aOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aOddPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEvenPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        na = 4
        nr = 4
        c = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        self.assertIsNotNone(c.getCoeffs())

    def test_getPdynDependentCoeffs(self):
        sym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        symPdynDependent = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        aOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aOddPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEvenPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        na = 4
        nr = 4
        c = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        self.assertIsNotNone(c.getPdynDependentCoeffs())

    def test_getPdynScaledCoeffs(self):
        sym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        symPdynDependent = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        aOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aOddPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        aEvenPdynDependent = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        na = 4
        nr = 4
        c = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        c2 = c.getPdynScaledCoeffs(2)
        self.assertIsNotNone(c2)


if __name__ == '__main__':
    unittest.main()
