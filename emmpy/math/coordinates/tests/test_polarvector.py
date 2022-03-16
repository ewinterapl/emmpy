"""Tests for the polarvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np
from emmpy.math.coordinates.cartesianvector2d import CartesianVector2D

from emmpy.math.coordinates.polarvector import (
    PolarVector, polarToCartesian, cartesianToPolar
)


# Test grids.
n = 33
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
rs = np.linspace(0, 10, n)
phis = np.linspace(0, 2*pi, n)

class TestBuilder(unittest.TestCase):
    """Tests for the polarvector module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v = PolarVector()
        self.assertIsInstance(v, PolarVector)
        for i in range(2):
            self.assertTrue(np.isnan(v[i]))
        # 2-argument form.
        (r, phi) = (1.1, 2.2)
        v = PolarVector(r, phi)
        self.assertIsInstance(v, PolarVector)
        self.assertAlmostEqual(v[0], r)
        self.assertAlmostEqual(v[1], phi)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (r, phi) = (1.1, 2.2)
        v = PolarVector(r, phi)
        self.assertAlmostEqual(v.r, r)
        self.assertAlmostEqual(v.phi, phi)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = PolarVector(0, 0)
        (r, phi) = (1.1, 2.2)
        v.r = r
        self.assertAlmostEqual(v.r, r)
        v.phi = phi
        self.assertAlmostEqual(v.phi, phi)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_polarToCartesian(self):
        """Test the polarToCartesian function."""
        for r in rs:
            for phi in phis:
                x = r*cos(phi)
                y = r*sin(phi)
                polar = PolarVector(r, phi)
                cartesian = polarToCartesian(polar)
                self.assertAlmostEqual(cartesian.x, x)
                self.assertAlmostEqual(cartesian.y, y)

    def test_cartesianToPolar(self):
        """Test the cartesianToPolar function."""
        for x in xs:
            for y in ys:
                cartesian = CartesianVector2D(x, y)
                r = sqrt(x**2 + y**2)
                phi = atan2(y, x)
                polar = cartesianToPolar(cartesian)
                self.assertAlmostEqual(polar.r, r)
                self.assertAlmostEqual(polar.phi, phi)


if __name__ == '__main__':
    unittest.main()
