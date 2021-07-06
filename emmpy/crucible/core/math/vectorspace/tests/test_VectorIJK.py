from emmpy.crucible.core.exceptions.bugexception import BugException
from math import pi, sqrt
import unittest
import warnings

import numpy as np
from numpy.core.numerictypes import ScalarType

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK, I, J, K


class TestBuilder(unittest.TestCase):

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v1 = VectorIJK()
        self.assertIsInstance(v1, VectorIJK)
        for i in range(3):
            self.assertTrue(np.isnan(v1[i]))
        # 1-argument forms
        (i, j, k) = (1.1, 2.2, 3.3)
        # list
        v1 = VectorIJK([i, j, k])
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        self.assertAlmostEqual(v1[2], k)
        # tuple
        v1 = VectorIJK((i, j, k))
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        self.assertAlmostEqual(v1[2], k)
        # np.ndarray
        a1 = np.array((i, j, k))
        v1 = VectorIJK(a1)
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        self.assertAlmostEqual(v1[2], k)
        # vector
        v2 = VectorIJK(v1)
        self.assertIsInstance(v2, VectorIJK)
        self.assertAlmostEqual(v2[0], i)
        self.assertAlmostEqual(v2[1], j)
        self.assertAlmostEqual(v2[2], k)
        # 2-argument forms
        # offset and list
        v1 = VectorIJK(1, [0, i, j, k])
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        self.assertAlmostEqual(v1[2], k)
        # offset and tuple
        v1 = VectorIJK(1, (0, i, j, k))
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        self.assertAlmostEqual(v1[2], k)
        # offset and np.ndarray
        a1 = np.array((0, i, j, k))
        v1 = VectorIJK(1, a1)
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        self.assertAlmostEqual(v1[2], k)
        # scale and vector
        scale = -2.2
        v2 = VectorIJK(scale, v1)
        self.assertIsInstance(v2, VectorIJK)
        self.assertAlmostEqual(v2[0], scale*i)
        self.assertAlmostEqual(v2[1], scale*j)
        self.assertAlmostEqual(v2[2], scale*k)
        # 3-argument form
        v1 = VectorIJK(i, j, k)
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        self.assertAlmostEqual(v1[2], k)
        # >= 4 args is invalid
        with self.assertRaises(ValueError):
            v1 = VectorIJK(0, i, j, k)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = VectorIJK(i, j, k)
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        with self.assertRaises(KeyError):
            v.bad

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

    def test_createScaled(self):
        """Test the createScaled() method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        scale = -4.4
        v1 = VectorIJK(i, j, k)
        v2 = v1.createScaled(scale)
        self.assertIsInstance(v2, VectorIJK)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        self.assertAlmostEqual(v2.k, scale*k)

    def test_scale(self):
        """Test the scale method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        scale = -4.4
        v1 = VectorIJK(i, j, k)
        v2 = v1.scale(scale)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        self.assertAlmostEqual(v2.k, scale*k)

    def test_unitize(self):
        """Test the unitize method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        length = sqrt(i**2 + j**2 + k**2)
        v1 = VectorIJK(i, j, k)
        v2 = v1.unitize()
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i/length)
        self.assertAlmostEqual(v2.j, j/length)
        self.assertAlmostEqual(v2.k, k/length)
        v1 = VectorIJK(0, 0, 0)
        # Temporarily disable the divide-by-zero warning from Numpy.
        warnings.filterwarnings("ignore", message="invalid value encountered in true_divide")
        v2 = v1.unitize()
        for i in range(3):
            self.assertTrue(np.isnan(v2[i]))
        # Restore normal warning handlers.
        warnings.resetwarnings()

    def test_negate(self):
        """Test the negate method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v1 = VectorIJK(i, j, k)
        v2 = v1.negate()
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, -i)
        self.assertAlmostEqual(v2.j, -j)
        self.assertAlmostEqual(v2.k, -k)

    def test_setTo(self):
        """Test the setTo  method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        # 1-argument forms
        v1 = VectorIJK(i, j, k)
        v2 = VectorIJK()
        v3 = v2.setTo(v1)
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # 2-argument forms
        scale = -4.4
        # Scale a VectorIJK.
        v3 = v2.setTo(scale, v1)
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v3.i, scale*i)
        self.assertAlmostEqual(v3.j, scale*j)
        self.assertAlmostEqual(v3.k, scale*k)
        # Scale a np.ndarray.
        v3 = v2.setTo(scale, np.array((i, j, k)))
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v3.i, scale*i)
        self.assertAlmostEqual(v3.j, scale*j)
        self.assertAlmostEqual(v3.k, scale*k)
        # Scale a list.
        v2 = VectorIJK()
        v3 = v2.setTo(scale, [i, j, k])
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v3.i, scale*i)
        self.assertAlmostEqual(v3.j, scale*j)
        self.assertAlmostEqual(v3.k, scale*k)
        # Scale a tuple.
        v2 = VectorIJK()
        v3 = v2.setTo(scale, (i, j, k))
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v3.i, scale*i)
        self.assertAlmostEqual(v3.j, scale*j)
        self.assertAlmostEqual(v3.k, scale*k)
        v3 = v2.setTo(1, (0, i, j, k))
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # 3-argument forms
        v2 = VectorIJK()
        v3 = v2.setTo((i, j, k))
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # Invalid forms
        with self.assertRaises(Exception):
            v2.setTo()
        with self.assertRaises(ValueError):
            v2.setTo(None, None, None, None)

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

    def test_add(self):
        """Test the add method."""
        v = VectorIJK()
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 1, 0)
        # 2-argument form
        v3 = VectorIJK.add(v1, v2)
        self.assertAlmostEqual(v3.i, 2)
        self.assertAlmostEqual(v3.j, 2)
        self.assertAlmostEqual(v3.k, 1)
        # 3-argument form
        v3 = VectorIJK.add(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 2)
        self.assertAlmostEqual(v3.j, 2)
        self.assertAlmostEqual(v3.k, 1)
        # Invalid forms.
        with self.assertRaises(ValueError):
            VectorIJK.add()
        with self.assertRaises(ValueError):
            VectorIJK.add(None)
        with self.assertRaises(ValueError):
            VectorIJK.add(None, None, None, None)

    def test_unitVectors(self):
        """Test the unit vector definitions."""
        IJK = (I, J, K)
        for i in range(3):
            for j in range(3):
                if i == j:
                    self.assertAlmostEqual(IJK[i][j], 1)
                else:
                    self.assertAlmostEqual(IJK[i][j], 0)


if __name__ == '__main__':
    unittest.main()
