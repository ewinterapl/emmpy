from math import pi, sqrt
import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        # 1-argument forms
        uv1 = UnwritableVectorIJ([1.1, 2.2])
        self.assertAlmostEqual(uv1.i, 1.1)
        self.assertAlmostEqual(uv1.j, 2.2)
        uv2 = UnwritableVectorIJ(uv1)
        self.assertAlmostEqual(uv2.i, 1.1)
        self.assertAlmostEqual(uv2.j, 2.2)
        with self.assertRaises(CrucibleRuntimeException):
            UnwritableVectorIJ(None)
        # 2-argument forms
        uv = UnwritableVectorIJ(1.11, 2.22)
        self.assertAlmostEqual(uv.i, 1.11)
        self.assertAlmostEqual(uv.j, 2.22)
        uv = UnwritableVectorIJ(2, [-1.1, 0.0, 2.2, 3.3, 4.4])
        self.assertAlmostEqual(uv.i, 2.2)
        self.assertAlmostEqual(uv.j, 3.3)
        uv2 = UnwritableVectorIJ(-2.0, uv)
        self.assertAlmostEqual(uv2.i, -4.4)
        self.assertAlmostEqual(uv2.j, -6.6)
        with self.assertRaises(CrucibleRuntimeException):
            UnwritableVectorIJ(None, None)
        with self.assertRaises(CrucibleRuntimeException):
            UnwritableVectorIJ()
        with self.assertRaises(CrucibleRuntimeException):
            UnwritableVectorIJ(0, 1, 2)

    def test_createUnitized(self):
        uv = UnwritableVectorIJ(1.0, 2.0)
        uv2 = uv.createUnitized()
        self.assertAlmostEqual(uv2.i, 1/sqrt(5))
        self.assertAlmostEqual(uv2.j, 2/sqrt(5))
        uv0 = UnwritableVectorIJ(0, 0)
        with self.assertRaises(Exception):
            uv2 = uv0.createUnitized()

    def test_createNegated(self):
        uv = UnwritableVectorIJ(1.0, 2.0)
        uv2 = uv.createNegated()
        self.assertAlmostEqual(uv2.i, -1.0)
        self.assertAlmostEqual(uv2.j, -2.0)

    def test_getI(self):
        uv = UnwritableVectorIJ(1.0, 2.0)
        self.assertAlmostEqual(uv.getI(), 1.0)

    def test_getJ(self):
        uv = UnwritableVectorIJ(1.0, 2.0)
        self.assertAlmostEqual(uv.getJ(), 2.0)

    def test_get(self):
        uv = UnwritableVectorIJ(1.0, 2.0)
        self.assertAlmostEqual(uv.i, 1.0)
        self.assertAlmostEqual(uv.j, 2.0)

    def test_getLength(self):
        uv = UnwritableVectorIJ(1.0, 2.0)
        self.assertAlmostEqual(uv.getLength(), sqrt(5))

    def test_getDot(self):
        uv1 = UnwritableVectorIJ(1.0, 2.0)
        uv2 = UnwritableVectorIJ(3.0, 4.0)
        self.assertAlmostEqual(uv1.getDot(uv2), 11.0)

    def test_getSeparation(self):
        uv1 = UnwritableVectorIJ(1.0, 1.0)
        uv2 = UnwritableVectorIJ(1.0, -1.0)
        self.assertAlmostEqual(uv1.getSeparation(uv2), pi/2)
        uv3 = UnwritableVectorIJ(0.0, 1.0)
        self.assertAlmostEqual(uv1.getSeparation(uv3), pi/4)

    def test_copyOf(self):
        uv1 = UnwritableVectorIJ(1.0, 2.0)
        uv2 = UnwritableVectorIJ.copyOf(uv1)
        self.assertAlmostEqual(uv1.i, uv2.i)
        self.assertAlmostEqual(uv1.j, uv2.j)

    # def test_hashCode(self):
    #     uv = UnwritableVectorIJ(1.0, 1.0)
    #     self.assertEqual(uv.hashCode(), 34091303873)

    # def test_equals(self):
    #     uv1 = UnwritableVectorIJ(1.0, 2.0)
    #     self.assertTrue(uv1.equals(uv1))
    #     self.assertFalse(uv1.equals(None))
    #     self.assertFalse(uv1.equals(CrucibleRuntimeException))
    #     uv3 = UnwritableVectorIJ(1.0, 3.0)
    #     self.assertFalse(uv1.equals(uv3))
    #     uv3 = UnwritableVectorIJ(3.0, 2.0)
    #     self.assertFalse(uv1.equals(uv3))
    #     uv3 = UnwritableVectorIJ(1.0, 3.0)
    #     self.assertFalse(uv1.equals(uv3))
    #     uv4 = UnwritableVectorIJ(1.0, 2.0)
    #     self.assertTrue(uv1.equals(uv4))

    # def test_toString(self):
    #     uv = UnwritableVectorIJ(1.1, 2.2)
    #     self.assertEqual(uv.toString(), "[1.1,2.2]")


if __name__ == '__main__':
    unittest.main()
