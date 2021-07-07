"""Tests for the matrixijk module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from numpy.core.getlimits import _register_known_types
from emmpy.math.matrices.matrix3d import Matrix3D
from math import cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___new__(self):
        """Test the __new__ method."""
        # 0 arguments - empty matrix
        m1 = MatrixIJK()
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertTrue(np.isnan(m1[row, col]))
        # 1 arg - list of lists, use upper-left 3x3 block.
        data = [[1, 2, 3, 4],
                [4, 5, 6, 7],
                [7, 8, 9, 0],
                [4, 3, 2, 1]]
        m1 = MatrixIJK(data)
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data[col][row])
        # 1 arg - tuple of tuples
        data = ((1, 2, 3, 4),
                (4, 5, 6, 7),
                (7, 8, 9, 0),
                (4, 3, 2, 1))
        m1 = MatrixIJK(data)
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data[col][row])
        # 1 arg - Numpy array
        m2 = MatrixIJK(m1)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1[row, col])
        # 1 arg - copy
        m2 = MatrixIJK(m1)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1[row, col])
        # 2 args - scale factor and matrix
        scale = -2.2
        m2 = MatrixIJK(scale, m1)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*m1[row, col])
        # 3 args - column vectors
        v1 = VectorIJK(data[0][:3])
        v2 = VectorIJK(data[1][:3])
        v3 = VectorIJK(data[2][:3])
        m1 = MatrixIJK(v1, v2, v3)
        self.assertIsInstance(m1, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data[col][row])
        # 4 args - 3 column scale factors and matrix
        (scaleI, scaleJ, scaleK) = (-1.1, 2.2, 3.3)
        scale = (-1.1, 2.2, 3.3)
        m2 = MatrixIJK(scaleI, scaleJ, scaleK, m1)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            self.assertAlmostEqual(m2[row, 0], scaleI*m1[row, 0])
            self.assertAlmostEqual(m2[row, 1], scaleJ*m1[row, 1])
            self.assertAlmostEqual(m2[row, 2], scaleK*m1[row, 2])
        # 6 args - scale factors and columns
        m2 = MatrixIJK(scaleI, v1, scaleJ, v2, scaleK, v3)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            self.assertAlmostEqual(m2[row, 0], scaleI*v1[row])
            self.assertAlmostEqual(m2[row, 1], scaleJ*v2[row])
            self.assertAlmostEqual(m2[row, 2], scaleK*v3[row])
        # 9 args - element values
        data = list(range(9))
        m2 = MatrixIJK(*data)
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                k = row + 3*col
                self.assertAlmostEqual(m2[row, col], k)
        # Invalid forms
        with self.assertRaises(ValueError):
            m1 = MatrixIJK(None)
        with self.assertRaises(ValueError):
            m1 = MatrixIJK(None, None, None, None, None)
        with self.assertRaises(ValueError):
            m1 = MatrixIJK(None, None, None, None, None, None, None)
        with self.assertRaises(ValueError):
            m1 = MatrixIJK(None, None, None, None, None, None, None, None)
        with self.assertRaises(ValueError):
            m1 = MatrixIJK(None, None, None, None, None, None, None, None,
                           None, None)
        with self.assertRaises(ValueError):
            data = [1]*10
            m1 = MatrixIJK(*data)

    def test___getattr__(self):
        """Test the __getattr__ method."""
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
            m.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        m = MatrixIJK()
        data = [i*1.1 for i in range(9)]
        m.ii = data[0]
        self.assertAlmostEqual(m.ii, data[0])
        m.ji = data[1]
        self.assertAlmostEqual(m.ji, data[1])
        m.ki = data[2]
        self.assertAlmostEqual(m.ki, data[2])
        m.ij = data[3]
        self.assertAlmostEqual(m.ij, data[3])
        m.jj = data[4]
        self.assertAlmostEqual(m.jj, data[4])
        m.kj = data[5]
        self.assertAlmostEqual(m.kj, data[5])
        m.ik = data[6]
        self.assertAlmostEqual(m.ik, data[6])
        m.jk = data[7]
        self.assertAlmostEqual(m.jk, data[7])
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
        m = MatrixIJK()
        data = list(range(3))
        v = VectorIJK(*data)
        m.setIthColumn(v)
        for row in range(3):
            self.assertAlmostEqual(m[row, 0], data[row])

    def test_setJthColumn(self):
        """Test the setJthColumn method."""
        m = MatrixIJK()
        data = list(range(3))
        v = VectorIJK(*data)
        m.setJthColumn(v)
        for row in range(3):
            self.assertAlmostEqual(m[row, 1], data[row])

    def test_setKthColumn(self):
        """Test the setKthColumn method."""
        m = MatrixIJK()
        data = list(range(3))
        v = VectorIJK(*data)
        m.setKthColumn(v)
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
        # matrix copy
        m3 = MatrixIJK(data)
        m2 = m1.setTo(m3)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m3[row, col])
        # 2-arg forms
        # Scale a matrix
        scale = -2.2
        m2 = m1.setTo(scale, m3)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scale*m3[row, col])
        # 3-arg forms
        # Column vectors
        data = list(range(9))
        v1 = VectorIJK(data[:3])
        v2 = VectorIJK(data[3:6])
        v3 = VectorIJK(data[6:9])
        m1 = MatrixIJK()
        m2 = m1.setTo(v1, v2, v3)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                k = col*3 + row
                self.assertAlmostEqual(m2[row, col], k)
        # 4 arg forms
        # scale a matrix by columns
        m1 = MatrixIJK(*data)
        scales = (1.1, 2.2, 3.3)
        m2 = MatrixIJK()
        m3 = m2.setTo(*scales, m1)
        self.assertIs(m3, m2)
        for row in range(3):
            for col in range(3):
                k = col*3 + row
                self.assertAlmostEqual(m3[row, col], scales[col]*k)
        # 6 arg forms
        # scaled column vectors
        m1 = MatrixIJK()
        v = (v1, v2, v3)
        m2 = m1.setTo(scales[0], v[0], scales[1], v[1], scales[2], v[2])
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], scales[col]*v[col][row])
        # 9 arg forms
        # individual values
        m1 = MatrixIJK()
        m2 = m1.setTo(*data)
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                k = col*3 + row
                self.assertAlmostEqual(m2[row, col], k)
        # Invalid forms
        with self.assertRaises(ValueError):
            m1.setTo()
        with self.assertRaises(ValueError):
            m1.setTo(None, None, None, None, None)
        with self.assertRaises(ValueError):
            m1.setTo(None, None, None, None, None, None, None)
        with self.assertRaises(ValueError):
            m1.setTo(None, None, None, None, None, None, None, None)
        with self.assertRaises(ValueError):
            m1.setTo(None, None, None, None, None, None, None, None, None, None)

    def test_transpose(self):
        """Test the tranpose method."""
        data = list(range(9))
        m1 = MatrixIJK(*data)
        m1_orig = MatrixIJK(m1)
        m2 = m1.transpose()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1_orig[col, row])

    def test_unitizeColumns(self):
        """Test the unitizeColumns method."""
        data = list(range(9))
        lengths = (
            sqrt(sum([x**2 for x in data[:3]])),
            sqrt(sum([x**2 for x in data[3:6]])),
            sqrt(sum([x**2 for x in data[6:9]]))
        )
        m1 = MatrixIJK(*data)
        m1_orig = MatrixIJK(m1)
        m2 = m1.unitizeColumns()
        self.assertIs(m2, m1)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1_orig[row, col]/lengths[col])

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
        data = list(range(9))
        lengths = (
            sqrt(sum([x**2 for x in data[:3]])),
            sqrt(sum([x**2 for x in data[3:6]])),
            sqrt(sum([x**2 for x in data[6:9]]))
        )
        m1 = MatrixIJK(*data)
        m2 = m1.createUnitizedColumns()
        self.assertIsInstance(m2, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], m1[row, col]/lengths[col])

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
        data = list(range(9))
        lengths = (
            sqrt(sum([x**2 for x in data[:3]])),
            sqrt(sum([x**2 for x in data[3:6]])),
            sqrt(sum([x**2 for x in data[6:9]]))
        )
        m1 = MatrixIJK(*data)
        m2 = MatrixIJK()
        m3 = m2.setToUnitizedColumns(m1)
        self.assertIs(m3, m2)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m3[row, col], m1[row, col]/lengths[col])

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
        # 2-arg form.
        # No buffer.
        m4 = MatrixIJK.add(m1, m2)
        self.assertIsInstance(m4, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 3-arg form.
        # Use buffer.
        m4 = MatrixIJK()
        m5 = MatrixIJK.add(m1, m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], m3[row, col])

    def test_subtract(self):
        """Test the subtract method."""
        data1 = list(range(1, 10))
        data2 = list(reversed(data1))
        data3 = [x1 - x2 for (x1, x2) in zip(data1, data2)]
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        m3 = MatrixIJK(*data3)
        # 2-arg form.
        # No buffer.
        m4 = MatrixIJK.subtract(m1, m2)
        self.assertIsInstance(m4, MatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 3-arg form.
        # Use buffer.
        m4 = MatrixIJK()
        m5 = MatrixIJK.subtract(m1, m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], m3[row, col])

    def test_mxm(self):
        """Test the mxm method."""
        data1 = list(range(1, 10))
        data2 = list(reversed(data1))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        p = np.zeros((3, 3))
        for row in range(3):
            for col in range(3):
                for k in range(3):
                    p[row][col] += m1[row][k]*m2[k][col]
        m3 = MatrixIJK(p)
        # 2-arg version
        # No buffer.
        m4 = MatrixIJK.mxm(m1, m2)
        self.assertIsInstance(m4, MatrixIJK)
        # |1 4 7| |9 6 3|
        # |2 5 8|*|8 5 2|
        # |3 6 9| |7 4 1|
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row][col])
        # 3-arg version.
        # With buffer.
        m4 = MatrixIJK()
        m5 = MatrixIJK.mxm(m1, m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m4[row, col], m3[row][col])
        # Invalid forms.
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt()
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt(None)
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt(None, None, None, None)

    def test_mxmt(self):
        """Test the mxmt method."""
        data1 = list(range(1, 10))
        data2 = list(reversed(data1))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        mp = np.zeros((3, 3))
        for row in range(3):
            for col in range(3):
                for k in range(3):
                    mp[row][col] += m1[row][k]*m2[col][k]
        # 2-arg version
        # No buffer.
        m3 = MatrixIJK.mxmt(m1, m2)
        self.assertIsInstance(m3, MatrixIJK)
        # |1 4 7| |9 6 3|T   |1 4 7| |9 8 7|
        # |2 5 8|*|8 5 2|  = |2 5 8|*|6 5 4|
        # |3 6 9| |7 4 1|    |3 6 9| |3 2 1|
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m3[row, col], mp[row][col])
        # 3-arg version.
        # With buffer.
        m4 = MatrixIJK()
        m5 = MatrixIJK.mxmt(m1, m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], mp[row][col])
        # Invalid forms.
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt()
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt(None)
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt(None, None, None, None)

    def test_mtxm(self):
        """Test the mtxm method."""
        data1 = list(range(1, 10))
        data2 = list(reversed(data1))
        m1 = MatrixIJK(*data1)
        m2 = MatrixIJK(*data2)
        mp = np.zeros((3, 3))
        for row in range(3):
            for col in range(3):
                for k in range(3):
                    mp[row][col] += m1[k][row]*m2[k][col]
        # 2-arg form
        # No buffer.
        m3 = MatrixIJK.mtxm(m1, m2)
        self.assertIsInstance(m3, MatrixIJK)
        # |1 4 7|T|9 6 3|    |1 2 3| |9 6 3|
        # |2 5 8|*|8 5 2|  = |4 5 6|*|8 5 2|
        # |3 6 9| |7 4 1|    |7 8 9| |7 4 1|
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m3[row, col], mp[row][col])
        # 3-arg form.
        # Use buffer.
        m4 = MatrixIJK()
        m5 = MatrixIJK.mtxm(m1, m2, m4)
        self.assertIs(m5, m4)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m5[row, col], mp[row][col])
        # Invalid forms.
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt()
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt(None)
        with self.assertRaises(ValueError):
            m3 = MatrixIJK.mxmt(None, None, None, None)

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
        #   |1 4 7| |2 5 8|   |4 7 1| |7 1 4|
        #   |2 5 8|*|3 6 9| + |5 8 2|*|8 2 5|
        #   |3 6 9| |4 7 1|   |6 9 3| |9 3 6|
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
        #   |1 4 7| |2 5 8|T  |4 7 1| |7 1 4|T
        #   |2 5 8|*|3 6 9| + |5 8 2|*|8 2 5|
        #   |3 6 9| |4 7 1|   |6 9 3| |9 3 6|
        #
        #   |1 4 7| |2 3 4|   |4 7 1| |7 8 9|
        #   |2 5 8|*|5 6 7| + |5 8 2|*|1 2 3|
        #   |3 6 9| |8 9 1|   |6 9 3| |4 5 6|
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
        #   |1 4 7|T|2 5 8|   |4 7 1|T|7 1 4|
        #   |2 5 8|*|3 6 9| + |5 8 2|*|8 2 5|
        #   |3 6 9| |4 7 1|   |6 9 3| |9 3 6|
        #
        #   |1 2 3| |2 5 8|   |4 5 6| |7 1 4|
        #   |4 5 6|*|3 6 9| + |7 8 9|*|8 2 5|
        #   |7 8 9| |4 7 1|   |1 2 3| |9 3 6|
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
        m = MatrixIJK(*data1)
        v1 = VectorIJK(*data2)
        v2 = m.dot(v1)
        # 2-arg form.
        # No buffer.
        v3 = MatrixIJK.mxv(m, v1)
        self.assertIsInstance(v3, VectorIJK)
        for row in range(3):
            self.assertAlmostEqual(v3[row], v2[row])
        # 3-arg form.
        # Use buffer.
        v3 = VectorIJK()
        v4 = MatrixIJK.mxv(m, v1, v3)
        self.assertIs(v4, v3)
        for row in range(3):
            self.assertAlmostEqual(v4[row], v2[row])

    def test_mtxv(self):
        data1 = list(range(9))
        data2 = list(range(3))
        m = MatrixIJK(*data1)
        v1 = VectorIJK(*data2)
        v2 = m.T.dot(v1)
        # 2-arg form.
        # No buffer.
        v3 = MatrixIJK.mtxv(m, v1)
        self.assertIsInstance(v3, VectorIJK)
        for row in range(3):
            self.assertAlmostEqual(v3[row], v2[row])
        # 3-arg form.
        # Use buffer.
        v3 = VectorIJK()
        v4 = MatrixIJK.mtxv(m, v1, v3)
        self.assertIs(v4, v3)
        for row in range(3):
            self.assertAlmostEqual(v4[row], v2[row])


if __name__ == '__main__':
    unittest.main()
