"""Tests for the vectorijk module."""


from math import pi, sqrt
import unittest
import warnings

import numpy as np

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


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
        """Test the rotate method."""
        v1 = VectorIJK(1, 0, 0)
        z_axis = VectorIJK(0, 0, 1)
        angle = pi/2
        # 3-argument form
        v2 = VectorIJK.rotate(v1, z_axis, angle)
        self.assertAlmostEqual(v2.i, 0)
        self.assertAlmostEqual(v2.j, 1)
        self.assertAlmostEqual(v2.k, 0)
        # 4-argument form
        v = VectorIJK()
        angle = pi/3
        v2 = VectorIJK.rotate(v1, z_axis, angle, v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 0.5)
        self.assertAlmostEqual(v2.j, sqrt(3)/2)
        self.assertAlmostEqual(v2.k, 0)
        # Invalid forms.
        with self.assertRaises(ValueError):
            VectorIJK.rotate()
        with self.assertRaises(ValueError):
            VectorIJK.rotate(None)
        with self.assertRaises(ValueError):
            VectorIJK.rotate(None, None)
        with self.assertRaises(ValueError):
            VectorIJK.rotate(None, None, None, None, None)

    def test_project(self):
        """Test the project method."""
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        # 2-argument form.
        v3 = VectorIJK.project(v1, v2)
        self.assertAlmostEqual(v3.i, 1)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 0)
        # 3-argument form.
        v4 = VectorIJK()
        v5 = VectorIJK.project(v1, v2, v4)
        self.assertIs(v5, v4)
        self.assertAlmostEqual(v5.i, 1)
        self.assertAlmostEqual(v5.j, 0)
        self.assertAlmostEqual(v5.k, 0)
        # Projection of 0 is 0.
        v1 = VectorIJK(0, 0, 0)
        v3 = VectorIJK.project(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 0)
        # Invalid forms.
        with self.assertRaises(ValueError):
            v3 = VectorIJK.project()
        with self.assertRaises(ValueError):
            v3 = VectorIJK.project(None)
        with self.assertRaises(ValueError):
            v3 = VectorIJK.project(None, None, None, None)
        # Can't project onto 0 vector.
        with self.assertRaises(BugException):
            v3 = VectorIJK.project(v2, v1)


if __name__ == '__main__':
    unittest.main()
