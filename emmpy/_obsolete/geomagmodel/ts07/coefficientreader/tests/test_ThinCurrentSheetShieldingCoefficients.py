import unittest

from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)
from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
    ThinCurrentSheetShieldingCoefficients
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )

    def test_getSymmetricTailExpansion(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertTrue(c.getSymmetricTailExpansion(), symTail)

    def test_getSymmetricTailWaveExpansion(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertTrue(c.getSymmetricTailWaveExpansion(), symTailWave)

    def test_getOddTailExpansion(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertTrue(c.getOddTailExpansion(), oddTail)

    def test_getOddTailWaveExpansion(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertTrue(c.getOddTailWaveExpansion(), oddTailWave)

    def test_getEvenTailExpansion(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertTrue(c.getEvenTailExpansion(), evenTail)

    def test_getEvenTailWaveExpansion(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertTrue(c.getEvenTailWaveExpansion(), evenTailWave)

    def test_getNumRadialExpansions(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertEqual(c.getNumRadialExpansions(), nr)

    def test_getNumAzimuthalExpansions(self):
        na = 3
        nr = 2
        symTail = CoefficientExpansion2D()
        symTailWave = CoefficientExpansion1D()
        oddTail = CoefficientExpansion2D()
        oddTailWave = CoefficientExpansion1D()
        evenTail = CoefficientExpansion2D()
        evenTailWave = CoefficientExpansion1D()
        c = ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )
        self.assertEqual(c.getNumAzimuthalExpansions(), na)


if __name__ == '__main__':
    unittest.main()
