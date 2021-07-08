"""Tests for the vectorij module."""


from math import sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):
    """Tests for the vectorij module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0-argument form.
        v = VectorIJ()
        self.assertIsInstance(v, VectorIJ)
        for x in v:
            self.assertTrue(np.isnan(x))
        # # 1-argument÷ forms
        (i, j) = (1.1, 2.2)
        # list
        v = VectorIJ([i, j])
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # tuple
        v = VectorIJ((i, j))
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # np.ndarray
        a = np.array((i, j))
        v = VectorIJ(a)
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # vector
        v2 = VectorIJ(v)
        self.assertIsInstance(v2, VectorIJ)
        self.assertAlmostEqual(v2[0], i)
        self.assertAlmostEqual(v2[1], j)
        # 2-argument forms
        # offset and list
        v = VectorIJ(1, [0, i, j])
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # offset and tuple
        v = VectorIJ(1, (0, i, j))
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # offset and np.ndarray
        a = np.array((0, i, j))
        v = VectorIJ(1, a)
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # scale and vector
        scale = -2.2
        v2 = VectorIJ(scale, v)
        self.assertIsInstance(v2, VectorIJ)
        self.assertAlmostEqual(v2[0], scale*i)
        self.assertAlmostEqual(v2[1], scale*j)
        # set components
        v = VectorIJ(i, j)
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # >= 3 args is invalid
        with self.assertRaises(ValueError):
            v = VectorIJ(i, j, 0)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (i, j) = (1.1, 2.2)
        v = VectorIJ(i, j)
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        with self.assertRaises(KeyError):
            bad = v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = VectorIJ()
        (i, j) = (1.1, 2.2)
        v.i = i
        self.assertAlmostEqual(v.i, i)
        v.j = j
        self.assertAlmostEqual(v.j, j)
        with self.assertRaises(KeyError):
            v.bad = 0


if __name__ == '__main__':
    unittest.main()
