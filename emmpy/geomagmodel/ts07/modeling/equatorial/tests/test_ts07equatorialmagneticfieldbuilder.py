import unittest

from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
    ThinCurrentSheetShieldingCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatoriallinearcoefficients import (
    Ts07EquatorialLinearCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients import (
    Ts07EquatorialVariableCoefficients
)
from emmpy.geomagmodel.ts07.modeling.equatorial.ts07equatorialmagneticfieldbuilder import (
    Ts07EquatorialMagneticFieldBuilder
)
from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tsc1 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the pressure-dependent coefficients needed by the equatorial
        # linear coefficients.
        tsc2 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the equatorial linear coefficients for the equatorial variable
        # coefficients.
        coeffs = tsc1
        pdynDependentCoeffs = tsc2
        na = 4
        nr = 4
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )

        # Build the TS07 equatorial variable coefficients object needed by the
        # builder.
        currThicks = 1.6
        hingeDist = 1.7
        warpingParam = 1.8
        twistParam = 1.9
        equatorialLinearCoeffs = [ts07elc]
        ts07evc = Ts07EquatorialVariableCoefficients(
            currThicks, hingeDist, warpingParam, twistParam,
            equatorialLinearCoeffs
        )

        # Build the thin current sheet shielding coefficients object needed by
        # the builder object.
        symTail = None
        symTailWave = None
        oddTail = None
        oddTailWave = None
        evenTail = None
        evenTailWave = None
        tcssc = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )

        # Build the builder.
        dipoleTiltAngle = 0.75
        dynamicPressure = 1.5
        coeffs = ts07evc
        tailLength = 2.5
        shieldingCoeffs = tcssc
        b = Ts07EquatorialMagneticFieldBuilder(
            dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
            shieldingCoeffs
        )
        self.assertIsNotNone(b)

    def test_withEquatorialShielding(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tsc1 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the pressure-dependent coefficients needed by the equatorial
        # linear coefficients.
        tsc2 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the equatorial linear coefficients for the equatorial variable
        # coefficients.
        coeffs = tsc1
        pdynDependentCoeffs = tsc2
        na = 4
        nr = 4
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )

        # Build the TS07 equatorial variable coefficients object needed by the
        # builder.
        currThicks = 1.6
        hingeDist = 1.7
        warpingParam = 1.8
        twistParam = 1.9
        equatorialLinearCoeffs = [ts07elc]
        ts07evc = Ts07EquatorialVariableCoefficients(
            currThicks, hingeDist, warpingParam, twistParam,
            equatorialLinearCoeffs
        )

        # Build the thin current sheet shielding coefficients object needed by
        # the builder object.
        symTail = None
        symTailWave = None
        oddTail = None
        oddTailWave = None
        evenTail = None
        evenTailWave = None
        tcssc = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )

        # Build the builder.
        dipoleTiltAngle = 0.75
        dynamicPressure = 1.5
        coeffs = ts07evc
        tailLength = 2.5
        shieldingCoeffs = tcssc
        b = Ts07EquatorialMagneticFieldBuilder(
            dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
            shieldingCoeffs
        )
        self.assertIs(b.withEquatorialShielding(), b)

    def test_withoutEquatorialShielding(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tsc1 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the pressure-dependent coefficients needed by the equatorial
        # linear coefficients.
        tsc2 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the equatorial linear coefficients for the equatorial variable
        # coefficients.
        coeffs = tsc1
        pdynDependentCoeffs = tsc2
        na = 4
        nr = 4
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )

        # Build the TS07 equatorial variable coefficients object needed by the
        # builder.
        currThicks = 1.6
        hingeDist = 1.7
        warpingParam = 1.8
        twistParam = 1.9
        equatorialLinearCoeffs = [ts07elc]
        ts07evc = Ts07EquatorialVariableCoefficients(
            currThicks, hingeDist, warpingParam, twistParam,
            equatorialLinearCoeffs
        )

        # Build the thin current sheet shielding coefficients object needed by
        # the builder object.
        symTail = None
        symTailWave = None
        oddTail = None
        oddTailWave = None
        evenTail = None
        evenTailWave = None
        tcssc = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )

        # Build the builder.
        dipoleTiltAngle = 0.75
        dynamicPressure = 1.5
        coeffs = ts07evc
        tailLength = 2.5
        shieldingCoeffs = tcssc
        b = Ts07EquatorialMagneticFieldBuilder(
            dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
            shieldingCoeffs
        )
        self.assertIs(b.withoutEquatorialShielding(), b)

    def test_build(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ScalarExpansion1D([0, 1, 2, 3])
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]
        )
        tsc1 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the pressure-dependent coefficients needed by the equatorial
        # linear coefficients.
        tsc2 = TailSheetCoefficients(tailSym, tailOdd, tailEven)

        # Build the equatorial linear coefficients for the equatorial variable
        # coefficients.
        coeffs = tsc1
        pdynDependentCoeffs = tsc2
        na = 4
        nr = 4
        ts07elc = Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, na, nr
        )

        # Build the TS07 equatorial variable coefficients object needed by the
        # builder.
        currThicks = 1.6
        hingeDist = 1.7
        warpingParam = 1.8
        twistParam = 1.9
        equatorialLinearCoeffs = [ts07elc]
        ts07evc = Ts07EquatorialVariableCoefficients(
            currThicks, hingeDist, warpingParam, twistParam,
            equatorialLinearCoeffs
        )

        # Build the thin current sheet shielding coefficients object needed by
        # the builder object.
        symTail = None
        symTailWave = None
        oddTail = None
        oddTailWave = None
        evenTail = None
        evenTailWave = None
        tcssc = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )

        # Build the builder.
        dipoleTiltAngle = 0.75
        dynamicPressure = 1.5
        coeffs = ts07evc
        tailLength = 2.5
        shieldingCoeffs = tcssc
        b = Ts07EquatorialMagneticFieldBuilder(
            dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
            shieldingCoeffs
        )

        # Build it.
        v = b.build()


if __name__ == '__main__':
    unittest.main()
