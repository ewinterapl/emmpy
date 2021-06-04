from math import sqrt
import unittest

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        # 0-argument form
        vij = VectorIJ()
        self.assertAlmostEqual(vij.i, 0)
        self.assertAlmostEqual(vij.j, 0)
        # 1-argument forms
        vij = VectorIJ([1.1, 2.2])
        self.assertAlmostEqual(vij.i, 1.1)
        self.assertAlmostEqual(vij.j, 2.2)
        vij2 = VectorIJ(vij)
        self.assertAlmostEqual(vij2.i, 1.1)
        self.assertAlmostEqual(vij2.j, 2.2)
        # 2-argument forms
        vij = VectorIJ(1.1, 2.2)
        self.assertAlmostEqual(vij.i, 1.1)
        self.assertAlmostEqual(vij.j, 2.2)
        vij = VectorIJ(1, [0.0, 1.1, 2.2, 3.3])
        self.assertAlmostEqual(vij.i, 1.1)
        self.assertAlmostEqual(vij.j, 2.2)
        vij1 = VectorIJ(1.1, 2.2)
        vij2 = VectorIJ(-2.0, vij1)
        self.assertAlmostEqual(vij2.i, -2.2)
        self.assertAlmostEqual(vij2.j, -4.4)
        # Invalid forms.
        with self.assertRaises(Exception):
            VectorIJ(None)
        with self.assertRaises(Exception):
            VectorIJ(None, None)
        with self.assertRaises(CrucibleRuntimeException):
            VectorIJ(0, 1, 2)

    def test_createUnitized(self):
        vij1 = VectorIJ(1, 2)
        vij2 = vij1.createUnitized()
        self.assertAlmostEqual(vij2.i, 1/sqrt(5))
        self.assertAlmostEqual(vij2.j, 2/sqrt(5))

    def test_createNegated(self):
        vij1 = VectorIJ(1.1, 2.2)
        vij2 = VectorIJ.createNegated(vij1)
        self.assertAlmostEqual(vij2.i, -1.1)
        self.assertAlmostEqual(vij2.j, -2.2)

    def test_scale(self):
        vij = VectorIJ(1, 2)
        vij.scale(-1.1)
        self.assertAlmostEqual(vij.i, -1.1)
        self.assertAlmostEqual(vij.j, -2.2)

    def test_unitize(self):
        vij = VectorIJ(1, 2)
        vij2 = vij.unitize()
        self.assertIs(vij2, vij)
        self.assertAlmostEqual(vij.i, 1/sqrt(5))
        self.assertAlmostEqual(vij.j, 2/sqrt(5))
        vij = VectorIJ(0, 0)
        with self.assertRaises(UnsupportedOperationException):
            vij.unitize()

    def test_negate(self):
        vij = VectorIJ(1, 2)
        vij2 = vij.negate()
        self.assertIs(vij2, vij)
        self.assertAlmostEqual(vij.i, -1)
        self.assertAlmostEqual(vij.j, -2)

    def test_clear(self):
        vij = VectorIJ(1, 2)
        vij2 = vij.clear()
        self.assertIs(vij2, vij)
        self.assertEqual(vij.i, 0)
        self.assertEqual(vij.j, 0)

    def test_setI(self):
        vij = VectorIJ(1.1, 2.2)
        vij.setI(3.3)
        self.assertAlmostEqual(vij.i, 3.3)

    def test_setJ(self):
        vij = VectorIJ(1.1, 2.2)
        vij.setJ(3.3)
        self.assertAlmostEqual(vij.j, 3.3)

    def test_set(self):
        vij = VectorIJ(1.1, 2.2)
        vij.set(0, 3.3)
        self.assertAlmostEqual(vij.i, 3.3)
        vij.set(1, 4.4)
        self.assertAlmostEqual(vij.j, 4.4)
        with self.assertRaises(BugException):
            vij.set(2, 5.5)

    def test_setTo(self):
        # 1-argument forms
        vij1 = VectorIJ(1.1, 2.2)
        vij2 = VectorIJ(3.3, 4.4)
        vij2.setTo(vij1)
        self.assertAlmostEqual(vij2.i, 1.1)
        self.assertAlmostEqual(vij2.j, 2.2)
        vij2.setTo([5.5, 6.6])
        self.assertAlmostEqual(vij2.i, 5.5)
        self.assertAlmostEqual(vij2.j, 6.6)
        # 2-argument forms
        vij2.setTo(-2, vij1)
        self.assertAlmostEqual(vij2.i, -2.2)
        self.assertAlmostEqual(vij2.j, -4.4)
        vij2.setTo(1, [1.11, 2.22, 3.33])
        self.assertAlmostEqual(vij2.i, 2.22)
        self.assertAlmostEqual(vij2.j, 3.33)
        vij2.setTo(7.77, 8.88)
        self.assertAlmostEqual(vij2.i, 7.77)
        self.assertAlmostEqual(vij2.j, 8.88)
        # Invalid forms
        with self.assertRaises(CrucibleRuntimeException):
            vij2.setTo()
        with self.assertRaises(Exception):
            vij2.setTo(1)
        with self.assertRaises(Exception):
            vij2.setTo(1, None)
        with self.assertRaises(CrucibleRuntimeException):
            vij2.setTo(1, 2, 3, 4)

    def test_setToUnitized(self):
        vij1 = VectorIJ(1, 1)
        vij2 = VectorIJ(3, 4)
        vij = vij2.setToUnitized(vij1)
        self.assertIs(vij, vij2)
        self.assertAlmostEqual(vij2.i, 1/sqrt(2))
        self.assertAlmostEqual(vij2.j, 1/sqrt(2))

    def setToNegated(self):
        vij1 = VectorIJ(1, 2)
        vij2 = VectorIJ(3, 4)
        vij = vij2.setToNegated(vij1)
        self.assertIs(vij, vij2)
        self.assertAlmostEqual(vij2.i, -1)
        self.assertAlmostEqual(vij2.j, -2)

    def test_asVectorIJK(self):
        v1 = VectorIJ(1.1, 2.2)
        v2 = v1.asVectorIJK()
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 0)
        v3 = VectorIJK(0, 0, 0)
        v2 = v1.asVectorIJK(v3)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 0)
        with self.assertRaises(Exception):
            v1.asVectorIJK(None, None)

    def test_lineProject(self):
        vij1 = VectorIJ(1, 1)
        vij2 = VectorIJ(0, 1)
        vij3 = VectorIJ.lineProject(vij1, vij2)
        self.assertAlmostEqual(vij3.i, 1)
        self.assertAlmostEqual(vij3.j, 0)
        vij4 = VectorIJ()
        vij5 = VectorIJ.lineProject(vij1, vij2, vij4)
        self.assertAlmostEqual(vij5.i, 1)
        self.assertAlmostEqual(vij5.j, 0)
        with self.assertRaises(Exception):
            VectorIJ.lineProject()
        with self.assertRaises(Exception):
            VectorIJ.lineProject(None)
        with self.assertRaises(Exception):
            VectorIJ.lineProject(None, None, None)

    def test_project(self):
        vij0 = VectorIJ(0, 0)
        vij1 = VectorIJ(1, 1)
        vij2 = VectorIJ(0, 1)
        vij3 = VectorIJ.project(vij1, vij2)
        self.assertAlmostEqual(vij3.i, 0)
        self.assertAlmostEqual(vij3.j, 1)
        vij4 = VectorIJ()
        vij5 = VectorIJ.project(vij1, vij2, vij4)
        self.assertIs(vij5, vij4)
        self.assertAlmostEqual(vij4.i, 0)
        self.assertAlmostEqual(vij4.j, 1)
        with self.assertRaises(Exception):
            VectorIJ.project(vij1, vij0)
        with self.assertRaises(BugException):
            VectorIJ.project(None)
        with self.assertRaises(BugException):
            VectorIJ.project(vij1)
        with self.assertRaises(BugException):
            VectorIJ.project(vij1, vij2, vij3, vij4)

    def test_combine(self):
        vij1 = VectorIJ(1, 2)
        vij2 = VectorIJ(3, 4)
        vij3 = VectorIJ(5, 6)
        vij4 = VectorIJ.combine(2, vij1, 3, vij2)
        self.assertAlmostEqual(vij4.i, 11)
        self.assertAlmostEqual(vij4.j, 16)
        vij4 = VectorIJ.combine(2, vij1, 3, vij2, 4, vij3)
        self.assertAlmostEqual(vij4.i, 31)
        self.assertAlmostEqual(vij4.j, 40)
        with self.assertRaises(Exception):
            VectorIJ.combine()
        with self.assertRaises(Exception):
            VectorIJ.combine(1)

    def test_uCross(self):
        vij1 = VectorIJ(1, 0)
        vij2 = VectorIJ(0, 1)
        vijk = VectorIJ.uCross(vij1, vij2)
        self.assertAlmostEqual(vijk.i, 0)
        self.assertAlmostEqual(vijk.j, 0)
        self.assertAlmostEqual(vijk.k, 1)
        vijk0 = VectorIJK()
        vijk = VectorIJ.uCross(vij1, vij2, vijk0)
        self.assertIs(vijk, vijk0)
        self.assertAlmostEqual(vijk.i, 0)
        self.assertAlmostEqual(vijk.j, 0)
        self.assertAlmostEqual(vijk.k, 1)
        with self.assertRaises(Exception):
            VectorIJ.uCross()

    def test_cross(self):
        vij1 = VectorIJ(1, 0)
        vij2 = VectorIJ(0, 1)
        vijk = VectorIJ.cross(vij1, vij2)
        self.assertAlmostEqual(vijk.i, 0)
        self.assertAlmostEqual(vijk.j, 0)
        self.assertAlmostEqual(vijk.k, 1)
        vijk0 = VectorIJK()
        vijk = VectorIJ.cross(vij1, vij2, vijk0)
        self.assertIs(vijk, vijk0)
        self.assertAlmostEqual(vijk.i, 0)
        self.assertAlmostEqual(vijk.j, 0)
        self.assertAlmostEqual(vijk.k, 1)
        with self.assertRaises(Exception):
            VectorIJ.cross()

    def test_subtract(self):
        vij1 = VectorIJ(1, 1)
        vij2 = VectorIJ(1, 0)
        vij3 = VectorIJ.subtract(vij1, vij2)
        self.assertAlmostEqual(vij3.i, 0)
        self.assertAlmostEqual(vij3.j, 1)
        vij = VectorIJ()
        vij4 = VectorIJ.subtract(vij1, vij2, vij)
        self.assertIs(vij4, vij)
        self.assertAlmostEqual(vij4.i, 0)
        self.assertAlmostEqual(vij4.j, 1)
        with self.assertRaises(Exception):
            VectorIJ.subtract()

    def test_add(self):
        vij1 = VectorIJ(1, 1)
        vij2 = VectorIJ(1, 0)
        vij3 = VectorIJ.add(vij1, vij2)
        self.assertAlmostEqual(vij3.i, 2)
        self.assertAlmostEqual(vij3.j, 1)
        vij = VectorIJ()
        vij4 = VectorIJ.add(vij1, vij2, vij)
        self.assertIs(vij4, vij)
        self.assertAlmostEqual(vij4.i, 2)
        self.assertAlmostEqual(vij4.j, 1)
        with self.assertRaises(Exception):
            VectorIJ.add()

    def test_addAll(self):
        vij1 = VectorIJ(1, 2)
        vij2 = VectorIJ(3, 4)
        vij3 = VectorIJ(5, 6)
        vij4 = VectorIJ.addAll([vij1, vij2, vij3])
        self.assertAlmostEqual(vij4.i, 9)
        self.assertAlmostEqual(vij4.j, 12)
        vij = VectorIJ()
        vij5 = VectorIJ.addAll([vij1, vij2, vij3], vij)
        self.assertIs(vij5, vij)
        self.assertAlmostEqual(vij5.i, 9)
        self.assertAlmostEqual(vij5.j, 12)
        with self.assertRaises(Exception):
            VectorIJ.addAll()

    def test_addRSS(self):
        vij1 = VectorIJ(1, 2)
        vij2 = VectorIJ(3, 4)
        vij3 = VectorIJ.addRSS(vij1, vij2)
        self.assertAlmostEqual(vij3.i, sqrt(10))
        self.assertAlmostEqual(vij3.j, sqrt(20))
        vij = VectorIJ()
        vij4 = VectorIJ.addRSS(vij1, vij2, vij)
        self.assertIs(vij4, vij)
        self.assertAlmostEqual(vij4.i, sqrt(10))
        self.assertAlmostEqual(vij4.j, sqrt(20))
        with self.assertRaises(Exception):
            VectorIJ.addRSS()


if __name__ == '__main__':
    unittest.main()
