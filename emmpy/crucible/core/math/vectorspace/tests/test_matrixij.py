"""Tests for the matrixij module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):
    """Tests for the matrixij module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0 arguments - empty matrix, all NaN
        m1 = MatrixIJ()
        self.assertIsInstance(m1, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertTrue(np.isnan(m1[row, col]))
        # 1-argument forms: 2x2 array-like of float
        # list of tuples (just to add some heterogeneity)
        data = [(0, 1), (2, 3)]
        m1 = MatrixIJ(data)
        self.assertIsInstance(m1, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m1[row, col], data[row][col])
        # np.ndarray
        a1 = np.array(data)
        m1 = MatrixIJ(a1)
        self.assertIsInstance(m1, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m1[row, col], data[row][col])
        # MatrixIJ
        m2 = MatrixIJ(data)
        m1 = MatrixIJ(m2)
        self.assertIsInstance(m1, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m1[row, col], data[row][col])
        # 4  args - individual elements in column-major order
        flat_data = data[0] + data[1]
        m1 = MatrixIJ(*flat_data)
        for row in range(2):
            for col in range(2):
                k = row + col*2
                self.assertAlmostEqual(m1[row, col], flat_data[k])
        # Invalid forms
        sizes = (2, 3, 5)
        for s in sizes:
            data = [None]*s
            with self.assertRaises(TypeError):
                m = MatrixIJ(*data)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        data = [[1, 2], [3, 4]]
        m = MatrixIJ(data)
        self.assertAlmostEqual(m.ii, data[0][0])
        self.assertAlmostEqual(m.ji, data[1][0])
        self.assertAlmostEqual(m.ij, data[0][1])
        self.assertAlmostEqual(m.jj, data[1][1])
        with self.assertRaises(KeyError):
            data = m.bad

    def test___setattr__(self):
        """Test the __getattr__ method."""
        data = [[1.1, 2.2], [3.3, 4.4]]
        m = MatrixIJ()
        m.ii = data[0][0]
        m.ij = data[0][1]
        m.ji = data[1][0]
        m.jj = data[1][1]
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        with self.assertRaises(KeyError):
            data = m.bad

    def test_invort(self):
        """Test the invort method."""
        a = pi/3
        m1 = MatrixIJ(cos(a), sin(a), -sin(a), cos(a))
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
        data = [(0, 2), (1, 3)]
        m1 = MatrixIJ()
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # np.ndarray
        a = np.array(data)
        m1 = MatrixIJ()
        m2 = m1.setTo(a)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # MatrixIJ
        m0 = MatrixIJ(data)
        m1 = MatrixIJ()
        m2 = m1.setTo(m0)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # 4-argument forms
        # 4 elements in column-major order
        m1 = MatrixIJ()
        m2 = m1.setTo(data[0][0], data[1][0], data[0][1], data[1][1])
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # Invalid forms
        sizes = (0, 5)
        for s in sizes:
            data = [None]*s
            with self.assertRaises(ValueError):
                m2.setTo(*data)

    def test_mxv(self):
        """Test the mxv method."""
        mdata = [[1, 2], [3, 4]]
        vdata1 = [1, 2]
        m = MatrixIJ(mdata)
        v1 = VectorIJ(vdata1)
        # No buffer
        v3 = m.dot(v1)
        v2 = MatrixIJ.mxv(m, v1)
        for col in range(2):
            self.assertAlmostEqual(v2[col], v3[col])
        # Buffer
        v4 = m.dot(v1)
        v3 = VectorIJ()
        v2 = MatrixIJ.mxv(m, v1, v3)
        self.assertIs(v2, v3)
        for col in range(2):
            self.assertAlmostEqual(v2[col], v4[col])


if __name__ == '__main__':
    unittest.main()
