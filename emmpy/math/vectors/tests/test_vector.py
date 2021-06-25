"""Tests for the vector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""

import unittest

from emmpy.math.vectors.vector import Vector


class TestBuilder(unittest.TestCase):
    """Tests for the vector module."""

    def test___new__(self):
        """Test the __new__ method."""
        # Constructor must not be invoked directly.
        with self.assertRaises(TypeError):
            Vector()


if __name__ == '__main__':
    unittest.main()
