import unittest

from emmpy.geomagmodel.ts07.coefficientreader.facregion import (
    REGION_1, REGION_2
)
from emmpy.geomagmodel.ts07.modeling.fieldaligned.facconfigurationoptions import (
    FacConfigurationOptions
)
from emmpy.magmodel.math.trigparity import EVEN


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        fco = FacConfigurationOptions(
            0.1, REGION_1, 2, EVEN, 4.4, 5.5, True, False
        )
        self.assertAlmostEqual(fco.amplitudeScaling, 0.1)
        self.assertEqual(fco.region, REGION_1)
        self.assertEqual(fco.mode, 2)
        self.assertEqual(fco.trigParity, EVEN)
        self.assertAlmostEqual(fco.theta0, 4.4)
        self.assertAlmostEqual(fco.deltaTheta, 5.5)
        self.assertTrue(fco.smoothed)
        self.assertFalse(fco.shielded)


if __name__ == '__main__':
    unittest.main()
