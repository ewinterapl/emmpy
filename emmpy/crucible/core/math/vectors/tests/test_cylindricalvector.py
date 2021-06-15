"""Tests for the cylindricalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.vectors.cylindricalvector import (
    CylindricalVector
)


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricalvector module."""

    def test___new__(self):
        """Test the __new__ method."""
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
        with self.assertRaises(AttributeError):
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
        with self.assertRaises(AttributeError):
            v.bad = 0


if __name__ == '__main__':
    unittest.main()
