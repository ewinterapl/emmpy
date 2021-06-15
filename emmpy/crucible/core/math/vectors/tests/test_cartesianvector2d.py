"""Tests for the cartesianvector2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.crucible.core.math.vectors.cartesianvector2d import (
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
            v.z


if __name__ == '__main__':
    unittest.main()
