"""Tests for the sphericalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.vectors.sphericalvector import SphericalVector


class TestBuilder(unittest.TestCase):
    """Tests for the sphericalvector module."""

    def test___new__(self):
        """Test the __new__ method."""
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
        with self.assertRaises(AttributeError):
            v.bad


if __name__ == '__main__':
    unittest.main()
