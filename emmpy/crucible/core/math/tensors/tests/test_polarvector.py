"""Tests for the polarvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.tensors.polarvector import PolarVector


class TestBuilder(unittest.TestCase):
    """Tests for the polarvector module."""

    def test___new__(self):
        """Test the __new__ method."""
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
        with self.assertRaises(AttributeError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = PolarVector(0, 0)
        (r, phi) = (1.1, 2.2)
        v.r = r
        self.assertAlmostEqual(v.r, r)
        v.phi = phi
        self.assertAlmostEqual(v.phi, phi)
        with self.assertRaises(AttributeError):
            v.bad = 0


if __name__ == '__main__':
    unittest.main()