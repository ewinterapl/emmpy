import unittest

from emmpy.crucible.crust.surfaces.ellipsoidalintersectioncomputer import (
    EllipsoidalIntersectionComputer
)


class TestBuilder(unittest.TestCase):

    def test__init__(self):
        (a, b, c) = (1.2, 3.4, 5.6)
        eic = EllipsoidalIntersectionComputer(a, b, c)
        self.assertIsNotNone(eic)
        self.assertAlmostEqual(eic.a, a)
        self.assertAlmostEqual(eic.b, b)
        self.assertAlmostEqual(eic.c, c)

    def test_scaleToUnit(self):
        pass

    def test_invertScaleToUnit(self):
        pass

    def test_intersects(self):
        pass

    def test_compute(self):
        pass


if __name__ == '__main__':
    unittest.main()
