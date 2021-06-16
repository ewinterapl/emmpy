"""Tests for UnwritableVectorIJK."""


from math import pi, sqrt
import unittest

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class TestBuilder(unittest.TestCase):
    """Build the tests."""

    def test___new__(self):
        """Test the __new__ method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        # 0 args is invalid
        with self.assertRaises(ValueError):
            UnwritableVectorIJK()
        # 1-argument forms
        # list
        v = UnwritableVectorIJK([i, j, k])
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        # tuple
        v = UnwritableVectorIJK((i, j, k))
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        # vector
        v2 = UnwritableVectorIJK(v)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        self.assertAlmostEqual(v2.k, k)
        # invalid single argument
        with self.assertRaises(ValueError):
            UnwritableVectorIJK(None)
        with self.assertRaises(ValueError):
            UnwritableVectorIJK({'i': i})
        # 2-argument forms
        # offset and list
        v = UnwritableVectorIJK(1, [0, i, j, k])
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        # offset and tuple
        v = UnwritableVectorIJK(1, (0, i, j, k))
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        # scale and vector
        scale = -2.2
        v2 = UnwritableVectorIJK(scale, v)
        self.assertAlmostEqual(v2.i, scale*v.i)
        self.assertAlmostEqual(v2.j, scale*v.j)
        self.assertAlmostEqual(v2.k, scale*v.k)
        # 2 bad args
        with self.assertRaises(ValueError):
            UnwritableVectorIJK(None, None)
        with self.assertRaises(ValueError):
            UnwritableVectorIJK(i, j)
        # 3-argument form
        v = UnwritableVectorIJK(i, j, k)
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        # 3 bad args
        with self.assertRaises(ValueError):
            UnwritableVectorIJK(None, [None], {'i': i})
        # >= 4 args is invalid
        with self.assertRaises(ValueError):
            UnwritableVectorIJK(0, i, j, k)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = UnwritableVectorIJK(i, j, k)
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        with self.assertRaises(KeyError):
            i = v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = UnwritableVectorIJK(0, 0, 0)
        (i, j, k) = (1.1, 2.2, 3.3)
        v.i = i
        self.assertAlmostEqual(v.i, i)
        v.j = j
        self.assertAlmostEqual(v.j, j)
        v.k = k
        self.assertAlmostEqual(v.k, k)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_createUnitized(self):
        """Test the createUnitized method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        length = sqrt(i**2 + j**2 + k**2)
        v = UnwritableVectorIJK(i, j, k)
        v2 = v.createUnitized()
        self.assertAlmostEqual(v2.i, i/length)
        self.assertAlmostEqual(v2.j, j/length)
        self.assertAlmostEqual(v2.k, k/length)
        v = UnwritableVectorIJK(0, 0, 0)
        with self.assertRaises(ZeroDivisionError):
            v.createUnitized()

    def test_createNegated(self):
        """Test the createNegated method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = UnwritableVectorIJK(i, j, k)
        v2 = v.createNegated()
        self.assertAlmostEqual(v2.i, -i)
        self.assertAlmostEqual(v2.j, -j)
        self.assertAlmostEqual(v2.k, -k)

    def test_createScaled(self):
        """Test the createScaled method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        scale = 2.2
        v = UnwritableVectorIJK(i, j, k)
        v2 = v.createScaled(scale)
        self.assertAlmostEqual(v2.i, scale*v.i)
        self.assertAlmostEqual(v2.j, scale*v.j)
        self.assertAlmostEqual(v2.k, scale*v.k)
        scale = -2.2
        v2 = v.createScaled(scale)
        self.assertAlmostEqual(v2.i, scale*v.i)
        self.assertAlmostEqual(v2.j, scale*v.j)
        self.assertAlmostEqual(v2.k, scale*v.k)
        scale = 0
        v2 = v.createScaled(scale)
        self.assertAlmostEqual(v2.i, scale*v.i)
        self.assertAlmostEqual(v2.j, scale*v.j)
        self.assertAlmostEqual(v2.k, scale*v.k)

    def test_getI(self):
        """Test the getI method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = UnwritableVectorIJK(i, j, k)
        self.assertAlmostEqual(v.getI(), i)

    def test_getJ(self):
        """Test the getJ method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = UnwritableVectorIJK(i, j, k)
        self.assertAlmostEqual(v.getJ(), j)

    def test_getK(self):
        """Test the getK method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = UnwritableVectorIJK(i, j, k)
        self.assertAlmostEqual(v.getK(), k)

    def test_get(self):
        """Test the get method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = UnwritableVectorIJK(i, j, k)
        self.assertAlmostEqual(v.get(0), i)
        self.assertAlmostEqual(v.get(1), j)
        self.assertAlmostEqual(v.get(2), k)
        with self.assertRaises(IndexError):
            v.get(3)
        with self.assertRaises(IndexError):
            v.get(-4)

    def test_getLength(self):
        """Test getLength()."""
        (i, j, k) = (1.1, 2.2, 3.3)
        length = sqrt(i**2 + j**2 + k**2)
        v = UnwritableVectorIJK(i, j, k)
        self.assertAlmostEqual(v.getLength(), length)

    def test_getDot(self):
        """Test the getDot method."""
        (i1, j1, k1) = (1.1, 2.2, 3.3)
        (i2, j2, k2) = (4.4, 5.5, 6.6)
        v1 = UnwritableVectorIJK(i1, j1, k1)
        v2 = UnwritableVectorIJK(i2, j2, k2)
        dot = i1*i2 + j1*j2 + k1*k2
        self.assertAlmostEqual(v1.getDot(v2), dot)

    def test_getSeparation(self):
        """Test the getSeparation method."""
        v0 = UnwritableVectorIJK(0, 0, 0)
        v1 = UnwritableVectorIJK(1, 1, 1)
        v2a = UnwritableVectorIJK(2, 1, 1)
        v2b = UnwritableVectorIJK(-2, 1, 1)
        v3 = UnwritableVectorIJK(-1, -1, -1)
        v4 = UnwritableVectorIJK(1, 0, 0)
        v5 = UnwritableVectorIJK(0, 1, 0)
        with self.assertRaises(BugException):
            v0.getSeparation(v1)
        with self.assertRaises(BugException):
            v1.getSeparation(v0)
        self.assertAlmostEqual(v1.getSeparation(v2a), 0.33983690945412204)
        self.assertAlmostEqual(v2a.getSeparation(v1), 0.33983690945412204)
        self.assertAlmostEqual(v1.getSeparation(v2b), 1.5707963267948966)
        self.assertAlmostEqual(v1.getSeparation(v1), 0)
        self.assertAlmostEqual(v4.getSeparation(v5), pi/2)
        self.assertAlmostEqual(v1.getSeparation(v3), pi)

    def test_getSeparationOutOfPlane(self):
        """Test the getSeparationOutOfPlane method."""
        v1 = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(2, 1, 1)
        v3 = UnwritableVectorIJK(-2, -1, -1)
        v4 = UnwritableVectorIJK(-1, -1, -1)
        v5 = UnwritableVectorIJK(1, 0, 0)
        v6 = UnwritableVectorIJK(0, 1, 0)
        v7 = UnwritableVectorIJK(0, 0, 1)
        self.assertAlmostEqual(v1.getSeparationOutOfPlane(v2),
                               1.2309594173407745)
        self.assertAlmostEqual(v1.getSeparationOutOfPlane(v3),
                               -1.2309594173407745)
        self.assertAlmostEqual(v1.getSeparationOutOfPlane(v1), pi/2)
        self.assertAlmostEqual(v1.getSeparationOutOfPlane(v4), -pi/2)
        self.assertAlmostEqual(v5.getSeparationOutOfPlane(v6), 0)
        self.assertAlmostEqual(v5.getSeparationOutOfPlane(v7), 0)

    def test_copyOf(self):
        """Test the copyOf method."""
        (x, y, z) = (1.1, 2.2, 3.3)
        v1 = UnwritableVectorIJK(x, y, z)
        v2 = UnwritableVectorIJK.copyOf(v1)
        self.assertEqual(v1.i, v2.i)
        self.assertEqual(v1.j, v2.j)
        self.assertEqual(v1.k, v2.k)


if __name__ == '__main__':
    unittest.main()
