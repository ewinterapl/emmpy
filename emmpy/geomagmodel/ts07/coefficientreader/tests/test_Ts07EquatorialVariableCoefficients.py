import unittest

from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
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

    def test_getCurrThicks(self):
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
        self.assertAlmostEqual(c.getCurrThicks(), [1])

    def test_getHingeDistance(self):
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
        self.assertAlmostEqual(c.getHingeDistance(), 1)

    def test_getWarpingParam(self):
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
        self.assertAlmostEqual(c.getWarpingParam(), 2)

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
        self.assertTrue(c.getLinearCoeffs()[0].equals(ts07elc))

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

    def test_toString(self):
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
        # self.assertEqual(
        #     c.toString(),
        #     "Ts07EquatorialVariableCoefficients [currThicks=[1], "
        #     "hingeDist=1, warpingParam=2, twistParam=3, equatorialLinearCoeffs"
        #     "=Ts07EquatorialLinearCoefficients [coeffs=TailSheetCoefficients "
        #     "[tailSheetSymmetricValues=ArrayCoefficientExpansion1D [array=[0, "
        #     "1, 2, 3], getLowerBoundIndex()=1, getUpperBoundIndex()=4], "
        #     "tailSheetOddValues=ArrayCoefficientExpansion2D [data=[[0, 1, 2, "
        #     "3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], "
        #     "getILowerBoundIndex()=1, getIUpperBoundIndex()=4, "
        #     "getJLowerBoundIndex()=1, getJUpperBoundIndex()=4], "
        #     "tailSheetEvenValues=ArrayCoefficientExpansion2D [data=[[0, 1, 2, "
        #     "3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], "
        #     "getILowerBoundIndex()=1, getIUpperBoundIndex()=4, "
        #     "getJLowerBoundIndex()=1, getJUpperBoundIndex()=4], "
        #     "numAzimuthalExpansions=4, numRadialExpansions=4], "
        #     "pdynDependentCoeffs=TailSheetCoefficients "
        #     "[tailSheetSymmetricValues=ArrayCoefficientExpansion1D [array=[0, "
        #     "1, 2, 3], getLowerBoundIndex()=1, getUpperBoundIndex()=4], "
        #     "tailSheetOddValues=ArrayCoefficientExpansion2D [data=[[0, 1, 2, "
        #     "3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], "
        #     "getILowerBoundIndex()=1, getIUpperBoundIndex()=4, "
        #     "getJLowerBoundIndex()=1, getJUpperBoundIndex()=4], "
        #     "tailSheetEvenValues=ArrayCoefficientExpansion2D [data=[[0, 1, 2, "
        #     "3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], "
        #     "getILowerBoundIndex()=1, getIUpperBoundIndex()=4, "
        #     "getJLowerBoundIndex()=1, getJUpperBoundIndex()=4], "
        #     "numAzimuthalExpansions=4, numRadialExpansions=4], "
        #     "numAzimuthalExpansions=3, numRadialExpansions=2]]"
        # )

    def test_hashCode(self):
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
        self.assertEqual(c.hashCode(), 1058323784831)

    def test_equals(self):
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
        c1 = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        c2 = Ts07EquatorialVariableCoefficients(1, 1, 2, 3, [ts07elc])
        c3 = Ts07EquatorialVariableCoefficients([1, 1], 1, 2, 3,
                                                [ts07elc, ts07elc])
        self.assertTrue(c1.equals(c2))
        self.assertFalse(c1.equals(c3))


if __name__ == '__main__':
    unittest.main()
