"""Tests for the vectorij module."""


from math import sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


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
        a = np.array([0, i, j])
        v = VectorIJ(1, a)
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # scale and vector
        scale = -2.2
        v = VectorIJ([i, j])
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

    def test_scale(self):
        """Test the scale() method."""
        vij = VectorIJ(1, 2)
        vij.scale(-1.1)
        self.assertAlmostEqual(vij.i, -1.1)
        self.assertAlmostEqual(vij.j, -2.2)

    def test_unitize(self):
        """Test the unitize() method."""
        vij = VectorIJ(1, 2)
        vij2 = vij.unitize()
        self.assertIs(vij2, vij)
        self.assertAlmostEqual(vij.i, 1/sqrt(5))
        self.assertAlmostEqual(vij.j, 2/sqrt(5))

    def test_setTo(self):
        """Test the setTo method."""
        # Test data
        (i, j, k) = (1.1, 2.2, 3.3)
        # 1-argument forms
        # list
        data = [i, j]
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # tuple
        data = (i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # np.ndarray
        data = np.array([i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # VectorIJ
        data = VectorIJ([i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # 2-argument forms
        # Offset and list
        offset = 1
        data = [k, i, j]
        v1 = VectorIJ()
        v2 = v1.setTo(offset, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Offset and tuple
        offset = 1
        data = (k, i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(offset, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Offset and np.ndarray
        offset = 1
        data = np.array([k, i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(offset, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Scale factor and list
        scale = 1.1
        data = [i, j]
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Scale factor and tuple
        data = (i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Scale factor and np.ndarray
        data = np.array([i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Scale factor and VectorIJ
        data = VectorIJ(i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Explicit values
        v1 = VectorIJ()
        v2 = v1.setTo(i, j)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Invalid forms
        sizes = (0, 3)
        for s in sizes:
            data = [None]*s
            v = VectorIJ()
            with self.assertRaises(TypeError):
                v2 = v.setTo(*data)


if __name__ == '__main__':
    unittest.main()
