from math import sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import UnwritableVectorIJK

class TestUnwritableVectorIJK(unittest.TestCase):

    def test___init__(self):

        # Test the various forms of the constructor.
        # 3 components
        v = UnwritableVectorIJK(1, 2, 3)
        self.assertEqual(v.i, 1.0)
        self.assertEqual(v.j, 2.0)
        self.assertEqual(v.k, 3.0)
        # List of 3 components
        v = UnwritableVectorIJK([1, 2, 3])
        self.assertEqual(v.i, 1.0)
        self.assertEqual(v.j, 2.0)
        self.assertEqual(v.k, 3.0)
        # Offset into list of > 3 components
        v = UnwritableVectorIJK(1, [0, 1, 2, 3])
        self.assertEqual(v.i, 1.0)
        self.assertEqual(v.j, 2.0)
        self.assertEqual(v.k, 3.0)
        v2 = UnwritableVectorIJK(v)
        self.assertEqual(v2.i, 1.0)
        self.assertEqual(v2.j, 2.0)
        self.assertEqual(v2.k, 3.0)
        v2 = UnwritableVectorIJK(-2, v)
        self.assertEqual(v2.i, -2.0)
        self.assertEqual(v2.j, -4.0)
        self.assertEqual(v2.k, -6.0)

    def test_createUnitized(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = v.createUnitized()
        self.assertEqual(v2.i, 1.0/sqrt(3))
        self.assertEqual(v2.j, 1.0/sqrt(3))
        self.assertEqual(v2.k, 1.0/sqrt(3))

    def test_createNegated(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = v.createNegated()
        self.assertEqual(v2.i, -1)
        self.assertEqual(v2.j, -1)
        self.assertEqual(v2.k, -1)

    def test_createScaled(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = v.createScaled(2)
        self.assertEqual(v2.i, 2)
        self.assertEqual(v2.j, 2)
        self.assertEqual(v2.k, 2)

    def test_getI(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertEqual(v.getI(), 1)

    def test_getJ(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertEqual(v.getJ(), 1)

    def test_getK(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertEqual(v.getK(), 1)

    def test_get(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertEqual(v.get(0), 1)
        self.assertEqual(v.get(1), 1)
        self.assertEqual(v.get(2), 1)

    def test_getLength(self):
        v = UnwritableVectorIJK(1, 1, 1)
        self.assertTrue(np.isclose(v.getLength(), sqrt(3)))

    def test_getDot(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(1, 1, 1)
        self.assertEqual(v.getDot(v2), 3)

    def test_getSeparation(self):
        v = UnwritableVectorIJK(1, 1, 1)
        v2 = UnwritableVectorIJK(2, 1, 1)
        v.getSeparation(v2)
        # self.assertEqual(v.getDot(v2), 3)


if __name__ == '__main__':
    unittest.main()
