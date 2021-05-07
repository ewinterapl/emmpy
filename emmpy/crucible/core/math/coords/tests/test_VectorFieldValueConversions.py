import unittest

from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.crucible.core.math.coords.cylindricalvector import (
    CylindricalVector
)
from emmpy.crucible.core.math.coords.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue
)
from emmpy.crucible.core.math.coords.sphericalvector import (
    SphericalVector
)
from emmpy.crucible.core.math.coords.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue
)
from emmpy.crucible.core.math.coords.vectorfieldvalueconversions import (
    VectorFieldValueConversions
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        vfvc = VectorFieldValueConversions()
        self.assertIsNotNone(vfvc)

    def test_convertToCylindrical(self):
        cartesianPosition = UnwritableVectorIJK(1, 2, 3)
        cartesianValue = UnwritableVectorIJK(4, 5, 6)
        cartesian = CartesianVectorFieldValue(
            cartesianPosition, cartesianValue
        )
        cylindrical = VectorFieldValueConversions.convertToCylindrical(
            cartesian
        )
        self.assertIsNotNone(cylindrical)
        self.assertAlmostEqual(cylindrical.position.getI(), 2.2360679774998)
        self.assertAlmostEqual(cylindrical.position.getJ(), 1.1071487177941)
        self.assertAlmostEqual(cylindrical.position.getK(), 3)
        self.assertAlmostEqual(cylindrical.value.getI(), 6.260990336999412)
        self.assertAlmostEqual(cylindrical.value.getJ(), -1.3416407864998732)
        self.assertAlmostEqual(cylindrical.value.getK(), 6)
        cylindrical = VectorFieldValueConversions.convertToCylindrical(
            cartesianPosition, cartesianValue
        )
        self.assertIsNotNone(cylindrical)
        self.assertAlmostEqual(cylindrical.position.getI(), 2.2360679774998)
        self.assertAlmostEqual(cylindrical.position.getJ(), 1.1071487177941)
        self.assertAlmostEqual(cylindrical.position.getK(), 3)
        self.assertAlmostEqual(cylindrical.value.getI(), 6.260990336999412)
        self.assertAlmostEqual(cylindrical.value.getJ(), -1.3416407864998732)
        self.assertAlmostEqual(cylindrical.value.getK(), 6)
        with self.assertRaises(Exception):
            VectorFieldValueConversions.convertToCylindrical(None, None, None)

    def test_convertToSpherical(self):
        cartesianPosition = UnwritableVectorIJK(1, 2, 3)
        cartesianValue = UnwritableVectorIJK(4, 5, 6)
        cartesian = CartesianVectorFieldValue(
            cartesianPosition, cartesianValue
        )
        spherical = VectorFieldValueConversions.convertToSpherical(
            cartesian
        )
        self.assertIsNotNone(spherical)
        self.assertAlmostEqual(spherical.position.getI(), 3.741657386773941)
        self.assertAlmostEqual(spherical.position.getJ(), 0.64052231267943)
        self.assertAlmostEqual(spherical.position.getK(), 1.1071487177941)
        self.assertAlmostEqual(spherical.value.getI(), 8.55235974119758)
        self.assertAlmostEqual(spherical.value.getJ(), 1.4342743312012725)
        self.assertAlmostEqual(spherical.value.getK(), -1.3416407864998732)
        spherical = VectorFieldValueConversions.convertToSpherical(
            cartesianPosition, cartesianValue
        )
        self.assertIsNotNone(spherical)
        self.assertAlmostEqual(spherical.position.getI(), 3.741657386773941)
        self.assertAlmostEqual(spherical.position.getJ(), 0.64052231267943)
        self.assertAlmostEqual(spherical.position.getK(), 1.1071487177941)
        self.assertAlmostEqual(spherical.value.getI(), 8.55235974119758)
        self.assertAlmostEqual(spherical.value.getJ(), 1.4342743312012725)
        self.assertAlmostEqual(spherical.value.getK(), -1.3416407864998732)
        with self.assertRaises(Exception):
            VectorFieldValueConversions.convertToSpherical(None, None, None)

    def test_convert(self):
        cylindricalPosition = CylindricalVector(1, 2, 3)
        cylindricalValue = CylindricalVector(4, 5, 6)
        cylindrical = CylindricalVectorFieldValue(
            cylindricalPosition, cylindricalValue
        )
        cartesian = VectorFieldValueConversions.convert(cylindrical)
        self.assertIsNotNone(cartesian)
        self.assertAlmostEqual(cartesian.position.getI(), -0.4161468365471424)
        self.assertAlmostEqual(cartesian.position.getJ(), 0.9092974268256817)
        self.assertAlmostEqual(cartesian.position.getK(), 3)
        self.assertAlmostEqual(cartesian.value.getI(), -6.211074480316978)
        self.assertAlmostEqual(cartesian.value.getJ(), 1.5564555245670149)
        self.assertAlmostEqual(cartesian.value.getK(), 6)
        cartesian = VectorFieldValueConversions.convert(
            cylindricalPosition, cylindricalValue
        )
        self.assertIsNotNone(cartesian)
        self.assertAlmostEqual(cartesian.position.getI(), -0.4161468365471424)
        self.assertAlmostEqual(cartesian.position.getJ(), 0.9092974268256817)
        self.assertAlmostEqual(cartesian.position.getK(), 3)
        self.assertAlmostEqual(cartesian.value.getI(), -6.211074480316978)
        self.assertAlmostEqual(cartesian.value.getJ(), 1.5564555245670149)
        self.assertAlmostEqual(cartesian.value.getK(), 6)
        sphericalPosition = SphericalVector(1, 2, 3)
        sphericalValue = SphericalVector(4, 5, 6)
        spherical = SphericalVectorFieldValue(
            sphericalPosition, sphericalValue
        )
        cartesian = VectorFieldValueConversions.convert(spherical)
        self.assertIsNotNone(cartesian)
        self.assertAlmostEqual(cartesian.position.getI(), -0.9001976297355174)
        self.assertAlmostEqual(cartesian.position.getJ(), 0.12832006020245673)
        self.assertAlmostEqual(cartesian.position.getK(), -0.4161468365471424)
        self.assertAlmostEqual(cartesian.value.getI(), -2.3875993389728580)
        self.assertAlmostEqual(cartesian.value.getJ(), -5.720307963430951)
        self.assertAlmostEqual(cartesian.value.getK(), -6.211074480316978)
        cartesian = VectorFieldValueConversions.convert(
            sphericalPosition, sphericalValue
        )
        self.assertIsNotNone(cartesian)
        self.assertAlmostEqual(cartesian.position.getI(), -0.9001976297355174)
        self.assertAlmostEqual(cartesian.position.getJ(), 0.12832006020245673)
        self.assertAlmostEqual(cartesian.position.getK(), -0.4161468365471424)
        self.assertAlmostEqual(cartesian.value.getI(), -2.3875993389728580)
        self.assertAlmostEqual(cartesian.value.getJ(), -5.720307963430951)
        self.assertAlmostEqual(cartesian.value.getK(), -6.211074480316978)
        with self.assertRaises(Exception):
            VectorFieldValueConversions.convert([])
        with self.assertRaises(Exception):
            VectorFieldValueConversions.convert([], [])
        with self.assertRaises(Exception):
            VectorFieldValueConversions.convert([], [], [])


if __name__ == '__main__':
    unittest.main()
