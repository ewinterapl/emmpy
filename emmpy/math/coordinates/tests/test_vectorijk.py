"""Tests for the vectorijk module."""


from math import pi, sqrt
import unittest
import warnings

import numpy as np

from emmpy.math.coordinates.vectorijk import (
    VectorIJK, project, rotate
)


class TestBuilder(unittest.TestCase):
    """Tests for the vectorijk module."""

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = VectorIJK(i, j, k)
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        with self.assertRaises(KeyError):
            i = v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = VectorIJK()
        (i, j, k) = (1.1, 2.2, 3.3)
        v.i = i
        self.assertAlmostEqual(v.i, i)
        v.j = j
        self.assertAlmostEqual(v.j, j)
        v.j = k
        self.assertAlmostEqual(v.j, k)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_rotate(self):
        """Test the rotate function."""
        v1 = VectorIJK(1, 0, 0)
        z_axis = VectorIJK(0, 0, 1)
        angle = pi/2
        # 3-argument form
        v2 = rotate(v1, z_axis, angle)
        self.assertAlmostEqual(v2.i, 0)
        self.assertAlmostEqual(v2.j, 1)
        self.assertAlmostEqual(v2.k, 0)

    def test_project(self):
        """Test the project function."""
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        # 2-argument form.
        v3 = project(v1, v2)
        self.assertAlmostEqual(v3.i, 1)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 0)
        # Projection of 0 is 0.
        v1 = VectorIJK(0, 0, 0)
        v3 = project(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 0)


if __name__ == '__main__':
    unittest.main()
