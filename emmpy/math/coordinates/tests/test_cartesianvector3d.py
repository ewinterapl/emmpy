"""Tests for the cartesianvector3d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D


class TestBuilder(unittest.TestCase):
    """Tests for the cartesianvector3d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v = CartesianVector3D()
        self.assertIsInstance(v, CartesianVector3D)
        for i in range(3):
            self.assertTrue(np.isnan(v[i]))
        # 3-argument form.
        (x, y, z) = (1.1, 2.2, 3.3)
        v = CartesianVector3D(x, y, z)
        self.assertIsInstance(v, CartesianVector3D)
        self.assertAlmostEqual(v[0], x)
        self.assertAlmostEqual(v[1], y)
        self.assertAlmostEqual(v[2], z)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (x, y, z) = (1.1, 2.2, 3.3)
        v = CartesianVector3D(x, y, z)
        self.assertAlmostEqual(v.x, x)
        self.assertAlmostEqual(v.y, y)
        self.assertAlmostEqual(v.z, z)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = CartesianVector3D()
        (x, y, z) = (1.1, 2.2, 3.3)
        v.x = x
        self.assertAlmostEqual(v.x, x)
        v.y = y
        self.assertAlmostEqual(v.y, y)
        v.z = z
        self.assertAlmostEqual(v.z, z)
        with self.assertRaises(KeyError):
            v.bad = 0


if __name__ == '__main__':
    unittest.main()
