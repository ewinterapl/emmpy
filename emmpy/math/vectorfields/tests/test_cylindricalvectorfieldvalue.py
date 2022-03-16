"""Tests for the cylindricalvectorfieldvalue module."""


import unittest

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.vectorfields.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.math.vectorfields.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue,
    convertToCylindrical, convertToCartesian
)


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricalvectorfieldvalue module."""

    def test_convertToCylindrical(self):
        """Test the convertToCylindrical method."""
        (x, y, z) = (1, 2, 3)
        (vx, vy, vz) = (4, 5, 6)
        (rho_ref, phi_ref, z_ref) = (2.2360679774998, 1.1071487177941, 3)
        (vrho_ref, vphi_ref, vz_ref) = (
            6.260990336999412, -1.3416407864998732, 6)
        cartesianPosition = CartesianVector(x, y, z)
        cartesianValue = CartesianVector(vx, vy, vz)
        # Test conversion of a CartesianVectorFieldValue.
        cartesian = CartesianVectorFieldValue(
            cartesianPosition, cartesianValue)
        cylindrical = convertToCylindrical(cartesian)
        self.assertIsInstance(cylindrical, CylindricalVectorFieldValue)
        self.assertAlmostEqual(cylindrical.position.rho, rho_ref)
        self.assertAlmostEqual(cylindrical.position.phi, phi_ref)
        self.assertAlmostEqual(cylindrical.position.z, z_ref)
        self.assertAlmostEqual(cylindrical.value.rho, vrho_ref)
        self.assertAlmostEqual(cylindrical.value.phi, vphi_ref)
        self.assertAlmostEqual(cylindrical.value.z, vz_ref)
        # Test conversion of position and value vectors separately.
        cylindrical = convertToCylindrical(cartesianPosition, cartesianValue)
        self.assertIsInstance(cylindrical, CylindricalVectorFieldValue)
        self.assertAlmostEqual(cylindrical.position.rho, rho_ref)
        self.assertAlmostEqual(cylindrical.position.phi, phi_ref)
        self.assertAlmostEqual(cylindrical.position.z, z_ref)
        self.assertAlmostEqual(cylindrical.value.rho, vrho_ref)
        self.assertAlmostEqual(cylindrical.value.phi, vphi_ref)
        self.assertAlmostEqual(cylindrical.value.z, vz_ref)
        # Catch bad cases.
        sizes = (0, 3)
        for s in sizes:
            args = [None]*s
            with self.assertRaises(TypeError):
                convertToCylindrical(*args)

    def test_convertToCartesian(self):
        """Test the converToCartesian method."""
        # Cylindrical position, value, and Cartesian equivalents.
        (crho, cphi, cz) = (1, 2, 3)
        (cx_ref, cy_ref, cz_ref) = (
            -0.4161468365471424, 0.9092974268256817, 3)
        (cvrho, cvphi, cvz) = (4, 5, 6)
        (cvx_ref, cvy_ref, cvz_ref) = (
            -6.211074480316978, 1.5564555245670149, 6)
        cylindricalPosition = CylindricalVector(crho, cphi, cz)
        cylindricalValue = CylindricalVector(cvrho, cvphi, cvz)
        # Convert a CylindricalVectorFieldValue to Cartesian.
        cylindrical = CylindricalVectorFieldValue(
            cylindricalPosition, cylindricalValue)
        cartesian = convertToCartesian(cylindrical)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.x, cx_ref)
        self.assertAlmostEqual(cartesian.position.y, cy_ref)
        self.assertAlmostEqual(cartesian.position.z, cz_ref)
        self.assertAlmostEqual(cartesian.value.x, cvx_ref)
        self.assertAlmostEqual(cartesian.value.y, cvy_ref)
        self.assertAlmostEqual(cartesian.value.z, cvz_ref)
        # Convert separate cylindrical position and value vectors to Cartesian.
        cartesian = convertToCartesian(
            cylindricalPosition, cylindricalValue)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.x, cx_ref)
        self.assertAlmostEqual(cartesian.position.y, cy_ref)
        self.assertAlmostEqual(cartesian.position.z, cz_ref)
        self.assertAlmostEqual(cartesian.value.x, cvx_ref)
        self.assertAlmostEqual(cartesian.value.y, cvy_ref)
        self.assertAlmostEqual(cartesian.value.z, cvz_ref)


if __name__ == "__main__":
    unittest.main()
