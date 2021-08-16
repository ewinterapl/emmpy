import unittest

from emmpy.crucible.core.math.coords.cylindricalcoordconverter import (
    CylindricalCoordConverter
)
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        ccc = CylindricalCoordConverter()
        self.assertIsNotNone(ccc)

    def test_toCoordinate(self):
        ccc = CylindricalCoordConverter()
        cart = VectorIJK(1, 2, 3)
        cyl = ccc.toCoordinate(cart)
        self.assertAlmostEqual(cyl.rho, 2.2360679774998)
        self.assertAlmostEqual(cyl.phi, 1.1071487177941)
        self.assertAlmostEqual(cyl.z, 3)

    def test_toCartesian(self):
        ccc = CylindricalCoordConverter()
        cyl = CylindricalVector(1, 2, 3)
        cart = ccc.toCartesian(cyl)
        self.assertAlmostEqual(cart.i, -0.4161468365)
        self.assertAlmostEqual(cart.j, 0.9092974268)
        self.assertAlmostEqual(cart.k, 3)


if __name__ == '__main__':
    unittest.main()
