"""Tests for the vector3d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.vectors.vector3d import Vector3D


class TestBuilder(unittest.TestCase):
    """Tests for the vector3d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v = Vector3D()
        self.assertIsInstance(v, Vector3D)
        for i in range(3):
            self.assertTrue(np.isnan(v[i]))
        # 3-argument form.
        data = (1.1, 2.2, 3.3)
        v = Vector3D(*data)
        self.assertIsInstance(v, Vector3D)
        for i in range(3):
            self.assertAlmostEqual(v[i], data[i])
        # Invalid forms.
        with self.assertRaises(ValueError):
            v = Vector3D(None)
        with self.assertRaises(ValueError):
            v = Vector3D(None, None)
        with self.assertRaises(ValueError):
            v = Vector3D(None, None, None, None)


if __name__ == '__main__':
    unittest.main()
