import unittest

from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.coords.cylindricalvector import (
    CylindricalVector
)
from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector
)
from emmpy.crucible.core.math.coords.polarvector import (
    PolarVector
)
from emmpy.crucible.core.math.coords.radecvector import (
    RaDecVector
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.core.math.coords.sphericalvector import (
    SphericalVector
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        cc = CoordConverters()
        self.assertIsNotNone(cc)

    def test_convertToCylindrical(self):
        cartesian = VectorIJK(1, 2, 3)
        cylindrical = CoordConverters.convertToCylindrical(cartesian)
        self.assertAlmostEqual(cylindrical.rho, 2.23606797749979)
        self.assertAlmostEqual(cylindrical.phi, 1.1071487177940904)
        self.assertAlmostEqual(cylindrical.z, 3)

    def test_convertToLatitudinal(self):
        cartesian = VectorIJK(1, 2, 3)
        latitudinal = CoordConverters.convertToLatitudinal(cartesian)
        self.assertAlmostEqual(latitudinal.getI(), 3.741657386773941)
        self.assertAlmostEqual(latitudinal.getJ(), 0.9302740141154721)
        self.assertAlmostEqual(latitudinal.getK(), 1.1071487177940904)

    def test_convertToPolar(self):
        cartesian = VectorIJ(1, 2)
        polar = CoordConverters.convertToPolar(cartesian)
        self.assertAlmostEqual(polar.getI(), 2.23606797749979)
        self.assertAlmostEqual(polar.getJ(), 1.1071487177940904)

    def test_convertToRaDec(self):
        cartesian = VectorIJK(1, 2, 3)
        radec = CoordConverters.convertToRaDec(cartesian)
        self.assertAlmostEqual(radec.getI(), 3.741657386773941)
        self.assertAlmostEqual(radec.getJ(), 1.1071487177940904)
        self.assertAlmostEqual(radec.getK(), 0.9302740141154721)

    def test_convertToSpherical(self):
        cartesian = VectorIJK(1, 2, 3)
        spherical = CoordConverters.convertToSpherical(cartesian)
        self.assertAlmostEqual(spherical.getI(), 3.741657386773941)
        self.assertAlmostEqual(spherical.getJ(), 0.6405223126794246)
        self.assertAlmostEqual(spherical.getK(), 1.1071487177940904)

    def test_convert(self):
        cylindrical = CylindricalVector(1, 2, 3)
        cartesian = CoordConverters.convert(cylindrical)
        self.assertAlmostEqual(cartesian.i, -0.4161468365471424)
        self.assertAlmostEqual(cartesian.j, 0.9092974268256817)
        self.assertAlmostEqual(cartesian.k, 3)
        latitudinal = LatitudinalVector(1, 2, 3)
        cartesian = CoordConverters.convert(latitudinal)
        self.assertAlmostEqual(cartesian.i, 0.411982245665683)
        self.assertAlmostEqual(cartesian.j, -0.05872664492762098)
        self.assertAlmostEqual(cartesian.k, 0.9092974268256817)
        polar = PolarVector(1, 2)
        cartesian = CoordConverters.convert(polar)
        self.assertAlmostEqual(cartesian.i, -0.4161468365471424)
        self.assertAlmostEqual(cartesian.j, 0.9092974268256817)
        radec = RaDecVector(1, 2, 3)
        cartesian = CoordConverters.convert(radec)
        self.assertAlmostEqual(cartesian.i, 0.411982245665683)
        self.assertAlmostEqual(cartesian.j, -0.9001976297355174)
        self.assertAlmostEqual(cartesian.k, 0.1411200080598672)
        spherical = SphericalVector(1, 2, 3)
        cartesian = CoordConverters.convert(spherical)
        self.assertAlmostEqual(cartesian.i, -0.9001976297355174)
        self.assertAlmostEqual(cartesian.j, 0.12832006020245673)
        self.assertAlmostEqual(cartesian.k, -0.4161468365471424)
        with self.assertRaises(Exception):
            CoordConverters.convert([])


if __name__ == '__main__':
    unittest.main()
