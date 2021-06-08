import unittest

from emmpy.crucible.core.math.coords.polarvector import PolarVector


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        pv = PolarVector(0.0, 0.1)
        self.assertIsNotNone(pv)

    def test_getRadius(self):
        pv = PolarVector(0.0, 0.1)
        self.assertAlmostEqual(pv.getRadius(), 0.0)

    def test_getAngle(self):
        pv = PolarVector(0.0, 0.1)
        self.assertAlmostEqual(pv.getAngle(), 0.1)


if __name__ == '__main__':
    unittest.main()
