"""Tests for the cylindricalcoordsxaligned module."""


from emmpy.math.coordinates.cylindricalvector import CylindricalVector
import unittest

from emmpy.magmodel.core.math.coords.cylindricalcoordsxaligned import (
    CylindricalCoordsXAligned
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricalcoordsxaligned module."""

    def test_convert(self):
        """Test the convert method."""
        # Test Cartesian->x-aligned cylindrical.
        (x, y, z) = (1, 2, 3)
        cartesian = VectorIJK(x, y, z)
        cylindrical = CylindricalCoordsXAligned.convert(cartesian)
        self.assertIsInstance(cylindrical, CylindricalVector)
        self.assertAlmostEqual(cylindrical.rho, 3.6055512754639896)
        self.assertAlmostEqual(cylindrical.phi, 0.982793723247329)
        self.assertAlmostEqual(cylindrical.z, 1)
        # Test x-aligned cylindrical->Cartesian.
        cartesian = CylindricalCoordsXAligned.convert(cylindrical)
        self.assertIsInstance(cartesian, VectorIJK)
        self.assertAlmostEqual(cartesian.i, 1)
        self.assertAlmostEqual(cartesian.j, 2)
        self.assertAlmostEqual(cartesian.k, 3)
        # Invalid cases.
        with self.assertRaises(TypeError):
            CylindricalCoordsXAligned.convert(None)

    def test_convertFieldValue(self):
        """Test the convertFieldValue method."""
        # Test Cartesian->x-aligned cylindrical.
        (x, y, z) = (1, 2, 3)
        (vx, vy, vz) = (4, 5, 6)
        cartesianPosition = VectorIJK(x, y, z)
        cartesianValue = VectorIJK(vx, vy, vz)
        cylindricalValue = CylindricalCoordsXAligned.convertFieldValue(
            cartesianPosition, cartesianValue
        )
        self.assertIsInstance(cylindricalValue, CylindricalVector)
        self.assertAlmostEqual(cylindricalValue.rho, 7.7658027471532085)
        self.assertAlmostEqual(cylindricalValue.phi, -0.832050294337844)
        self.assertAlmostEqual(cylindricalValue.z, 4)
        # Test x-aligned cylindrical->Cartesian.
        cylindricalPosition = CylindricalCoordsXAligned.convert(
            cartesianPosition
        )
        cartesianValue = CylindricalCoordsXAligned.convertFieldValue(
            cylindricalPosition, cylindricalValue
        )
        self.assertIsInstance(cartesianValue, VectorIJK)
        self.assertAlmostEqual(cartesianValue.i, vx)
        self.assertAlmostEqual(cartesianValue.j, vy)
        self.assertAlmostEqual(cartesianValue.k, vz)
        # Invalid forms.
        with self.assertRaises(TypeError):
            CylindricalCoordsXAligned.convertFieldValue(None, None)

    def test_convertBasisField(self):
        """Test the convertBasisField method."""
        # NEED THESE TESTS.
        # Invalid forms.
        with self.assertRaises(TypeError):
            CylindricalCoordsXAligned.convertBasisField(None)


if __name__ == '__main__':
    unittest.main()
