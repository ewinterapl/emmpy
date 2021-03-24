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

    def test_toString(self):
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
        self.assertEqual(
            c.toString(),
            "Ts07EquatorialLinearCoefficients [coeffs=TailSheetCoefficients "
            "[tailSheetSymmetricValues=ArrayCoefficientExpansion1D "
            "[array=[0, 1, 2, 3], getLowerBoundIndex()=1, "
            "getUpperBoundIndex()=4], tailSheetOddValues="
            "ArrayCoefficientExpansion2D [data=[[0, 1, 2, 3], [4, 5, 6, 7], "
            "[8, 9, 0, 1], [2, 3, 4, 5]], getILowerBoundIndex()=1, "
            "getIUpperBoundIndex()=4, getJLowerBoundIndex()=1, "
            "getJUpperBoundIndex()=4], tailSheetEvenValues="
            "ArrayCoefficientExpansion2D [data=[[0, 1, 2, 3], [4, 5, 6, 7], "
            "[8, 9, 0, 1], [2, 3, 4, 5]], getILowerBoundIndex()=1, "
            "getIUpperBoundIndex()=4, getJLowerBoundIndex()=1, "
            "getJUpperBoundIndex()=4], numAzimuthalExpansions=4, "
            "numRadialExpansions=4], pdynDependentCoeffs=TailSheetCoefficients "
            "[tailSheetSymmetricValues=ArrayCoefficientExpansion1D "
            "[array=[0, 1, 2, 3], getLowerBoundIndex()=1, "
            "getUpperBoundIndex()=4], tailSheetOddValues="
            "ArrayCoefficientExpansion2D [data=[[0, 1, 2, 3], [4, 5, 6, 7], "
            "[8, 9, 0, 1], [2, 3, 4, 5]], getILowerBoundIndex()=1, "
            "getIUpperBoundIndex()=4, getJLowerBoundIndex()=1, "
            "getJUpperBoundIndex()=4], tailSheetEvenValues="
            "ArrayCoefficientExpansion2D [data=[[0, 1, 2, 3], [4, 5, 6, 7], "
            "[8, 9, 0, 1], [2, 3, 4, 5]], getILowerBoundIndex()=1, "
            "getIUpperBoundIndex()=4, getJLowerBoundIndex()=1, "
            "getJUpperBoundIndex()=4], numAzimuthalExpansions=4, "
            "numRadialExpansions=4], numAzimuthalExpansions=4, "
            "numRadialExpansions=4]"
        )

    def test_hashCode(self):
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
        self.assertEqual(c.hashCode(), 59670751393)

    def test_equals(self):
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
        c1 = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        c2 = Ts07EquatorialLinearCoefficients.create(
            sym, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        sym2 = ArrayCoefficientExpansion1D([1, 1, 2, 3], 1)
        c3 = Ts07EquatorialLinearCoefficients.create(
            sym2, symPdynDependent,
            aOdd, aOddPdynDependent,
            aEven, aEvenPdynDependent,
            na, nr
        )
        self.assertTrue(c1.equals(c2))
        self.assertFalse(c1.equals(c3))


if __name__ == '__main__':
    unittest.main()
