"""Tests for the vectorij module."""


import unittest
from math import sqrt
import numpy as np
from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        """Test the __init__ method."""
        # 0-argument form - all NaN.
        v = VectorIJ()
        self.assertIsInstance(v, VectorIJ)
        for x in v:
            self.assertTrue(np.isnan(x))
        # Test data
        (i, j) = (1.1, 2.2)
        # 1-argument forms
        # list
        v = VectorIJ([i, j])
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # tuple
        v = VectorIJ((i, j))
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # np.ndarray
        v = VectorIJ(np.array([i, j]))
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # vector
        v2 = VectorIJ(v)
        self.assertIsInstance(v2, VectorIJ)
        self.assertAlmostEqual(v2[0], i)
        self.assertAlmostEqual(v2[1], j)
        # 2-argument forms
        # offset and list
        v = VectorIJ(1, [0, i, j])
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # offset and tuple
        v = VectorIJ(1, (0, i, j))
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # offset and np.ndarray
        a = np.array([0, i, j])
        v = VectorIJ(1, a)
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # scale and vector
        scale = -2.2
        v = VectorIJ([i, j])
        v2 = VectorIJ(scale, v)
        self.assertIsInstance(v2, VectorIJ)
        self.assertAlmostEqual(v2[0], scale*i)
        self.assertAlmostEqual(v2[1], scale*j)
        # set components
        v = VectorIJ(i, j)
        self.assertIsInstance(v, VectorIJ)
        self.assertAlmostEqual(v[0], i)
        self.assertAlmostEqual(v[1], j)
        # >= 3 args is invalid
        with self.assertRaises(ValueError):
            v = VectorIJ(i, j, None)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (i, j) = (1.1, 2.2)
        v = VectorIJ(i, j)
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        with self.assertRaises(KeyError):
            bad = v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = VectorIJ()
        (i, j) = (1.1, 2.2)
        v.i = i
        self.assertAlmostEqual(v.i, i)
        v.j = j
        self.assertAlmostEqual(v.j, j)
        with self.assertRaises(KeyError):
            v.bad = 0

    # def test_createUnitized(self):
    #     vij1 = VectorIJ(1, 2)
    #     vij2 = vij1.createUnitized()
    #     self.assertAlmostEqual(vij2.i, 1/sqrt(5))
    #     self.assertAlmostEqual(vij2.j, 2/sqrt(5))

    # def test_createNegated(self):
    #     vij1 = VectorIJ(1.1, 2.2)
    #     vij2 = VectorIJ.createNegated(vij1)
    #     self.assertAlmostEqual(vij2.i, -1.1)
    #     self.assertAlmostEqual(vij2.j, -2.2)

    def test_scale(self):
        """Test the scale() method."""
        vij = VectorIJ(1, 2)
        vij.scale(-1.1)
        self.assertAlmostEqual(vij.i, -1.1)
        self.assertAlmostEqual(vij.j, -2.2)

    def test_unitize(self):
        """Test the unitize() method."""
        vij = VectorIJ(1, 2)
        vij2 = vij.unitize()
        self.assertIs(vij2, vij)
        self.assertAlmostEqual(vij.i, 1/sqrt(5))
        self.assertAlmostEqual(vij.j, 2/sqrt(5))

    # def test_negate(self):
    #     vij = VectorIJ(1, 2)
    #     vij2 = vij.negate()
    #     self.assertIs(vij2, vij)
    #     self.assertAlmostEqual(vij.i, -1)
    #     self.assertAlmostEqual(vij.j, -2)

    # def test_clear(self):
    #     vij = VectorIJ(1, 2)
    #     vij2 = vij.clear()
    #     self.assertIs(vij2, vij)
    #     self.assertEqual(vij.i, 0)
    #     self.assertEqual(vij.j, 0)

    # def test_setI(self):
    #     vij = VectorIJ(1.1, 2.2)
    #     vij.setI(3.3)
    #     self.assertAlmostEqual(vij.i, 3.3)

    # def test_setJ(self):
    #     vij = VectorIJ(1.1, 2.2)
    #     vij.setJ(3.3)
    #     self.assertAlmostEqual(vij.j, 3.3)

    # def test_set(self):
    #     vij = VectorIJ(1.1, 2.2)
    #     vij.set(0, 3.3)
    #     self.assertAlmostEqual(vij.i, 3.3)
    #     vij.set(1, 4.4)
    #     self.assertAlmostEqual(vij.j, 4.4)
    #     with self.assertRaises(BugException):
    #         vij.set(2, 5.5)

    def test_setTo(self):
        """Test the setTo method."""
        # Test data
        (i, j, k) = (1.1, 2.2, 3.3)
        # 1-argument forms
        # list
        data = [i, j]
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # tuple
        data = (i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # np.ndarray
        data = np.array([i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # VectorIJ
        data = VectorIJ([i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # 2-argument forms
        # Offset and list
        offset = 1
        data = [k, i, j]
        v1 = VectorIJ()
        v2 = v1.setTo(offset, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Offset and tuple
        offset = 1
        data = (k, i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(offset, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Offset and np.ndarray
        offset = 1
        data = np.array([k, i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(offset, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Scale factor and list
        scale = 1.1
        data = [i, j]
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Scale factor and tuple
        data = (i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Scale factor and np.ndarray
        data = np.array([i, j])
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Scale factor and VectorIJ
        data = VectorIJ(i, j)
        v1 = VectorIJ()
        v2 = v1.setTo(scale, data)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, scale*i)
        self.assertAlmostEqual(v2.j, scale*j)
        # Explicit values
        v1 = VectorIJ()
        v2 = v1.setTo(i, j)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        # Invalid forms
        sizes = (0, 3)
        for s in sizes:
            data = [None]*s
            v = VectorIJ()
            with self.assertRaises(TypeError):
                v2 = v.setTo(*data)

    # def test_setToUnitized(self):
    #     vij1 = VectorIJ(1, 1)
    #     vij2 = VectorIJ(3, 4)
    #     vij = vij2.setToUnitized(vij1)
    #     self.assertIs(vij, vij2)
    #     self.assertAlmostEqual(vij2.i, 1/sqrt(2))
    #     self.assertAlmostEqual(vij2.j, 1/sqrt(2))

    # def setToNegated(self):
    #     vij1 = VectorIJ(1, 2)
    #     vij2 = VectorIJ(3, 4)
    #     vij = vij2.setToNegated(vij1)
    #     self.assertIs(vij, vij2)
    #     self.assertAlmostEqual(vij2.i, -1)
    #     self.assertAlmostEqual(vij2.j, -2)

    # def test_asVectorIJK(self):
    #     v1 = VectorIJ(1.1, 2.2)
    #     v2 = v1.asVectorIJK()
    #     self.assertAlmostEqual(v2.i, 1.1)
    #     self.assertAlmostEqual(v2.j, 2.2)
    #     self.assertAlmostEqual(v2.k, 0)
    #     v3 = VectorIJK(0, 0, 0)
    #     v2 = v1.asVectorIJK(v3)
    #     self.assertAlmostEqual(v2.i, 1.1)
    #     self.assertAlmostEqual(v2.j, 2.2)
    #     self.assertAlmostEqual(v2.k, 0)
    #     with self.assertRaises(Exception):
    #         v1.asVectorIJK(None, None)

    # def test_lineProject(self):
    #     vij1 = VectorIJ(1, 1)
    #     vij2 = VectorIJ(0, 1)
    #     vij3 = VectorIJ.lineProject(vij1, vij2)
    #     self.assertAlmostEqual(vij3.i, 1)
    #     self.assertAlmostEqual(vij3.j, 0)
    #     vij4 = VectorIJ()
    #     vij5 = VectorIJ.lineProject(vij1, vij2, vij4)
    #     self.assertAlmostEqual(vij5.i, 1)
    #     self.assertAlmostEqual(vij5.j, 0)
    #     with self.assertRaises(Exception):
    #         VectorIJ.lineProject()
    #     with self.assertRaises(Exception):
    #         VectorIJ.lineProject(None)
    #     with self.assertRaises(Exception):
    #         VectorIJ.lineProject(None, None, None)

    # def test_project(self):
    #     vij0 = VectorIJ(0, 0)
    #     vij1 = VectorIJ(1, 1)
    #     vij2 = VectorIJ(0, 1)
    #     vij3 = VectorIJ.project(vij1, vij2)
    #     self.assertAlmostEqual(vij3.i, 0)
    #     self.assertAlmostEqual(vij3.j, 1)
    #     vij4 = VectorIJ()
    #     vij5 = VectorIJ.project(vij1, vij2, vij4)
    #     self.assertIs(vij5, vij4)
    #     self.assertAlmostEqual(vij4.i, 0)
    #     self.assertAlmostEqual(vij4.j, 1)
    #     with self.assertRaises(Exception):
    #         VectorIJ.project(vij1, vij0)
    #     with self.assertRaises(BugException):
    #         VectorIJ.project(None)
    #     with self.assertRaises(BugException):
    #         VectorIJ.project(vij1)
    #     with self.assertRaises(BugException):
    #         VectorIJ.project(vij1, vij2, vij3, vij4)

    # def test_combine(self):
    #     vij1 = VectorIJ(1, 2)
    #     vij2 = VectorIJ(3, 4)
    #     vij3 = VectorIJ(5, 6)
    #     vij4 = VectorIJ.combine(2, vij1, 3, vij2)
    #     self.assertAlmostEqual(vij4.i, 11)
    #     self.assertAlmostEqual(vij4.j, 16)
    #     vij4 = VectorIJ.combine(2, vij1, 3, vij2, 4, vij3)
    #     self.assertAlmostEqual(vij4.i, 31)
    #     self.assertAlmostEqual(vij4.j, 40)
    #     with self.assertRaises(Exception):
    #         VectorIJ.combine()
    #     with self.assertRaises(Exception):
    #         VectorIJ.combine(1)

    # def test_uCross(self):
    #     vij1 = VectorIJ(1, 0)
    #     vij2 = VectorIJ(0, 1)
    #     vijk = VectorIJ.uCross(vij1, vij2)
    #     self.assertAlmostEqual(vijk.i, 0)
    #     self.assertAlmostEqual(vijk.j, 0)
    #     self.assertAlmostEqual(vijk.k, 1)
    #     vijk0 = VectorIJK()
    #     vijk = VectorIJ.uCross(vij1, vij2, vijk0)
    #     self.assertIs(vijk, vijk0)
    #     self.assertAlmostEqual(vijk.i, 0)
    #     self.assertAlmostEqual(vijk.j, 0)
    #     self.assertAlmostEqual(vijk.k, 1)
    #     with self.assertRaises(Exception):
    #         VectorIJ.uCross()

    # def test_cross(self):
    #     vij1 = VectorIJ(1, 0)
    #     vij2 = VectorIJ(0, 1)
    #     vijk = VectorIJ.cross(vij1, vij2)
    #     self.assertAlmostEqual(vijk.i, 0)
    #     self.assertAlmostEqual(vijk.j, 0)
    #     self.assertAlmostEqual(vijk.k, 1)
    #     vijk0 = VectorIJK()
    #     vijk = VectorIJ.cross(vij1, vij2, vijk0)
    #     self.assertIs(vijk, vijk0)
    #     self.assertAlmostEqual(vijk.i, 0)
    #     self.assertAlmostEqual(vijk.j, 0)
    #     self.assertAlmostEqual(vijk.k, 1)
    #     with self.assertRaises(Exception):
    #         VectorIJ.cross()

    # def test_subtract(self):
    #     vij1 = VectorIJ(1, 1)
    #     vij2 = VectorIJ(1, 0)
    #     vij3 = VectorIJ.subtract(vij1, vij2)
    #     self.assertAlmostEqual(vij3.i, 0)
    #     self.assertAlmostEqual(vij3.j, 1)
    #     vij = VectorIJ()
    #     vij4 = VectorIJ.subtract(vij1, vij2, vij)
    #     self.assertIs(vij4, vij)
    #     self.assertAlmostEqual(vij4.i, 0)
    #     self.assertAlmostEqual(vij4.j, 1)
    #     with self.assertRaises(Exception):
    #         VectorIJ.subtract()

    # def test_add(self):
    #     vij1 = VectorIJ(1, 1)
    #     vij2 = VectorIJ(1, 0)
    #     vij3 = VectorIJ.add(vij1, vij2)
    #     self.assertAlmostEqual(vij3.i, 2)
    #     self.assertAlmostEqual(vij3.j, 1)
    #     vij = VectorIJ()
    #     vij4 = VectorIJ.add(vij1, vij2, vij)
    #     self.assertIs(vij4, vij)
    #     self.assertAlmostEqual(vij4.i, 2)
    #     self.assertAlmostEqual(vij4.j, 1)
    #     with self.assertRaises(Exception):
    #         VectorIJ.add()

    # def test_addAll(self):
    #     vij1 = VectorIJ(1, 2)
    #     vij2 = VectorIJ(3, 4)
    #     vij3 = VectorIJ(5, 6)
    #     vij4 = VectorIJ.addAll([vij1, vij2, vij3])
    #     self.assertAlmostEqual(vij4.i, 9)
    #     self.assertAlmostEqual(vij4.j, 12)
    #     vij = VectorIJ()
    #     vij5 = VectorIJ.addAll([vij1, vij2, vij3], vij)
    #     self.assertIs(vij5, vij)
    #     self.assertAlmostEqual(vij5.i, 9)
    #     self.assertAlmostEqual(vij5.j, 12)
    #     with self.assertRaises(Exception):
    #         VectorIJ.addAll()

    # def test_addRSS(self):
    #     vij1 = VectorIJ(1, 2)
    #     vij2 = VectorIJ(3, 4)
    #     vij3 = VectorIJ.addRSS(vij1, vij2)
    #     self.assertAlmostEqual(vij3.i, sqrt(10))
    #     self.assertAlmostEqual(vij3.j, sqrt(20))
    #     vij = VectorIJ()
    #     vij4 = VectorIJ.addRSS(vij1, vij2, vij)
    #     self.assertIs(vij4, vij)
    #     self.assertAlmostEqual(vij4.i, sqrt(10))
    #     self.assertAlmostEqual(vij4.j, sqrt(20))
    #     with self.assertRaises(Exception):
    #         VectorIJ.addRSS()


if __name__ == '__main__':
    unittest.main()
