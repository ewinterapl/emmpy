from math import cos, pi, sin, sqrt
import unittest
import numpy as np
from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        """Test the __init__ method."""
        # 0 arguments - empty matrix
        m = MatrixIJ()
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertTrue(np.isnan(m[row, col]))
        # 1-argument forms: 2x2 array-like of float
        # list of lists
        data = [[0, 2], [1, 3]]
        m = MatrixIJ(data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of tuples
        data = ((0, 2), (1, 3))
        m = MatrixIJ(data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # list of tuples
        data = [(0, 2), (1, 3)]
        m = MatrixIJ(data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of lists
        data = ([0, 2], [1, 3])
        m = MatrixIJ(data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # np.ndarray
        a = np.array(data)
        m = MatrixIJ(a)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # MatrixIJ
        m2 = MatrixIJ(data)
        m = MatrixIJ(m2)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # 2 arg forms - scale factor and 2x2 array-like
        scale = -2.2
        # Scale and list of lists
        data = [[0, 2], [1, 3]]
        m = MatrixIJ(scale, data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and tuple of tuples
        data = ((0, 2), (1, 3))
        m = MatrixIJ(scale, data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and list of tuples
        data = [(0, 2), (1, 3)]
        m = MatrixIJ(scale, data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and tuple of lists
        data = ([0, 2], [1, 3])
        m = MatrixIJ(scale, data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and np.ndarray
        a = np.array(data)
        m = MatrixIJ(scale, data)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # Scale and MatrixIJ
        m2 = MatrixIJ(data)
        m = MatrixIJ(scale, m2)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], scale*data[row][col])
        # 2 args - column vectors
        # lists
        v = [[row[0] for row in data],
             [row[1] for row in data]]
        m = MatrixIJ(*v)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuples
        v = [tuple([row[0] for row in data]),
             tuple([row[1] for row in data])]
        m = MatrixIJ(*v)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # np.ndarrays
        v = [np.array([row[0] for row in data]),
             np.array([row[1] for row in data])]
        m = MatrixIJ(*v)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # VectorIJs
        v = [VectorIJ([row[0] for row in data]),
             VectorIJ([row[1] for row in data])]
        m = MatrixIJ(*v)
        self.assertIsInstance(m, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # 3-argument forms
        # Column scale factors and matrix
        scales = (-1.1, -2.2)
        m2 = MatrixIJ(*scales, m)
        self.assertIsInstance(m2, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scales[col]*data[row][col])
        # 4-argument forms
        # 4 individual elements COLUMN-MAJOR ORDER
        data = list(range(4))
        m = MatrixIJ(*data)
        for row in range(2):
            for col in range(2):
                k = row + 2*col
                self.assertAlmostEqual(m[row, col], data[k])
        # Scale factors and columns
        m = MatrixIJ(scales[0], v[0], scales[1], v[1])
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m[row, col], scales[col]*v[col][row])
        # Invalid forms
        data = [None]*5
        with self.assertRaises(TypeError):
            m = MatrixIJ(*data)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        data = [[1.1, 2.2], [3.3, 4.4]]
        m = MatrixIJ(data)
        self.assertAlmostEqual(m.ii, data[0][0])
        self.assertAlmostEqual(m.ij, data[0][1])
        self.assertAlmostEqual(m.ji, data[1][0])
        self.assertAlmostEqual(m.jj, data[1][1])
        with self.assertRaises(KeyError):
            data = m.bad

    def test___setattr__(self):
        """Test the __getattr__ method."""
        data = [[1.1, 2.2], [3.3, 4.4]]
        m = MatrixIJ()
        m.ii = data[0][0]
        self.assertAlmostEqual(m.ii, data[0][0])
        m.ij = data[0][1]
        self.assertAlmostEqual(m.ij, data[0][1])
        m.ji = data[1][0]
        self.assertAlmostEqual(m.ji, data[1][0])
        m.jj = data[1][1]
        self.assertAlmostEqual(m.jj, data[1][1])
        with self.assertRaises(KeyError):
            data = m.bad

    def test_createTranspose(self):
        m1 = MatrixIJ(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        m2 = m1.createTranspose()
        self.assertAlmostEqual(m2.ii, 1)
        self.assertAlmostEqual(m2.ji, 3)
        self.assertAlmostEqual(m2.ij, 2)
        self.assertAlmostEqual(m2.jj, 4)

    def test_createUnitizedColumns(self):
        m1 = MatrixIJ(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        m2 = m1.createUnitizedColumns()
        self.assertAlmostEqual(m2.ii, 1/sqrt(5))
        self.assertAlmostEqual(m2.ji, 2/sqrt(5))
        self.assertAlmostEqual(m2.ij, 3/5)
        self.assertAlmostEqual(m2.jj, 4/5)

    def test_createInverse(self):
        m1 = MatrixIJ(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        m2 = m1.createInverse()
        self.assertAlmostEqual(m2.ii, -2)
        self.assertAlmostEqual(m2.ji, 1)
        self.assertAlmostEqual(m2.ij, 3/2)
        self.assertAlmostEqual(m2.jj, -1/2)
        m3 = m2.createInverse(1e-4)
        self.assertAlmostEqual(m3.ii, 1)
        self.assertAlmostEqual(m3.ji, 2)
        self.assertAlmostEqual(m3.ij, 3)
        self.assertAlmostEqual(m3.jj, 4)

    def test_createInvorted(self):
        a = pi/3
        m1 = MatrixIJ(cos(a), sin(a), -sin(a), cos(a))
        m2 = m1.createInvorted()
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, -sin(a))
        self.assertAlmostEqual(m2.ij, sin(a))
        self.assertAlmostEqual(m2.jj, cos(a))

    def test_transpose(self):
        m = MatrixIJ(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        m.transpose()
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 3)
        self.assertAlmostEqual(m.ij, 2)
        self.assertAlmostEqual(m.jj, 4)

    def test_unitizeColumns(self):
        m = MatrixIJ(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        m.unitizeColumns()
        self.assertAlmostEqual(m.ii, 1/sqrt(5))
        self.assertAlmostEqual(m.ji, 2/sqrt(5))
        self.assertAlmostEqual(m.ij, 3/5)
        self.assertAlmostEqual(m.jj, 4/5)

    def test_invert(self):
        m1 = MatrixIJ(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        m2 = m1.invert()
        self.assertIs(m2, m1)
        self.assertAlmostEqual(m1.ii, -2)
        self.assertAlmostEqual(m1.ji, 1)
        self.assertAlmostEqual(m1.ij, 3/2)
        self.assertAlmostEqual(m1.jj, -1/2)
        m2 = m1.invert(1e-4)
        self.assertIs(m2, m1)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 2)
        self.assertAlmostEqual(m1.ij, 3)
        self.assertAlmostEqual(m1.jj, 4)
        m1 = MatrixIJ(0, 0, 0, 0)
        with self.assertRaises(Exception):
            m1.invert()
        with self.assertRaises(Exception):
            m1.invert(1e-4)

    def test_invort(self):
        a = pi/3
        m1 = MatrixIJ(cos(a), sin(a), -sin(a), cos(a))
        m2 = m1.invort()
        self.assertIs(m2, m1)
        self.assertAlmostEqual(m1.ii, cos(a))
        self.assertAlmostEqual(m1.ji, -sin(a))
        self.assertAlmostEqual(m1.ij, sin(a))
        self.assertAlmostEqual(m1.jj, cos(a))
        with self.assertRaises(Exception):
            m1 = MatrixIJ(0, 0, 0, 0)
            m1.invort()

    def test_scale(self):
        m = MatrixIJ(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        m.scale(-2)
        self.assertAlmostEqual(m.ii, -2)
        self.assertAlmostEqual(m.ji, -4)
        self.assertAlmostEqual(m.ij, -6)
        self.assertAlmostEqual(m.jj, -8)
        m.scale(-1, -2)
        self.assertAlmostEqual(m.ii, 2)
        self.assertAlmostEqual(m.ji, 4)
        self.assertAlmostEqual(m.ij, 12)
        self.assertAlmostEqual(m.jj, 16)

    def test_setII(self):
        m = MatrixIJ(1, 2, 3, 4)
        m.setII(-1)
        self.assertAlmostEqual(m.ii, -1)

    def test_setJI(self):
        m = MatrixIJ(1, 2, 3, 4)
        m.setJI(-1)
        self.assertAlmostEqual(m.ji, -1)

    def test_setIJ(self):
        m = MatrixIJ(1, 2, 3, 4)
        m.setIJ(-1)
        self.assertAlmostEqual(m.ij, -1)

    def test_setJJ(self):
        m = MatrixIJ(1, 2, 3, 4)
        m.setJJ(-1)
        self.assertAlmostEqual(m.jj, -1)

    def test_set(self):
        m = MatrixIJ(0, 0, 0, 0)
        m.set(0, 0, 1)
        m.set(1, 0, 2)
        m.set(0, 1, 3)
        m.set(1, 1, 4)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)
        self.assertAlmostEqual(m.ij, 3)
        self.assertAlmostEqual(m.jj, 4)
        with self.assertRaises(Exception):
            m.set(0, 2, -1)
        with self.assertRaises(Exception):
            m.set(1, 2, -1)
        with self.assertRaises(Exception):
            m.set(2, 0, -1)

    def test_setIthColumn(self):
        m = MatrixIJ(0, 0, 0, 0)
        v = VectorIJ(1, 2)
        m.setIthColumn(v)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)

    def test_setJthColumn(self):
        m = MatrixIJ(0, 0, 0, 0)
        v = VectorIJ(1, 2)
        m.setJthColumn(v)
        self.assertAlmostEqual(m.ij, 1)
        self.assertAlmostEqual(m.jj, 2)

    def test_setColumn(self):
        m = MatrixIJ(0, 0, 0, 0)
        v = VectorIJ(1, 2)
        m.setColumn(0, v)
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 2)
        v = VectorIJ(3, 4)
        m.setColumn(1, v)
        self.assertAlmostEqual(m.ij, 3)
        self.assertAlmostEqual(m.jj, 4)
        with self.assertRaises(Exception):
            m.setColumn(2, v)

    def test_setTo(self):
        m0 = MatrixIJ(0, 0, 0, 0)
        m1 = MatrixIJ()
        # 1-argument forms
        # COLUMN-MAJOR ORDER
        m2 = m1.setTo([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertIs(m2, m1)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 4)
        self.assertAlmostEqual(m1.ij, 2)
        self.assertAlmostEqual(m1.jj, 5)
        m2 = MatrixIJ()
        m3 = m2.setTo(m0)
        self.assertIs(m3, m2)
        self.assertAlmostEqual(m2.ii, 0)
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 0)
        # 2-argument forms
        m2 = MatrixIJ(1, 2, 3, 4)
        m3 = m1.setTo(-2, m2)
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m1.ii, -2)
        self.assertAlmostEqual(m1.ji, -4)
        self.assertAlmostEqual(m1.ij, -6)
        self.assertAlmostEqual(m1.jj, -8)
        v1 = VectorIJ(1, 2)
        v2 = VectorIJ(3, 4)
        m2 = m1.setTo(v1, v2)
        self.assertIs(m2, m1)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 2)
        self.assertAlmostEqual(m1.ij, 3)
        self.assertAlmostEqual(m1.jj, 4)
        # 3-argument form
        m1 = MatrixIJ(1, 2, 3, 4)
        m3 = m2.setTo(-1, -2, m1)
        self.assertIs(m3, m2)
        self.assertAlmostEqual(m2.ii, -1)
        self.assertAlmostEqual(m2.ji, -2)
        self.assertAlmostEqual(m2.ij, -6)
        self.assertAlmostEqual(m2.jj, -8)
        # 4-argument forms
        m1 = MatrixIJ()
        m2 = m1.setTo(1, 2, 3, 4)  # COLUMN-MAJOR ORDER
        self.assertIs(m2, m1)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 2)
        self.assertAlmostEqual(m1.ij, 3)
        self.assertAlmostEqual(m1.jj, 4)
        m2 = m1.setTo(-1, v1, 2, v2)
        self.assertIs(m2, m1)
        self.assertAlmostEqual(m1.ii, -1)
        self.assertAlmostEqual(m1.ji, -2)
        self.assertAlmostEqual(m1.ij, 6)
        self.assertAlmostEqual(m1.jj, 8)
        # Invalid forms
        with self.assertRaises(Exception):
            m2.setTo()

    def test_setToTranspose(self):
        m1 = MatrixIJ()
        m2 = MatrixIJ(1, 2, 3, 4)
        m1.setToTranspose(m2)
        self.assertAlmostEqual(m1.ii, 1)
        self.assertAlmostEqual(m1.ji, 3)
        self.assertAlmostEqual(m1.ij, 2)
        self.assertAlmostEqual(m1.jj, 4)

    def test_setToUnitizedColumns(self):
        m1 = MatrixIJ()
        m2 = MatrixIJ(1, 2, 3, 4)
        m1.setToUnitizedColumns(m2)
        self.assertAlmostEqual(m1.ii, 1/sqrt(5))
        self.assertAlmostEqual(m1.ji, 2/sqrt(5))
        self.assertAlmostEqual(m1.ij, 3/5)
        self.assertAlmostEqual(m1.jj, 4/5)

    def test_setToInverse(self):
        m1 = MatrixIJ()
        m2 = MatrixIJ(1, 2, 3, 4)
        m3 = m1.setToInverse(m2)
        self.assertIs(m3, m1)
        self.assertAlmostEqual(m1.ii, -2)
        self.assertAlmostEqual(m1.ji, 1)
        self.assertAlmostEqual(m1.ij, 3/2)
        self.assertAlmostEqual(m1.jj, -1/2)
        m4 = MatrixIJ()
        m5 = m4.setToInverse(m1, 1e-4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m4.ii, 1)
        self.assertAlmostEqual(m4.ji, 2)
        self.assertAlmostEqual(m4.ij, 3)
        self.assertAlmostEqual(m4.jj, 4)
        with self.assertRaises(Exception):
            m6 = MatrixIJ(0, 0, 0, 0)
            m5.setToInverse(m6)
        with self.assertRaises(Exception):
            m6 = MatrixIJ(0, 0, 0, 0)
            m5.setToInverse(m6, 1e-4)

    def test_setToInvorted(self):
        a = pi/3
        m1 = MatrixIJ(cos(a), sin(a), -sin(a), cos(a))
        m2 = MatrixIJ()
        m2.setToInvorted(m1)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, -sin(a))
        self.assertAlmostEqual(m2.ij, sin(a))
        self.assertAlmostEqual(m2.jj, cos(a))

    def test_mxmt(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(5, 6, 7, 8)
        m3 = MatrixIJ.mxmt(m1, m2)
        # |1 3| |5 7|T = |1 3| |5 6|
        # |2 4| |6 8|    |2 4| |7 8|
        self.assertAlmostEqual(m3.ii, 1*5 + 3*7)
        self.assertAlmostEqual(m3.ij, 1*6 + 3*8)
        self.assertAlmostEqual(m3.ji, 2*5 + 4*7)
        self.assertAlmostEqual(m3.jj, 2*6 + 4*8)
        m4 = MatrixIJ()
        m5 = MatrixIJ.mxmt(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 1*5 + 3*7)
        self.assertAlmostEqual(m5.ij, 1*6 + 3*8)
        self.assertAlmostEqual(m5.ji, 2*5 + 4*7)
        self.assertAlmostEqual(m5.jj, 2*6 + 4*8)

    def test_mtxm(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(5, 6, 7, 8)
        m3 = MatrixIJ.mtxm(m1, m2)
        # |1 3|T |5 7| = |1 2| |5 7|
        # |2 4|  |6 8|   |3 4| |6 8|
        self.assertAlmostEqual(m3.ii, 1*5 + 2*6)
        self.assertAlmostEqual(m3.ij, 1*7 + 2*8)
        self.assertAlmostEqual(m3.ji, 3*5 + 4*6)
        self.assertAlmostEqual(m3.jj, 3*7 + 4*8)
        m4 = MatrixIJ()
        m5 = MatrixIJ.mtxm(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 1*5 + 2*6)
        self.assertAlmostEqual(m5.ij, 1*7 + 2*8)
        self.assertAlmostEqual(m5.ji, 3*5 + 4*6)
        self.assertAlmostEqual(m5.jj, 3*7 + 4*8)

    def test_mxm(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(5, 6, 7, 8)
        m3 = MatrixIJ.mxm(m1, m2)
        # |1 3| |5 7|
        # |2 4| |6 8|
        self.assertAlmostEqual(m3.ii, 1*5 + 3*6)
        self.assertAlmostEqual(m3.ij, 1*7 + 3*8)
        self.assertAlmostEqual(m3.ji, 2*5 + 4*6)
        self.assertAlmostEqual(m3.jj, 2*7 + 4*8)
        m4 = MatrixIJ()
        m5 = MatrixIJ.mxm(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 1*5 + 3*6)
        self.assertAlmostEqual(m5.ij, 1*7 + 3*8)
        self.assertAlmostEqual(m5.ji, 2*5 + 4*6)
        self.assertAlmostEqual(m5.jj, 2*7 + 4*8)

    def test_mxmtadd(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(5, 6, 7, 8)
        m3 = MatrixIJ(9, 1, 2, 3)
        m4 = MatrixIJ(4, 5, 6, 7)
        # |1 3| |5 7|T + |9 2| |4 6|T = |1 3| |5 6| + |9 2| |4 5|
        # |2 4| |6 8|    |1 3| |5 7|    |2 4| |7 8|   |1 3| |6 7|
        m5 = MatrixIJ.mxmtadd(m1, m2, m3, m4)
        self.assertAlmostEqual(m5.ii, 1*5 + 3*7 + 9*4 + 2*6)
        self.assertAlmostEqual(m5.ji, 2*5 + 4*7 + 1*4 + 3*6)
        self.assertAlmostEqual(m5.ij, 1*6 + 3*8 + 9*5 + 2*7)
        self.assertAlmostEqual(m5.jj, 2*6 + 4*8 + 1*5 + 3*7)
        m6 = MatrixIJ()
        m7 = MatrixIJ.mxmtadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        self.assertAlmostEqual(m7.ii, 1*5 + 3*7 + 9*4 + 2*6)
        self.assertAlmostEqual(m7.ji, 2*5 + 4*7 + 1*4 + 3*6)
        self.assertAlmostEqual(m7.ij, 1*6 + 3*8 + 9*5 + 2*7)
        self.assertAlmostEqual(m7.jj, 2*6 + 4*8 + 1*5 + 3*7)

    def test_mtxmadd(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(5, 6, 7, 8)
        m3 = MatrixIJ(9, 1, 2, 3)
        m4 = MatrixIJ(4, 5, 6, 7)
        # |1 3|T|5 7| + |9 2|T|4 6| = |1 2| |5 7| + |9 1| |4 6|
        # |2 4| |6 8|   |1 3| |5 7|   |3 4| |6 8|   |2 3| |5 7|
        m5 = MatrixIJ.mtxmadd(m1, m2, m3, m4)
        self.assertAlmostEqual(m5.ii, 1*5 + 2*6 + 9*4 + 1*5)
        self.assertAlmostEqual(m5.ji, 3*5 + 4*6 + 2*4 + 3*5)
        self.assertAlmostEqual(m5.ij, 1*7 + 2*8 + 9*6 + 1*7)
        self.assertAlmostEqual(m5.jj, 3*7 + 4*8 + 2*6 + 3*7)
        m6 = MatrixIJ()
        m7 = MatrixIJ.mtxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        self.assertAlmostEqual(m7.ii, 1*5 + 2*6 + 9*4 + 1*5)
        self.assertAlmostEqual(m7.ji, 3*5 + 4*6 + 2*4 + 3*5)
        self.assertAlmostEqual(m7.ij, 1*7 + 2*8 + 9*6 + 1*7)
        self.assertAlmostEqual(m7.jj, 3*7 + 4*8 + 2*6 + 3*7)

    def test_mxmadd(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(5, 6, 7, 8)
        m3 = MatrixIJ(9, 1, 2, 3)
        m4 = MatrixIJ(4, 5, 6, 7)
        # |1 3| |5 7| + |9 2| |4 6|
        # |2 4| |6 8|   |1 3| |5 7|
        m5 = MatrixIJ.mxmadd(m1, m2, m3, m4)
        self.assertAlmostEqual(m5.ii, 1*5 + 3*6 + 9*4 + 2*5)
        self.assertAlmostEqual(m5.ji, 2*5 + 4*6 + 1*4 + 3*5)
        self.assertAlmostEqual(m5.ij, 1*7 + 3*8 + 9*6 + 2*7)
        self.assertAlmostEqual(m5.jj, 2*7 + 4*8 + 1*6 + 3*7)
        m6 = MatrixIJ()
        m7 = MatrixIJ.mxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        self.assertAlmostEqual(m7.ii, 1*5 + 3*6 + 9*4 + 2*5)
        self.assertAlmostEqual(m7.ji, 2*5 + 4*6 + 1*4 + 3*5)
        self.assertAlmostEqual(m7.ij, 1*7 + 3*8 + 9*6 + 2*7)
        self.assertAlmostEqual(m7.jj, 2*7 + 4*8 + 1*6 + 3*7)

    def test_subtract(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(1.1, 2.2, 3.3, 4.4)
        m3 = MatrixIJ.subtract(m1, m2)
        self.assertAlmostEqual(m3.ii, -0.1)
        self.assertAlmostEqual(m3.ji, -0.2)
        self.assertAlmostEqual(m3.ij, -0.3)
        self.assertAlmostEqual(m3.jj, -0.4)
        m4 = MatrixIJ()
        m5 = MatrixIJ.subtract(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, -0.1)
        self.assertAlmostEqual(m5.ji, -0.2)
        self.assertAlmostEqual(m5.ij, -0.3)
        self.assertAlmostEqual(m5.jj, -0.4)

    def test_add(self):
        m1 = MatrixIJ(1, 2, 3, 4)
        m2 = MatrixIJ(1.1, 2.2, 3.3, 4.4)
        m3 = MatrixIJ.add(m1, m2)
        self.assertAlmostEqual(m3.ii, 2.1)
        self.assertAlmostEqual(m3.ji, 4.2)
        self.assertAlmostEqual(m3.ij, 6.3)
        self.assertAlmostEqual(m3.jj, 8.4)
        m4 = MatrixIJ()
        m5 = MatrixIJ.add(m1, m2, m4)
        self.assertIs(m5, m4)
        self.assertAlmostEqual(m5.ii, 2.1)
        self.assertAlmostEqual(m5.ji, 4.2)
        self.assertAlmostEqual(m5.ij, 6.3)
        self.assertAlmostEqual(m5.jj, 8.4)

    def test_diagonalizeSymmetricMatrix(self):
        m1 = MatrixIJ(6, 2, 2, 3)
        v = VectorIJ()
        m2 = MatrixIJ()
        MatrixIJ.diagonalizeSymmetricMatrix(m1, v, m2)
        self.assertAlmostEqual(v.i, 7)
        self.assertAlmostEqual(v.j, 2)
        self.assertAlmostEqual(m2.ii, 0.8944271909999159)
        self.assertAlmostEqual(m2.ji, 0.44721359549995787)
        self.assertAlmostEqual(m2.ij, -0.44721359549995787)
        self.assertAlmostEqual(m2.jj, 0.8944271909999159)

    def test_solveQuadratic(self):
        # (x - 1)*(x - 2) = x**2 - 3*x + 2
        a = 1
        b = -3
        c = 2
        v = VectorIJ()
        MatrixIJ.solveQuadratic(a, b, c, v)
        self.assertAlmostEqual(v.i, 2)
        self.assertAlmostEqual(v.j, 1)
        # (x - 1)*(x - 1) = x**2 - 2*x + 1
        a = 1
        b = -2
        c = 1
        v = VectorIJ()
        MatrixIJ.solveQuadratic(a, b, c, v)
        self.assertAlmostEqual(v.i, 1)
        self.assertAlmostEqual(v.j, 1)
        # (x + 2)*(x - 1) = x**2 + x - 2
        a = 1
        b = 1
        c = -2
        v = VectorIJ()
        MatrixIJ.solveQuadratic(a, b, c, v)
        self.assertAlmostEqual(v.i, 1)
        self.assertAlmostEqual(v.j, -2)
        # (2x + 1)*(x - 1) = 2*x**2 - x - 1
        a = 2
        b = -1
        c = -1
        v = VectorIJ()
        MatrixIJ.solveQuadratic(a, b, c, v)
        self.assertAlmostEqual(v.i, 1)
        self.assertAlmostEqual(v.j, -1/2)
        # x - 2
        a = 0
        b = 1
        c = -2
        v = VectorIJ()
        MatrixIJ.solveQuadratic(a, b, c, v)
        self.assertAlmostEqual(v.i, 2)
        self.assertAlmostEqual(v.j, 2)

    def test_mtxv(self):
        m = MatrixIJ(1, 2, 3, 4)
        v1 = VectorIJ(5, 6)
        v2 = MatrixIJ.mtxv(m, v1)
        self.assertAlmostEqual(v2.i, 17)
        self.assertAlmostEqual(v2.j, 39)
        v3 = VectorIJ()
        v4 = MatrixIJ.mtxv(m, v1, v3)
        self.assertIs(v4, v3)
        self.assertAlmostEqual(v4.i, 17)
        self.assertAlmostEqual(v4.j, 39)

    def test_mxv(self):
        m = MatrixIJ(1, 2, 3, 4)
        v1 = VectorIJ(5, 6)
        v2 = MatrixIJ.mxv(m, v1)
        self.assertAlmostEqual(v2.i, 23)
        self.assertAlmostEqual(v2.j, 34)
        v3 = VectorIJ()
        v4 = MatrixIJ.mxv(m, v1, v3)
        self.assertIs(v4, v3)
        self.assertAlmostEqual(v4.i, 23)
        self.assertAlmostEqual(v4.j, 34)

    def test_getDeterminant(self):
        data = [0, 1, 2, 3]  # COLUMN-MAJOR ORDER
        m = MatrixIJ(*data)
        self.assertAlmostEqual(m.getDeterminant(), -2)

    def test_getII(self):
        data = [0, 1, 2, 3]  # COLUMN-MAJOR ORDER
        m = MatrixIJ(*data)
        self.assertAlmostEqual(m.getII(), data[0])

    def test_getJI(self):
        data = [0, 1, 2, 3]  # COLUMN-MAJOR ORDER
        m = MatrixIJ(*data)
        self.assertAlmostEqual(m.getJI(), data[1])

    def test_getIJ(self):
        data = [0, 1, 2, 3]  # COLUMN-MAJOR ORDER
        m = MatrixIJ(*data)
        self.assertAlmostEqual(m.getIJ(), data[2])

    def test_getJJ(self):
        data = [0, 1, 2, 3]  # COLUMN-MAJOR ORDER
        m = MatrixIJ(*data)
        self.assertAlmostEqual(m.getJJ(), data[3])


if __name__ == '__main__':
    unittest.main()
