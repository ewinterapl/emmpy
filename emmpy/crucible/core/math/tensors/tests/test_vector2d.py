"""Tests for the vector2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.crucible.core.math.tensors.vector2d import Vector2D


class TestBuilder(unittest.TestCase):
    """Tests for the vector2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v = Vector2D()
        self.assertIsInstance(v, Vector2D)
        self.assertTrue(np.isnan(v[0]))
        self.assertTrue(np.isnan(v[1]))
        # 2-argument form.
        (x, y) = (1.1, 2.2)
        v = Vector2D(x, y)
        self.assertIsInstance(v, Vector2D)
        self.assertAlmostEqual(v[0], x)
        self.assertAlmostEqual(v[1], y)


if __name__ == '__main__':
    unittest.main()
