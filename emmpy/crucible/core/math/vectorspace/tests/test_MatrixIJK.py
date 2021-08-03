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


if __name__ == '__main__':
    unittest.main()
