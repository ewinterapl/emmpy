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
        # 0-argument form.
        v = Vector2D()
        self.assertIsInstance(v, Vector2D)
        for i in range(2):
            self.assertTrue(np.isnan(v[i]))
        # 2-argument form.
        data = (1.1, 2.2)
        v = Vector2D(*data)
        self.assertIsInstance(v, Vector2D)
        for i in range(2):
            self.assertAlmostEqual(v[i], data[i])
        # Invalid forms.
        with self.assertRaises(ValueError):
            v = Vector2D(None)
        with self.assertRaises(ValueError):
            v = Vector2D(None, None, None)


if __name__ == '__main__':
    unittest.main()
