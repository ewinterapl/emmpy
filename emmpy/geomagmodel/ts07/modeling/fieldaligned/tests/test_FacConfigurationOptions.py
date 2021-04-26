import unittest

from emmpy.geomagmodel.ts07.coefficientreader.facregion import FacRegion
from emmpy.geomagmodel.ts07.modeling.fieldaligned.facconfigurationoptions import (
    FacConfigurationOptions
)
from emmpy.magmodel.core.math.trigparity import TrigParity


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.amplitudeScaling, 0.1)
        self.assertEqual(fco.region, FacRegion.REGION_1)
        self.assertEqual(fco.mode, 2)
        self.assertEqual(fco.trigParity, TrigParity.EVEN)
        self.assertAlmostEqual(fco.theta0, 4.4)
        self.assertAlmostEqual(fco.deltaTheta, 5.5)
        self.assertTrue(fco.smoothed)
        self.assertFalse(fco.shielded)

    def test_getAmplitudeScaling(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.getAmplitudeScaling(), 0.1)

    def test_getRegion(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertEqual(fco.getRegion(), FacRegion.REGION_1)

    def test_getMode(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertEqual(fco.getMode(), 2)

    def test_getTrigParity(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertEqual(fco.getTrigParity(), TrigParity.EVEN)

    def test_getTheta0(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.getTheta0(), 4.4)

    def test_getDeltaTheta(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.getDeltaTheta(), 5.5)

    def test_isSmoothed(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertTrue(fco.isSmoothed())

    def test_isShielded(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertFalse(fco.isShielded())

    def test_toString(self):
        # UNABLE TO TEST SINCE SOME SUBOBJECTS DO NOT HAVE toString().
        pass
        # fco = FacConfigurationOptions(
        #     0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True,False
        # )
        # self.assertEqual(
        #     fco.toString(),
        #     "FacConfigurationOptions [amplitudeScaling=0.1, region=1,mode=2,"
        #     " trigParity=3, theta0=4, deltaTheta=5.0, smoothed=True, "
        #     "shielded=False]"
        # )

    def test_hashCode(self):
        fco = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        # TEMPORARY - NEED trigParity.hashCode()
        self.assertEqual(fco.hashCode(), 951262734975931584)

    def test_equals(self):
        fco1 = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        fco2 = FacConfigurationOptions(
            0.1, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        fco3 = FacConfigurationOptions(
            0.2, FacRegion.REGION_1, 2, TrigParity.EVEN, 4.4, 5.5, True, False
        )
        self.assertTrue(fco1.equals(fco2))
        self.assertFalse(fco1.equals(fco3))


if __name__ == '__main__':
    unittest.main()
