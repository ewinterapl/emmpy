"""Tests for the matrixijk module."""


import unittest

import numpy as np

from emmpy.math.matrices.matrixijk import MatrixIJK


class TestBuilder(unittest.TestCase):
    """Tests for the matrixijk module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0 arguments - empty matrix, all NaN
        m1 = MatrixIJK()
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertTrue(np.isnan(m1[row, col]))
        # 1 arg forms
        # list of tuples (just to add some heterogeneity)
        data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        m1 = MatrixIJK(data)
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data[row][col])
        # np.ndarray
        a1 = np.array(data)
        m1 = MatrixIJK(a1)
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data[row][col])
        # MatrixIJK
        m2 = MatrixIJK(data)
        m1 = MatrixIJK(m2)
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data[row][col])
        # Invalid forms
        sizes = (2, 3, 4, 5, 6, 7, 8, 10)
        for s in sizes:
            with self.assertRaises(ValueError):
                data = [None]*s
                m1 = MatrixIJK(*data)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = MatrixIJK(data)
        self.assertAlmostEqual(m.ii, data[0][0])
        self.assertAlmostEqual(m.ji, data[1][0])
        self.assertAlmostEqual(m.ki, data[2][0])
        self.assertAlmostEqual(m.ij, data[0][1])
        self.assertAlmostEqual(m.jj, data[1][1])
        self.assertAlmostEqual(m.kj, data[2][1])
        self.assertAlmostEqual(m.ik, data[0][2])
        self.assertAlmostEqual(m.jk, data[1][2])
        self.assertAlmostEqual(m.kk, data[2][2])
        with self.assertRaises(KeyError):
            data = m.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        m = MatrixIJK()
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m.ii = data[0][0]
        m.ji = data[1][0]
        m.ki = data[2][0]
        m.ij = data[0][1]
        m.jj = data[1][1]
        m.kj = data[2][1]
        m.ik = data[0][2]
        m.jk = data[1][2]
        m.kk = data[2][2]
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        with self.assertRaises(KeyError):
            m.bad = 0


if __name__ == '__main__':
    unittest.main()
