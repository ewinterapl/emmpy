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
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
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
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
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

    def test_withAlbertBessel(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
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
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
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
        self.assertIs(b.withAlbertBessel(), b)

    def test_set_withTA15deformation(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
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
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
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
        self.assertIs(b.set_withTA15deformation(0.5), b)

    def test_withEquatorialShielding(self):

        # Build the tail sheet coefficients for the equatorial linear
        # coefficients.
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
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
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
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
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
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
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
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
        tailSym = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        tailOdd = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
        )
        tailEven = ArrayCoefficientExpansion2D(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]], 1, 1
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
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
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