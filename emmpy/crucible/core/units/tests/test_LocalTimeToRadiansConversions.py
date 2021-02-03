import unittest

from emmpy.crucible.core.units.localtimetoradiansconversions import LocalTimeToRadiansConversions
from emmpy.crucible.core.math.cruciblemath import CrucibleMath

class TestLocalTimeToRadiansConversions(unittest.TestCase):

    def test_localtimeHoursToRadians(self):
        self.assertAlmostEqual(LocalTimeToRadiansConversions.localtimeHoursToRadians(0), -CrucibleMath.PI)

    def test_radiansToLocaltime(self):
        self.assertAlmostEqual(LocalTimeToRadiansConversions.radiansToLocaltime(0), 12)

if __name__ == '__main__':
    unittest.main()
