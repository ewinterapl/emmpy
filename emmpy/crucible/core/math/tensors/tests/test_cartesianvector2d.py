"""Tests for the cartesianvector2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.tensors.cartesianvector2d import (
    CartesianVector2D
)


class TestBuilder(unittest.TestCase):
    """Tests for the cartesianvector2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        (x, y) = (1.1, 2.2)
        v = CartesianVector2D(x, y)
        self.assertIsInstance(v, CartesianVector2D)
        self.assertAlmostEqual(v[0], x)
        self.assertAlmostEqual(v[1], y)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (x, y) = (1.1, 2.2)
        v = CartesianVector2D(x, y)
        self.assertAlmostEqual(v.x, x)
        self.assertAlmostEqual(v.y, y)
        with self.assertRaises(AttributeError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = CartesianVector2D(0, 0)
        (x, y) = (1.1, 2.2)
        v.x = x
        self.assertAlmostEqual(v.x, x)
        v.y = y
        self.assertAlmostEqual(v.y, y)
        with self.assertRaises(AttributeError):
            v.bad = 0


if __name__ == '__main__':
    unittest.main()
