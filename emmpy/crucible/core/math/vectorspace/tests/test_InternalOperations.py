"""Tests for the internaloperations module."""


from math import cos, pi, sin, sqrt
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
        normTolerance, detTolerance = 1e-6, 1e-6
        # Valid 2-D rotations.
        # Unit rotation matrix.
        data = [1, 0, 0, 1]
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except:
            self.assertTrue(False)
        # Rotate by pi/3 radians ccw around z-axis.
        a = pi/3
        data = [cos(a), -sin(a), cos(a), sin(a)]
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except:
            self.assertTrue(False)
        # Valid 3-D rotations.
        # Unit rotation matrix.
        data = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except:
            self.assertTrue(False)
        # Rotate by pi/3 radians ccw around z-axis.
        a = pi/3
        data = [cos(a), -sin(a), 0, sin(a), cos(a), 0, 0, 0, 1]
        try:
            checkRotation(*data, normTolerance, detTolerance)
        except:
            self.assertTrue(False)
        # Invalid rotations.
        with self.assertRaises(MalformedRotationException):
            checkRotation(1, 1, 0, 1, normTolerance, detTolerance)
        with self.assertRaises(MalformedRotationException):
            checkRotation(1, 1, 0, 0, 1, 0, 0, 0, 1,
                          normTolerance, detTolerance)
        sizes = (0, 1, 2, 3, 5, 7, 8, 10, 12)
        # No size 4, 9 since it triggers first case in method.
        for s in sizes:
            data = [0]*s
            with self.assertRaises(ValueError):
                checkRotation(*data, normTolerance, detTolerance)

if __name__ == '__main__':
    unittest.main()
