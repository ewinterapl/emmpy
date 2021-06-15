"""Tests for the vector2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.vectors.vector2d import Vector2D


class TestBuilder(unittest.TestCase):
    """Tests for the vector2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        (x, y) = (1.1, 2.2)
        v = Vector2D(x, y)
        self.assertIsInstance(v, Vector2D)
        self.assertEqual(v.shape, (2,))
        self.assertAlmostEqual(v[0], x)
        self.assertAlmostEqual(v[1], y)


if __name__ == '__main__':
    unittest.main()
