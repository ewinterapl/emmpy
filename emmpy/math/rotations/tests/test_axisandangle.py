"""Tests for the axisandangle module."""


import unittest

from emmpy.math.rotations.axisandangle import AxisAndAngle
from emmpy.math.rotations.privilegedrotationmatrixijk import (
    PrivilegedRotationMatrixIJK
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the axisandangle module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0-arg form
        aaa = AxisAndAngle()
        self.assertIsInstance(aaa, AxisAndAngle)
        self.assertAlmostEqual(aaa.axis.i, 0)
        self.assertAlmostEqual(aaa.axis.j, 0)
        self.assertAlmostEqual(aaa.axis.k, 1)
        self.assertAlmostEqual(aaa.angle, 0)
        # 2-arg form
        # Axis and angle
        data = [1, 0, 0]
        axis = VectorIJK(*data)
        angle = 1.1
        aaa = AxisAndAngle(axis, angle)
        self.assertAlmostEqual(aaa.axis.i, axis.i)
        self.assertAlmostEqual(aaa.axis.j, axis.j)
        self.assertAlmostEqual(aaa.axis.k, axis.k)
        self.assertAlmostEqual(aaa.angle, angle)
        # Invalid forms
        sizes = (1, 3)
        for s in sizes:
            args = [None]*s
            with self.assertRaises(TypeError):
                aaa = AxisAndAngle(*args)

    def test_getRotation(self):
        """Test the getRotation method."""
        aaa = AxisAndAngle()
        buffer = PrivilegedRotationMatrixIJK()
        rotationMatrix_ref = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        rotationMatrix = aaa.getRotation(buffer)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(rotationMatrix[row][col],
                                       rotationMatrix_ref[row][col])


if __name__ == '__main__':
    unittest.main()
