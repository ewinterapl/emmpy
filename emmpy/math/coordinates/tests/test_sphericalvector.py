"""Tests for the sphericalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.coordinates.sphericalvector import SphericalVector


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


if __name__ == '__main__':
    unittest.main()