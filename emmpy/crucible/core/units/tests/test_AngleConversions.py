import unittest

from emmpy.crucible.core.units.angleconversions import AngleConversions

class TestAngleConversions(unittest.TestCase):

    def test_convertHourAngle(self):
        self.assertAlmostEqual(AngleConversions.convertHourAngle(0, 0, 0.0), 0)

    def test_convertSexagesimal(self):
        self.assertAlmostEqual(AngleConversions.convertSexagesimal(0, 0, 0.0), 0)

if __name__ == '__main__':
    unittest.main()
