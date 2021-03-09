from math import sqrt
import unittest

from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class TestUnwritableVectorIJK(unittest.TestCase):

    def test___init__(self):
        pass
        # Test the various forms of the constructor.
        # 3 components
        v = UnwritableVectorIJK(1.1, 2.2, 3.3)
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        # List of 3 components
        v = UnwritableVectorIJK([1.1, 2.2, 3.3])
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        # Offset into list of > 3 components
        v = UnwritableVectorIJK(1, [0, 1.1, 2.2, 3.3])
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        v2 = UnwritableVectorIJK(v)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 3.3)
        v2 = UnwritableVectorIJK(-2, v)
        self.assertAlmostEqual(v2.i, -2.2)
        self.assertAlmostEqual(v2.j, -4.4)
        self.assertAlmostEqual(v2.k, -6.6)

    def test_createUnitized(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = v.createUnitized()
        self.assertAlmostEqual(v2.i, 1.0/sqrt(3))
        self.assertAlmostEqual(v2.j, 1.0/sqrt(3))
        self.assertAlmostEqual(v2.k, 1.0/sqrt(3))

    def test_createNegated(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = v.createNegated()
        self.assertAlmostEqual(v2.i, -1)
        self.assertAlmostEqual(v2.j, -1)
        self.assertAlmostEqual(v2.k, -1)

    def test_createScaled(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = v.createScaled(2)
        self.assertAlmostEqual(v2.i, 2)
        self.assertAlmostEqual(v2.j, 2)
        self.assertAlmostEqual(v2.k, 2)

    def test_getI(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertAlmostEqual(v.getI(), 1)

    def test_getJ(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertAlmostEqual(v.getJ(), 1)

    def test_getK(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertAlmostEqual(v.getK(), 1)

    def test_get(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertAlmostEqual(v.get(0), 1)
        self.assertAlmostEqual(v.get(1), 1)
        self.assertAlmostEqual(v.get(2), 1)

    def test_getLength(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertAlmostEqual(v.getLength(), sqrt(3))

    def test_getDot(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(1, 1, 1)
        self.assertAlmostEqual(v.getDot(v2), 3)

    def test_getSeparation(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(2, 1, 1)
        self.assertAlmostEqual(v.getSeparation(v2), 0.33983690945412204)

    def test_getSeparationOutOfPlane(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(2, 1, 1)
        self.assertAlmostEqual(v.getSeparationOutOfPlane(v2),
                               1.2309594173407745)

    def test_copyOf(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK.copyOf(v)
        self.assertEqual(v, v2)

    def test_hashCode(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertEqual(v.hashCode(), 1057895773279)

    def test_equals(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(1, 1, 1)
        v3 = UnwritableVectorIJK(1, 1, 2)
        self.assertTrue(v.equals(v2))
        self.assertFalse(v.equals(v3))

    def test_toString(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertEqual(v.toString(), "[1,1,1]")


if __name__ == '__main__':
    unittest.main()
