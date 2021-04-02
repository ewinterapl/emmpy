import unittest

from emmpy.crucible.core.math.coords.polarvector import PolarVector


class TestPolarVector(unittest.TestCase):

    def test___init__(self):
        pv = PolarVector(0.0, 0.1)
        self.assertIsNotNone(pv)

    def test_getRadius(self):
        pv = PolarVector(0.0, 0.1)
        self.assertAlmostEqual(pv.getRadius(), 0.0)

    def test_getAngle(self):
        pv = PolarVector(0.0, 0.1)
        self.assertAlmostEqual(pv.getAngle(), 0.1)

    def test_toString(self):
        pv = PolarVector(0.0, 0.1)
        self.assertEqual(
            pv.toString(), "PolarVector [radius: 0.0, angle: 0.1]"
        )


if __name__ == '__main__':
    unittest.main()
