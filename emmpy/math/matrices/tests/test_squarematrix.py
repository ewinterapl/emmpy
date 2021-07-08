"""Tests for the squarematrix module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""

import unittest

from emmpy.math.matrices.squarematrix import SquareMatrix


class TestBuilder(unittest.TestCase):
    """Tests for the squarematrix module."""

    def test___new__(self):
        """Test the __new__ method."""
        # Constructor must not be invoked directly.
        # 1-arg form - number of elements in each dimension.
        # Use different sizes.
        for n in range(1, 11):
            # Positional form
            m = SquareMatrix.__new__(SquareMatrix, n)
            self.assertIsInstance(m, SquareMatrix)
            self.assertEqual(m.shape, (n, n))
            # Keyword form
            m = SquareMatrix(n)
            self.assertIsInstance(m, SquareMatrix)
            self.assertEqual(m.shape, (n, n))
        # Invalid forms.
        for n in (0, 2):
            with self.assertRaises(TypeError):
                args = (None,)*n
                m = SquareMatrix(*args)


if __name__ == '__main__':
    unittest.main()
