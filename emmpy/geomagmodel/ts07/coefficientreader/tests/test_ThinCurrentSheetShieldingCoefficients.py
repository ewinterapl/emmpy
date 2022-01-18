import unittest

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
        symTailWave = None
        oddTail = CoefficientExpansion2D()
        oddTailWave = None
        evenTail = CoefficientExpansion2D()
        evenTailWave = None
        ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )


if __name__ == '__main__':
    unittest.main()
