import unittest

from emmpy.crucible.core.math.coords.radeccoordconverter import (
    RaDecCoordConverter
)
from emmpy.crucible.core.math.coords.radecvector import (
    RaDecVector
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        rdcc = RaDecCoordConverter()
        self.assertIsNotNone(rdcc)

    def test_toCoordinate(self):
        rdcc = RaDecCoordConverter()
        cartesian = VectorIJK(1, 2, 3)
        radv = rdcc.toCoordinate(cartesian)
        self.assertAlmostEqual(radv.getRadius(), 3.741657386773941)
        self.assertAlmostEqual(radv.getRightAscension(), 1.1071487177940904)
        self.assertAlmostEqual(radv.getDeclination(), 0.9302740141154721)

    def test_toCartesian(self):
        rdcc = RaDecCoordConverter()
        radv = RaDecVector(
            3.741657386773941, 1.1071487177940904, 0.9302740141154721
        )
        cartesian = rdcc.toCartesian(radv)
        self.assertAlmostEqual(cartesian.i, 1)
        self.assertAlmostEqual(cartesian.j, 2)
        self.assertAlmostEqual(cartesian.k, 3)


if __name__ == '__main__':
    unittest.main()
