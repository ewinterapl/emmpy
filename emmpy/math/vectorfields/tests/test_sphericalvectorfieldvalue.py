"""Tests for the sphericalvectorfieldvalue module."""


import unittest

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.vectorfields.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.math.vectorfields.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue,
    convertToSpherical, convertToCartesian
)
from emmpy.math.coordinates.sphericalvector import SphericalVector


class TestBuilder(unittest.TestCase):
    """Tests for the sphericalvectorfieldvalue module."""

    def test_convertToSpherical(self):
        """Test the convertToSpherical method."""
        (x, y, z) = (1, 2, 3)
        (vx, vy, vz) = (4, 5, 6)
        (r_ref, theta_ref, phi_ref) = (
            3.741657386773941, 0.64052231267943, 1.1071487177941)
        (vr_ref, vtheta_ref, vphi_ref) = (
            8.55235974119758, 1.4342743312012725, -1.3416407864998732)
        cartesianPosition = CartesianVector(x, y, z)
        cartesianValue = CartesianVector(vx, vy, vz)
        # Test conversion of a CartesianVectorFieldValue.
        cartesian = CartesianVectorFieldValue(
            cartesianPosition, cartesianValue)
        spherical = convertToSpherical(cartesian)
        self.assertIsInstance(spherical, SphericalVectorFieldValue)
        self.assertAlmostEqual(spherical.position.r, r_ref)
        self.assertAlmostEqual(spherical.position.theta, theta_ref)
        self.assertAlmostEqual(spherical.position.phi, phi_ref)
        self.assertAlmostEqual(spherical.value.r, vr_ref)
        self.assertAlmostEqual(spherical.value.theta, vtheta_ref)
        self.assertAlmostEqual(spherical.value.phi, vphi_ref)
        # Test conversion of position and value vectors separately.
        spherical = convertToSpherical(
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
                convertToSpherical(*args)

    def test_convertToCartesian(self):
        """Test the convertToSpherical method."""
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
        cartesian = convertToCartesian(spherical)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.x, sx_ref)
        self.assertAlmostEqual(cartesian.position.y, sy_ref)
        self.assertAlmostEqual(cartesian.position.z, sz_ref)
        self.assertAlmostEqual(cartesian.value.x, svx_ref)
        self.assertAlmostEqual(cartesian.value.y, svy_ref)
        self.assertAlmostEqual(cartesian.value.z, svz_ref)
        # Convert separate spherical position and value vectors to Cartesian.
        cartesian = convertToCartesian(
            sphericalPosition, sphericalValue)
        self.assertIsInstance(cartesian, CartesianVectorFieldValue)
        self.assertAlmostEqual(cartesian.position.x, sx_ref)
        self.assertAlmostEqual(cartesian.position.y, sy_ref)
        self.assertAlmostEqual(cartesian.position.z, sz_ref)
        self.assertAlmostEqual(cartesian.value.x, svx_ref)
        self.assertAlmostEqual(cartesian.value.y, svy_ref)
        self.assertAlmostEqual(cartesian.value.z, svz_ref)
        # Catch bad cases.
        sizes = (0, 3)
        for s in sizes:
            args = [None]*s
            with self.assertRaises(TypeError):
                convertToCartesian(*args)


if __name__ == "__main__":
    unittest.main()
