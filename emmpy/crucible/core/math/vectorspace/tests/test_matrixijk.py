"""Tests for the matrixijk module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


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
        # 9 args - element values in column-major order
        flat_data = data[0] + data[1] + data[2]
        m1 = MatrixIJK(*flat_data)
        for row in range(3):
            for col in range(3):
                k = row + col*3
                self.assertAlmostEqual(m1[row, col], flat_data[k])
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

    def test_invert(self):
        """Test the invert method."""
        data = [[1, 0, 5], [2, 1, 6], [3, 5, 0]]
        m1 = MatrixIJK(data)
        inv1 = np.linalg.inv(m1)
        m2 = m1.invert()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], inv1[row, col])

    def test_invort(self):
        """Test the invort method."""
        a = pi/3
        data = [[cos(a), 0, sin(a)], [0, 1, 0], [-sin(a), 0, cos(a)]]
        m1 = MatrixIJK(data)
        inv1 = np.linalg.inv(m1)
        m2 = m1.invort()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], inv1[row, col])

    def test_setTo(self):
        """Test the setTo method."""
        # 1-argument forms
        # list of tuples (for some heterogeneity)
        data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        m1 = MatrixIJK()
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # np.ndarray
        a = np.array(data)
        m1 = MatrixIJK()
        m2 = m1.setTo(a)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # MatrixIJK
        m = MatrixIJK(data)
        m1 = MatrixIJK()
        m2 = m1.setTo(m)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # 9 args - individual values, column-major oder
        flat_data = np.array(data).T.flatten()
        m1 = MatrixIJK()
        m2 = m1.setTo(*flat_data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # Invalid forms
        sizes = (0, 2, 3, 4, 5, 6, 7, 8, 10)
        for s in sizes:
            data = [None]*s
            with self.assertRaises(TypeError):
                m1.setTo(*data)

    def test_mtxv(self):
        """Test the mtxv method."""
        mdata = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        vdata1 = [1, 2, 3]
        m = MatrixIJK(mdata)
        v1 = VectorIJK(vdata1)
        # No buffer
        v3 = m.T.dot(v1)
        v2 = MatrixIJK.mtxv(m, v1)
        for col in range(3):
            self.assertAlmostEqual(v2[col], v3[col])
        # Buffer
        v4 = m.T.dot(v1)
        v3 = VectorIJK()
        v2 = MatrixIJK.mtxv(m, v1, v3)
        self.assertIs(v2, v3)
        for col in range(3):
            self.assertAlmostEqual(v2[col], v4[col])

    def test_mxv(self):
        """Test the mxv method."""
        mdata = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        vdata1 = [1, 2, 3]
        m = MatrixIJK(mdata)
        v1 = VectorIJK(vdata1)
        # No buffer
        v3 = m.dot(v1)
        v2 = MatrixIJK.mxv(m, v1)
        for col in range(3):
            self.assertAlmostEqual(v2[col], v3[col])
        # Buffer
        v4 = m.dot(v1)
        v3 = VectorIJK()
        v2 = MatrixIJK.mxv(m, v1, v3)
        self.assertIs(v2, v3)
        for col in range(3):
            self.assertAlmostEqual(v2[col], v4[col])


if __name__ == '__main__':
    unittest.main()
