"""Tests for the internaloperations module."""


from emmpy.math.vectorspace.rotationmatrixijk import RotationMatrixIJK
from math import cos, pi, sin
import unittest

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    checkRotation
)
from emmpy.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


class TestBuilder(unittest.TestCase):
    """Tests for the internaloperations module."""

    def test_checkRotation(self):
        """Test the checkRotation function."""
        # NOTE: The values are provided in column-major order.
        normTolerance, detTolerance = 1e-6, 1e-5
        # Valid 3-D rotations.
        # Unit rotation matrix.
        data = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertTrue(isRotation)
        # Rotate by pi/3 radians around z-axis.
        a = pi/3
        data = [cos(a), -sin(a), 0, sin(a), cos(a), 0, 0, 0, 1]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertTrue(isRotation)
        # Invalid rotations.
        # Invalid 3-D rotation
        a = pi/3
        data = [cos(a) + 1, -sin(a), 0, sin(a), cos(a), 0, 0, 0, 1]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertFalse(isRotation)
        # Check that tolerances work.
        normTolerance, detTolerance = (0.1, 0.1)
        # 3-D
        a = pi/3
        data = [cos(a) + 0.1, -sin(a), 0, sin(a), cos(a), 0, 0, 0, 1]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertTrue(isRotation)
        # Invalid arguments
        sizes = (0, 1, 2, 4, 5, 7, 8, 9, 10, 12)
        for s in sizes:
            data = [0]*s
            with self.assertRaises(ValueError):
                checkRotation(*data)


if __name__ == '__main__':
    unittest.main()
