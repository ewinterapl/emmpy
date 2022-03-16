"""Tests for the rotationmatrix2d module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin
import unittest

import numpy as np

from emmpy.math.rotations.rotationmatrix2d import RotationMatrix2D


class TestBuilder(unittest.TestCase):
    """Tests for the rotationmatrix2d module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0-arg form should give a 2-D identity matrix.
        m = RotationMatrix2D()
        self.assertIsInstance(m, RotationMatrix2D)
        eye2d = np.eye(2)
        self.assertTrue(np.isclose(m, eye2d).all())
        # 1 arg form - valid matrix
        a = 1.0
        data = np.array([[cos(a), -sin(a)], [sin(a), cos(a)]])
        m = RotationMatrix2D(data)
        self.assertIsInstance(m, RotationMatrix2D)
        self.assertTrue(np.isclose(m, data).all())
        # 1 arg form - invalid matrix
        a = 1.0
        data = np.array([[cos(a), sin(a)], [sin(a), cos(a)]])
        with self.assertRaises(TypeError):
            m = RotationMatrix2D(data)

    def test_isValidRotation(self):
        """Test the isValidRotation method."""
        # Valid rotation matrix
        a = 1.0
        data = np.array([[cos(a), -sin(a)], [sin(a), cos(a)]])
        self.assertTrue(RotationMatrix2D.isValidRotation(data))
        # Invalid rotation matrix
        a = 1.0
        data = np.array([[-cos(a), -sin(a)], [sin(a), cos(a)]])
        self.assertFalse(RotationMatrix2D.isValidRotation(data))


if __name__ == "__main__":
    unittest.main()
