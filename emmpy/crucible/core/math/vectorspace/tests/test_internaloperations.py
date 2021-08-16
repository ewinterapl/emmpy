"""Tests for the internaloperations module."""


from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import RotationMatrixIJK
from math import cos, pi, sin
import unittest

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent,
    checkRotation,
)
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


class TestBuilder(unittest.TestCase):
    """Tests for the internaloperations module."""

    def test_absMaxComponent(self):
        """Test the absMaxComponent function."""
        self.assertEqual(absMaxComponent(0), 0)
        self.assertEqual(absMaxComponent(0, 0), 0)
        self.assertEqual(absMaxComponent(1, -2), 2)
        self.assertEqual(absMaxComponent(2, -2), 2)
        self.assertEqual(absMaxComponent(0, 0, 0), 0)
        self.assertEqual(absMaxComponent(1, 2, -3), 3)

    def test_checkRotation(self):
        """Test the checkRotation function."""
        # NOTE: The values are provided in column-major order.
        normTolerance, detTolerance = 1e-6, 1e-5
        # Valid 2-D rotations.
        # Unit rotation matrix.
        m = RotationMatrixIJK()
        isRotation = True
        try:
            checkRotation(m, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertTrue(isRotation)
        # Unit rotation matrix (flat).
        data = [1, 0, 0, 1]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertTrue(isRotation)
        # Rotate by pi/3 radians around z-axis.
        a = pi/3
        data = [cos(a), -sin(a), cos(a), sin(a)]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertTrue(isRotation)
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
        # Invalid 2-D rotation
        a = pi/3
        data = [cos(a) + 1, -sin(a), cos(a), sin(a)]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertFalse(isRotation)
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
        # 2-D
        a = pi/3
        data = [cos(a) + 0.1, -sin(a), cos(a), sin(a)]
        isRotation = True
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except MalformedRotationException:
            isRotation = False
        self.assertTrue(isRotation)
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
