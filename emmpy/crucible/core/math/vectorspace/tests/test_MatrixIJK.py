"""Tests for the matrixijk module."""


from math import cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the matrixijk module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0 arguments - empty matrix
        m = MatrixIJK()
        self.assertIsInstance(m, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertTrue(np.isnan(m[row, col]))
        # 1 arg - list of lists
        m = MatrixIJK([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 4)
        self.assertAlmostEqual(m.ki, 7)
        self.assertAlmostEqual(m.ij, 2)
        self.assertAlmostEqual(m.jj, 5)
        self.assertAlmostEqual(m.kj, 8)
        self.assertAlmostEqual(m.ik, 3)
        self.assertAlmostEqual(m.jk, 6)
        self.assertAlmostEqual(m.kk, 9)
        # 1 arg - copy
        m2 = MatrixIJK(m)
        self.assertAlmostEqual(m2.ii, 1)
        self.assertAlmostEqual(m2.ji, 4)
        self.assertAlmostEqual(m2.ki, 7)
        self.assertAlmostEqual(m2.ij, 2)
        self.assertAlmostEqual(m2.jj, 5)
        self.assertAlmostEqual(m2.kj, 8)
        self.assertAlmostEqual(m2.ik, 3)
        self.assertAlmostEqual(m2.jk, 6)
        self.assertAlmostEqual(m2.kk, 9)
        # 2 args - scale factor and matrix
        m2 = MatrixIJK(-2, m)
        self.assertAlmostEqual(m2.ii, -2)
        self.assertAlmostEqual(m2.ji, -8)
        self.assertAlmostEqual(m2.ki, -14)
        self.assertAlmostEqual(m2.ij, -4)
        self.assertAlmostEqual(m2.jj, -10)
        self.assertAlmostEqual(m2.kj, -16)
        self.assertAlmostEqual(m2.ik, -6)
        self.assertAlmostEqual(m2.jk, -12)
        self.assertAlmostEqual(m2.kk, -18)
        # 3 args - column vectors
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(4, 5, 6)
        v3 = VectorIJK(7, 8, 9)
        m = MatrixIJK(v1, v2, v3)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)
        self.assertAlmostEqual(m.ki, 3)
        self.assertAlmostEqual(m.ij, 4)
        self.assertAlmostEqual(m.jj, 5)
        self.assertAlmostEqual(m.kj, 6)
        self.assertAlmostEqual(m.ik, 7)
        self.assertAlmostEqual(m.jk, 8)
        self.assertAlmostEqual(m.kk, 9)
        # 4 args - 3 column scale factors and matrix
        m2 = MatrixIJK(-1, 2, 3, m)
        self.assertAlmostEqual(m2.ii, -1)
        self.assertAlmostEqual(m2.ji, -2)
        self.assertAlmostEqual(m2.ki, -3)
        self.assertAlmostEqual(m2.ij, 8)
        self.assertAlmostEqual(m2.jj, 10)
        self.assertAlmostEqual(m2.kj, 12)
        self.assertAlmostEqual(m2.ik, 21)
        self.assertAlmostEqual(m2.jk, 24)
        self.assertAlmostEqual(m2.kk, 27)
        # 6 args - scale factors and columns
        m2 = MatrixIJK(-1, v1, 2, v2, 3, v3)
        self.assertAlmostEqual(m2.ii, -1)
        self.assertAlmostEqual(m2.ji, -2)
        self.assertAlmostEqual(m2.ki, -3)
        self.assertAlmostEqual(m2.ij, 8)
        self.assertAlmostEqual(m2.jj, 10)
        self.assertAlmostEqual(m2.kj, 12)
        self.assertAlmostEqual(m2.ik, 21)
        self.assertAlmostEqual(m2.jk, 24)
        self.assertAlmostEqual(m2.kk, 27)
        # 9 args - element values
        m = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)
        self.assertAlmostEqual(m.ki, 3)
        self.assertAlmostEqual(m.ij, 4)
        self.assertAlmostEqual(m.jj, 5)
        self.assertAlmostEqual(m.kj, 6)
        self.assertAlmostEqual(m.ik, 7)
        self.assertAlmostEqual(m.jk, 8)
        self.assertAlmostEqual(m.kk, 9)
        # Invalid form
        sizes = (5, 7, 8, 10)
        for s in sizes:
            with self.assertRaises(ValueError):
                data = [None]*s
                m = MatrixIJK(*data)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        # COLUMN-MAJOR ORDER
        data = [i*1.1 for i in range(9)]
        m = MatrixIJK(*data)
        self.assertAlmostEqual(m.ii, 0)
        self.assertAlmostEqual(m.ji, 1.1)
        self.assertAlmostEqual(m.ki, 2.2)
        self.assertAlmostEqual(m.ij, 3.3)
        self.assertAlmostEqual(m.jj, 4.4)
        self.assertAlmostEqual(m.kj, 5.5)
        self.assertAlmostEqual(m.ik, 6.6)
        self.assertAlmostEqual(m.jk, 7.7)
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

    def test_createTranspose(self):
        """Test the createTranspose method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = m1.createTranspose()
        self.assertAlmostEqual(m2.ii, 1)
        self.assertAlmostEqual(m2.ji, 4)
        self.assertAlmostEqual(m2.ki, 7)
        self.assertAlmostEqual(m2.ij, 2)
        self.assertAlmostEqual(m2.jj, 5)
        self.assertAlmostEqual(m2.kj, 8)
        self.assertAlmostEqual(m2.ik, 3)
        self.assertAlmostEqual(m2.jk, 6)
        self.assertAlmostEqual(m2.kk, 9)

    def test_createUnitizedColumns(self):
        """Test the createUnitizedColumns method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = m1.createUnitizedColumns()
        self.assertAlmostEqual(m2.ii, 1/sqrt(14))
        self.assertAlmostEqual(m2.ji, 2/sqrt(14))
        self.assertAlmostEqual(m2.ki, 3/sqrt(14))
        self.assertAlmostEqual(m2.ij, 4/sqrt(77))
        self.assertAlmostEqual(m2.jj, 5/sqrt(77))
        self.assertAlmostEqual(m2.kj, 6/sqrt(77))
        self.assertAlmostEqual(m2.ik, 7/sqrt(194))
        self.assertAlmostEqual(m2.jk, 8/sqrt(194))
        self.assertAlmostEqual(m2.kk, 9/sqrt(194))

    def test_createInverse(self):
        """Test the createInverse method."""
        m = MatrixIJK(1, 0, 5, 2, 1, 6, 3, 5, 0)
        m2 = m.createInverse()
        self.assertAlmostEqual(m2.ii, -6)
        self.assertAlmostEqual(m2.ji, 5)
        self.assertAlmostEqual(m2.ki, -1)
        self.assertAlmostEqual(m2.ij, 3.6)
        self.assertAlmostEqual(m2.jj, -3)
        self.assertAlmostEqual(m2.kj, 0.8)
        self.assertAlmostEqual(m2.ik, 1.4)
        self.assertAlmostEqual(m2.jk, -1)
        self.assertAlmostEqual(m2.kk, 0.2)
        m3 = m2.createInverse(1e-4)
        self.assertAlmostEqual(m3.ii, 1)
        self.assertAlmostEqual(m3.ji, 0)
        self.assertAlmostEqual(m3.ki, 5)
        self.assertAlmostEqual(m3.ij, 2)
        self.assertAlmostEqual(m3.jj, 1)
        self.assertAlmostEqual(m3.kj, 6)
        self.assertAlmostEqual(m3.ik, 3)
        self.assertAlmostEqual(m3.jk, 5)
        self.assertAlmostEqual(m3.kk, 0)

    def test_createInvorted(self):
        """Test the createInvorted method."""
        a = pi/3
        m = MatrixIJK(cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        m2 = m.createInvorted()
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, -sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))

    def test_transpose(self):
        """Test the transpose method."""
        # COLUMN-MAJOR ORDER
        m = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = m.transpose()
        self.assertIs(m2, m)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 4)
        self.assertAlmostEqual(m.ki, 7)
        self.assertAlmostEqual(m.ij, 2)
        self.assertAlmostEqual(m.jj, 5)
        self.assertAlmostEqual(m.kj, 8)
        self.assertAlmostEqual(m.ik, 3)
        self.assertAlmostEqual(m.jk, 6)
        self.assertAlmostEqual(m.kk, 9)

    def test_unitizeColumns(self):
        """Test the unitizeColumns method."""
        m = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m.unitizeColumns()
        self.assertAlmostEqual(m.ii, 1/sqrt(14))
        self.assertAlmostEqual(m.ji, 2/sqrt(14))
        self.assertAlmostEqual(m.ki, 3/sqrt(14))
        self.assertAlmostEqual(m.ij, 4/sqrt(77))
        self.assertAlmostEqual(m.jj, 5/sqrt(77))
        self.assertAlmostEqual(m.kj, 6/sqrt(77))
        self.assertAlmostEqual(m.ik, 7/sqrt(194))
        self.assertAlmostEqual(m.jk, 8/sqrt(194))
        self.assertAlmostEqual(m.kk, 9/sqrt(194))

    def test_invert(self):
        """Test the invert method."""
        m = MatrixIJK(1, 0, 5, 2, 1, 6, 3, 5, 0)
        m2 = m.invert()
        self.assertIs(m2, m)
        self.assertAlmostEqual(m.ii, -6)
        self.assertAlmostEqual(m.ji, 5)
        self.assertAlmostEqual(m.ki, -1)
        self.assertAlmostEqual(m.ij, 3.6)
        self.assertAlmostEqual(m.jj, -3)
        self.assertAlmostEqual(m.kj, 0.8)
        self.assertAlmostEqual(m.ik, 1.4)
        self.assertAlmostEqual(m.jk, -1)
        self.assertAlmostEqual(m.kk, 0.2)
        with self.assertRaises(Exception):
            m = MatrixIJK(0, 0, 0, 0, 0, 0, 0, 0, 0)
            m.invert()

    def test_invort(self):
        """Test the invort method."""
        a = pi/3
        m = MatrixIJK(cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        m.invort()
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, -sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))

    def test_scale(self):
        """Test the scale method."""
        m = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = m.scale(-2)
        self.assertIs(m2, m)
        self.assertAlmostEqual(m.ii, -2)
        self.assertAlmostEqual(m.ji, -4)
        self.assertAlmostEqual(m.ki, -6)
        self.assertAlmostEqual(m.ij, -8)
        self.assertAlmostEqual(m.jj, -10)
        self.assertAlmostEqual(m.kj, -12)
        self.assertAlmostEqual(m.ik, -14)
        self.assertAlmostEqual(m.jk, -16)
        self.assertAlmostEqual(m.kk, -18)
        m2 = m.scale(-1, -2, -3)
        self.assertIs(m2, m)
        self.assertAlmostEqual(m.ii, 2)
        self.assertAlmostEqual(m.ji, 4)
        self.assertAlmostEqual(m.ki, 6)
        self.assertAlmostEqual(m.ij, 16)
        self.assertAlmostEqual(m.jj, 20)
        self.assertAlmostEqual(m.kj, 24)
        self.assertAlmostEqual(m.ik, 42)
        self.assertAlmostEqual(m.jk, 48)
        self.assertAlmostEqual(m.kk, 54)

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
        m.set(0, 0, 1)
        m.set(1, 0, 2)
        m.set(2, 0, 3)
        m.set(0, 1, 4)
        m.set(1, 1, 5)
        m.set(2, 1, 6)
        m.set(0, 2, 7)
        m.set(1, 2, 8)
        m.set(2, 2, 9)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)
        self.assertAlmostEqual(m.ki, 3)
        self.assertAlmostEqual(m.ij, 4)
        self.assertAlmostEqual(m.jj, 5)
        self.assertAlmostEqual(m.kj, 6)
        self.assertAlmostEqual(m.ik, 7)
        self.assertAlmostEqual(m.jk, 8)
        self.assertAlmostEqual(m.kk, 9)
        with self.assertRaises(Exception):
            m.set(0, 3, 0)
        with self.assertRaises(Exception):
            m.set(1, 3, 0)
        with self.assertRaises(Exception):
            m.set(2, 3, 0)
        with self.assertRaises(Exception):
            m.set(3, 0, 0)

    def test_setIthColumn(self):
        """Test the setIthColumn method."""
        m = MatrixIJK()
        v = VectorIJK(1, 2, 3)
        m.setIthColumn(v)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)
        self.assertAlmostEqual(m.ki, 3)

    def test_setJthColumn(self):
        """Test the setJthColumn method."""
        m = MatrixIJK()
        v = VectorIJK(1, 2, 3)
        m.setJthColumn(v)
        self.assertAlmostEqual(m.ij, 1)
        self.assertAlmostEqual(m.jj, 2)
        self.assertAlmostEqual(m.kj, 3)

    def test_setKthColumn(self):
        """Test the setKthColumn method."""
        m = MatrixIJK()
        v = VectorIJK(1, 2, 3)
        m.setKthColumn(v)
        self.assertAlmostEqual(m.ik, 1)
        self.assertAlmostEqual(m.jk, 2)
        self.assertAlmostEqual(m.kk, 3)

    def test_setColumn(self):
        """Test the setColumn method."""
        m = MatrixIJK()
        v = VectorIJK(1, 2, 3)
        m.setColumn(0, v)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)
        self.assertAlmostEqual(m.ki, 3)
        m.setColumn(1, v)
        self.assertAlmostEqual(m.ij, 1)
        self.assertAlmostEqual(m.jj, 2)
        self.assertAlmostEqual(m.kj, 3)
        m.setColumn(2, v)
        self.assertAlmostEqual(m.ik, 1)
        self.assertAlmostEqual(m.jk, 2)
        self.assertAlmostEqual(m.kk, 3)
        with self.assertRaises(Exception):
            m.setColumn(3, v)

    def test_setTo(self):
        """Test the setTo method."""
        m1 = MatrixIJK()
        # 1 arg - list of lists
        m3 = m1.setTo([[1, 4, 7, 4], [2, 5, 8, 9], [3, 6, 9, 2], [3, 4, 5, 6]])
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 2)
        self.assertAlmostEqual(m1.ki, 3)
        self.assertAlmostEqual(m1.ij, 4)
        self.assertAlmostEqual(m1.jj, 5)
        self.assertAlmostEqual(m1.kj, 6)
        self.assertAlmostEqual(m1.ik, 7)
        self.assertAlmostEqual(m1.jk, 8)
        self.assertAlmostEqual(m1.kk, 9)
        # 1 arg - copy existing matrix
        m2 = MatrixIJK()
        m3 = m2.setTo(m1)
        self.assertIs(m3, m2)
        self.assertAlmostEqual(m2.ii, 1)
        self.assertAlmostEqual(m2.ji, 2)
        self.assertAlmostEqual(m2.ki, 3)
        self.assertAlmostEqual(m2.ij, 4)
        self.assertAlmostEqual(m2.jj, 5)
        self.assertAlmostEqual(m2.kj, 6)
        self.assertAlmostEqual(m2.ik, 7)
        self.assertAlmostEqual(m2.jk, 8)
        self.assertAlmostEqual(m2.kk, 9)
        # 2 args - scale a matrix
        m2.setTo(-2, m1)
        self.assertAlmostEqual(m2.ii, -2)
        self.assertAlmostEqual(m2.ji, -4)
        self.assertAlmostEqual(m2.ki, -6)
        self.assertAlmostEqual(m2.ij, -8)
        self.assertAlmostEqual(m2.jj, -10)
        self.assertAlmostEqual(m2.kj, -12)
        self.assertAlmostEqual(m2.ik, -14)
        self.assertAlmostEqual(m2.jk, -16)
        self.assertAlmostEqual(m2.kk, -18)
        # 3 args - column vectors
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(4, 5, 6)
        v3 = VectorIJK(7, 8, 9)
        m3 = m2.setTo(v1, v2, v3)
        self.assertIs(m3, m2)
        self.assertAlmostEqual(m2.ii, 1)
        self.assertAlmostEqual(m2.ji, 2)
        self.assertAlmostEqual(m2.ki, 3)
        self.assertAlmostEqual(m2.ij, 4)
        self.assertAlmostEqual(m2.jj, 5)
        self.assertAlmostEqual(m2.kj, 6)
        self.assertAlmostEqual(m2.ik, 7)
        self.assertAlmostEqual(m2.jk, 8)
        self.assertAlmostEqual(m2.kk, 9)
        # 4 args - scale a matrix by columns
        m3 = m2.setTo(-1, 2, 3, m1)
        self.assertIs(m3, m2)
        self.assertAlmostEqual(m2.ii, -1)
        self.assertAlmostEqual(m2.ji, -2)
        self.assertAlmostEqual(m2.ki, -3)
        self.assertAlmostEqual(m2.ij, 8)
        self.assertAlmostEqual(m2.jj, 10)
        self.assertAlmostEqual(m2.kj, 12)
        self.assertAlmostEqual(m2.ik, 21)
        self.assertAlmostEqual(m2.jk, 24)
        self.assertAlmostEqual(m2.kk, 27)
        # 6 args - scaled column vectors
        m3 = m2.setTo(-1, v1, 2, v2, 3, v3)
        self.assertIs(m3, m2)
        self.assertAlmostEqual(m2.ii, -1)
        self.assertAlmostEqual(m2.ji, -2)
        self.assertAlmostEqual(m2.ki, -3)
        self.assertAlmostEqual(m2.ij, 8)
        self.assertAlmostEqual(m2.jj, 10)
        self.assertAlmostEqual(m2.kj, 12)
        self.assertAlmostEqual(m2.ik, 21)
        self.assertAlmostEqual(m2.jk, 24)
        self.assertAlmostEqual(m2.kk, 27)
        # 9 args - individual values
        m3 = m1.setTo(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 2)
        self.assertAlmostEqual(m1.ki, 3)
        self.assertAlmostEqual(m1.ij, 4)
        self.assertAlmostEqual(m1.jj, 5)
        self.assertAlmostEqual(m1.kj, 6)
        self.assertAlmostEqual(m1.ik, 7)
        self.assertAlmostEqual(m1.jk, 8)
        self.assertAlmostEqual(m1.kk, 9)
        # Invalid form
        with self.assertRaises(Exception):
            m1.setTo()

    def test_setToTranspose(self):
        """Test the setToTranspose method."""
        m1 = MatrixIJK()
        m2 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m3 = m1.setToTranspose(m2)
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 4)
        self.assertAlmostEqual(m1.ki, 7)
        self.assertAlmostEqual(m1.ij, 2)
        self.assertAlmostEqual(m1.jj, 5)
        self.assertAlmostEqual(m1.kj, 8)
        self.assertAlmostEqual(m1.ik, 3)
        self.assertAlmostEqual(m1.jk, 6)
        self.assertAlmostEqual(m1.kk, 9)

    def test_setToUnitizedColumns(self):
        """Test the setToUnitizedCollumns method."""
        m1 = MatrixIJK()
        m2 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m3 = m1.setToUnitizedColumns(m2)
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m1.ii, 1/sqrt(14))
        self.assertAlmostEqual(m1.ji, 2/sqrt(14))
        self.assertAlmostEqual(m1.ki, 3/sqrt(14))
        self.assertAlmostEqual(m1.ij, 4/sqrt(77))
        self.assertAlmostEqual(m1.jj, 5/sqrt(77))
        self.assertAlmostEqual(m1.kj, 6/sqrt(77))
        self.assertAlmostEqual(m1.ik, 7/sqrt(194))
        self.assertAlmostEqual(m1.jk, 8/sqrt(194))
        self.assertAlmostEqual(m1.kk, 9/sqrt(194))

    def test_setToInverse(self):
        """Test the setToInverse method."""
        m1 = MatrixIJK()
        m2 = MatrixIJK(1, 0, 5, 2, 1, 6, 3, 5, 0)
        m3 = m1.setToInverse(m2)
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m1.ii, -6)
        self.assertAlmostEqual(m1.ji, 5)
        self.assertAlmostEqual(m1.ki, -1)
        self.assertAlmostEqual(m1.ij, 3.6)
        self.assertAlmostEqual(m1.jj, -3)
        self.assertAlmostEqual(m1.kj, 0.8)
        self.assertAlmostEqual(m1.ik, 1.4)
        self.assertAlmostEqual(m1.jk, -1)
        self.assertAlmostEqual(m1.kk, 0.2)
        m4 = m3.setToInverse(m1)
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m4.ii, 1)
        self.assertAlmostEqual(m4.ji, 0)
        self.assertAlmostEqual(m4.ki, 5)
        self.assertAlmostEqual(m4.ij, 2)
        self.assertAlmostEqual(m4.jj, 1)
        self.assertAlmostEqual(m4.kj, 6)
        self.assertAlmostEqual(m4.ik, 3)
        self.assertAlmostEqual(m4.jk, 5)
        self.assertAlmostEqual(m4.kk, 0)

    def test_setToInvorted(self):
        """Test the setToInvorted method."""
        a = pi/3
        m = MatrixIJK()
        m1 = MatrixIJK(cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        m2 = m.setToInvorted(m1)
        self.assertIs(m2, m)
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, -sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))

    def test_mxmt(self):
        """Test the mxmt method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(9, 8, 7, 6, 5, 4, 3, 2, 1)
        m3 = MatrixIJK.mxmt(m1, m2)
        # |1 4 7| |9 6 3|T   |1 4 7| |9 8 7|
        # |2 5 8|*|8 5 2|  = |2 5 8|*|6 5 4|
        # |3 6 9| |7 4 1|    |3 6 9| |3 2 1|
        self.assertAlmostEqual(m3.ii, 1*9 + 4*6 + 7*3)
        self.assertAlmostEqual(m3.ji, 2*9 + 5*6 + 8*3)
        self.assertAlmostEqual(m3.ki, 3*9 + 6*6 + 9*3)
        self.assertAlmostEqual(m3.ij, 1*8 + 4*5 + 7*2)
        self.assertAlmostEqual(m3.jj, 2*8 + 5*5 + 8*2)
        self.assertAlmostEqual(m3.kj, 3*8 + 6*5 + 9*2)
        self.assertAlmostEqual(m3.ik, 1*7 + 4*4 + 7*1)
        self.assertAlmostEqual(m3.jk, 2*7 + 5*4 + 8*1)
        self.assertAlmostEqual(m3.kk, 3*7 + 6*4 + 9*1)
        m4 = MatrixIJK()
        m5 = MatrixIJK.mxmt(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 1*9 + 4*6 + 7*3)
        self.assertAlmostEqual(m5.ji, 2*9 + 5*6 + 8*3)
        self.assertAlmostEqual(m5.ki, 3*9 + 6*6 + 9*3)
        self.assertAlmostEqual(m5.ij, 1*8 + 4*5 + 7*2)
        self.assertAlmostEqual(m5.jj, 2*8 + 5*5 + 8*2)
        self.assertAlmostEqual(m5.kj, 3*8 + 6*5 + 9*2)
        self.assertAlmostEqual(m5.ik, 1*7 + 4*4 + 7*1)
        self.assertAlmostEqual(m5.jk, 2*7 + 5*4 + 8*1)
        self.assertAlmostEqual(m5.kk, 3*7 + 6*4 + 9*1)

    def test_mtxm(self):
        """Test the mtxm method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(9, 8, 7, 6, 5, 4, 3, 2, 1)
        m3 = MatrixIJK.mtxm(m1, m2)
        # |1 4 7|T|9 6 3|    |1 2 3| |9 6 3|
        # |2 5 8|*|8 5 2|  = |4 5 6|*|8 5 2|
        # |3 6 9| |7 4 1|    |7 8 9| |7 4 1|
        self.assertAlmostEqual(m3.ii, 1*9 + 2*8 + 3*7)
        self.assertAlmostEqual(m3.ji, 4*9 + 5*8 + 6*7)
        self.assertAlmostEqual(m3.ki, 7*9 + 8*8 + 9*7)
        self.assertAlmostEqual(m3.ij, 1*6 + 2*5 + 3*4)
        self.assertAlmostEqual(m3.jj, 4*6 + 5*5 + 6*4)
        self.assertAlmostEqual(m3.kj, 7*6 + 8*5 + 9*4)
        self.assertAlmostEqual(m3.ik, 1*3 + 2*2 + 3*1)
        self.assertAlmostEqual(m3.jk, 4*3 + 5*2 + 6*1)
        self.assertAlmostEqual(m3.kk, 7*3 + 8*2 + 9*1)
        m4 = MatrixIJK()
        m5 = MatrixIJK.mtxm(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 1*9 + 2*8 + 3*7)
        self.assertAlmostEqual(m5.ji, 4*9 + 5*8 + 6*7)
        self.assertAlmostEqual(m5.ki, 7*9 + 8*8 + 9*7)
        self.assertAlmostEqual(m5.ij, 1*6 + 2*5 + 3*4)
        self.assertAlmostEqual(m5.jj, 4*6 + 5*5 + 6*4)
        self.assertAlmostEqual(m5.kj, 7*6 + 8*5 + 9*4)
        self.assertAlmostEqual(m5.ik, 1*3 + 2*2 + 3*1)
        self.assertAlmostEqual(m5.jk, 4*3 + 5*2 + 6*1)
        self.assertAlmostEqual(m5.kk, 7*3 + 8*2 + 9*1)

    def test_mxm(self):
        """Test the mxm method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(9, 8, 7, 6, 5, 4, 3, 2, 1)
        m3 = MatrixIJK.mxm(m1, m2)
        # |1 4 7| |9 6 3|
        # |2 5 8|*|8 5 2|
        # |3 6 9| |7 4 1|
        self.assertAlmostEqual(m3.ii, 1*9 + 4*8 + 7*7)
        self.assertAlmostEqual(m3.ji, 2*9 + 5*8 + 8*7)
        self.assertAlmostEqual(m3.ki, 3*9 + 6*8 + 9*7)
        self.assertAlmostEqual(m3.ij, 1*6 + 4*5 + 7*4)
        self.assertAlmostEqual(m3.jj, 2*6 + 5*5 + 8*4)
        self.assertAlmostEqual(m3.kj, 3*6 + 6*5 + 9*4)
        self.assertAlmostEqual(m3.ik, 1*3 + 4*2 + 7*1)
        self.assertAlmostEqual(m3.jk, 2*3 + 5*2 + 8*1)
        self.assertAlmostEqual(m3.kk, 3*3 + 6*2 + 9*1)
        m4 = MatrixIJK()
        m5 = MatrixIJK.mxm(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 1*9 + 4*8 + 7*7)
        self.assertAlmostEqual(m5.ji, 2*9 + 5*8 + 8*7)
        self.assertAlmostEqual(m5.ki, 3*9 + 6*8 + 9*7)
        self.assertAlmostEqual(m5.ij, 1*6 + 4*5 + 7*4)
        self.assertAlmostEqual(m5.jj, 2*6 + 5*5 + 8*4)
        self.assertAlmostEqual(m5.kj, 3*6 + 6*5 + 9*4)
        self.assertAlmostEqual(m5.ik, 1*3 + 4*2 + 7*1)
        self.assertAlmostEqual(m5.jk, 2*3 + 5*2 + 8*1)
        self.assertAlmostEqual(m5.kk, 3*3 + 6*2 + 9*1)

    def test_mxmtadd(self):
        """Test the mxmtadd method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(2, 3, 4, 5, 6, 7, 8, 9, 1)
        m3 = MatrixIJK(4, 5, 6, 7, 8, 9, 1, 2, 3)
        m4 = MatrixIJK(7, 8, 9, 1, 2, 3, 4, 5, 6)
        #   |1 4 7| |2 5 8|T  |4 7 1| |7 1 4|T
        #   |2 5 8|*|3 6 9| + |5 8 2|*|8 2 5|
        #   |3 6 9| |4 7 1|   |6 9 3| |9 3 6|
        #
        #   |1 4 7| |2 3 4|   |4 7 1| |7 8 9|
        #   |2 5 8|*|5 6 7| + |5 8 2|*|1 2 3|
        #   |3 6 9| |8 9 1|   |6 9 3| |4 5 6|
        m5 = MatrixIJK.mxmtadd(m1, m2, m3, m4)
        self.assertAlmostEqual(
            m5.ii, 1*2 + 4*5 + 7*8 + 4*7 + 7*1 + 1*4)
        self.assertAlmostEqual(
            m5.ji, 2*2 + 5*5 + 8*8 + 5*7 + 8*1 + 2*4)
        self.assertAlmostEqual(
            m5.ki, 3*2 + 6*5 + 9*8 + 6*7 + 9*1 + 3*4)
        self.assertAlmostEqual(
            m5.ij, 1*3 + 4*6 + 7*9 + 4*8 + 7*2 + 1*5)
        self.assertAlmostEqual(
            m5.jj, 2*3 + 5*6 + 8*9 + 5*8 + 8*2 + 2*5)
        self.assertAlmostEqual(
            m5.kj, 3*3 + 6*6 + 9*9 + 6*8 + 9*2 + 3*5)
        self.assertAlmostEqual(
            m5.ik, 1*4 + 4*7 + 7*1 + 4*9 + 7*3 + 1*6)
        self.assertAlmostEqual(
            m5.jk, 2*4 + 5*7 + 8*1 + 5*9 + 8*3 + 2*6)
        self.assertAlmostEqual(
            m5.kk, 3*4 + 6*7 + 9*1 + 6*9 + 9*3 + 3*6)
        m6 = MatrixIJK()
        m7 = MatrixIJK.mxmtadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        self.assertAlmostEqual(
            m7.ii, 1*2 + 4*5 + 7*8 + 4*7 + 7*1 + 1*4)
        self.assertAlmostEqual(
            m7.ji, 2*2 + 5*5 + 8*8 + 5*7 + 8*1 + 2*4)
        self.assertAlmostEqual(
            m7.ki, 3*2 + 6*5 + 9*8 + 6*7 + 9*1 + 3*4)
        self.assertAlmostEqual(
            m7.ij, 1*3 + 4*6 + 7*9 + 4*8 + 7*2 + 1*5)
        self.assertAlmostEqual(
            m7.jj, 2*3 + 5*6 + 8*9 + 5*8 + 8*2 + 2*5)
        self.assertAlmostEqual(
            m7.kj, 3*3 + 6*6 + 9*9 + 6*8 + 9*2 + 3*5)
        self.assertAlmostEqual(
            m7.ik, 1*4 + 4*7 + 7*1 + 4*9 + 7*3 + 1*6)
        self.assertAlmostEqual(
            m7.jk, 2*4 + 5*7 + 8*1 + 5*9 + 8*3 + 2*6)
        self.assertAlmostEqual(
            m7.kk, 3*4 + 6*7 + 9*1 + 6*9 + 9*3 + 3*6)

    def test_mtxmadd(self):
        """Test the mtxmadd method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(2, 3, 4, 5, 6, 7, 8, 9, 1)
        m3 = MatrixIJK(4, 5, 6, 7, 8, 9, 1, 2, 3)
        m4 = MatrixIJK(7, 8, 9, 1, 2, 3, 4, 5, 6)
        #   |1 4 7|T|2 5 8|   |4 7 1|T|7 1 4|
        #   |2 5 8|*|3 6 9| + |5 8 2|*|8 2 5|
        #   |3 6 9| |4 7 1|   |6 9 3| |9 3 6|
        #
        #   |1 2 3| |2 5 8|   |4 5 6| |7 1 4|
        #   |4 5 6|*|3 6 9| + |7 8 9|*|8 2 5|
        #   |7 8 9| |4 7 1|   |1 2 3| |9 3 6|
        m5 = MatrixIJK.mtxmadd(m1, m2, m3, m4)
        self.assertAlmostEqual(
            m5.ii, 1*2 + 2*3 + 3*4 + 4*7 + 5*8 + 6*9)
        self.assertAlmostEqual(
            m5.ji, 4*2 + 5*3 + 6*4 + 7*7 + 8*8 + 9*9)
        self.assertAlmostEqual(
            m5.ki, 7*2 + 8*3 + 9*4 + 1*7 + 2*8 + 3*9)
        self.assertAlmostEqual(
            m5.ij, 1*5 + 2*6 + 3*7 + 4*1 + 5*2 + 6*3)
        self.assertAlmostEqual(
            m5.jj, 4*5 + 5*6 + 6*7 + 7*1 + 8*2 + 9*3)
        self.assertAlmostEqual(
            m5.kj, 7*5 + 8*6 + 9*7 + 1*1 + 2*2 + 3*3)
        self.assertAlmostEqual(
            m5.ik, 1*8 + 2*9 + 3*1 + 4*4 + 5*5 + 6*6)
        self.assertAlmostEqual(
            m5.jk, 4*8 + 5*9 + 6*1 + 7*4 + 8*5 + 9*6)
        self.assertAlmostEqual(
            m5.kk, 7*8 + 8*9 + 9*1 + 1*4 + 2*5 + 3*6)
        m6 = MatrixIJK()
        m7 = MatrixIJK.mtxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        self.assertAlmostEqual(
            m7.ii, 1*2 + 2*3 + 3*4 + 4*7 + 5*8 + 6*9)
        self.assertAlmostEqual(
            m7.ji, 4*2 + 5*3 + 6*4 + 7*7 + 8*8 + 9*9)
        self.assertAlmostEqual(
            m7.ki, 7*2 + 8*3 + 9*4 + 1*7 + 2*8 + 3*9)
        self.assertAlmostEqual(
            m7.ij, 1*5 + 2*6 + 3*7 + 4*1 + 5*2 + 6*3)
        self.assertAlmostEqual(
            m7.jj, 4*5 + 5*6 + 6*7 + 7*1 + 8*2 + 9*3)
        self.assertAlmostEqual(
            m7.kj, 7*5 + 8*6 + 9*7 + 1*1 + 2*2 + 3*3)
        self.assertAlmostEqual(
            m7.ik, 1*8 + 2*9 + 3*1 + 4*4 + 5*5 + 6*6)
        self.assertAlmostEqual(
            m7.jk, 4*8 + 5*9 + 6*1 + 7*4 + 8*5 + 9*6)
        self.assertAlmostEqual(
            m7.kk, 7*8 + 8*9 + 9*1 + 1*4 + 2*5 + 3*6)

    def test_mxmadd(self):
        """Test the mxmadd method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(2, 3, 4, 5, 6, 7, 8, 9, 1)
        m3 = MatrixIJK(4, 5, 6, 7, 8, 9, 1, 2, 3)
        m4 = MatrixIJK(7, 8, 9, 1, 2, 3, 4, 5, 6)
        #   |1 4 7| |2 5 8|   |4 7 1| |7 1 4|
        #   |2 5 8|*|3 6 9| + |5 8 2|*|8 2 5|
        #   |3 6 9| |4 7 1|   |6 9 3| |9 3 6|
        m5 = MatrixIJK.mxmadd(m1, m2, m3, m4)
        self.assertAlmostEqual(
            m5.ii, 1*2 + 4*3 + 7*4 + 4*7 + 7*8 + 1*9)
        self.assertAlmostEqual(
            m5.ji, 2*2 + 5*3 + 8*4 + 5*7 + 8*8 + 2*9)
        self.assertAlmostEqual(
            m5.ki, 3*2 + 6*3 + 9*4 + 6*7 + 9*8 + 3*9)
        self.assertAlmostEqual(
            m5.ij, 1*5 + 4*6 + 7*7 + 4*1 + 7*2 + 1*3)
        self.assertAlmostEqual(
            m5.jj, 2*5 + 5*6 + 8*7 + 5*1 + 8*2 + 2*3)
        self.assertAlmostEqual(
            m5.kj, 3*5 + 6*6 + 9*7 + 6*1 + 9*2 + 3*3)
        self.assertAlmostEqual(
            m5.ik, 1*8 + 4*9 + 7*1 + 4*4 + 7*5 + 1*6)
        self.assertAlmostEqual(
            m5.jk, 2*8 + 5*9 + 8*1 + 5*4 + 8*5 + 2*6)
        self.assertAlmostEqual(
            m5.kk, 3*8 + 6*9 + 9*1 + 6*4 + 9*5 + 3*6)
        m6 = MatrixIJK()
        m7 = MatrixIJK.mxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        self.assertAlmostEqual(
            m7.ii, 1*2 + 4*3 + 7*4 + 4*7 + 7*8 + 1*9)
        self.assertAlmostEqual(
            m7.ji, 2*2 + 5*3 + 8*4 + 5*7 + 8*8 + 2*9)
        self.assertAlmostEqual(
            m7.ki, 3*2 + 6*3 + 9*4 + 6*7 + 9*8 + 3*9)
        self.assertAlmostEqual(
            m7.ij, 1*5 + 4*6 + 7*7 + 4*1 + 7*2 + 1*3)
        self.assertAlmostEqual(
            m7.jj, 2*5 + 5*6 + 8*7 + 5*1 + 8*2 + 2*3)
        self.assertAlmostEqual(
            m7.kj, 3*5 + 6*6 + 9*7 + 6*1 + 9*2 + 3*3)
        self.assertAlmostEqual(
            m7.ik, 1*8 + 4*9 + 7*1 + 4*4 + 7*5 + 1*6)
        self.assertAlmostEqual(
            m7.jk, 2*8 + 5*9 + 8*1 + 5*4 + 8*5 + 2*6)
        self.assertAlmostEqual(
            m7.kk, 3*8 + 6*9 + 9*1 + 6*4 + 9*5 + 3*6)

    def test_subtract(self):
        """Test the subtract method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(9, 8, 7, 6, 5, 4, 3, 2, 1)
        m3 = MatrixIJK.subtract(m1, m2)
        self.assertAlmostEqual(m3.ii, -8)
        self.assertAlmostEqual(m3.ji, -6)
        self.assertAlmostEqual(m3.ki, -4)
        self.assertAlmostEqual(m3.ij, -2)
        self.assertAlmostEqual(m3.jj, 0)
        self.assertAlmostEqual(m3.kj, 2)
        self.assertAlmostEqual(m3.ik, 4)
        self.assertAlmostEqual(m3.jk, 6)
        self.assertAlmostEqual(m3.kk, 8)
        m4 = MatrixIJK()
        m5 = MatrixIJK.subtract(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, -8)
        self.assertAlmostEqual(m5.ji, -6)
        self.assertAlmostEqual(m5.ki, -4)
        self.assertAlmostEqual(m5.ij, -2)
        self.assertAlmostEqual(m5.jj, 0)
        self.assertAlmostEqual(m5.kj, 2)
        self.assertAlmostEqual(m5.ik, 4)
        self.assertAlmostEqual(m5.jk, 6)
        self.assertAlmostEqual(m5.kk, 8)

    def test_add(self):
        """Test the add method."""
        m1 = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = MatrixIJK(9, 8, 7, 6, 5, 4, 3, 2, 1)
        m3 = MatrixIJK.add(m1, m2)
        self.assertAlmostEqual(m3.ii, 10)
        self.assertAlmostEqual(m3.ji, 10)
        self.assertAlmostEqual(m3.ki, 10)
        self.assertAlmostEqual(m3.ij, 10)
        self.assertAlmostEqual(m3.jj, 10)
        self.assertAlmostEqual(m3.kj, 10)
        self.assertAlmostEqual(m3.ik, 10)
        self.assertAlmostEqual(m3.jk, 10)
        self.assertAlmostEqual(m3.kk, 10)
        m4 = MatrixIJK()
        m5 = MatrixIJK.add(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 10)
        self.assertAlmostEqual(m5.ji, 10)
        self.assertAlmostEqual(m5.ki, 10)
        self.assertAlmostEqual(m5.ij, 10)
        self.assertAlmostEqual(m5.jj, 10)
        self.assertAlmostEqual(m5.kj, 10)
        self.assertAlmostEqual(m5.ik, 10)
        self.assertAlmostEqual(m5.jk, 10)
        self.assertAlmostEqual(m5.kk, 10)

    def test_mtxv(self):
        """Test the mtxv method."""
        m = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v1 = VectorIJK(1, 2, 3)
        v2 = MatrixIJK.mtxv(m, v1)
        # | 1 4 7 |T  | 1 |   | 1 2 3 | | 1 |   | 14 |
        # | 2 5 8 |   | 2 | = | 4 5 6 | | 2 | = | 32 |
        # | 3 6 9 |   | 3 |   | 7 8 9 | | 3 |   | 50 |
        self.assertAlmostEqual(v2.i, 14)
        self.assertAlmostEqual(v2.j, 32)
        self.assertAlmostEqual(v2.k, 50)
        v3 = VectorIJK()
        v4 = MatrixIJK.mtxv(m, v1, v3)
        self.assertIs(v4, v3)
        self.assertAlmostEqual(v4.i, 14)
        self.assertAlmostEqual(v4.j, 32)
        self.assertAlmostEqual(v4.k, 50)

    def test_mxv(self):
        """Test the mxv method."""
        m = MatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v1 = VectorIJK(1, 2, 3)
        v2 = MatrixIJK.mxv(m, v1)
        self.assertAlmostEqual(v2.i, 1*1 + 4*2 + 7*3)
        self.assertAlmostEqual(v2.j, 2*1 + 5*2 + 8*3)
        self.assertAlmostEqual(v2.k, 3*1 + 6*2 + 9*3)
        v3 = VectorIJK()
        v4 = m.mxv(v1, v3)
        self.assertIs(v4, v3)
        self.assertAlmostEqual(v4.i, 1*1 + 4*2 + 7*3)
        self.assertAlmostEqual(v4.j, 2*1 + 5*2 + 8*3)
        self.assertAlmostEqual(v4.k, 3*1 + 6*2 + 9*3)

    def test_getDeterminant(self):
        """Test the getDeterminant method."""
        pass


if __name__ == '__main__':
    unittest.main()
