"""Tests for UnwritableVectorIJK."""


from math import sqrt
import unittest

from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class TestBuilder(unittest.TestCase):
    """Build the tests."""

    def test___init__(self):
        """Test __init__()."""
        # 0 args is invalid
        with self.assertRaises(Exception):
            UnwritableVectorIJK()
        # Basic 3-argument form
        v = UnwritableVectorIJK(1.1, 2.2, 3.3)
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        # 1-argument forms
        # list
        v = UnwritableVectorIJK([1.1, 2.2, 3.3])
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        # copy constructor
        v2 = UnwritableVectorIJK(v)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 3.3)
        # invalid single argument
        with self.assertRaises(Exception):
            UnwritableVectorIJK(None)
        # 2-argument forms
        # offset and list
        v = UnwritableVectorIJK(1, [0, 1.11, 2.22, 3.33])
        self.assertAlmostEqual(v.i, 1.11)
        self.assertAlmostEqual(v.j, 2.22)
        self.assertAlmostEqual(v.k, 3.33)
        # scale and vector
        v2 = UnwritableVectorIJK(-2, v)
        self.assertAlmostEqual(v2.i, -2.22)
        self.assertAlmostEqual(v2.j, -4.44)
        self.assertAlmostEqual(v2.k, -6.66)
        # 2 bad args
        with self.assertRaises(Exception):
            UnwritableVectorIJK(None, None)
        # 4 args is invalid
        with self.assertRaises(Exception):
            UnwritableVectorIJK(1, 2, 3, 4)

    def test_createUnitized(self):
        """Test createUnitized()."""
        v = UnwritableVectorIJK(1, 2, 3)
        v2 = v.createUnitized()
        self.assertAlmostEqual(v2.i, 1/sqrt(14))
        self.assertAlmostEqual(v2.j, 2/sqrt(14))
        self.assertAlmostEqual(v2.k, 3/sqrt(14))
        v = UnwritableVectorIJK(0, 0, 0)
        with self.assertRaises(Exception):
            v.createUnitized()

    def test_createNegated(self):
        """Test createNegated()."""
        v = UnwritableVectorIJK(1, 2, 3)
        v2 = v.createNegated()
        self.assertAlmostEqual(v2.i, -1)
        self.assertAlmostEqual(v2.j, -2)
        self.assertAlmostEqual(v2.k, -3)

    def test_createScaled(self):
        """Test createScaled()."""
        v = UnwritableVectorIJK(1, 2, 3)
        v2 = v.createScaled(2)
        self.assertAlmostEqual(v2.i, 2)
        self.assertAlmostEqual(v2.j, 4)
        self.assertAlmostEqual(v2.k, 6)

    def test_getI(self):
        """Test getI()."""
        v = UnwritableVectorIJK(1, 2, 3)
        self.assertAlmostEqual(v.getI(), 1)

    def test_getJ(self):
        """Test getJ()."""
        v = UnwritableVectorIJK(1, 2, 3)
        self.assertAlmostEqual(v.getJ(), 2)

    def test_getK(self):
        """Test getK()."""
        v = UnwritableVectorIJK(1, 2, 3)
        self.assertAlmostEqual(v.getK(), 3)

    def test_get(self):
        """Test get()."""
        v = UnwritableVectorIJK(1, 2, 3)
        self.assertAlmostEqual(v.get(0), 1)
        self.assertAlmostEqual(v.get(1), 2)
        self.assertAlmostEqual(v.get(2), 3)
        with self.assertRaises(Exception):
            v.get(3)

    def test_getLength(self):
        """Test getLength()."""
        v = UnwritableVectorIJK(1, 2, 3)
        self.assertAlmostEqual(v.getLength(), sqrt(14))

    def test_getDot(self):
        """Test getDot()."""
        v = UnwritableVectorIJK(1, 2, 3)
        v2 = UnwritableVectorIJK(2, 3, 4)
        self.assertAlmostEqual(v.getDot(v2), 20)

    def test_getSeparation(self):
        """Test getSeparation()."""
        v0 = UnwritableVectorIJK(0, 0, 0)
        v1 = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(2, 1, 1)
        with self.assertRaises(Exception):
            v0.getSeparation(v1)
        with self.assertRaises(Exception):
            v2.getSeparation(v0)
        self.assertAlmostEqual(v1.getSeparation(v2), 0.33983690945412204)

    def test_getSeparationOutOfPlane(self):
        """Test getSeparationOutOfPlane()."""
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(2, 1, 1)
        self.assertAlmostEqual(v.getSeparationOutOfPlane(v2),
                               1.2309594173407745)

    def test_copyOf(self):
        """Test copyOf()."""
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK.copyOf(v)
        self.assertEqual(v, v2)

    def test___repr__(self):
        """Test __repr__()."""
        v = UnwritableVectorIJK(1.1, 2.2, 3.3)
        self.assertEqual(v.__repr__(), "[1.1,2.2,3.3]")


if __name__ == '__main__':
    unittest.main()
