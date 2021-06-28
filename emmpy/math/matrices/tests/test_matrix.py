"""Tests for the matrix module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""

import unittest

from emmpy.math.matrices.matrix import Matrix


class TestBuilder(unittest.TestCase):
    """Tests for the matrix module."""

    def test___new__(self):
        """Test the __new__ method."""
        # Constructor must not be invoked directly.
        with self.assertRaises(TypeError):
            Matrix()


if __name__ == '__main__':
    unittest.main()
