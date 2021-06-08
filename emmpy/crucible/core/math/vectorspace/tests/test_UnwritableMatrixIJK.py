from math import cos, sin, sqrt
import unittest

from emmpy.crucible.core.math.vectorspace.unwritablematrixijk import (
    UnwritableMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        # 0-argument form
        m = UnwritableMatrixIJK()
        self.assertIsNone(m.ii)
        self.assertIsNone(m.ij)
        self.assertIsNone(m.ik)
        self.assertIsNone(m.ji)
        self.assertIsNone(m.jj)
        self.assertIsNone(m.jk)
        self.assertIsNone(m.ki)
        self.assertIsNone(m.kj)
        self.assertIsNone(m.kk)
        # 1-argument forms
        m = UnwritableMatrixIJK([[1.1, 2.2, 3.3, 4.4],
                                 [5.5, 6.6, 7.7, 8.8],
                                 [9.9, 1.2, 3.4, 5.6],
                                 [7.8, 9.1, 1.3, 2.4]])
        self.assertAlmostEqual(m.ii, 1.1)
        self.assertAlmostEqual(m.ji, 5.5)
        self.assertAlmostEqual(m.ki, 9.9)
        self.assertAlmostEqual(m.ij, 2.2)
        self.assertAlmostEqual(m.jj, 6.6)
        self.assertAlmostEqual(m.kj, 1.2)
        self.assertAlmostEqual(m.ik, 3.3)
        self.assertAlmostEqual(m.jk, 7.7)
        self.assertAlmostEqual(m.kk, 3.4)
        m2 = UnwritableMatrixIJK(m)
        self.assertAlmostEqual(m2.ii, 1.1)
        self.assertAlmostEqual(m2.ji, 5.5)
        self.assertAlmostEqual(m2.ki, 9.9)
        self.assertAlmostEqual(m2.ij, 2.2)
        self.assertAlmostEqual(m2.jj, 6.6)
        self.assertAlmostEqual(m2.kj, 1.2)
        self.assertAlmostEqual(m2.ik, 3.3)
        self.assertAlmostEqual(m2.jk, 7.7)
        self.assertAlmostEqual(m2.kk, 3.4)
        # 2-argument form
        m2 = UnwritableMatrixIJK(2.0, m)
        self.assertAlmostEqual(m2.ii, 2.2)
        self.assertAlmostEqual(m2.ji, 11)
        self.assertAlmostEqual(m2.ki, 19.8)
        self.assertAlmostEqual(m2.ij, 4.4)
        self.assertAlmostEqual(m2.jj, 13.2)
        self.assertAlmostEqual(m2.kj, 2.4)
        self.assertAlmostEqual(m2.ik, 6.6)
        self.assertAlmostEqual(m2.jk, 15.4)
        self.assertAlmostEqual(m2.kk, 6.8)
        # 3-argument form
        v1 = UnwritableVectorIJK(1.1, 2.2, 3.3)
        v2 = UnwritableVectorIJK(4.4, 5.5, 6.6)
        v3 = UnwritableVectorIJK(7.7, 8.8, 9.9)
        m = UnwritableMatrixIJK(v1, v2, v3)
        self.assertAlmostEqual(m.ii, 1.1)
        self.assertAlmostEqual(m.ji, 2.2)
        self.assertAlmostEqual(m.ki, 3.3)
        self.assertAlmostEqual(m.ij, 4.4)
        self.assertAlmostEqual(m.jj, 5.5)
        self.assertAlmostEqual(m.kj, 6.6)
        self.assertAlmostEqual(m.ik, 7.7)
        self.assertAlmostEqual(m.jk, 8.8)
        self.assertAlmostEqual(m.kk, 9.9)
        # 4-argument form
        m2 = UnwritableMatrixIJK(-1.0, 2, 3, m)
        self.assertAlmostEqual(m2.ii, -1.1)
        self.assertAlmostEqual(m2.ji, -2.2)
        self.assertAlmostEqual(m2.ki, -3.3)
        self.assertAlmostEqual(m2.ij, 8.8)
        self.assertAlmostEqual(m2.jj, 11)
        self.assertAlmostEqual(m2.kj, 13.2)
        self.assertAlmostEqual(m2.ik, 23.1)
        self.assertAlmostEqual(m2.jk, 26.4)
        self.assertAlmostEqual(m2.kk, 29.7)
        # 6-argument form
        v1 = UnwritableVectorIJK(1, 2, 3)
        v2 = UnwritableVectorIJK(4, 5, 6)
        v3 = UnwritableVectorIJK(7, 8, 9)
        m = UnwritableMatrixIJK(-1, v1, 2, v2, 3, v3)
        self.assertAlmostEqual(m.ii, -1)
        self.assertAlmostEqual(m.ji, -2)
        self.assertAlmostEqual(m.ki, -3)
        self.assertAlmostEqual(m.ij, 8)
        self.assertAlmostEqual(m.jj, 10)
        self.assertAlmostEqual(m.kj, 12)
        self.assertAlmostEqual(m.ik, 21)
        self.assertAlmostEqual(m.jk, 24)
        self.assertAlmostEqual(m.kk, 27)
        # 9-argument form
        m = UnwritableMatrixIJK(1.1, 2.2, 3.3,
                                4.4, 5.5, 6.6,
                                7.7, 8.8, 9.9)
        self.assertAlmostEqual(m.ii, 1.1)
        self.assertAlmostEqual(m.ji, 2.2)
        self.assertAlmostEqual(m.ki, 3.3)
        self.assertAlmostEqual(m.ij, 4.4)
        self.assertAlmostEqual(m.jj, 5.5)
        self.assertAlmostEqual(m.kj, 6.6)
        self.assertAlmostEqual(m.ik, 7.7)
        self.assertAlmostEqual(m.jk, 8.8)
        self.assertAlmostEqual(m.kk, 9.9)
        # Invalid form
        with self.assertRaises(Exception):
            UnwritableMatrixIJK(None)

    def test_createTranspose(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = m.createTranspose()
        self.assertAlmostEqual(m2.ii, 1)
        self.assertAlmostEqual(m2.ji, 4)
        self.assertAlmostEqual(m2.ki, 7)
        self.assertAlmostEqual(m2.ij, 2)
        self.assertAlmostEqual(m2.jj, 5)
        self.assertAlmostEqual(m2.kj, 8)
        self.assertAlmostEqual(m2.ik, 3)
        self.assertAlmostEqual(m2.jk, 6)
        self.assertAlmostEqual(m2.kk, 9)

    def test_createUnitizedColumns(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = m.createUnitizedColumns()
        self.assertAlmostEqual(m2.ii, 1/sqrt(14))
        self.assertAlmostEqual(m2.ji, 2/sqrt(14))
        self.assertAlmostEqual(m2.ki, 3/sqrt(14))
        self.assertAlmostEqual(m2.ij, 4/sqrt(77))
        self.assertAlmostEqual(m2.jj, 5/sqrt(77))
        self.assertAlmostEqual(m2.kj, 6/sqrt(77))
        self.assertAlmostEqual(m2.ik, 7/sqrt(194))
        self.assertAlmostEqual(m2.jk, 8/sqrt(194))
        self.assertAlmostEqual(m2.kk, 9/sqrt(194))

    def test_createInverse(self):
        m = UnwritableMatrixIJK(1, 0, 5, 2, 1, 6, 3, 5, 0)
        m2 = m.createInverse()
        self.assertAlmostEqual(m2.ii, -6)
        self.assertAlmostEqual(m2.ji, 5)
        self.assertAlmostEqual(m2.ki, -1)
        self.assertAlmostEqual(m2.ij, 3.6)
        self.assertAlmostEqual(m2.jj, -3)
        self.assertAlmostEqual(m2.kj, 0.8)
        self.assertAlmostEqual(m2.jk, -1)
        self.assertAlmostEqual(m2.ik, 1.4)
        self.assertAlmostEqual(m2.kk, 0.2)
        with self.assertRaises(Exception):
            m = UnwritableMatrixIJK(0, 0, 0, 0, 0, 0, 0, 0, 0)
            m.createInverse()

    def test_createInvorted(self):
        a = 1
        m = UnwritableMatrixIJK(
            cos(a), 0, sin(a),
            0, 1, 0,
            -sin(a), 0, cos(a)
            )
        # 0.540302  | 0 | 0.841471
        # 0         | 1 | 0
        # -0.841471 | 0 | 0.540302
        m2 = m.createInvorted()
        self.assertAlmostEqual(m2.ii, cos(1))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, -sin(1))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, sin(1))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(1))
        with self.assertRaises(Exception):
            m = UnwritableMatrixIJK(0, 0, 0, 0, 0, 0, 0, 0, 0)
            m.createInvorted()

    def test_getII(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getII(), 1)

    def test_getJI(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getJI(), 2)

    def test_getKI(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getKI(), 3)

    def test_getIJ(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getIJ(), 4)

    def test_getJJ(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getJJ(), 5)

    def test_getKJ(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getKJ(), 6)

    def test_getIK(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getIK(), 7)

    def test_getJK(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getJK(), 8)

    def test_getKK(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getKK(), 9)

    def test_get(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.get(0, 0), 1)
        self.assertAlmostEqual(m.get(1, 0), 2)
        self.assertAlmostEqual(m.get(2, 0), 3)
        self.assertAlmostEqual(m.get(0, 1), 4)
        self.assertAlmostEqual(m.get(1, 1), 5)
        self.assertAlmostEqual(m.get(2, 1), 6)
        self.assertAlmostEqual(m.get(0, 2), 7)
        self.assertAlmostEqual(m.get(1, 2), 8)
        self.assertAlmostEqual(m.get(2, 2), 9)
        with self.assertRaises(Exception):
            m.get(0, 3)
        with self.assertRaises(Exception):
            m.get(1, 3)
        with self.assertRaises(Exception):
            m.get(2, 3)
        with self.assertRaises(Exception):
            m.get(3, 0)

    def test_getIthColumn(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = VectorIJK()
        v2 = m.getIthColumn()
        self.assertAlmostEqual(v2.i, 1)
        self.assertAlmostEqual(v2.j, 2)
        self.assertAlmostEqual(v2.k, 3)
        v2 = m.getIthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 1)
        self.assertAlmostEqual(v2.j, 2)
        self.assertAlmostEqual(v2.k, 3)

    def test_getJthColumn(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = VectorIJK()
        v2 = m.getJthColumn()
        self.assertAlmostEqual(v2.i, 4)
        self.assertAlmostEqual(v2.j, 5)
        self.assertAlmostEqual(v2.k, 6)
        v2 = m.getJthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 4)
        self.assertAlmostEqual(v2.j, 5)
        self.assertAlmostEqual(v2.k, 6)

    def test_getKthColumn(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = VectorIJK()
        v2 = m.getKthColumn()
        self.assertAlmostEqual(v2.i, 7)
        self.assertAlmostEqual(v2.j, 8)
        self.assertAlmostEqual(v2.k, 9)
        v2 = m.getKthColumn(v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 7)
        self.assertAlmostEqual(v2.j, 8)
        self.assertAlmostEqual(v2.k, 9)

    def test_getColumn(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v2 = VectorIJK()
        v = m.getColumn(0)
        self.assertAlmostEqual(v.i, 1)
        self.assertAlmostEqual(v.j, 2)
        self.assertAlmostEqual(v.k, 3)
        v = m.getColumn(1)
        self.assertAlmostEqual(v.i, 4)
        self.assertAlmostEqual(v.j, 5)
        self.assertAlmostEqual(v.k, 6)
        v = m.getColumn(2)
        self.assertAlmostEqual(v.i, 7)
        self.assertAlmostEqual(v.j, 8)
        self.assertAlmostEqual(v.k, 9)
        v = m.getColumn(0, v2)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v.i, 1)
        self.assertAlmostEqual(v.j, 2)
        self.assertAlmostEqual(v.k, 3)
        v = m.getColumn(1, v2)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v.i, 4)
        self.assertAlmostEqual(v.j, 5)
        self.assertAlmostEqual(v.k, 6)
        v = m.getColumn(2, v2)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v.i, 7)
        self.assertAlmostEqual(v.j, 8)
        self.assertAlmostEqual(v.k, 9)
        with self.assertRaises(Exception):
            m.getColumn(3)
        with self.assertRaises(Exception):
            m.getColumn(0, 0, 0)

    def test_getDeterminant(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getDeterminant(), 0)

    def test_getTrace(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertAlmostEqual(m.getTrace(), 15)

    def test_isRotation(self):
        a = 1
        m = UnwritableMatrixIJK(
            cos(a), 0, sin(a),
            0, 1, 0,
            -sin(a), 0, cos(a)
            )
        self.assertTrue(m.isRotation())
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertFalse(m.isRotation())

    def test_mxv(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = UnwritableVectorIJK(1, 2, 3)
        vb = UnwritableVectorIJK(0, 0, 0)
        v2 = m.mxv(v)
        self.assertAlmostEqual(v2.i, 1*1 + 4*2 + 7*3)
        self.assertAlmostEqual(v2.j, 2*1 + 5*2 + 8*3)
        self.assertAlmostEqual(v2.k, 3*1 + 6*2 + 9*3)
        v2 = m.mxv(v, vb)
        self.assertIs(v2, vb)
        self.assertAlmostEqual(v2.i, 1*1 + 4*2 + 7*3)
        self.assertAlmostEqual(v2.j, 2*1 + 5*2 + 8*3)
        self.assertAlmostEqual(v2.k, 3*1 + 6*2 + 9*3)

    def test_mtxv(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        v = UnwritableVectorIJK(1, 2, 3)
        vb = UnwritableVectorIJK(0, 0, 0)
        v2 = m.mtxv(v, vb)
        self.assertIs(v2, vb)
        self.assertAlmostEqual(v2.i, 1*1 + 2*2 + 3*3)
        self.assertAlmostEqual(v2.j, 4*1 + 5*2 + 6*3)
        self.assertAlmostEqual(v2.k, 7*1 + 8*2 + 9*3)

    def test_copyOf(self):
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = UnwritableMatrixIJK.copyOf(m)
        self.assertAlmostEqual(m2.ii, 1)
        self.assertAlmostEqual(m2.ji, 2)
        self.assertAlmostEqual(m2.ki, 3)
        self.assertAlmostEqual(m2.ij, 4)
        self.assertAlmostEqual(m2.jj, 5)
        self.assertAlmostEqual(m2.kj, 6)
        self.assertAlmostEqual(m2.ik, 7)
        self.assertAlmostEqual(m2.jk, 8)
        self.assertAlmostEqual(m2.kk, 9)

    # def test_hashCode(self):
    #     m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
    #     self.assertEqual(m.hashCode(), 939400226682508505375)

    # def test_equals(self):
    #     m1 = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
    #     m2 = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
    #     self.assertTrue(m1.equals(m1))
    #     self.assertFalse(m1.equals(None))
    #     self.assertFalse(m1.equals([]))
    #     self.assertTrue(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(0, 2, 3, 4, 5, 6, 7, 8, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 0, 3, 4, 5, 6, 7, 8, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 2, 0, 4, 5, 6, 7, 8, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 2, 3, 0, 5, 6, 7, 8, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 2, 3, 4, 0, 6, 7, 8, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 2, 3, 4, 5, 0, 7, 8, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 0, 8, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 0, 9)
    #     self.assertFalse(m1.equals(m2))
    #     m2 = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 0)
    #     self.assertFalse(m1.equals(m2))

    # def test_toString(self):
    #     m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
    #     self.assertEqual(m.toString(), "[1,2,3;4,5,6;7,8,9]")


if __name__ == '__main__':
    unittest.main()
