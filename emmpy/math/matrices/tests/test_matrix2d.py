"""Tests for the matrix2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.matrices.matrix2d import Matrix2D


class TestBuilder(unittest.TestCase):
    """Tests for the matrix2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-arg form
        m = Matrix2D()
        self.assertIsInstance(m, Matrix2D)
        for i in range(2):
            for j in  range(2):
                self.assertTrue(np.isnan(m[i, j]))
        # 1-arg forms.
        # list of lists
        data = [[1.1, 2.2], [3.3, 4.4]]
        m = Matrix2D(data)
        self.assertIsInstance(m, Matrix2D)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of tuples
        data = ((1.1, 2.2), (3.3, 4.4))
        m = Matrix2D(data)
        self.assertIsInstance(m, Matrix2D)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # list of tuples
        data = [(1.1, 2.2), (3.3, 4.4)]
        m = Matrix2D(data)
        self.assertIsInstance(m, Matrix2D)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of lists
        data = ([1.1, 2.2], [3.3, 4.4])
        m = Matrix2D(data)
        self.assertIsInstance(m, Matrix2D)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # ndarray
        data = [i*1.1 for i in range(4)]
        a = np.array(data).reshape((2, 2))
        m = Matrix2D(*data)
        self.assertIsInstance(m, Matrix2D)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], a[row, col])
        # 4-argument form - individual components
        data = [i*1.1 for i in range(4)]
        m = Matrix2D(*data)
        self.assertIsInstance(m, Matrix2D)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row*2 + col])
        # Invalid forms.
        for n in (2, 3, 5, 6, 7, 8, 9, 10):
            with self.assertRaises(ValueError):
                data = (None,)*n
                m = Matrix2D(*data)

if __name__ == '__main__':
    unittest.main()
