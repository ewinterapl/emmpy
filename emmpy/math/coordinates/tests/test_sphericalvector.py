"""Tests for the sphericalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np
from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D

from emmpy.math.coordinates.sphericalvector import (
    SphericalVector, sphericalToCartesian, cartesianToSpherical
)


# Test grids.
n = 33
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rs = np.linspace(0, 10, n)
thetas = np.linspace(0, pi, n)
phis = np.linspace(0, 2*pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the sphericalvector module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v = SphericalVector()
        self.assertIsInstance(v, SphericalVector)
        for i in range(3):
            self.assertTrue(np.isnan(v[i]))
        # 3-argument form.
        (r, theta, phi) = (1.1, 2.2, 3.3)
        v = SphericalVector(r, theta, phi)
        self.assertIsInstance(v, SphericalVector)
        self.assertAlmostEqual(v[0], r)
        self.assertAlmostEqual(v[1], theta)
        self.assertAlmostEqual(v[2], phi)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (r, theta, phi) = (1.1, 2.2, 3.3)
        v = SphericalVector(r, theta, phi)
        self.assertAlmostEqual(v.r, r)
        self.assertAlmostEqual(v.theta, theta)
        self.assertAlmostEqual(v.phi, phi)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = SphericalVector(0, 0, 0)
        (r, theta, phi) = (1.1, 2.2, 3.3)
        v.r = r
        self.assertAlmostEqual(v.r, r)
        v.theta = theta
        self.assertAlmostEqual(v.theta, theta)
        v.phi = phi
        self.assertAlmostEqual(v.phi, phi)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_sphericalToCartesian(self):
        """Test the sphericalToCartesian function."""
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    spherical = SphericalVector(r, theta, phi)
                    x = r*sin(theta)*cos(phi)
                    y = r*sin(theta)*sin(phi)
                    z = r*cos(theta)
                    cartesian = sphericalToCartesian(spherical)
                    self.assertAlmostEqual(cartesian.x, x)
                    self.assertAlmostEqual(cartesian.y, y)
                    self.assertAlmostEqual(cartesian.z, z)

    def test_cartesianToSpherical(self):
        """Test the cartesianToSpherical function."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = CartesianVector3D(x, y, z)
                    r = sqrt(x**2 + y**2 + z**2)
                    theta = atan2(sqrt(x**2 + y**2), z)
                    phi = atan2(y, x)
                    spherical = cartesianToSpherical(cartesian)
                    self.assertAlmostEqual(spherical.r, r)
                    self.assertAlmostEqual(spherical.theta, theta)
                    self.assertAlmostEqual(spherical.phi, phi)


if __name__ == '__main__':
    unittest.main()
