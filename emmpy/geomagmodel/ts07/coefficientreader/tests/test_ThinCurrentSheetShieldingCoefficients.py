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


if __name__ == '__main__':
    unittest.main()
