from math import pi, sqrt
import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)


class TestUnwritableVectorIJ(unittest.TestCase):

    def test___init__(self):
        uv = UnwritableVectorIJ(1.1, 2.2)
        self.assertAlmostEqual(uv.i, 1.1)
        self.assertAlmostEqual(uv.j, 2.2)
        uv = UnwritableVectorIJ([1.1, 2.2])
        self.assertAlmostEqual(uv.i, 1.1)
        self.assertAlmostEqual(uv.j, 2.2)
        uv2 = UnwritableVectorIJ(uv)
        self.assertAlmostEqual(uv2.i, 1.1)
        self.assertAlmostEqual(uv2.j, 2.2)
        uv = UnwritableVectorIJ(2, [-1.1, 0.0, 1.1, 2.2])
        self.assertAlmostEqual(uv.i, 1.1)
        self.assertAlmostEqual(uv.j, 2.2)
        uv2 = UnwritableVectorIJ(-2.0, uv)
        self.assertAlmostEqual(uv2.i, -2.2)
        self.assertAlmostEqual(uv2.j, -4.4)
        with self.assertRaises(CrucibleRuntimeException):
            uv = UnwritableVectorIJ()

    def test_createUnitized(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        uv2 = uv.createUnitized()
        self.assertAlmostEqual(uv2.i, 1/sqrt(2))
        self.assertAlmostEqual(uv2.j, 1/sqrt(2))

    def test_createNegated(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        uv2 = uv.createNegated()
        self.assertAlmostEqual(uv2.i, -1.0)
        self.assertAlmostEqual(uv2.j, -1.0)

    def test_getI(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        self.assertAlmostEqual(uv.getI(), 1.0)

    def test_getJ(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        self.assertAlmostEqual(uv.getJ(), 1.0)

    def test_get(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        self.assertAlmostEqual(uv.getI(), 1.0)
        self.assertAlmostEqual(uv.getJ(), 1.0)

    def test_getLength(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        self.assertAlmostEqual(uv.getLength(), sqrt(2))

    def test_getDot(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        self.assertAlmostEqual(uv.getDot(uv), 2.0)

    def test_getSeparation(self):
        uv1 = UnwritableVectorIJ(1.0, 1.0)
        uv2 = UnwritableVectorIJ(1.0, -1.0)
        self.assertAlmostEqual(uv1.getSeparation(uv2), pi/2)

    def test_copyOf(self):
        uv1 = UnwritableVectorIJ(1.0, 1.0)
        uv2 = UnwritableVectorIJ.copyOf(uv1)
        self.assertAlmostEqual(uv1.i, uv2.i)
        self.assertAlmostEqual(uv1.j, uv2.j)

    def test_hashCode(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        self.assertEqual(uv.hashCode(), 34091303873)

    def test_equals(self):
        uv1 = UnwritableVectorIJ(1.0, 1.0)
        uv2 = UnwritableVectorIJ.copyOf(uv1)
        self.assertTrue(uv1.equals(uv2))

    def test_toString(self):
        uv = UnwritableVectorIJ(1.0, 1.0)
        self.assertEqual(uv.toString(), "[1,1]")


if __name__ == '__main__':
    unittest.main()
