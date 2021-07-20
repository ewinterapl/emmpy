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
        # 0-arg form - 3 elements
        v = Vector3D.__new__(Vector3D)
        self.assertIsInstance(v, Vector3D)
        self.assertEqual(len(v), 3)

    def test___init__(self):
        """Test the __init__ method."""
        # 0-argument form - vector of nan.
        v = Vector3D()
        self.assertIsInstance(v, Vector3D)
        for x in v:
            self.assertTrue(np.isnan(x))
        # 1-argument forms
        # list
        data = [1.1, 2.2, 3.3]
        v = Vector3D(data)
        for (x1, x2) in zip(v, data):
            self.assertAlmostEqual(x1, x2)
        # tuple
        data = (1.1, 2.2, 3.3)
        v = Vector3D(data)
        for (x1, x2) in zip(v, data):
            self.assertAlmostEqual(x1, x2)
        # np.ndarray
        a = np.array(data)
        v = Vector3D(a)
        for (x1, x2) in zip(v, a):
            self.assertAlmostEqual(x1, x2)
        # 3-argument form: 3 values for elements
        v = Vector3D(*data)
        self.assertIsInstance(v, Vector3D)
        for (x1, x2) in zip(v, data):
            self.assertAlmostEqual(x1, x2)
        # Invalid forms.
        for n in (2, 4):
            args = (None,)*n
            with self.assertRaises(ValueError):
                v = Vector3D(*args)


if __name__ == '__main__':
    unittest.main()
