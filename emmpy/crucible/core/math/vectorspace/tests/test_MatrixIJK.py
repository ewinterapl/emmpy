"""Tests for the matrixijk module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the mtrixijk module."""

    def test___init__(self):
        """Test the __new__ method."""

        # 0 arguments - empty matrix
        m = MatrixIJK()
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertTrue(np.isnan(m[row, col]))

        # 1 arg forms: 3x3 array-like of float
        # list of lists
        data = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        m = MatrixIJK(data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of tuples
        data = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
        m = MatrixIJK(data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # list of tuples
        data = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
        m = MatrixIJK(data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of lists
        data = ([0, 3, 6], [1, 4, 7], [2, 5, 8])
        m = MatrixIJK(data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # np.array
        a = np.array(data)
        m = MatrixIJK(a)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # MatrixIJK
        m2 = MatrixIJK(m)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])

        # 2 arg forms - scale factor and 3x3 array-like
        scale = -2.2
        # Scale and list of lists
        m = MatrixIJK(scale, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and tuple of tuples
        data = ((0, 3, 7), (1, 4, 7), (2, 5, 8))
        m = MatrixIJK(scale, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and list of tuples
        data = [(0, 3, 7), (1, 4, 7), (2, 5, 8)]
        m = MatrixIJK(scale, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and tuple of lists
        data = ([0, 3, 6], [1, 4, 7], [2, 5, 8])
        m = MatrixIJK(scale, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and np.ndarray
        a = np.array(data)
        m = MatrixIJK(scale, a)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and MatrixIJK
        m = MatrixIJK(data)
        m2 = MatrixIJK(scale, m)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])

        # 3 args - column vectors
        # lists
        v = [[row[0] for row in data],
             [row[1] for row in data],
             [row[2] for row in data]]
        m = MatrixIJK(*v)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuples
        v = [tuple([row[0] for row in data]),
             tuple([row[1] for row in data]),
             tuple([row[2] for row in data])]
        m = MatrixIJK(*v)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # np.ndarrays
        v = [np.array([row[0] for row in data]),
             np.array([row[1] for row in data]),
             np.array([row[2] for row in data])]
        m = MatrixIJK(*v)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # VectorIJKs
        v = [VectorIJK([row[0] for row in data]),
             VectorIJK([row[1] for row in data]),
             VectorIJK([row[2] for row in data])]
        m = MatrixIJK(*v)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])

        # 4 args - 3 column scale factors and array-like
        scales = (-1.1, -2.2, -3.3)
        # Scales and list of lists
        data = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        m = MatrixIJK(*scales, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # Scales and tuple of tuples
        data = ((0, 3, 7), (1, 4, 7), (2, 5, 8))
        m = MatrixIJK(scales, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # Scales and list of tuples
        data = [(0, 3, 7), (1, 4, 7), (2, 5, 8)]
        m = MatrixIJK(scales, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # Scales and tuple of lists
        data = ([0, 3, 6], [1, 4, 7], [2, 5, 8])
        m = MatrixIJK(scales, data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # Scale and np.ndarray
        a = np.array(data)
        m = MatrixIJK(scales, a)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # # Scale and MatrixIJK
        m2 = MatrixIJK(data)
        m = MatrixIJK(scales, m2)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])

        # 6 args - scale factors and columns
        # lists
        v = [[row[0] for row in data],
             [row[1] for row in data],
             [row[2] for row in data]]
        m = MatrixIJK(scales[0], v[0], scales[1], v[1], scales[2], v[2])
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # tuples
        v = [tuple([row[0] for row in data]),
             tuple([row[1] for row in data]),
             tuple([row[2] for row in data])]
        m = MatrixIJK(scales[0], v[0], scales[1], v[1], scales[2], v[2])
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # np.ndarrays
        v = [np.array([row[0] for row in data]),
             np.array([row[1] for row in data]),
             np.array([row[2] for row in data])]
        m = MatrixIJK(scales[0], v[0], scales[1], v[1], scales[2], v[2])
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])
        # VectorIJKs
        v = [VectorIJK([row[0] for row in data]),
             VectorIJK([row[1] for row in data]),
             VectorIJK([row[2] for row in data])]
        m = MatrixIJK(scales[0], v[0], scales[1], v[1], scales[2], v[2])
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], scales[col]*data[row][col])

        # 9 args - element values in row-major order
        data = list(range(9))
        m = MatrixIJK(*data)
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                k = row*3 + col
                self.assertAlmostEqual(m[row, col], k)

        # Invalid forms
        for n in (5, 7, 8, 10):
            args = (None,)*n
            with self.assertRaises(ValueError):
                m1 = MatrixIJK(*args)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        data = [i*1.1 for i in range(9)]
        m = MatrixIJK(*data)
        self.assertAlmostEqual(m.ii, 0)
        self.assertAlmostEqual(m.ij, 1.1)
        self.assertAlmostEqual(m.ik, 2.2)
        self.assertAlmostEqual(m.ji, 3.3)
        self.assertAlmostEqual(m.jj, 4.4)
        self.assertAlmostEqual(m.jk, 5.5)
        self.assertAlmostEqual(m.ki, 6.6)
        self.assertAlmostEqual(m.kj, 7.7)
        self.assertAlmostEqual(m.kk, 8.8)
        with self.assertRaises(KeyError):
            data = m.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        m = MatrixIJK()
        data = [i*1.1 for i in range(9)]
        m.ii = data[0]
        self.assertAlmostEqual(m.ii, data[0])
        m.ij = data[1]
        self.assertAlmostEqual(m.ij, data[1])
        m.ik = data[2]
        self.assertAlmostEqual(m.ik, data[2])
        m.ji = data[3]
        self.assertAlmostEqual(m.ji, data[3])
        m.jj = data[4]
        self.assertAlmostEqual(m.jj, data[4])
        m.jk = data[5]
        self.assertAlmostEqual(m.jk, data[5])
        m.ki = data[6]
        self.assertAlmostEqual(m.ki, data[6])
        m.kj = data[7]
        self.assertAlmostEqual(m.kj, data[7])
        m.kk = data[8]
        self.assertAlmostEqual(m.kk, data[8])
        with self.assertRaises(KeyError):
            m.bad = 0

    def test_setII(self):
        """Test the setII method."""
        m = MatrixIJK()
        m.setII(-1)
        self.assertAlmostEqual(m.ii, -1)

    def test_setJI(self):
        """Test the setJI method."""
        m = MatrixIJK()
        m.setJI(-1)
        self.assertAlmostEqual(m.ji, -1)

    def test_setKI(self):
        """Test the setKI method."""
        m = MatrixIJK()
        m.setKI(-1)
        self.assertAlmostEqual(m.ki, -1)

    def test_setIJ(self):
        """Test the setIJ method."""
        m = MatrixIJK()
        m.setIJ(-1)
        self.assertAlmostEqual(m.ij, -1)

    def test_setJJ(self):
        """Test the setJJ method."""
        m = MatrixIJK()
        m.setJJ(-1)
        self.assertAlmostEqual(m.jj, -1)

    def test_setKJ(self):
        """Test the setKJ method."""
        m = MatrixIJK()
        m.setKJ(-1)
        self.assertAlmostEqual(m.kj, -1)

    def test_setIK(self):
        """Test the setIK method."""
        m = MatrixIJK()
        m.setIK(-1)
        self.assertAlmostEqual(m.ik, -1)

    def test_setJK(self):
        """Test the setJK method."""
        m = MatrixIJK()
        m.setJK(-1)
        self.assertAlmostEqual(m.jk, -1)

    def test_setKK(self):
        """Test the setKK method."""
        m = MatrixIJK()
        m.setKK(-1)
        self.assertAlmostEqual(m.kk, -1)

    def test_set(self):
        """Test the set method."""
        m = MatrixIJK()
        for row in range(3):
            for col in range(3):
                val = row*10 + col
                m.set(row, col, val)
                self.assertAlmostEqual(m[row, col], val)

    def test_setIthColumn(self):
        """Test the setIthColumn method."""
        # list
        m = MatrixIJK()
        data = list(range(3))
        m.setIthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 0], data[row])
        # tuple
        m = MatrixIJK()
        data = tuple(range(3))
        m.setIthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 0], data[row])
        # np.ndarray
        m = MatrixIJK()
        data = np.array(range(3))
        m.setIthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 0], data[row])
        # VectorIJK
        m = MatrixIJK()
        data = VectorIJK(list(range(3)))
        m.setIthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 0], data[row])

    def test_setJthColumn(self):
        """Test the setJthColumn method."""
        # list
        m = MatrixIJK()
        data = list(range(3))
        m.setJthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 1], data[row])
        # tuple
        m = MatrixIJK()
        data = tuple(range(3))
        m.setJthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 1], data[row])
        # np.ndarray
        m = MatrixIJK()
        data = np.array(range(3))
        m.setJthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 1], data[row])
        # VectorIJK
        m = MatrixIJK()
        data = VectorIJK(list(range(3)))
        m.setJthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 1], data[row])

    def test_setKthColumn(self):
        """Test the setKthColumn method."""
        # list
        m = MatrixIJK()
        data = list(range(3))
        m.setKthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 2], data[row])
        # tuple
        m = MatrixIJK()
        data = tuple(range(3))
        m.setKthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 2], data[row])
        # np.ndarray
        m = MatrixIJK()
        data = np.array(range(3))
        m.setKthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 2], data[row])
        # VectorIJK
        m = MatrixIJK()
        data = VectorIJK(list(range(3)))
        m.setKthColumn(data)
        for row in range(3):
            self.assertAlmostEqual(m[row, 2], data[row])

    def test_setColumn(self):
        """Test the setColumn method."""
        m = MatrixIJK()
        data = list(range(3))
        v = VectorIJK(*data)
        for col in range(3):
            m.setColumn(col, v)
            for row in range(3):
                self.assertAlmostEqual(m[row, col], data[row])

    def test_setTo(self):
        """Test the setTo method."""
        m1 = MatrixIJK()
        # 1 arg forms
        # list of lists
        data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # tuple of tuples
        data = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # list of tuples
        data = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # tuple of lists
        data = ([0, 1, 2], [3, 4, 5], [6, 7, 8])
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # np.ndarray
        data = ([0, 1, 2], [3, 4, 5], [6, 7, 8])
        a = np.array(data)
        m2 = m1.setTo(a)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # matrix
        m3 = MatrixIJK(data)
        m2 = m1.setTo(m3)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # 2-arg forms: scale factor and array-like
        scale = -2.2
        # Scale and list of lists.
        data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and tuple of tuples
        data = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and list of tuples
        data = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and tuple of lists
        data = ([0, 1, 2], [3, 4, 5], [6, 7, 8])
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and np.ndarray
        a = np.array(data)
        m2 = m1.setTo(scale, a)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and matrix
        m3 = MatrixIJK(data)
        m2 = m1.setTo(scale, m3)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])

        # 3-arg forms: Column vectors
        data = ([0, 3, 6], [1, 4, 7], [2, 5, 8])
        # list of lists
        v = [[row[0] for row in data],
             [row[1] for row in data],
             [row[2] for row in data]]
        m2 = m1.setTo(*v)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # list of tuples
        v = [tuple([row[0] for row in data]),
             tuple([row[1] for row in data]),
             tuple([row[2] for row in data])]
        m2 = m1.setTo(*v)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # list of np.ndarray
        v = [np.array([row[0] for row in data]),
             np.array([row[1] for row in data]),
             np.array([row[2] for row in data])]
        m2 = m1.setTo(*v)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data[row][col])

        # 4 arg forms: scale an array-like by columns
        scales = (-1.1, -2.2, -3.3)
        # Scales and list of lists
        data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and tuple of tuples
        data = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and list of tuples
        data = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and tuple of lists
        data = ([0, 1, 2], [3, 4, 5], [6, 7, 8])
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and np.ndarray
        a = np.array(data)
        m2 = m1.setTo(*scales, a)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and MatrixIJK
        m3 = MatrixIJK(data)
        m2 = m1.setTo(*scales, m3)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # 6 arg forms: individually-scaled columns
        s = (-1.1, -2.2, -3.3)
        data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        # lists
        v = [[row[0] for row in data],
             [row[1] for row in data],
             [row[2] for row in data]]
        m1 = MatrixIJK()
        m2 = m1.setTo(s[0], v[0], s[1], v[1], s[2], v[2])
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])
        # tuples
        v = [tuple([row[0] for row in data]),
             tuple([row[1] for row in data]),
             tuple([row[2] for row in data])]
        m1 = MatrixIJK()
        m2 = m1.setTo(s[0], v[0], s[1], v[1], s[2], v[2])
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])
        # np.ndarray
        v = [np.array([row[0] for row in data]),
             np.array([row[1] for row in data]),
             np.array([row[2] for row in data])]
        m1 = MatrixIJK()
        m2 = m1.setTo(s[0], v[0], s[1], v[1], s[2], v[2])
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])
        # VectorIJK
        v = [VectorIJK([row[0] for row in data]),
             VectorIJK([row[1] for row in data]),
             VectorIJK([row[2] for row in data])]
        m1 = MatrixIJK()
        m2 = m1.setTo(s[0], v[0], s[1], v[1], s[2], v[2])
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])

        # 9 arg forms
        # individual values
        m1 = MatrixIJK()
        m2 = m1.setTo(*(data[0] + data[1] + data[2]))
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                k = col*3 + row
                self.assertAlmostEqual(m2[row, col], k)

        # Invalid forms
        for n in (0, 5, 7, 8, 10):
            data = [None]*n
            with self.assertRaises(ValueError):
                m1.setTo(*data)

    def test_transposeInPlace(self):
        """Test the tranpose method."""
        data = list(range(9))
        m1 = MatrixIJK(*data)
        m1_orig = MatrixIJK(m1)
        m2 = m1.transposeInPlace()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1_orig[col, row])

    def test_unitizeColumns(self):
        """Test the unitizeColumns method."""
        data1 = list(range(9))
        a1 = np.array(data1).reshape((3, 3))
        lengths = np.linalg.norm(a1, axis=0)
        a2 = a1/lengths
        m1 = MatrixIJK(*data1)
        m2 = m1.unitizeColumns()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], a2[row, col])

    def test_invert(self):
        """Test the invert method."""
        data = (1, 0, 5, 2, 1, 6, 3, 5, 0)
        data_inv = (-6, 5, -1, 3.6, -3, 0.8, 1.4, -1, 0.2)
        m1 = MatrixIJK(*data)
        m1_inv = MatrixIJK(*data_inv)
        m2 = m1.invert()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1_inv[row, col])

    def test_invort(self):
        """Test the invort method."""
        a = pi/3
        data = (cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        data_inv = (cos(a), 0, -sin(a), 0, 1, 0, sin(a), 0, cos(a))
        m1 = MatrixIJK(*data)
        m1_inv = MatrixIJK(*data_inv)
        m2 = m1.invort()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1_inv[row, col])

    def test_scale(self):
        """Test the scale method."""
        data = list(range(9))
        # 1 arg form
        # Single scale factor.
        scale = -1.1
        m1 = MatrixIJK(*data)
        m1_orig = MatrixIJK(m1)
        m2 = m1.scale(scale)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*m1_orig[row, col])
        # 3-arg form.
        # Column scale factors.
        scales = (-1.1, -2.2, -3.3)
        m1 = MatrixIJK(*data)
        m2 = m1.scale(*scales)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*m1_orig[row, col])
        # Invalid forms.
        for n in (0, 2, 4):
            data = [None]*n
            with self.assertRaises(ValueError):
                m1.scale(*data)

    def test_createTranspose(self):
        """Test the createTranspose method."""
        data = list(range(9))
        m1 = MatrixIJK(*data)
        m2 = m1.createTranspose()
        self.assertIsInstance(m2, MatrixIJK)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m2[i, j], m1[j, i])

    def test_createUnitizedColumns(self):
        """Test the createUnitizedColumns method."""
        data1 = list(range(9))
        a1 = np.array(data1).reshape((3, 3))
        lengths = np.linalg.norm(a1, axis=0)
        a2 = a1/lengths
        m1 = MatrixIJK(*data1)
        m2 = m1.createUnitizedColumns()
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], a2[row, col])

    def test_createInverse(self):
        """Test the createInverse method."""
        data = (1, 0, 5, 2, 1, 6, 3, 5, 0)
        data_inv = (-6, 5, -1, 3.6, -3, 0.8, 1.4, -1, 0.2)
        m1 = MatrixIJK(*data)
        m1_inv = MatrixIJK(*data_inv)
        m2 = m1.createInverse()
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1_inv[row, col])

    def test_createInvorted(self):
        """Test the createInvorted method."""
        a = pi/3
        data = (cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        data_inv = (cos(a), 0, -sin(a), 0, 1, 0, sin(a), 0, cos(a))
        m1 = MatrixIJK(*data)
        m1_inv = MatrixIJK(*data_inv)
        m2 = m1.createInvorted()
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1_inv[row, col])

    def test_setToTranspose(self):
        """Test the setToTranspose method."""
        data = list(range(9))
        m1 = MatrixIJK(*data)
        m2 = MatrixIJK()
        m3 = m2.setToTranspose(m1)
        self.assertIs(m3, m2)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m3[i, j], m1[j, i])

    def test_setToUnitizedColumns(self):
        """Test the createUnitizedColumns method."""
        data1 = list(range(9))
        a1 = np.array(data1).reshape((3, 3))
        lengths = np.linalg.norm(a1, axis=0)
        a2 = a1/lengths
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK()
        m3 = m2.setToUnitizedColumns(m1)
        self.assertIs(m3, m2)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m3[row, col], a2[row, col])

    def test_setToInverse(self):
        """Test the setToInverse method."""
        data = (1, 0, 5, 2, 1, 6, 3, 5, 0)
        data_inv = (-6, 5, -1, 3.6, -3, 0.8, 1.4, -1, 0.2)
        m1 = MatrixIJK(*data)
        m1_inv = MatrixIJK(*data_inv)
        m2 = MatrixIJK()
        m3 = m2.setToInverse(m1)
        self.assertIs(m3, m2)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m3[row, col], m1_inv[row, col])

    def test_setToInvorted(self):
        """Test the setToInvorted method."""
        a = pi/3
        data = (cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        data_inv = (cos(a), 0, -sin(a), 0, 1, 0, sin(a), 0, cos(a))
        m1 = MatrixIJK(*data)
        m1_inv = MatrixIJK(*data_inv)
        m2 = MatrixIJK()
        m3 = m2.setToInvorted(m1)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m3[row, col], m1_inv[row, col])

    def test_add(self):
        """Test the add method."""
        data1 = list(range(1, 10))
        data2 = list(reversed(data1))
        data3 = [x1 + x2 for (x1, x2) in zip(data1, data2)]
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = MatrixIJK(*data3)
        # 1-arg form.
        # No buffer.
        m4 = m1.add(m2)
        self.assertIsInstance(m4, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg form.
        # Use buffer.
        m4 = MatrixIJK()
        m5 = m1.add(m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            with self.assertRaises(ValueError):
                data = [None]*n
                m1.add(*data)

    def test_subtract(self):
        """Test the subtract method."""
        data1 = list(range(1, 10))
        data2 = list(reversed(data1))
        data3 = [x1 - x2 for (x1, x2) in zip(data1, data2)]
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = MatrixIJK(*data3)
        # 1-arg form.
        # No buffer.
        m4 = m1.subtract(m2)
        self.assertIsInstance(m4, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg form.
        # Use buffer.
        m4 = MatrixIJK()
        m5 = m1.subtract(m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            with self.assertRaises(ValueError):
                data = [None]*n
                m1.subtract(*data)

    def test_mxm(self):
        """Test the mxm method."""
        data1 = list(range(9))
        data2 = list(reversed(data1))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        p = np.zeros((3, 3))
        for row in range(3):
            for col in range(3):
                for k in range(3):
                    p[row][col] += m1[row][k]*m2[k][col]
        m3 = MatrixIJK(p)
        # 1-arg version
        # No buffer.
        m4 = m1.mxm(m2)
        self.assertIsInstance(m4, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg version.
        # With buffer.
        m4 = MatrixIJK()
        m5 = m1.mxm(m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                m3 = m1.mxm(*data)

    def test_mxmt(self):
        """Test the mxmt method."""
        data1 = list(range(9))
        data2 = list(reversed(data1))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = m1.dot(m2.T)
        # 1-arg version
        # No buffer.
        m4 = MatrixIJK.mxmt(m1, m2)
        self.assertIsInstance(m4, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg version.
        # With buffer.
        m4 = MatrixIJK()
        m5 = m1.mxmt(m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                m3 = m1.mxmt(*data)

    def test_mtxm(self):
        """Test the mtxm method."""
        data1 = list(range(1, 10))
        data2 = list(reversed(data1))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = m1.T.dot(m2)
        # 1-arg form
        # No buffer.
        m4 = m1.mtxm(m2)
        self.assertIsInstance(m4, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg form.
        # Use buffer.
        m4 = MatrixIJK()
        m5 = m1.mtxm(m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                m3 = m1.mtxm(*data)

    def test_mxmadd(self):
        """Test the mxmadd method."""
        data1 = list(range(1, 10))
        data2 = list(range(2, 10)) + [1]
        data3 = list(range(4, 10)) + list(range(1, 4))
        data4 = list(range(7, 10)) + list(range(1, 7))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = MatrixIJK(*data3)
        m4 = MatrixIJK(*data4)
        m5a = MatrixIJK.mxm(m1, m2)
        m5b = MatrixIJK.mxm(m3, m4)
        m5 = m5a + m5b
        # 4-arg form.
        # No buffer.
        m6 = MatrixIJK.mxmadd(m1, m2, m3, m4)
        self.assertIsInstance(m6, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m6[row, col], m5[row, col])
        # 5-arg form.
        # Use buffer.
        m6 = MatrixIJK()
        m7 = MatrixIJK.mxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m7[row, col], m5[row, col])

    def test_mxmtadd(self):
        """Test the mxmtadd method."""
        data1 = list(range(1, 10))
        data2 = list(range(2, 10)) + [1]
        data3 = list(range(4, 10)) + list(range(1, 4))
        data4 = list(range(7, 10)) + list(range(1, 7))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = MatrixIJK(*data3)
        m4 = MatrixIJK(*data4)
        m5a = MatrixIJK.mxmt(m1, m2)
        m5b = MatrixIJK.mxmt(m3, m4)
        m5 = m5a + m5b
        # 4-arg form.
        # No buffer.
        m6 = MatrixIJK.mxmtadd(m1, m2, m3, m4)
        self.assertIsInstance(m6, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m6[row, col], m5[row, col])
        # 5-arg form.
        # Use buffer.
        m6 = MatrixIJK()
        m7 = MatrixIJK.mxmtadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m7[row, col], m5[row, col])

    def test_mtxmadd(self):
        """Test the mtxmadd method."""
        data1 = list(range(1, 10))
        data2 = list(range(2, 10)) + [1]
        data3 = list(range(4, 10)) + list(range(1, 4))
        data4 = list(range(7, 10)) + list(range(1, 7))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = MatrixIJK(*data3)
        m4 = MatrixIJK(*data4)
        m5a = MatrixIJK.mtxm(m1, m2)
        m5b = MatrixIJK.mtxm(m3, m4)
        m5 = m5a + m5b
        # 4-arg form.
        # No buffer.
        m6 = MatrixIJK.mtxmadd(m1, m2, m3, m4)
        self.assertIsInstance(m6, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m6[row, col], m5[row, col])
        # 5-arg form.
        # Use buffer.
        m6 = MatrixIJK()
        m7 = MatrixIJK.mtxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m7[row, col], m5[row, col])

    def test_mxv(self):
        """Test the mxv method."""
        data1 = list(range(9))
        data2 = list(range(3))
        m1 = MatrixIJK(*data1)
        v1 = VectorIJK(*data2)
        v2 = m1.dot(v1)
        # 1-arg form.
        # No buffer.
        v3 = m1.mxv(v1)
        self.assertIsInstance(v3, VectorIJK)
        for row in range(3):
            self.assertAlmostEqual(v3[row], v2[row])
        # 2-arg form.
        # Use buffer.
        v3 = VectorIJK()
        v4 = m1.mxv(v1, v3)
        self.assertIs(v4, v3)
        for row in range(3):
            self.assertAlmostEqual(v4[row], v2[row])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                v2 = m1.mxv(*data)

    def test_mtxv(self):
        """Test the mtxv method."""
        data1 = list(range(9))
        data2 = list(range(3))
        m1 = MatrixIJK(*data1)
        v1 = VectorIJK(*data2)
        v2 = m1.T.dot(v1)
        # 1-arg form.
        # No buffer.
        v3 = m1.mtxv(v1)
        self.assertIsInstance(v3, VectorIJK)
        for row in range(3):
            self.assertAlmostEqual(v3[row], v2[row])
        # 2-arg form.
        # Use buffer.
        v3 = VectorIJK()
        v4 = m1.mtxv(v1, v3)
        self.assertIs(v4, v3)
        for row in range(3):
            self.assertAlmostEqual(v4[row], v2[row])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                v2 = m1.mtxv(*data)


if __name__ == '__main__':
    unittest.main()
