"""Tests for the matrix3d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.matrices.matrix3d import Matrix3D


class TestBuilder(unittest.TestCase):
    """Tests for the matrix3d module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-arg form
        m = Matrix3D()
        self.assertIsInstance(m, Matrix3D)
        for x in m.flatten():
            self.assertTrue(np.isnan(x))
        # 1-arg forms.
        # list of lists
        data = [[0.0, 1.1, 2.2], [3.3, 4.4, 5.5], [6.6, 7.7, 8.8]]
        m = Matrix3D(data)
        self.assertIsInstance(m, Matrix3D)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of tuples
        data = ((0.0, 1.1, 2.2), (3.3, 4.4, 5.5), (6.6, 7.7, 8.8))
        m = Matrix3D(data)
        self.assertIsInstance(m, Matrix3D)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # list of tuples
        data = [(0.0, 1.1, 2.2), (3.3, 4.4, 5.5), (6.6, 7.7, 8.8)]
        m = Matrix3D(data)
        self.assertIsInstance(m, Matrix3D)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # tuple of lists
        data = ([0.0, 1.1, 2.2], [3.3, 4.4, 5.5], [6.6, 7.7, 8.8])
        m = Matrix3D(data)
        self.assertIsInstance(m, Matrix3D)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row][col])
        # ndarray
        data = [i*1.1 for i in range(9)]
        a = np.array(data).reshape((3, 3))
        m = Matrix3D(*data)
        self.assertIsInstance(m, Matrix3D)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], a[row, col])
        # 9-argument form - individual components
        data = [i*1.1 for i in range(9)]
        m = Matrix3D(*data)
        self.assertIsInstance(m, Matrix3D)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m[row, col], data[row*3 + col])
        # Invalid forms.
        for n in (2, 3, 4, 5, 6, 7, 8, 10):
            with self.assertRaises(ValueError):
                args = (None,)*n
                m = Matrix3D(*args)

if __name__ == '__main__':
    unittest.main()
