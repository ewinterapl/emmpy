import unittest

from emmpy.geomagmodel.ts07.coefficientreader.facregion import FacRegion
from emmpy.geomagmodel.ts07.modeling.fieldaligned.facconfigurationoptions import (
    FacConfigurationOptions
)
from emmpy.magmodel.core.math.trigparity import EVEN


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.amplitudeScaling, 0.1)
        self.assertEqual(fco.region, FacRegion.REGION_1)
        self.assertEqual(fco.mode, 2)
        self.assertEqual(fco.trigParity, EVEN)
        self.assertAlmostEqual(fco.theta0, 4.4)
        self.assertAlmostEqual(fco.deltaTheta, 5.5)
        self.assertTrue(fco.smoothed)
        self.assertFalse(fco.shielded)

    def test_getAmplitudeScaling(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.getAmplitudeScaling(), 0.1)

    def test_getRegion(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertEqual(fco.getRegion(), FacRegion.REGION_1)

    def test_getMode(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertEqual(fco.getMode(), 2)

    def test_getTheta0(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.getTheta0(), 4.4)

    def test_getDeltaTheta(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.getDeltaTheta(), 5.5)

    def test_isSmoothed(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertTrue(fco.isSmoothed())

    def test_isShielded(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertFalse(fco.isShielded())


if __name__ == '__main__':
    unittest.main()
