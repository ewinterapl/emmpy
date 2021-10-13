"""Tests for the vectorfieldvalueconversions module."""


import unittest

from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.coords.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.crucible.core.math.coords.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue)
from emmpy.crucible.core.math.coords.vectorfieldvalueconversions import (
    VectorFieldValueConversions)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfieldvalueconversions module."""

    def test_convertToCylindrical(self):
        """Test the convertToCylindrical method."""
        (x, y, z) = (1, 2, 3)
        (vx, vy, vz) = (4, 5, 6)
        (rho_ref, phi_ref, z_ref) = (2.2360679774998, 1.1071487177941, 3)
        (vrho_ref, vphi_ref, vz_ref) = (
            6.260990336999412, -1.3416407864998732, 6)
        cartesianPosition = VectorIJK(x, y, z)
        cartesianValue = VectorIJK(vx, vy, vz)
        # Test conversion of a CartesianVectorFieldValue.
        cartesian = CartesianVectorFieldValue(
            cartesianPosition, cartesianValue)
        cylindrical = VectorFieldValueConversions.convertToCylindrical(
            cartesian)
        self.assertIsInstance(cylindrical, CylindricalVectorFieldValue)
        self.assertAlmostEqual(cylindrical.position.rho, rho_ref)
        self.assertAlmostEqual(cylindrical.position.phi, phi_ref)
        self.assertAlmostEqual(cylindrical.position.z, z_ref)
        self.assertAlmostEqual(cylindrical.value.rho, vrho_ref)
        self.assertAlmostEqual(cylindrical.value.phi, vphi_ref)
        self.assertAlmostEqual(cylindrical.value.z, vz_ref)
        # Test conversion of position and value vectors separately.
        cylindrical = VectorFieldValueConversions.convertToCylindrical(
            cartesianPosition, cartesianValue)
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
                VectorFieldValueConversions.convertToCylindrical(*args)

    def test_convertToSpherical(self):
        """Test the convertToSpherical method."""
        (x, y, z) = (1, 2, 3)
        (vx, vy, vz) = (4, 5, 6)
        (r_ref, theta_ref, phi_ref) = (
            3.741657386773941, 0.64052231267943, 1.1071487177941)
        (vr_ref, vtheta_ref, vphi_ref) = (
            8.55235974119758, 1.4342743312012725, -1.3416407864998732)
        cartesianPosition = VectorIJK(x, y, z)
        cartesianValue = VectorIJK(vx, vy, vz)
        # Test conversion of a CartesianVectorFieldValue.
        cartesian = CartesianVectorFieldValue(
            cartesianPosition, cartesianValue)
        spherical = VectorFieldValueConversions.convertToSpherical(cartesian)
        self.assertIsInstance(spherical, SphericalVectorFieldValue)
        self.assertAlmostEqual(spherical.position.r, r_ref)
        self.assertAlmostEqual(spherical.position.theta, theta_ref)
        self.assertAlmostEqual(spherical.position.phi, phi_ref)
        self.assertAlmostEqual(spherical.value.r, vr_ref)
        self.assertAlmostEqual(spherical.value.theta, vtheta_ref)
        self.assertAlmostEqual(spherical.value.phi, vphi_ref)
        # Test conversion of position and value vectors separately.
        spherical = VectorFieldValueConversions.convertToSpherical(
            cartesianPosition, cartesianValue)
        self.assertIsInstance(spherical, SphericalVectorFieldValue)
        self.assertAlmostEqual(spherical.position.r, r_ref)
        self.assertAlmostEqual(spherical.position.theta, theta_ref)
        self.assertAlmostEqual(spherical.position.phi, phi_ref)
        self.assertAlmostEqual(spherical.value.r, vr_ref)
        self.assertAlmostEqual(spherical.value.theta, vtheta_ref)
        self.assertAlmostEqual(spherical.value.phi, vphi_ref)
        # Catch bad cases.
        sizes = (0, 3)
        for s in sizes:
            args = [None]*s
            with self.assertRaises(TypeError):
                VectorFieldValueConversions.convertToSpherical(*args)

    def test_convert(self):
        """Test the convert method."""
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
        cartesian = VectorFieldValueConversions.convert(cylindrical)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.i, cx_ref)
        self.assertAlmostEqual(cartesian.position.j, cy_ref)
        self.assertAlmostEqual(cartesian.position.k, cz_ref)
        self.assertAlmostEqual(cartesian.value.i, cvx_ref)
        self.assertAlmostEqual(cartesian.value.j, cvy_ref)
        self.assertAlmostEqual(cartesian.value.k, cvz_ref)
        # Convert separate cylindrical position and value vectors to Cartesian.
        cartesian = VectorFieldValueConversions.convert(
            cylindricalPosition, cylindricalValue)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.i, cx_ref)
        self.assertAlmostEqual(cartesian.position.j, cy_ref)
        self.assertAlmostEqual(cartesian.position.k, cz_ref)
        self.assertAlmostEqual(cartesian.value.i, cvx_ref)
        self.assertAlmostEqual(cartesian.value.j, cvy_ref)
        self.assertAlmostEqual(cartesian.value.k, cvz_ref)

        # Spherical position, value, and Cartesian equivalents.
        (sr, stheta, sphi) = (1, 2, 3)
        (sx_ref, sy_ref, sz_ref) = (
            -0.9001976297355174, 0.12832006020245673, -0.4161468365471424)
        (svr, svtheta, svphi) = (4, 5, 6)
        (svx_ref, svy_ref, svz_ref) = (
            -2.3875993389728580, -5.720307963430951, -6.211074480316978)
        sphericalPosition = SphericalVector(sr, stheta, sphi)
        sphericalValue = SphericalVector(svr, svtheta, svphi)
        # Convert a SphericalVectorFieldValue to Cartesian.
        spherical = SphericalVectorFieldValue(
            sphericalPosition, sphericalValue)
        cartesian = VectorFieldValueConversions.convert(spherical)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.i, sx_ref)
        self.assertAlmostEqual(cartesian.position.j, sy_ref)
        self.assertAlmostEqual(cartesian.position.k, sz_ref)
        self.assertAlmostEqual(cartesian.value.i, svx_ref)
        self.assertAlmostEqual(cartesian.value.j, svy_ref)
        self.assertAlmostEqual(cartesian.value.k, svz_ref)
        # Convert separate spherical position and value vectors to Cartesian.
        cartesian = VectorFieldValueConversions.convert(
            sphericalPosition, sphericalValue)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.i, sx_ref)
        self.assertAlmostEqual(cartesian.position.j, sy_ref)
        self.assertAlmostEqual(cartesian.position.k, sz_ref)
        self.assertAlmostEqual(cartesian.value.i, svx_ref)
        self.assertAlmostEqual(cartesian.value.j, svy_ref)
        self.assertAlmostEqual(cartesian.value.k, svz_ref)
        # Catch bad cases.
        sizes = (0, 3)
        for s in sizes:
            args = [None]*s
            with self.assertRaises(TypeError):
                VectorFieldValueConversions.convert(*args)


if __name__ == '__main__':
    unittest.main()
