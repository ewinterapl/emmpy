"""Tests for the matrix3d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.tensors.matrix3d import Matrix3D


class TestBuilder(unittest.TestCase):
    """Tests for the matrix3d module."""

    def test___new__(self):
        """Test the __new__ method."""
        (xx, yx, zx, xy, yy, zy, xz, yz, zz) = (
            1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9)
        m = Matrix3D(xx, yx, zx, xy, yy, zy, xz, yz, zz)
        self.assertIsInstance(m, Matrix3D)
        self.assertAlmostEqual(m[0, 0], xx)
        self.assertAlmostEqual(m[1, 0], yx)
        self.assertAlmostEqual(m[2, 0], zx)
        self.assertAlmostEqual(m[0, 1], xy)
        self.assertAlmostEqual(m[1, 1], yy)
        self.assertAlmostEqual(m[2, 1], zy)
        self.assertAlmostEqual(m[0, 2], xz)
        self.assertAlmostEqual(m[1, 2], yz)
        self.assertAlmostEqual(m[2, 2], zz)


if __name__ == '__main__':
    unittest.main()
