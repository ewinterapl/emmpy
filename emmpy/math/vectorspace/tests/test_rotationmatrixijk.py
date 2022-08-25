"""Tests for the rotationmatrixijk module."""


from math import cos, sin
import unittest

import numpy as np

from emmpy.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the rotationmatrixijk module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0 args - identity matrix
        m1 = RotationMatrixIJK()
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                if row == col:
                    self.assertAlmostEqual(m1[row, col], 1)
                else:
                    self.assertAlmostEqual(m1[row, col], 0)
        # 1 arg forms
        # list of tuples, for heterogeneity
        a = 1  # Rotate by a radians about z-axis
        data1 = [(cos(a), sin(a), 0), (-sin(a), cos(a), 0), (0, 0, 1)]
        m1 = RotationMatrixIJK(data1)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row][col])
        # np.ndarray
        a = 1  # Rotate by a radians about z-axis
        data1 = [(cos(a), sin(a), 0), (-sin(a), cos(a), 0), (0, 0, 1)]
        a1 = np.array(data1)
        m1 = RotationMatrixIJK(a1)
        self.assertIsInstance(m1, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m1[row, col], data1[row][col])
        # RotationMatrixIJK
        m2 = RotationMatrixIJK(m1)
        self.assertIsInstance(m2, RotationMatrixIJK)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(m2[row, col], data1[row][col])


if __name__ == "__main__":
    unittest.main()
