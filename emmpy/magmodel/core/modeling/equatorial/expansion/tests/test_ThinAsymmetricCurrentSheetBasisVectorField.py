import unittest

from emmpy.geomagmodel.ts07.modeling.equatorial.currentsheethalfthicknesses import (
    CurrentSheetHalfThicknesses
)
from emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield import (
    ThinAsymmetricCurrentSheetBasisVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        pass

    def test_createUnity(self):
        tailLength = 20.0
        currSheetThick = 2.3
        currentSheetHalfThickness = (
            CurrentSheetHalfThicknesses.createConstant(currSheetThick)
        )
        numAzimuthalExpansions = 4
        numRadialExpansions = 5
        bessel = None
        tacsbvf = ThinAsymmetricCurrentSheetBasisVectorField.createUnity(
            tailLength, currentSheetHalfThickness, numAzimuthalExpansions,
            numRadialExpansions, bessel
        )
        self.assertIsNotNone(tacsbvf)
        self.assertAlmostEqual(
            tacsbvf.numAzimuthalExpansions, numAzimuthalExpansions
        )
        self.assertAlmostEqual(
            tacsbvf.numRadialExpansions, numRadialExpansions
        )
        self.assertAlmostEqual(tacsbvf.tailLength, tailLength)
        self.assertIsNone(tacsbvf.bessel)


if __name__ == '__main__':
    unittest.main()
