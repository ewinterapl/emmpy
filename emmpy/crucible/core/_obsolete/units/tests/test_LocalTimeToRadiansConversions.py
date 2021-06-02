import unittest

from math import pi

from emmpy.crucible.core.units.localtimetoradiansconversions import (
    LocalTimeToRadiansConversions
)


class TestLocalTimeToRadiansConversions(unittest.TestCase):

    def test_localtimeHoursToRadians(self):
        self.assertAlmostEqual(
            LocalTimeToRadiansConversions.localtimeHoursToRadians(0), -pi)

    def test_radiansToLocaltime(self):
        self.assertAlmostEqual(
            LocalTimeToRadiansConversions.radiansToLocaltime(0), 12)


if __name__ == '__main__':
    unittest.main()
