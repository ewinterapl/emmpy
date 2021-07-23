import unittest

from emmpy.crucible.core.math.coords.latitudinalcoordconverter import (
    LatitudinalCoordConverter
)
from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        lcc = LatitudinalCoordConverter()
        self.assertIsNotNone(lcc)

    def test_toCoordinate(self):
        lcc = LatitudinalCoordConverter()
        cart = VectorIJK(1, 2, 3)
        latv = lcc.toCoordinate(cart)
        self.assertAlmostEqual(latv.getI(), 3.741657386773941)
        self.assertAlmostEqual(latv.getJ(), 0.9302740141154721)
        self.assertAlmostEqual(latv.getK(), 1.1071487177940904)

    def test_toCartesian(self):
        lcc = LatitudinalCoordConverter()
        latv = LatitudinalVector(
            3.741657386773941, 0.9302740141154721, 1.1071487177940904
        )
        cart = lcc.toCartesian(latv)
        self.assertAlmostEqual(cart.i, 1)
        self.assertAlmostEqual(cart.getJ(), 2)
        self.assertAlmostEqual(cart.getK(), 3)


if __name__ == '__main__':
    unittest.main()
