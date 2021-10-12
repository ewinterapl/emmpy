"""Tests for the vectorij module."""


# from math import sqrt
import unittest

import numpy as np

from emmpy.math.coordinates.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):
    """Tests for the vectorij module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0-argument form - all NaN.
        v = VectorIJ()
        self.assertIsInstance(v, VectorIJ)
        for x in v:
            self.assertTrue(np.isnan(x))
        # Test data
        (i, j) = (1.1, 2.2)
        # 1-argument forms
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
        v = VectorIJ(np.array([i, j]))
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # vector
        v2 = VectorIJ(v)
        self.assertIsInstance(v2, VectorIJ)
        self.assertAlmostEqual(v2[0], i)
        self.assertAlmostEqual(v2[1], j)
        # 2-argument forms
        # set components
        v = VectorIJ(i, j)
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # >= 3 args is invalid
        with self.assertRaises(ValueError):
            v = VectorIJ(i, j, None)

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
