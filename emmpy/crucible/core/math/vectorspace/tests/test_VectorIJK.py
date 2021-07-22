from math import pi, sqrt
import unittest
import numpy as np

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        """Test the __init__ method."""
        # 0-argument form
        v = VectorIJK()
        self.assertTrue(np.isnan(v.i))
        self.assertTrue(np.isnan(v.j))
        self.assertTrue(np.isnan(v.k))
        # 1-argument forms
        v = VectorIJK([1.1, 2.2, 3.3])
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        v2 = VectorIJK(v)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 3.3)
        # 2-argument forms
        # Offset and list
        v = VectorIJK(1, [0.0, 1.1, 2.2, 3.3])
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        # Scale and vector
        v2 = VectorIJK(-2.0, v)
        self.assertAlmostEqual(v2.i, -2.2)
        self.assertAlmostEqual(v2.j, -4.4)
        self.assertAlmostEqual(v2.k, -6.6)
        # 3-argument form
        v = VectorIJK(1.1, 2.2, 3.3)
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        # Invalid forms
        with self.assertRaises(Exception):
            VectorIJK(0)
        with self.assertRaises(Exception):
            VectorIJK(0, 1)
        with self.assertRaises(Exception):
            VectorIJK(0, 1, 2, 3)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v = VectorIJK(i, j, k)
        self.assertAlmostEqual(v.i, i)
        self.assertAlmostEqual(v.j, j)
        self.assertAlmostEqual(v.k, k)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = VectorIJK()
        (i, j, k) = (1.1, 2.2, 3.3)
        v.i = i
        self.assertAlmostEqual(v.i, i)
        v.j = j
        self.assertAlmostEqual(v.j, j)
        v.j = k
        self.assertAlmostEqual(v.j, k)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_createUnitized(self):
        v1 = VectorIJK(1, 2, 3)
        v2 = v1.createUnitized()
        self.assertAlmostEqual(v2.i, 1/sqrt(14))
        self.assertAlmostEqual(v2.j, 2/sqrt(14))
        self.assertAlmostEqual(v2.k, 3/sqrt(14))

    def test_createNegated(self):
        v1 = VectorIJK(1.1, 2.2, 3.3)
        v2 = VectorIJK.createNegated(v1)
        self.assertAlmostEqual(v2.i, -1.1)
        self.assertAlmostEqual(v2.j, -2.2)
        self.assertAlmostEqual(v2.k, -3.3)

    def test_createScaled(self):
        v1 = VectorIJK(1.1, 2.2, 3.3)
        v2 = v1.createScaled(-2)
        self.assertAlmostEqual(v2.i, -2.2)
        self.assertAlmostEqual(v2.j, -4.4)
        self.assertAlmostEqual(v2.k, -6.6)

    def test_scale(self):
        v = VectorIJK(1, 2, 3)
        v2 = v.scale(-2)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v.i, -2)
        self.assertAlmostEqual(v.j, -4)
        self.assertAlmostEqual(v.k, -6)

    def test_unitize(self):
        v = VectorIJK(1, 2, 3)
        v2 = v.unitize()
        self.assertIs(v2, v)
        self.assertAlmostEqual(v.i, 1/sqrt(14))
        self.assertAlmostEqual(v.j, 2/sqrt(14))
        self.assertAlmostEqual(v.k, 3/sqrt(14))
        v = VectorIJK(0, 0, 0)
        with self.assertRaises(Exception):
            v.unitize()

    def test_negate(self):
        v = VectorIJK(1, 2, 3)
        v2 = v.negate()
        self.assertIs(v2, v)
        self.assertAlmostEqual(v.i, -1)
        self.assertAlmostEqual(v.j, -2)
        self.assertAlmostEqual(v.k, -3)

    def test_clear(self):
        v = VectorIJK(1, 2, 3)
        v2 = v.clear()
        self.assertIs(v2, v)
        self.assertEqual(v.i, 0)
        self.assertEqual(v.j, 0)
        self.assertEqual(v.k, 0)

    def test_setI(self):
        v = VectorIJK(1.1, 2.2, 3.3)
        v.setI(4.4)
        self.assertAlmostEqual(v.i, 4.4)

    def test_setJ(self):
        v = VectorIJK(1.1, 2.2, 3.3)
        v.setJ(4.4)
        self.assertAlmostEqual(v.j, 4.4)

    def test_setK(self):
        v = VectorIJK(1.1, 2.2, 3.3)
        v.setK(4.4)
        self.assertAlmostEqual(v.k, 4.4)

    def test_set(self):
        v = VectorIJK(1.1, 2.2, 3.3)
        v.set(0, 4.4)
        self.assertAlmostEqual(v.i, 4.4)
        v.set(1, 5.5)
        self.assertAlmostEqual(v.j, 5.5)
        v.set(2, 6.6)
        self.assertAlmostEqual(v.k, 6.6)
        with self.assertRaises(Exception):
            v.set(3, 7.7)

    def test_setTo(self):
        # 1-argument forms
        # vector
        v1 = VectorIJK(1.1, 2.2, 3.3)
        v2 = VectorIJK()
        v3 = v2.setTo(v1)
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 3.3)
        # list
        v3 = v2.setTo([5.5, 6.6, 7.7])
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v2.i, 5.5)
        self.assertAlmostEqual(v2.j, 6.6)
        self.assertAlmostEqual(v2.k, 7.7)
        # 2-argument forms
        # scale and vector
        v3 = v2.setTo(-2, v1)
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v2.i, -2.2)
        self.assertAlmostEqual(v2.j, -4.4)
        self.assertAlmostEqual(v2.k, -6.6)
        # offset and list
        v3 = v2.setTo(1, [1.11, 2.22, 3.33, 4.44])
        self.assertIs(v3, v2)
        self.assertAlmostEqual(v2.i, 2.22)
        self.assertAlmostEqual(v2.j, 3.33)
        self.assertAlmostEqual(v2.k, 4.44)
        # 3-argument forms
        v1 = VectorIJK(1.1, 2.2, 3.3)
        v2 = VectorIJK(4.4, 5.5, 6.6)
        v2.setTo(v1)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 3.3)
        # Invalid forms
        with self.assertRaises(Exception):
            v2.setTo()
        with self.assertRaises(Exception):
            v2.setTo(None)

    def test_setToUnitized(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(3, 4, 5)
        v = v2.setToUnitized(v1)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v2.i, 1/sqrt(3))
        self.assertAlmostEqual(v2.j, 1/sqrt(3))
        self.assertAlmostEqual(v2.k, 1/sqrt(3))

    def setToNegated(self):
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(4, 5, 6)
        v = v2.setToNegated(v1)
        self.assertIs(v, v2)
        self.assertAlmostEqual(v2.i, -1)
        self.assertAlmostEqual(v2.j, -2)
        self.assertAlmostEqual(v2.k, -3)

    def test_rotate(self):
        v1 = VectorIJK(1, 0, 0)
        z_axis = VectorIJK(0, 0, 1)
        angle = pi/2
        v2 = VectorIJK.rotate(v1, z_axis, angle)
        self.assertAlmostEqual(v2.i, 0)
        self.assertAlmostEqual(v2.j, 1)
        self.assertAlmostEqual(v2.k, 0)
        v = VectorIJK()
        v2 = VectorIJK.rotate(v1, z_axis, angle, v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 0)
        self.assertAlmostEqual(v2.j, 1)
        self.assertAlmostEqual(v2.k, 0)
        with self.assertRaises(Exception):
            VectorIJK.rotate()

    def test_planeProject(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        v3 = VectorIJK.planeProject(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 1)
        self.assertAlmostEqual(v3.k, 1)
        v = VectorIJK()
        v3 = VectorIJK.planeProject(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 1)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.planeProject()

    def test_project(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        v3 = VectorIJK.project(v1, v2)
        self.assertAlmostEqual(v3.i, 1)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 0)
        v4 = VectorIJK()
        v5 = VectorIJK.project(v1, v2, v4)
        self.assertIs(v5, v4)
        self.assertAlmostEqual(v5.i, 1)
        self.assertAlmostEqual(v5.j, 0)
        self.assertAlmostEqual(v5.k, 0)
        with self.assertRaises(Exception):
            VectorIJK.project(None)

    def test_combine(self):
        v = VectorIJK()
        v0 = VectorIJK(0, 0, 0)
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(2, 3, 4)
        v3 = VectorIJK(3, 4, 5)
        v4 = VectorIJK(4, 5, 6)
        v5 = VectorIJK(5, 6, 7)
        v6 = VectorIJK(6, 7, 8)
        v7 = VectorIJK(7, 8, 9)
        # 2 vectors
        vc = VectorIJK.combine(1, v0, 2, v1)
        self.assertAlmostEqual(vc.i, 2)
        self.assertAlmostEqual(vc.j, 4)
        self.assertAlmostEqual(vc.k, 6)
        vc = VectorIJK.combine(1, v0, 2, v1, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 2)
        self.assertAlmostEqual(vc.j, 4)
        self.assertAlmostEqual(vc.k, 6)
        # 3 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2)
        self.assertAlmostEqual(vc.i, 8)
        self.assertAlmostEqual(vc.j, 13)
        self.assertAlmostEqual(vc.k, 18)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 8)
        self.assertAlmostEqual(vc.j, 13)
        self.assertAlmostEqual(vc.k, 18)
        # 4 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3)
        self.assertAlmostEqual(vc.i, 20)
        self.assertAlmostEqual(vc.j, 29)
        self.assertAlmostEqual(vc.k, 38)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 20)
        self.assertAlmostEqual(vc.j, 29)
        self.assertAlmostEqual(vc.k, 38)
        # 5 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4)
        self.assertAlmostEqual(vc.i, 40)
        self.assertAlmostEqual(vc.j, 54)
        self.assertAlmostEqual(vc.k, 68)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 40)
        self.assertAlmostEqual(vc.j, 54)
        self.assertAlmostEqual(vc.k, 68)
        # 6 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5)
        self.assertAlmostEqual(vc.i, 70)
        self.assertAlmostEqual(vc.j, 90)
        self.assertAlmostEqual(vc.k, 110)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 70)
        self.assertAlmostEqual(vc.j, 90)
        self.assertAlmostEqual(vc.k, 110)
        # 7 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6)
        self.assertAlmostEqual(vc.i, 112)
        self.assertAlmostEqual(vc.j, 139)
        self.assertAlmostEqual(vc.k, 166)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 112)
        self.assertAlmostEqual(vc.j, 139)
        self.assertAlmostEqual(vc.k, 166)
        # 8 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6, 8, v7)
        self.assertAlmostEqual(vc.i, 168)
        self.assertAlmostEqual(vc.j, 203)
        self.assertAlmostEqual(vc.k, 238)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6, 8, v7, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 168)
        self.assertAlmostEqual(vc.j, 203)
        self.assertAlmostEqual(vc.k, 238)
        # Invalid forms
        with self.assertRaises(Exception):
            VectorIJK.combine()

    def test_uCross(self):
        v = VectorIJK()
        v1 = VectorIJK(2, 0, 0)
        v2 = VectorIJK(0, 3, 0)
        v3 = VectorIJK.uCross(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        v3 = VectorIJK.uCross(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.uCross()

    def test_cross(self):
        v = VectorIJK()
        v1 = VectorIJK(1, 0, 0)
        v2 = VectorIJK(0, 1, 0)
        v3 = VectorIJK.cross(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        v3 = VectorIJK.cross(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.cross()

    def test_pointwiseMultiply(self):
        v = VectorIJK()
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(4, 5, 6)
        v3 = VectorIJK.pointwiseMultiply(v1, v2)
        self.assertAlmostEqual(v3.i, 4)
        self.assertAlmostEqual(v3.j, 10)
        self.assertAlmostEqual(v3.k, 18)
        v3 = VectorIJK.pointwiseMultiply(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 4)
        self.assertAlmostEqual(v3.j, 10)
        self.assertAlmostEqual(v3.k, 18)
        with self.assertRaises(Exception):
            VectorIJK.pointwiseMultiply()

    def test_subtract(self):
        v = VectorIJK()
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 1, 0)
        v3 = VectorIJK.subtract(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        v3 = VectorIJK.subtract(v1, v2, v)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.subtract()

    def test_add(self):
        v = VectorIJK()
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 1, 0)
        v3 = VectorIJK.add(v1, v2)
        self.assertAlmostEqual(v3.i, 2)
        self.assertAlmostEqual(v3.j, 2)
        self.assertAlmostEqual(v3.k, 1)
        v3 = VectorIJK.add(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 2)
        self.assertAlmostEqual(v3.j, 2)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.add()

    def test_addAll(self):
        v = VectorIJK()
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(3, 4, 5)
        v3 = VectorIJK(5, 6, 7)
        v4 = VectorIJK.addAll([v1, v2, v3])
        self.assertAlmostEqual(v4.i, 9)
        self.assertAlmostEqual(v4.j, 12)
        self.assertAlmostEqual(v4.k, 15)
        v4 = VectorIJK.addAll([v1, v2, v3], v)
        self.assertIs(v4, v)
        self.assertAlmostEqual(v4.i, 9)
        self.assertAlmostEqual(v4.j, 12)
        self.assertAlmostEqual(v4.k, 15)
        with self.assertRaises(Exception):
            VectorIJK.addAll()

    def test_addRSS(self):
        v = VectorIJK()
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(3, 4, 5)
        v3 = VectorIJK.addRSS(v1, v2)
        self.assertAlmostEqual(v3.i, sqrt(10))
        self.assertAlmostEqual(v3.j, sqrt(20))
        self.assertAlmostEqual(v3.k, sqrt(34))
        v3 = VectorIJK.addRSS(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, sqrt(10))
        self.assertAlmostEqual(v3.j, sqrt(20))
        self.assertAlmostEqual(v3.k, sqrt(34))
        with self.assertRaises(Exception):
            VectorIJK.addRSS()

    def test_getI(self):
        (i, j, k) = (1.1, 2.2, 3.3)
        v = VectorIJK(i, j, k)
        self.assertAlmostEqual(v.getI(), i)

    def test_getJ(self):
        (i, j, k) = (1.1, 2.2, 3.3)
        v = VectorIJK(i, j, k)
        self.assertAlmostEqual(v.getJ(), j)

    def test_getI(self):
        (i, j, k) = (1.1, 2.2, 3.3)
        v = VectorIJK(i, j, k)
        self.assertAlmostEqual(v.getK(), k)

    def test_copyOf(self):
        (i, j, k) = (1.1, 2.2, 3.3)
        v1 = VectorIJK(i, j, k)
        v2 = VectorIJK.copyOf(v1)
        self.assertAlmostEqual(v2.i, i)
        self.assertAlmostEqual(v2.j, j)
        self.assertAlmostEqual(v2.k, k)


if __name__ == '__main__':
    unittest.main()
