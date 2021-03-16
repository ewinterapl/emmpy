import unittest

from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
    ThinCurrentSheetShieldingCoefficients
)
from emmpy.geomagmodel.ts07.modeling.equatorial.ts07equtorialmagneticfieldbuilder import (
    Ts07EquatorialMagneticFieldBuilder
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients import (
    Ts07EquatorialVariableCoefficients
)


class TestTs07EquatorialMagneticFieldBuilder(unittest.TestCase):

    def test___init__(self):
        b = Ts07EquatorialMagneticFieldBuilder(
            0, 0, Ts07EquatorialVariableCoefficients(),
            0, ThinCurrentSheetShieldingCoefficients())


if __name__ == '__main__':
    unittest.main()
