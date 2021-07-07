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
        # 0-argument form
        m1 = Matrix3D()
        self.assertIsInstance(m1, Matrix3D)
        for i in range(3):
            for j in  range(3):
                self.assertTrue(np.isnan(m1[i, j]))
        # 9-argument form - individual components
        data1 = [i*1.1 for i in range(9)]
        a1 = np.array(data1).reshape((3, 3))
        m1 = Matrix3D(*data1)
        self.assertIsInstance(m1, Matrix3D)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], a1[row, col])
        # Invalid forms.
        for n in (1, 2, 3, 4, 5, 6, 7, 8, 10):
            with self.assertRaises(ValueError):
                data1 = [None]*n
                m1 = Matrix3D(*data1)

if __name__ == '__main__':
    unittest.main()
