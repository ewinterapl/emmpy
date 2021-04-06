from math import cos, pi, sin, sqrt
import unittest

from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.core.math.vectorspace.unwritablematrixij import (
    UnwritableMatrixIJ
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)
from emmpy.java.lang.illegalargumentexception import (
    IllegalArgumentException
)
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)


class TestUnwritableMatrixIJ(unittest.TestCase):

    def test___init__(self):
        # 0-argument form
        m = UnwritableMatrixIJ()
        self.assertIsNone(m.ii)
        self.assertIsNone(m.ij)
        self.assertIsNone(m.ji)
        self.assertIsNone(m.jj)
        # 1-argument forms
        m = UnwritableMatrixIJ([[1.1, 2.2], [3.3, 4.4]])
        self.assertAlmostEqual(m.ii, 1.1)
        self.assertAlmostEqual(m.ji, 3.3)
        self.assertAlmostEqual(m.ij, 2.2)
        self.assertAlmostEqual(m.jj, 4.4)
        m2 = UnwritableMatrixIJ(m)
        self.assertAlmostEqual(m2.ii, 1.1)
        self.assertAlmostEqual(m2.ji, 3.3)
        self.assertAlmostEqual(m2.ij, 2.2)
        self.assertAlmostEqual(m2.jj, 4.4)
        # 2-argument forms
        m2 = UnwritableMatrixIJ(2.0, m)
        self.assertAlmostEqual(m2.ii, 2.2)
        self.assertAlmostEqual(m2.ji, 6.6)
        self.assertAlmostEqual(m2.ij, 4.4)
        self.assertAlmostEqual(m2.jj, 8.8)
        v1 = UnwritableVectorIJ(1.1, 2.2)
        v2 = UnwritableVectorIJ(3.3, 4.4)
        m = UnwritableMatrixIJ(v1, v2)
        self.assertAlmostEqual(m.ii, 1.1)
        self.assertAlmostEqual(m.ji, 2.2)
        self.assertAlmostEqual(m.ij, 3.3)
        self.assertAlmostEqual(m.jj, 4.4)
        # 3-argument form
        m = UnwritableMatrixIJ(1.1, 2.2, 3.3, 4.4)
        m2 = UnwritableMatrixIJ(-1.0, 2.0, m)
        self.assertAlmostEqual(m2.ii, -1.1)
        self.assertAlmostEqual(m2.ji, -2.2)
        self.assertAlmostEqual(m2.ij, 6.6)
        self.assertAlmostEqual(m2.jj, 8.8)
        # 4-argument forms
        m = UnwritableMatrixIJ(1.1, 2.2, 3.3, 4.4)
        self.assertAlmostEqual(m.ii, 1.1)
        self.assertAlmostEqual(m.ji, 2.2)
        self.assertAlmostEqual(m.ij, 3.3)
        self.assertAlmostEqual(m.jj, 4.4)
        v1 = UnwritableVectorIJ(1.1, 2.2)
        v2 = UnwritableVectorIJ(3.3, 4.4)
        m = UnwritableMatrixIJ(-1.0, v1, 2.0, v2)
        self.assertAlmostEqual(m.ii, -1.1)
        self.assertAlmostEqual(m.ji, -2.2)
        self.assertAlmostEqual(m.ij, 6.6)
        self.assertAlmostEqual(m.jj, 8.8)
        # Invalid cases
        with self.assertRaises(Exception):
            UnwritableMatrixIJ(1, 2, 3, 4, 5)

    def test_createTranspose(self):
        m = UnwritableMatrixIJ(1.1, 2.2, 3.3, 4.4)
        m2 = m.createTranspose()
        self.assertAlmostEqual(m2.ii, 1.1)
        self.assertAlmostEqual(m2.ji, 3.3)
        self.assertAlmostEqual(m2.ij, 2.2)
        self.assertAlmostEqual(m2.jj, 4.4)

    def test_createUnitizedColumns(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        m2 = m.createUnitizedColumns()
        self.assertAlmostEqual(m2.ii, 1/sqrt(5))
        self.assertAlmostEqual(m2.ji, 2/sqrt(5))
        self.assertAlmostEqual(m2.ij, 3/5)
        self.assertAlmostEqual(m2.jj, 4/5)

    def test_createInverse(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        m2 = m.createInverse()
        self.assertAlmostEqual(m2.ii, -2)
        self.assertAlmostEqual(m2.ji, 1)
        self.assertAlmostEqual(m2.ij, 1.5)
        self.assertAlmostEqual(m2.jj, -0.5)
        with self.assertRaises(UnsupportedOperationException):
            m = UnwritableMatrixIJ(0, 0, 1, 1)
            m.createInverse()

    def test_createInvorted(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        m2 = m.createInvorted()
        self.assertAlmostEqual(m2.ii, 0.2)
        self.assertAlmostEqual(m2.ji, 0.12)
        self.assertAlmostEqual(m2.ij, 0.4)
        self.assertAlmostEqual(m2.jj, 0.16)
        with self.assertRaises(UnsupportedOperationException):
            m = UnwritableMatrixIJ(0, 0, 1, 1)
            m.createInvorted()

    def test_getII(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertAlmostEqual(m.getII(), 1)

    def test_getJI(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertAlmostEqual(m.getJI(), 2)

    def test_getIJ(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertAlmostEqual(m.getIJ(), 3)

    def test_getJJ(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertAlmostEqual(m.getJJ(), 4)

    def test_get(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertAlmostEqual(m.get(0, 0), 1)
        self.assertAlmostEqual(m.get(1, 0), 2)
        self.assertAlmostEqual(m.get(0, 1), 3)
        self.assertAlmostEqual(m.get(1, 1), 4)
        with self.assertRaises(IllegalArgumentException):
            m.get(0, 2)
        with self.assertRaises(IllegalArgumentException):
            m.get(1, 2)
        with self.assertRaises(IllegalArgumentException):
            m.get(2, 0)

    def test_getIthColumn(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        v = VectorIJ()
        v2 = m.getIthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 1)
        self.assertAlmostEqual(v2.j, 2)

    def test_getJthColumn(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        v = VectorIJ()
        v2 = m.getJthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 3)
        self.assertAlmostEqual(v2.j, 4)

    def test_getColumn(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        v = VectorIJ()
        v2 = m.getColumn(0, v)
        self.assertAlmostEqual(v2.i, 1)
        self.assertAlmostEqual(v2.j, 2)
        v2 = m.getColumn(1, v)
        self.assertAlmostEqual(v2.i, 3)
        self.assertAlmostEqual(v2.j, 4)
        with self.assertRaises(IllegalArgumentException):
            m.getColumn(2, v)

    def test_getDeterminant(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertAlmostEqual(m.getDeterminant(), -2)

    def test_getTrace(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertAlmostEqual(m.getTrace(), 5)

    def test_isRotation(self):
        a = pi/3
        m = UnwritableMatrixIJ(cos(a), sin(a), -sin(a), cos(a))
        self.assertTrue(m.isRotation())
        # THIS SHOULD BE FALSE!
        # m = UnwritableMatrixIJ(1, 2, 3, 4)
        # self.assertFalse(m.isRotation())

    def test_isSymmetric(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertFalse(m.isSymmetric())
        m = UnwritableMatrixIJ(1, 2, 2, 4)
        self.assertTrue(m.isSymmetric())

    def test_mxv(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        v = VectorIJ(5, 6)
        v2 = m.mxv(v)
        self.assertAlmostEqual(v2.i, 23)
        self.assertAlmostEqual(v2.j, 34)
        vb = VectorIJ()
        v2 = m.mxv(v, vb)
        self.assertIs(v2, vb)
        self.assertAlmostEqual(v2.i, 23)
        self.assertAlmostEqual(v2.j, 34)

    def test_mtxv(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        v = VectorIJ(5, 6)
        v2 = m.mtxv(v)
        self.assertAlmostEqual(v2.i, 17)
        self.assertAlmostEqual(v2.j, 39)
        vb = VectorIJ()
        v2 = m.mtxv(v, vb)
        self.assertIs(v2, vb)
        self.assertAlmostEqual(v2.i, 17)
        self.assertAlmostEqual(v2.j, 39)

    def test_copyOf(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        m2 = UnwritableMatrixIJ.copyOf(m)
        self.assertAlmostEqual(m2.get(0, 0), 1)
        self.assertAlmostEqual(m2.get(1, 0), 2)
        self.assertAlmostEqual(m2.get(0, 1), 3)
        self.assertAlmostEqual(m2.get(1, 1), 4)

    def test_hashCode(self):
        m = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertEqual(m.hashCode(), 1017055385278623)

    def test_equals(self):
        m1 = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertTrue(m1.equals(m1))
        self.assertFalse(m1.equals(None))
        self.assertFalse(m1.equals([1, 2, 3, 4]))
        m2 = UnwritableMatrixIJ(0, 2, 3, 4)
        self.assertFalse(m1.equals(m2))
        m2 = UnwritableMatrixIJ(0, 2, 3, 4)
        self.assertFalse(m1.equals(m2))
        m2 = UnwritableMatrixIJ(1, 0, 3, 4)
        self.assertFalse(m1.equals(m2))
        m2 = UnwritableMatrixIJ(1, 2, 0, 4)
        self.assertFalse(m1.equals(m2))
        m2 = UnwritableMatrixIJ(1, 2, 3, 4)
        self.assertTrue(m1.equals(m2))

    def test_toString(self):
        m = UnwritableMatrixIJ(1.1, 2.2, 3.3, 4.4)
        self.assertEqual(m.toString(), "[1.1,2.2;3.3,4.4]")


if __name__ == '__main__':
    unittest.main()
