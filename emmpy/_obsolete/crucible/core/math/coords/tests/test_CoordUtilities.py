from math import pi
import unittest

from emmpy.crucible.core.math.coords.coordutilities import (
    toLatitude,
    toColatitude
)


class TestBuilder(unittest.TestCase):

    def test_toLatitude(self):
        self.assertAlmostEqual(toLatitude(-1), pi/2 + 1)
        self.assertAlmostEqual(toLatitude(0), pi/2)
        self.assertAlmostEqual(toLatitude(pi/4), pi/4)
        self.assertAlmostEqual(toLatitude(pi/3), pi/6)
        self.assertAlmostEqual(toLatitude(1), pi/2 - 1)
        self.assertAlmostEqual(toLatitude(pi/2), 0)
        self.assertAlmostEqual(toLatitude(3), pi/2 - 3)

    def test_toColatitude(self):
        self.assertAlmostEqual(toColatitude(-1), pi/2 + 1)
        self.assertAlmostEqual(toColatitude(0), pi/2)
        self.assertAlmostEqual(toColatitude(pi/4), pi/4)
        self.assertAlmostEqual(toColatitude(pi/3), pi/6)
        self.assertAlmostEqual(toColatitude(1), pi/2 - 1)
        self.assertAlmostEqual(toColatitude(pi/2), 0)
        self.assertAlmostEqual(toColatitude(3), pi/2 - 3)


if __name__ == '__main__':
    unittest.main()
