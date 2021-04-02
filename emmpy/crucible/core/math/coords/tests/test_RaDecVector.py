import unittest

from emmpy.crucible.core.math.coords.radecvector import RaDecVector


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        rdv = RaDecVector(0.1, 0.2, 0.3)
        self.assertIsNotNone(rdv)

    def test_getRadius(self):
        rdv = RaDecVector(0.1, 0.2, 0.3)
        self.assertAlmostEqual(rdv.getRadius(), 0.1)

    def test_getRightAscension(self):
        rdv = RaDecVector(0.1, 0.2, 0.3)
        self.assertAlmostEqual(rdv.getRightAscension(), 0.2)

    def test_getDeclination(self):
        rdv = RaDecVector(0.1, 0.2, 0.3)
        self.assertAlmostEqual(rdv.getDeclination(), 0.3)

    def test_toString(self):
        rdv = RaDecVector(0.1, 0.2, 0.3)
        self.assertEqual(
            rdv.toString(),
            "RaDecVector [radius: 0.1, rightAscension: 0.2, declination: 0.3]"
        )


if __name__ == '__main__':
    unittest.main()
