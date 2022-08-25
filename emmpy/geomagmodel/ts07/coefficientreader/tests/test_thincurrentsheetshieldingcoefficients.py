import unittest

from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
    ThinCurrentSheetShieldingCoefficients
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        na = 3
        nr = 2
        symTail = None
        symTailWave = None
        oddTail = None
        oddTailWave = None
        evenTail = None
        evenTailWave = None
        ThinCurrentSheetShieldingCoefficients(
            na, nr,
            symTail, symTailWave,
            oddTail, oddTailWave,
            evenTail, evenTailWave
        )


if __name__ == '__main__':
    unittest.main()
