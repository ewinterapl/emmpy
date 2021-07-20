"""Tests for the rotationmatrixijk module."""


from math import cos, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)
from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the rotationmatrixijk module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0-arg form - creates identity matrix.
        m1 = RotationMatrixIJK()
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                if row == col:
                    self.assertAlmostEqual(m1[row, col], 1)
                else:
                    self.assertAlmostEqual(m1[row, col], 0)
        # 1 arg forms.
        # list of lists.
        a = 1
        data1 = [[cos(a), 0, sin(a)],
                 [0, 1, 0],
                 [-sin(a), 0, cos(a)]]
        m1 = RotationMatrixIJK(data1)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row][col])
        # tuple of tuples
        data1 = ((cos(a), 0, sin(a)),
                 (0, 1, 0),
                 (-sin(a), 0, cos(a)))
        m1 = RotationMatrixIJK(data1)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row][col])
        # list of tuples
        data1 = [(cos(a), 0, sin(a)),
                 (0, 1, 0),
                 (-sin(a), 0, cos(a))]
        m1 = RotationMatrixIJK(data1)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row][col])
        # tuple of lists
        data1 = ([cos(a), 0, sin(a)],
                 [0, 1, 0],
                 [-sin(a), 0, cos(a)])
        m1 = RotationMatrixIJK(data1)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row][col])
        # Numpy array
        a1 = np.array(data1)
        m2 = RotationMatrixIJK(m1)
        self.assertIsInstance(m2, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], a1[row, col])
        # 3 args - column vectors
        v = []
        for col in range(3):
            data = [row[col] for row in data1]
            v.append(VectorIJK(*data))
        m1 = RotationMatrixIJK(*v)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row][col])
        # 9-arg form - all components
        data1 = (cos(a), 0, sin(a),
                 0, 1, 0,
                 -sin(a), 0, cos(a))
        m1 = RotationMatrixIJK(*data1)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row*3 + col])
        # Invalid forms.
        for n in (2, 4, 5, 6, 7, 8, 10):
            with self.assertRaises(ValueError):
                args = [None]*n
                m1 = RotationMatrixIJK(*args)
        with self.assertRaises(MalformedRotationException):
            args = (1, 0, sin(a),
                    0, 1, 0,
                    -sin(a), 0, cos(a))
            m1 = RotationMatrixIJK(*args)

    def test_isRotation(self):
        """Test the isRotation method."""
        # A rotation.
        a = 1
        data1 = (cos(a), 0, sin(a),
                 0, 1, 0,
                 -sin(a), 0, cos(a))
        m1 = RotationMatrixIJK(*data1)
        self.assertTrue(m1.isRotation())
        # A non-rotation.
        m1[0, 0] = 1
        self.assertFalse(m1.isRotation())

    def test_sharpen(self):
        """Test the sharpen method."""
        a = 1
        data1 = ((cos(a), 0, sin(a)),
                 (0, 1, 0),
                 (-sin(a), 0, cos(a)))
        m1 = RotationMatrixIJK(data1)
        m1.sharpen()
        self.assertTrue(m1.isRotation())

    def test_createSharpened(self):
        """Test the createSharpened method."""
        a = 1
        data1 = ((cos(a), 0, sin(a)),
                 (0, 1, 0),
                 (-sin(a), 0, cos(a)))
        m1 = RotationMatrixIJK(data1)
        m2 = m1.createSharpened()
        self.assertIsInstance(m2, RotationMatrixIJK)
        self.assertTrue(m2.isRotation())

    def test_createTranspose(self):
        """Test the createTranspose method."""
        a = 1
        data1 = ((cos(a), 0, sin(a)),
                 (0, 1, 0),
                 (-sin(a), 0, cos(a)))
        m1 = RotationMatrixIJK(data1)
        m2 = m1.createTranspose()
        self.assertIsInstance(m2, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row][col], data1[col][row])

    def test_createInverse(self):
        """Test the createInverse"""
        a = 1
        data1 = ((cos(a), 0, sin(a)),
                 (0, 1, 0),
                 (-sin(a), 0, cos(a)))
        m1 = RotationMatrixIJK(data1)
        m2 = m1.createInverse()
        self.assertIsInstance(m2, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row][col], data1[col][row])

    def test_setToSharpened(self):
        """Test the setToSharpened method."""
        a = 1
        data1 = ((cos(a), 0, sin(a)),
                 (0, 1, 0),
                 (-sin(a), 0, cos(a)))
        m1 = RotationMatrixIJK(data1)
        m2 = RotationMatrixIJK()
        m3 = m2.setToSharpened(m1)
        self.assertIs(m3, m2)
        self.assertTrue(m3.isRotation())


if __name__ == '__main__':
    unittest.main()
