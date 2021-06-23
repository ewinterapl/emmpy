"""Tests for the unwritablematrixijk module."""


from math import cos, sin, sqrt
import numpy as np

import unittest

from emmpy.crucible.core.math.vectorspace.unwritablematrixijk import (
    UnwritableMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Build and run tests for the unwritablematrixijk module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form
        m1 = UnwritableMatrixIJK()
        self.assertIsInstance(m1, UnwritableMatrixIJK)
        for x in m1.flatten():
            self.assertTrue(np.isnan(x))
        # 1 argument forms
        # List of lists of floats
        data = [[1.1, 2.2, 3.3, 4.4],
                [5.5, 6.6, 7.7, 8.8],
                [9.9, 1.2, 3.4, 5.6],
                [7.8, 9.1, 1.3, 2.4]]
        m1 = UnwritableMatrixIJK(data)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m1[i, j], data[i][j])
        # Copy a matrix
        m2 = UnwritableMatrixIJK(m1)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m2[i, j], m1[i, j])
        # 2-argument forms
        # Scaling constructor
        scale = 2.0
        m2 = UnwritableMatrixIJK(2.0, m1)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m2[i, j], scale*m1[i, j])
        # 3-argument forms
        # Column vectors.
        vs = []
        for i in range(3):
            vs.append(UnwritableVectorIJK(data[0][i], data[1][i], data[2][i]))
        m2 = UnwritableMatrixIJK(*vs)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m2[i, j], data[i][j])
        # 4-argument forms
        (scaleI, scaleJ, scaleK) = (1.1, -2.2, 3.3)
        m2 = UnwritableMatrixIJK(scaleI, scaleJ, scaleK, m1)
        for j in range(3):
            self.assertAlmostEqual(m2[j, 0], scaleI*m1[j, 0])
            self.assertAlmostEqual(m2[j, 1], scaleJ*m1[j, 1])
            self.assertAlmostEqual(m2[j, 2], scaleK*m1[j, 2])
        # 6-argument forms.
        vi = UnwritableVectorIJK(1, 2, 3)
        vj = UnwritableVectorIJK(4, 5, 6)
        vk = UnwritableVectorIJK(7, 8, 9)
        m2 = UnwritableMatrixIJK(scaleI, vi, scaleJ, vj, scaleK, vk)
        for j in range(3):
            self.assertAlmostEqual(m2[j, 0], scaleI*vi[j])
            self.assertAlmostEqual(m2[j, 1], scaleJ*vj[j])
            self.assertAlmostEqual(m2[j, 2], scaleK*vk[j])
        # 9-argument forms
        m2 = UnwritableMatrixIJK(data[0][0], data[1][0], data[2][0],
                                 data[0][1], data[1][1], data[2][1],
                                 data[0][2], data[1][2], data[2][2])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m2[i, j], data[i][j])
        # Invalid forms
        with self.assertRaises(ValueError):
            UnwritableMatrixIJK(None)

    def test___getattr__(self):
        """Test the __getattr_ method."""
        (ii, ji, ki, ij, jj, kj, ik, jk, kk) = (
            1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9)
        m1 = UnwritableMatrixIJK(ii, ji, ki, ij, jj, kj, ik, jk, kk)
        self.assertAlmostEqual(m1.ii, ii)
        self.assertAlmostEqual(m1.ji, ji)
        self.assertAlmostEqual(m1.ki, ki)
        self.assertAlmostEqual(m1.ij, ij)
        self.assertAlmostEqual(m1.jj, jj)
        self.assertAlmostEqual(m1.kj, kj)
        self.assertAlmostEqual(m1.ik, ik)
        self.assertAlmostEqual(m1.jk, jk)
        self.assertAlmostEqual(m1.kk, kk)
        with self.assertRaises(KeyError):
            bad = m1.bad

    def test___setattr__(self):
        """Test the __setattr_ method."""
        (ii, ji, ki, ij, jj, kj, ik, jk, kk) = (
            1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9)
        m1 = UnwritableMatrixIJK()
        m1.ii = ii
        self.assertAlmostEqual(m1.ii, ii)
        m1.ji = ji
        self.assertAlmostEqual(m1.ji, ji)
        m1.ki = ki
        self.assertAlmostEqual(m1.ki, ki)
        m1.ij = ij
        self.assertAlmostEqual(m1.ij, ij)
        m1.jj = jj
        self.assertAlmostEqual(m1.jj, jj)
        m1.kj = kj
        self.assertAlmostEqual(m1.kj, kj)
        m1.ik = ik
        self.assertAlmostEqual(m1.ik, ik)
        m1.jk = jk
        self.assertAlmostEqual(m1.jk, jk)
        m1.kk = kk
        self.assertAlmostEqual(m1.kk, kk)
        with self.assertRaises(KeyError):
            bad = m1.bad

    def test_createTranspose(self):
        """Test the createTranspose method."""
        data = [[1.1, 2.2, 3.3],
                [5.5, 6.6, 7.7],
                [9.9, 1.2, 3.4]]
        m1 = UnwritableMatrixIJK(data)
        m2 = m1.createTranspose()
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m2[i, j], m1[j, i])

    def test_createUnitizedColumns(self):
        """Test the createUnitizedColumns method."""
        data = [[1.1, 2.2, 3.3],
                [5.5, 6.6, 7.7],
                [9.9, 1.2, 3.4]]
        lengths = [0, 0, 0]
        for i in range(3):
            lengths[i] = sqrt(data[0][i]**2 + data[1][i]**2 + data[2][i]**2)
        m1 = UnwritableMatrixIJK(data)
        m2 = m1.createUnitizedColumns()
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m2[i, j], data[i][j]/lengths[j])

    def test_createInverse(self):
        """Test the createInverse method."""
        m1 = UnwritableMatrixIJK(1, 0, 5, 2, 1, 6, 3, 5, 0)
        m2 = m1.createInverse()
        self.assertAlmostEqual(m2[0, 0], -6)
        self.assertAlmostEqual(m2[1, 0], 5)
        self.assertAlmostEqual(m2[2, 0], -1)
        self.assertAlmostEqual(m2[0, 1], 3.6)
        self.assertAlmostEqual(m2[1, 1], -3)
        self.assertAlmostEqual(m2[2, 1], 0.8)
        self.assertAlmostEqual(m2[0, 2], 1.4)
        self.assertAlmostEqual(m2[1, 2], -1)
        self.assertAlmostEqual(m2[2, 2], 0.2)
        with self.assertRaises(np.linalg.LinAlgError):
            m1 = UnwritableMatrixIJK(0, 0, 0, 0, 0, 0, 0, 0, 0)
            m2 = m1.createInverse()

    def test_createInvorted(self):
        """Test the createInvorted method."""
        a = 1
        m = UnwritableMatrixIJK(
            cos(a), 0, sin(a),
            0, 1, 0,
            -sin(a), 0, cos(a)
            )
        # 0.540302  | 0 | 0.841471
        # 0         | 1 | 0
        # -0.841471 | 0 | 0.540302
        m2 = m.createInvorted()
        self.assertAlmostEqual(m2[0, 0], cos(a))
        self.assertAlmostEqual(m2[1, 0], 0)
        self.assertAlmostEqual(m2[2, 0], -sin(a))
        self.assertAlmostEqual(m2[0, 1], 0)
        self.assertAlmostEqual(m2[1, 1], 1)
        self.assertAlmostEqual(m2[2, 1], 0)
        self.assertAlmostEqual(m2[0, 2], sin(a))
        self.assertAlmostEqual(m2[1, 2], 0)
        self.assertAlmostEqual(m2[2, 2], cos(a))
        with self.assertRaises(np.linalg.LinAlgError):
            m1 = UnwritableMatrixIJK(0, 0, 0, 0, 0, 0, 0, 0, 0)
            m2 = m1.createInvorted()

    def test_getII(self):
        """Test the getII method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getII(), 1)

    def test_getJI(self):
        """Test the getJI method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getJI(), 2)

    def test_getKI(self):
        """Test the getKI method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getKI(), 3)

    def test_getIJ(self):
        """Test the getIJ method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getIJ(), 4)

    def test_getJJ(self):
        """Test the getJJ method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getJJ(), 5)

    def test_getKJ(self):
        """Test the getKJ method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getKJ(), 6)

    def test_getIK(self):
        """Test the getIK method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getIK(), 7)

    def test_getJK(self):
        """Test the getJK method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getJK(), 8)

    def test_getKK(self):
        """Test the getKK method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getKK(), 9)

    def test_get(self):
        """Test the get method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.get(0, 0), 1)
        self.assertAlmostEqual(m.get(1, 0), 2)
        self.assertAlmostEqual(m.get(2, 0), 3)
        self.assertAlmostEqual(m.get(0, 1), 4)
        self.assertAlmostEqual(m.get(1, 1), 5)
        self.assertAlmostEqual(m.get(2, 1), 6)
        self.assertAlmostEqual(m.get(0, 2), 7)
        self.assertAlmostEqual(m.get(1, 2), 8)
        self.assertAlmostEqual(m.get(2, 2), 9)
        with self.assertRaises(Exception):
            m.get(0, 3)
        with self.assertRaises(Exception):
            m.get(1, 3)
        with self.assertRaises(Exception):
            m.get(2, 3)
        with self.assertRaises(Exception):
            m.get(3, 0)

    def test_getIthColumn(self):
        """Test the getIthColumn method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = VectorIJK()
        v2 = m.getIthColumn()
        self.assertAlmostEqual(v2.i, 1)
        self.assertAlmostEqual(v2.j, 2)
        self.assertAlmostEqual(v2.k, 3)
        v2 = m.getIthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 1)
        self.assertAlmostEqual(v2.j, 2)
        self.assertAlmostEqual(v2.k, 3)

    def test_getJthColumn(self):
        """Test the getJthColumn method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = VectorIJK()
        v2 = m.getJthColumn()
        self.assertAlmostEqual(v2.i, 4)
        self.assertAlmostEqual(v2.j, 5)
        self.assertAlmostEqual(v2.k, 6)
        v2 = m.getJthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 4)
        self.assertAlmostEqual(v2.j, 5)
        self.assertAlmostEqual(v2.k, 6)

    def test_getKthColumn(self):
        """Test the getKthColumn method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = VectorIJK()
        v2 = m.getKthColumn()
        self.assertAlmostEqual(v2.i, 7)
        self.assertAlmostEqual(v2.j, 8)
        self.assertAlmostEqual(v2.k, 9)
        v2 = m.getKthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 7)
        self.assertAlmostEqual(v2.j, 8)
        self.assertAlmostEqual(v2.k, 9)

    def test_getColumn(self):
        """Test the getColumn method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v2 = VectorIJK()
        v = m.getColumn(0)
        self.assertAlmostEqual(v.i, 1)
        self.assertAlmostEqual(v.j, 2)
        self.assertAlmostEqual(v.k, 3)
        v = m.getColumn(1)
        self.assertAlmostEqual(v.i, 4)
        self.assertAlmostEqual(v.j, 5)
        self.assertAlmostEqual(v.k, 6)
        v = m.getColumn(2)
        self.assertAlmostEqual(v.i, 7)
        self.assertAlmostEqual(v.j, 8)
        self.assertAlmostEqual(v.k, 9)
        v = m.getColumn(0, v2)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v.i, 1)
        self.assertAlmostEqual(v.j, 2)
        self.assertAlmostEqual(v.k, 3)
        v = m.getColumn(1, v2)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v.i, 4)
        self.assertAlmostEqual(v.j, 5)
        self.assertAlmostEqual(v.k, 6)
        v = m.getColumn(2, v2)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v.i, 7)
        self.assertAlmostEqual(v.j, 8)
        self.assertAlmostEqual(v.k, 9)
        with self.assertRaises(IndexError):
            m.getColumn(3)
        with self.assertRaises(ValueError):
            m.getColumn(0, 0, 0)

    def test_getDeterminant(self):
        """Test the getDeterminant method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getDeterminant(), 0)

    def test_getTrace(self):
        """Test the getTrace method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getTrace(), 15)

    def test_isRotation(self):
        """Test the isRotation method."""
        a = 1
        m = UnwritableMatrixIJK(
            cos(a), 0, sin(a),
            0, 1, 0,
            -sin(a), 0, cos(a)
            )
        self.assertTrue(m.isRotation())
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertFalse(m.isRotation())

    def test_mxv(self):
        """Test the mxv method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = UnwritableVectorIJK(1, 2, 3)
        vb = UnwritableVectorIJK(0, 0, 0)
        v2 = m.mxv(v)
        self.assertAlmostEqual(v2.i, 1*1 + 4*2 + 7*3)
        self.assertAlmostEqual(v2.j, 2*1 + 5*2 + 8*3)
        self.assertAlmostEqual(v2.k, 3*1 + 6*2 + 9*3)
        v2 = m.mxv(v, vb)
        self.assertIs(v2, vb)
        self.assertAlmostEqual(v2.i, 1*1 + 4*2 + 7*3)
        self.assertAlmostEqual(v2.j, 2*1 + 5*2 + 8*3)
        self.assertAlmostEqual(v2.k, 3*1 + 6*2 + 9*3)

    def test_mtxv(self):
        """Test the mtxv method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = UnwritableVectorIJK(1, 2, 3)
        vb = UnwritableVectorIJK(0, 0, 0)
        v2 = m.mtxv(v, vb)
        self.assertIs(v2, vb)
        self.assertAlmostEqual(v2.i, 1*1 + 2*2 + 3*3)
        self.assertAlmostEqual(v2.j, 4*1 + 5*2 + 6*3)
        self.assertAlmostEqual(v2.k, 7*1 + 8*2 + 9*3)

    def test_copyOf(self):
        """Test the copyOf method."""
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = UnwritableMatrixIJK.copyOf(m)
        self.assertAlmostEqual(m2[0, 0], 1)
        self.assertAlmostEqual(m2[1, 0], 2)
        self.assertAlmostEqual(m2[2, 0], 3)
        self.assertAlmostEqual(m2[0, 1], 4)
        self.assertAlmostEqual(m2[1, 1], 5)
        self.assertAlmostEqual(m2[2, 1], 6)
        self.assertAlmostEqual(m2[0, 2], 7)
        self.assertAlmostEqual(m2[1, 2], 8)
        self.assertAlmostEqual(m2[2, 2], 9)


if __name__ == '__main__':
    unittest.main()
