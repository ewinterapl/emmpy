import unittest

from emmpy.crucible.core.math.coords.sphericalcoordconverter import (
    SphericalCoordConverter
)
from emmpy.crucible.core.math.coords.sphericalvector import (
    SphericalVector
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        scc = SphericalCoordConverter()
        self.assertIsNotNone(scc)

    def test_toCoordinate(self):
        scc = SphericalCoordConverter()
        cartesian = VectorIJK(1, 2, 3)
        spherical = scc.toCoordinate(cartesian)
        self.assertAlmostEqual(spherical.getI(), 3.741657386773941)
        self.assertAlmostEqual(spherical.getJ(), 0.6405223126794246)
        self.assertAlmostEqual(spherical.getK(), 1.1071487177940904)

    def test_toCartesian(self):
        scc = SphericalCoordConverter()
        spherical = SphericalVector(
            3.741657386773941, 0.6405223126794246, 1.1071487177940904
        )
        cartesian = scc.toCartesian(spherical)
        self.assertAlmostEqual(cartesian.i, 1)
        self.assertAlmostEqual(cartesian.j, 2)
        self.assertAlmostEqual(cartesian.getK(), 3)


if __name__ == '__main__':
    unittest.main()
