"""Tests for the privilegedrotationmatrix module."""


import unittest

import numpy as np

from emmpy.math.rotations.privilegedrotationmatrixijk import (
    PrivilegedRotationMatrixIJK
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the privilegedrotationmatrix module."""

    def test_setToWithoutCheck(self):
        """Test the setWithoutCheck method."""
        data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        # 1-arg form.
        prm = PrivilegedRotationMatrixIJK()
        prm2 = prm.setToWithoutCheck(data)
        self.assertIs(prm2, prm)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(prm2[row][col], data[row][col])
        # 3-arg form.
        v0 = VectorIJK(data[:, 0])
        v1 = VectorIJK(data[:, 1])
        v2 = VectorIJK(data[:, 2])
        prm = PrivilegedRotationMatrixIJK()
        prm2 = prm.setToWithoutCheck(v0, v1, v2)
        self.assertIs(prm2, prm)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(prm2[row][col], data[row][col])
        # 6-arg form.
        s = [1.1, 2.2, 3.3]
        v = [v0, v1, v2]
        prm = PrivilegedRotationMatrixIJK()
        prm2 = prm.setToWithoutCheck(s[0], v[0], s[1], v[1], s[2], v[2])
        self.assertIs(prm2, prm)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(prm2[row][col], v[col][row]*s[col])
        # 9-arg form.
        args = data.T.flatten()  # Column-major order
        prm = PrivilegedRotationMatrixIJK()
        prm2 = prm.setToWithoutCheck(*args)
        self.assertIs(prm2, prm)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(prm2[row][col], data[row][col])
        # Invalid forms.
        sizes = [0, 2, 4, 5, 7, 8, 10]
        for s in sizes:
            args = [None]*s
            with self.assertRaises(TypeError):
                PrivilegedRotationMatrixIJK.setToWithoutCheck(None, *args)


if __name__ == '__main__':
    unittest.main()
