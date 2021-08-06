import unittest

from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        CylindricalVector(1.1, 2.2, 3.3)

    # def test_getCylindricalRadius(self):
    #     cv = CylindricalVector(1.1, 2.2, 3.3)
    #     self.assertAlmostEqual(cv.getCylindricalRadius(), 1.1)

    def test_getLongitude(self):
        cv = CylindricalVector(1.1, 2.2, 3.3)
        self.assertAlmostEqual(cv.getLongitude(), 2.2)

    def test_getHeight(self):
        cv = CylindricalVector(1.1, 2.2, 3.3)
        self.assertAlmostEqual(cv.getHeight(), 3.3)


if __name__ == '__main__':
    unittest.main()
