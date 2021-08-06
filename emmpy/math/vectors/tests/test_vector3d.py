"""Tests for the vector3d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.math.vectors.vector3d import Vector3D


class TestBuilder(unittest.TestCase):
    """Tests for the vector3d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-arg form - 3 elements
        v = Vector3D.__new__(Vector3D)
        self.assertIsInstance(v, Vector3D)
        self.assertEqual(len(v), 3)


if __name__ == '__main__':
    unittest.main()
