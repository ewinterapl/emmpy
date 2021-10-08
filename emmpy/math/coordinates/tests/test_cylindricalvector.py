"""Tests for the cylindricalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D
from emmpy.math.coordinates.cylindricalvector import (
    CylindricalVector, cartesianToCylindrical, cylindricalToCartesian
)


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricalvector module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v = CylindricalVector()
        self.assertIsInstance(v, CylindricalVector)
        for i in range(3):
            self.assertTrue(np.isnan(v[i]))
        # 3-argument form.
        (rho, phi, z) = (1.1, 2.2, 3.3)
        v = CylindricalVector(rho, phi, z)
        self.assertIsInstance(v, CylindricalVector)
        self.assertAlmostEqual(v[0], rho)
        self.assertAlmostEqual(v[1], phi)
        self.assertAlmostEqual(v[2], z)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (rho, phi, z) = (1.1, 2.2, 3.3)
        v = CylindricalVector(rho, phi, z)
        self.assertAlmostEqual(v.rho, rho)
        self.assertAlmostEqual(v.phi, phi)
        self.assertAlmostEqual(v.z, z)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = CylindricalVector(0, 0, 0)
        (rho, phi, z) = (1.1, 2.2, 3.3)
        v.rho = rho
        self.assertAlmostEqual(v.rho, rho)
        v.phi = phi
        self.assertAlmostEqual(v.phi, phi)
        v.z = z
        self.assertAlmostEqual(v.z, z)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_cylindricalToCartesian(self):
        """Test the cylindricalToCartesian function."""
        (rho, phi, z) = (1.1, 2.2, 3.3)
        cylindrical = CylindricalVector(rho, phi, z)
        cartesian = cylindricalToCartesian(cylindrical)
        x = rho*cos(phi)
        y = rho*sin(phi)
        # z is unchanged.
        self.assertAlmostEqual(cartesian.x, x)
        self.assertAlmostEqual(cartesian.y, y)
        self.assertAlmostEqual(cartesian.z, z)

    def test_cartesianToCylindrical(self):
        """Test the cartesianToCylindrical function."""
        # Test at the origin.
        (x, y, z) = (0, 0, 0)
        cartesian = CartesianVector3D(x, y, z)
        cylindrical = cartesianToCylindrical(cartesian)
        rho = 0
        phi = 0
        # z is unchanged.
        self.assertAlmostEqual(cylindrical.rho, rho)
        self.assertAlmostEqual(cylindrical.phi, phi)
        self.assertAlmostEqual(cylindrical.z, z)
        # Test a typical point.
        (x, y, z) = (1.1, 2.2, 3.3)
        cartesian = CartesianVector3D(x, y, z)
        cylindrical = cartesianToCylindrical(cartesian)
        rho = sqrt(x**2 + y**2)
        phi = atan2(y, x)
        if phi < 0:
            phi += 2*pi
        # z is unchanged.
        self.assertAlmostEqual(cylindrical.rho, rho)
        self.assertAlmostEqual(cylindrical.phi, phi)
        self.assertAlmostEqual(cylindrical.z, z)


if __name__ == '__main__':
    unittest.main()
