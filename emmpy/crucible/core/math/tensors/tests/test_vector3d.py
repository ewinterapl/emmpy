"""Tests for the vector3d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.tensors.vector3d import Vector3D


class TestBuilder(unittest.TestCase):
    """Tests for the vector3d module."""

    def test___new__(self):
        """Test the __new__ method."""
        (x, y, z) = (1.1, 2.2, 3.3)
        v = Vector3D(x, y, z)
        self.assertIsInstance(v, Vector3D)
        self.assertAlmostEqual(v[0], x)
        self.assertAlmostEqual(v[1], y)
        self.assertAlmostEqual(v[2], z)


if __name__ == '__main__':
    unittest.main()
