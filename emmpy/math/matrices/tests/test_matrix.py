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
        # 2-arg form - row and column counts.
        # Use different sizes.
        for nrows in range(1, 11):
            for ncols in range(1, 11):
                # Positional form
                m = Matrix.__new__(Matrix, nrows, ncols)
                self.assertIsInstance(m, Matrix)
                self.assertEqual(m.shape, (nrows, ncols))
                # Keyword form
                m = Matrix(nrows=nrows, ncols=ncols)
                self.assertIsInstance(m, Matrix)
                self.assertEqual(m.shape, (nrows, ncols))
        # Invalid forms.
        for n in (0, 1, 3):
            with self.assertRaises(TypeError):
                args = (None,)*n
                m = Matrix(*args)


if __name__ == '__main__':
    unittest.main()
