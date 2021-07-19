"""Tests for the matrixij module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):
    """Tests for the matrixij module."""

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
        # 4 individual elements
        data = list(range(4))
        m = MatrixIJ(*data)
        for row in range(2):
            for col in range(2):
                k = row*2 + col
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

    def test_setII(self):
        """Test the setII method."""
        m = MatrixIJ()
        m.setII(-1)
        self.assertAlmostEqual(m.ii, -1)

    def test_setJI(self):
        """Test the setJI method."""
        m = MatrixIJ()
        m.setJI(-1)
        self.assertAlmostEqual(m.ji, -1)

    def test_setIJ(self):
        """Test the setIJ method."""
        m = MatrixIJ()
        m.setIJ(-1)
        self.assertAlmostEqual(m.ij, -1)

    def test_setJJ(self):
        """Test the setJJ method."""
        m = MatrixIJ()
        m.setJJ(-1)
        self.assertAlmostEqual(m.jj, -1)

    def test_set(self):
        """Test the set method."""
        m = MatrixIJ()
        for row in range(2):
            for col in range(2):
                val = row*10 + col
                m.set(row, col, val)
                self.assertAlmostEqual(m[row, col], val)

    def test_setIthColumn(self):
        """Test the setIthColumn method."""
        # list
        m = MatrixIJ()
        data = list(range(2))
        m.setIthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 0], data[row])
        # tuple
        m = MatrixIJ()
        data = tuple(range(2))
        m.setIthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 0], data[row])
        # np.ndarray
        m = MatrixIJ()
        data = np.array(range(2))
        m.setIthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 0], data[row])
        # VectorIJ
        m = MatrixIJ()
        data = VectorIJ(list(range(2)))
        m.setIthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 0], data[row])

    def test_setJthColumn(self):
        """Test the setJthColumn method."""
        # list
        m = MatrixIJ()
        data = list(range(2))
        m.setJthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 1], data[row])
        # tuple
        m = MatrixIJ()
        data = tuple(range(2))
        m.setJthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 1], data[row])
        # np.ndarray
        m = MatrixIJ()
        data = np.array(range(2))
        m.setJthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 1], data[row])
        # VectorIJK
        m = MatrixIJ()
        data = VectorIJ(list(range(2)))
        m.setJthColumn(data)
        for row in range(2):
            self.assertAlmostEqual(m[row, 1], data[row])

    def test_setColumn(self):
        """Test the setColumn method."""
        m = MatrixIJ()
        data = list(range(2))
        v = VectorIJ(*data)
        for col in range(2):
            m.setColumn(col, v)
            for row in range(2):
                self.assertAlmostEqual(m[row, col], data[row])

    def test_setTo(self):
        """Test the setTo method."""
        m1 = MatrixIJ()
        # 1 arg forms
        # list of lists
        data = [[0, 1], [2, 3]]
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # tuple of tuples
        data = ((0, 1), (2, 3))
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # list of tuples
        data = [(0, 1), (2, 3)]
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # tuple of lists
        data = ([0, 1], [2, 3])
        m2 = m1.setTo(data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # np.ndarray
        a = np.array(data)
        m2 = m1.setTo(a)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # matrix
        m3 = MatrixIJ(data)
        m2 = m1.setTo(m3)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # 2-arg forms: scale factor and array-like
        scale = -2.2
        # Scale and list of lists.
        data = [[0, 1], [3, 4]]
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and tuple of tuples
        data = ((0, 1), (3, 4))
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and list of tuples
        data = [(0, 1), (3, 4)]
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and tuple of lists
        data = ([0, 1], [3, 4])
        m2 = m1.setTo(scale, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and np.ndarray
        a = np.array(data)
        m2 = m1.setTo(scale, a)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Scale and matrix
        m3 = MatrixIJ(data)
        m2 = m1.setTo(scale, m3)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scale*data[row][col])
        # Column vectors
        data = [[0, 1], [2, 3]]
        # list of lists
        v = [[row[0] for row in data],
             [row[1] for row in data]]
        m2 = m1.setTo(*v)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # list of tuples
        v = [tuple([row[0] for row in data]),
             tuple([row[1] for row in data])]
        m2 = m1.setTo(*v)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # list of np.ndarray
        v = [np.array([row[0] for row in data]),
             np.array([row[1] for row in data])]
        m2 = m1.setTo(*v)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data[row][col])
        # 3 arg forms: scale an array-like by columns
        scales = (-1.1, -2.2)
        # Scales and list of lists
        data = [[0, 1], [2, 3]]
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and tuple of tuples
        data = ((0, 1), (2, 3))
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and list of tuples
        data = [(0, 1), (2, 3)]
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and tuple of lists
        data = ([0, 1], [2, 3])
        m2 = m1.setTo(*scales, data)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and np.ndarray
        a = np.array(data)
        m2 = m1.setTo(*scales, a)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # Scale and MatrixIJ
        m3 = MatrixIJ(data)
        m2 = m1.setTo(*scales, m3)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*data[row][col])
        # 4 arg forms: individually-scaled columns
        s = (-1.1, -2.2)
        data = [[0, 1], [3, 4]]
        # lists
        v = [[row[0] for row in data],
             [row[1] for row in data]]
        m1 = MatrixIJ()
        m2 = m1.setTo(s[0], v[0], s[1], v[1])
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])
        # tuples
        v = [tuple([row[0] for row in data]),
             tuple([row[1] for row in data])]
        m1 = MatrixIJ()
        m2 = m1.setTo(s[0], v[0], s[1], v[1])
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])
        # np.ndarray
        v = [np.array([row[0] for row in data]),
             np.array([row[1] for row in data])]
        m1 = MatrixIJ()
        m2 = m1.setTo(s[0], v[0], s[1], v[1])
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])
        # VectorIJ
        v = [VectorIJ([row[0] for row in data]),
             VectorIJ([row[1] for row in data])]
        m1 = MatrixIJ()
        m2 = m1.setTo(s[0], v[0], s[1], v[1])
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], s[col]*data[row][col])
        # individual values
        m1 = MatrixIJ()
        m2 = m1.setTo(*(data[0] + data[1]))
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                k = col*3 + row
                self.assertAlmostEqual(m2[row, col], k)
        # Invalid forms
        for n in (0, 5):
            data = [None]*n
            with self.assertRaises(ValueError):
                m1.setTo(*data)

    def test_transposeInPlace(self):
        """Test the tranposeInPlace method."""
        data = list(range(4))
        m1 = MatrixIJ(*data)
        m1_orig = MatrixIJ(m1)
        m2 = m1.transposeInPlace()
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], m1_orig[col, row])

    def unitizeColumns(self):
        """Convert each column to a unit vector.

        Unitize the columns of the matrix in-place.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        for col in range(2):
            length = np.linalg.norm(self[:, col])
            self[:, col] /= length
        return self

    def test_unitizeColumns(self):
        """Test the unitizeColumns method."""
        data1 = list(range(4))
        a1 = np.array(data1).reshape((2, 2))
        lengths = np.linalg.norm(a1, axis=0)
        a2 = a1/lengths
        m1 = MatrixIJ(*data1)
        m2 = m1.unitizeColumns()
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], a2[row, col])

    def test_invert(self):
        """Test the invert method."""
        data = [[1, 2], [3, 4]]
        data_inv = (-2, 1.5, 1.0, -0.5)
        m1 = MatrixIJ(*data)
        m1_inv = MatrixIJ(*data_inv)
        m2 = m1.invert()
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], m1_inv[row, col])

    def test_invort(self):
        a = pi/3
        data = (cos(a), -sin(a), sin(a), cos(a))
        data_inv = [[cos(a), sin(a)], [-sin(a), cos(a)]]
        m1 = MatrixIJ(*data)
        m2 = m1.invort()
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], data_inv[row][col])

    def test_scale(self):
        """Test the scale method."""
        data = list(range(4))
        # 1 arg form
        # Single scale factor.
        scale = -1.1
        m1 = MatrixIJ(*data)
        m1_orig = MatrixIJ(m1)
        m2 = m1.scale(scale)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], scale*m1_orig[row, col])
        # 2-arg form.
        # Column scale factors.
        scales = (-1.1, -2.2)
        m1 = MatrixIJ(*data)
        m2 = m1.scale(*scales)
        self.assertIs(m2, m1)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col],
                                       scales[col]*m1_orig[row, col])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                m1.scale(*data)

    def test_createTranspose(self):
        """Test the createTranspose method."""
        data = list(range(4))
        m1 = MatrixIJ(*data)
        m2 = m1.createTranspose()
        self.assertIsInstance(m2, MatrixIJ)
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(m2[i, j], m1[j, i])

    def test_createUnitizedColumns(self):
        """Test the createUnitizedColumns method."""
        data1 = list(range(4))
        a1 = np.array(data1).reshape((2, 2))
        lengths = np.linalg.norm(a1, axis=0)
        a2 = a1/lengths
        m1 = MatrixIJ(*data1)
        m2 = m1.createUnitizedColumns()
        self.assertIsInstance(m2, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], a2[row, col])

    def test_createInverse(self):
        """Test the createInverse method."""
        data = (1, 3, 2, 4)
        data_inv = (-2, 1.5, 1, -0.5)
        m1 = MatrixIJ(*data)
        m1_inv = MatrixIJ(*data_inv)
        m2 = m1.createInverse()
        self.assertIsInstance(m2, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], m1_inv[row, col])

    def test_createInvorted(self):
        """Test the createInvorted method."""
        a = pi/3
        data = (cos(a), -sin(a), sin(a), cos(a))
        data_inv = (cos(a), sin(a), -sin(a), cos(a))
        m1 = MatrixIJ(*data)
        m1_inv = MatrixIJ(*data_inv)
        m2 = m1.createInvorted()
        self.assertIsInstance(m2, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m2[row, col], m1_inv[row, col])

    def test_setToTranspose(self):
        """Test the setToTranspose method."""
        data = list(range(4))
        m1 = MatrixIJ(*data)
        m2 = MatrixIJ()
        m3 = m2.setToTranspose(m1)
        self.assertIs(m3, m2)
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(m3[i, j], m1[j, i])

    def test_setToUnitizedColumns(self):
        """Test the createUnitizedColumns method."""
        data1 = list(range(4))
        a1 = np.array(data1).reshape((2, 2))
        lengths = np.linalg.norm(a1, axis=0)
        a2 = a1/lengths
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ()
        m3 = m2.setToUnitizedColumns(m1)
        self.assertIs(m3, m2)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m3[row, col], a2[row, col])

    def test_setToInverse(self):
        """Test the setToInverse method."""
        data = (1, 3, 2, 4)
        data_inv = (-2, 1.5, 1, -0.5)
        m1 = MatrixIJ(*data)
        m1_inv = MatrixIJ(*data_inv)
        m2 = MatrixIJ()
        m3 = m2.setToInverse(m1)
        self.assertIs(m3, m2)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m3[row, col], m1_inv[row, col])

    def test_createInvorted(self):
        """Test the createInvorted method."""
        a = pi/3
        data = (cos(a), -sin(a), sin(a), cos(a))
        data_inv = (cos(a), sin(a), -sin(a), cos(a))
        m1 = MatrixIJ(*data)
        m1_inv = MatrixIJ(*data_inv)
        m2 = MatrixIJ()
        m3 = m2.setToInvorted(m1)
        self.assertIsInstance(m3, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m3[row, col], m1_inv[row, col])

    def test_add(self):
        """Test the add method."""
        data1 = list(range(1, 5))
        data2 = list(reversed(data1))
        data3 = [x1 + x2 for (x1, x2) in zip(data1, data2)]
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        m3 = MatrixIJ(*data3)
        # 1-arg form.
        # No buffer.
        m4 = m1.add(m2)
        self.assertIsInstance(m4, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg form.
        # Use buffer.
        m4 = MatrixIJ()
        m5 = m1.add(m2, m4)
        self.assertIs(m5, m4)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            with self.assertRaises(ValueError):
                data = [None]*n
                m1.add(*data)

    def test_subtract(self):
        """Test the subtract method."""
        data1 = list(range(1, 5))
        data2 = list(reversed(data1))
        data3 = [x1 - x2 for (x1, x2) in zip(data1, data2)]
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        m3 = MatrixIJ(*data3)
        # 1-arg form.
        # No buffer.
        m4 = m1.subtract(m2)
        self.assertIsInstance(m4, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg form.
        # Use buffer.
        m4 = MatrixIJ()
        m5 = m1.subtract(m2, m4)
        self.assertIs(m5, m4)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            with self.assertRaises(ValueError):
                data = [None]*n
                m1.subtract(*data)

    def test_mxm(self):
        """Test the mxm method."""
        data1 = list(range(4))
        data2 = list(reversed(data1))
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        p = np.zeros((2, 2))
        for row in range(2):
            for col in range(2):
                for k in range(2):
                    p[row][col] += m1[row][k]*m2[k][col]
        m3 = MatrixIJ(p)
        # 1-arg version
        # No buffer.
        m4 = m1.mxm(m2)
        self.assertIsInstance(m4, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg version.
        # With buffer.
        m4 = MatrixIJ()
        m5 = m1.mxm(m2, m4)
        self.assertIs(m5, m4)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                m3 = m1.mxm(*data)

    def test_mxmt(self):
        """Test the mxmt method."""
        data1 = list(range(4))
        data2 = list(reversed(data1))
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        m3 = m1.dot(m2.T)
        # 1-arg version
        # No buffer.
        m4 = MatrixIJ.mxmt(m1, m2)
        self.assertIsInstance(m4, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg version.
        # With buffer.
        m4 = MatrixIJ()
        m5 = m1.mxmt(m2, m4)
        self.assertIs(m5, m4)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                m3 = m1.mxmt(*data)

    def test_mtxm(self):
        """Test the mtxm method."""
        data1 = list(range(1, 5))
        data2 = list(reversed(data1))
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        m3 = m1.T.dot(m2)
        # 1-arg form
        # No buffer.
        m4 = m1.mtxm(m2)
        self.assertIsInstance(m4, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m4[row, col], m3[row, col])
        # 2-arg form.
        # Use buffer.
        m4 = MatrixIJ()
        m5 = m1.mtxm(m2, m4)
        self.assertIs(m5, m4)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m5[row, col], m3[row, col])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                m3 = m1.mtxm(*data)

    def test_mxmadd(self):
        """Test the mxmadd method."""
        data1 = (1, 2, 3, 4)
        data2 = (2, 3, 4, 1)
        data3 = (3, 4, 1, 2)
        data4 = (4, 1, 2, 3)
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        m3 = MatrixIJ(*data3)
        m4 = MatrixIJ(*data4)
        m5a = MatrixIJ.mxm(m1, m2)
        m5b = MatrixIJ.mxm(m3, m4)
        m5 = m5a + m5b
        # 4-arg form.
        # No buffer.
        m6 = MatrixIJ.mxmadd(m1, m2, m3, m4)
        self.assertIsInstance(m6, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m6[row, col], m5[row, col])
        # 5-arg form.
        # Use buffer.
        m6 = MatrixIJ()
        m7 = MatrixIJ.mxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m7[row, col], m5[row, col])

    def test_mxmtadd(self):
        """Test the mxmtadd method."""
        data1 = (1, 2, 3, 4)
        data2 = (2, 3, 4, 1)
        data3 = (3, 4, 1, 2)
        data4 = (4, 1, 2, 3)
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        m3 = MatrixIJ(*data3)
        m4 = MatrixIJ(*data4)
        m5a = MatrixIJ.mxmt(m1, m2)
        m5b = MatrixIJ.mxmt(m3, m4)
        m5 = m5a + m5b
        # 4-arg form.
        # No buffer.
        m6 = MatrixIJ.mxmtadd(m1, m2, m3, m4)
        self.assertIsInstance(m6, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m6[row, col], m5[row, col])
        # 5-arg form.
        # Use buffer.
        m6 = MatrixIJ()
        m7 = MatrixIJ.mxmtadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m7[row, col], m5[row, col])

    def test_mtxmadd(self):
        """Test the mtxmadd method."""
        data1 = (1, 2, 3, 4)
        data2 = (2, 3, 4, 1)
        data3 = (3, 4, 1, 2)
        data4 = (4, 1, 2, 3)
        m1 = MatrixIJ(*data1)
        m2 = MatrixIJ(*data2)
        m3 = MatrixIJ(*data3)
        m4 = MatrixIJ(*data4)
        m5a = MatrixIJ.mtxm(m1, m2)
        m5b = MatrixIJ.mtxm(m3, m4)
        m5 = m5a + m5b
        # 4-arg form.
        # No buffer.
        m6 = MatrixIJ.mtxmadd(m1, m2, m3, m4)
        self.assertIsInstance(m6, MatrixIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m6[row, col], m5[row, col])
        # 5-arg form.
        # Use buffer.
        m6 = MatrixIJ()
        m7 = MatrixIJ.mtxmadd(m1, m2, m3, m4, m6)
        self.assertIs(m7, m6)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(m7[row, col], m5[row, col])

    def test_mxv(self):
        """Test the mxv method."""
        data1 = list(range(4))
        data2 = list(range(2))
        m1 = MatrixIJ(*data1)
        v1 = VectorIJ(*data2)
        v2 = m1.dot(v1)
        # 1-arg form.
        # No buffer.
        v3 = m1.mxv(v1)
        self.assertIsInstance(v3, VectorIJ)
        for row in range(2):
            self.assertAlmostEqual(v3[row], v2[row])
        # 2-arg form.
        # Use buffer.
        v3 = VectorIJ()
        v4 = m1.mxv(v1, v3)
        self.assertIs(v4, v3)
        for row in range(2):
            self.assertAlmostEqual(v4[row], v2[row])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                v2 = m1.mxv(*data)

    def test_mtxv(self):
        """Test the mtxv method."""
        data1 = list(range(4))
        data2 = list(range(2))
        m1 = MatrixIJ(*data1)
        v1 = VectorIJ(*data2)
        v2 = m1.T.dot(v1)
        # 1-arg form.
        # No buffer.
        v3 = m1.mtxv(v1)
        self.assertIsInstance(v3, VectorIJ)
        for row in range(2):
            self.assertAlmostEqual(v3[row], v2[row])
        # 2-arg form.
        # Use buffer.
        v3 = VectorIJ()
        v4 = m1.mtxv(v1, v3)
        self.assertIs(v4, v3)
        for row in range(2):
            self.assertAlmostEqual(v4[row], v2[row])
        # Invalid forms.
        for n in (0, 3):
            data = [None]*n
            with self.assertRaises(ValueError):
                v2 = m1.mtxv(*data)


if __name__ == '__main__':
    unittest.main()
