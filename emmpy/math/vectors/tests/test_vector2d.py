"""Tests for the vector2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.math.vectors.vector2d import Vector2D


class TestBuilder(unittest.TestCase):
    """Tests for the vector2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-arg form - 2 elements
        v = Vector2D.__new__(Vector2D)
        self.assertIsInstance(v, Vector2D)
        self.assertEqual(len(v), 2)


if __name__ == '__main__':
    unittest.main()
