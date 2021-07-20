"""Tests for the vector2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.vectors.vector2d import Vector2D


class TestBuilder(unittest.TestCase):
    """Tests for the vector2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-arg form - 2 elements
        v = Vector2D.__new__(Vector2D)
        self.assertIsInstance(v, Vector2D)
        self.assertEqual(len(v), 2)

    def test___init__(self):
        """Test the __init__ method."""
        # 0-argument form - vector of nan.
        v = Vector2D()
        self.assertIsInstance(v, Vector2D)
        for x in v:
            self.assertTrue(np.isnan(x))
        # 1-argument forms
        # list
        data = [1.1, 2.2]
        v = Vector2D(data)
        for (x1, x2) in zip(v, data):
            self.assertAlmostEqual(x1, x2)
        # tuple
        data = (1.1, 2.2)
        v = Vector2D(data)
        for (x1, x2) in zip(v, data):
            self.assertAlmostEqual(x1, x2)
        # np.ndarray
        a = np.array(data)
        v = Vector2D(a)
        for (x1, x2) in zip(v, a):
            self.assertAlmostEqual(x1, x2)
        # 2-argument form: 2 values for elements
        v = Vector2D(*data)
        self.assertIsInstance(v, Vector2D)
        for (x1, x2) in zip(v, data):
            self.assertAlmostEqual(x1, x2)
        # Invalid forms.
        with self.assertRaises(ValueError):
            args = (None,)*3
            v = Vector2D(*args)


if __name__ == '__main__':
    unittest.main()
