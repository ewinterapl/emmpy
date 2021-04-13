import unittest

from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        sv = SphericalVector(0.1, 0.2, 0.3)
        self.assertIsNotNone(sv)

    def test_getRadius(self):
        sv = SphericalVector(0.1, 0.2, 0.3)
        self.assertAlmostEqual(sv.getRadius(), 0.1)

    def test_getColatitude(self):
        sv = SphericalVector(0.1, 0.2, 0.3)
        self.assertAlmostEqual(sv.getColatitude(), 0.2)

    def test_getLongitude(self):
        sv = SphericalVector(0.1, 0.2, 0.3)
        self.assertAlmostEqual(sv.getLongitude(), 0.3)

    def test_toString(self):
        sv = SphericalVector(0.1, 0.2, 0.3)
        self.assertEqual(
            sv.toString(),
            "SphericalVector [radius: 0.1, colatitude: 0.2, longitude: 0.3]"
        )


if __name__ == '__main__':
    unittest.main()
