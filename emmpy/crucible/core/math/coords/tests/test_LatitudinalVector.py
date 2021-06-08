import unittest

from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        lv = LatitudinalVector(0.0, 0.1, 0.2)
        self.assertIsNotNone(lv)

    def test_getRadius(self):
        lv = LatitudinalVector(0.0, 0.1, 0.2)
        self.assertAlmostEqual(lv.getRadius(), 0.0)

    def test_getLatitude(self):
        lv = LatitudinalVector(0.0, 0.1, 0.2)
        self.assertAlmostEqual(lv.getLatitude(), 0.1)

    def test_getLongitude(self):
        lv = LatitudinalVector(0.0, 0.1, 0.2)
        self.assertAlmostEqual(lv.getLongitude(), 0.2)


if __name__ == '__main__':
    unittest.main()
