from math import pi, sqrt
import unittest

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestVectorIJK(unittest.TestCase):

    def test___init__(self):
        v = VectorIJK()
        self.assertAlmostEqual(v.i, 0)
        self.assertAlmostEqual(v.j, 0)
        self.assertAlmostEqual(v.k, 0)
        v = VectorIJK(1.1, 2.2, 3.3)
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        v = VectorIJK([1.1, 2.2, 3.3])
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        v = VectorIJK(1, [0.0, 1.1, 2.2, 3.3])
        self.assertAlmostEqual(v.i, 1.1)
        self.assertAlmostEqual(v.j, 2.2)
        self.assertAlmostEqual(v.k, 3.3)
        v1 = VectorIJK(1.1, 2.2, 3.3)
        v2 = VectorIJK(v1)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 3.3)
        v1 = VectorIJK(1.1, 2.2, 3.3)
        v2 = VectorIJK(-2.0, v1)
        self.assertAlmostEqual(v2.i, -2.2)
        self.assertAlmostEqual(v2.j, -4.4)
        self.assertAlmostEqual(v2.k, -6.6)

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
        v.scale(-2)
        self.assertAlmostEqual(v.i, -2)
        self.assertAlmostEqual(v.j, -4)
        self.assertAlmostEqual(v.k, -6)

    def test_unitize(self):
        v = VectorIJK(1, 2, 3)
        v.unitize()
        self.assertAlmostEqual(v.i, 1/sqrt(14))
        self.assertAlmostEqual(v.j, 2/sqrt(14))
        self.assertAlmostEqual(v.k, 3/sqrt(14))

    def test_negate(self):
        v = VectorIJK(1, 2, 3)
        v.negate()
        self.assertAlmostEqual(v.i, -1)
        self.assertAlmostEqual(v.j, -2)
        self.assertAlmostEqual(v.k, -3)

    def test_clear(self):
        v = VectorIJK(1, 2, 3)
        v.clear()
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
        v1 = VectorIJK(1.1, 2.2, 3.3)
        v2 = VectorIJK(4.4, 5.5, 6.6)
        v2.setTo(v1)
        self.assertAlmostEqual(v2.i, 1.1)
        self.assertAlmostEqual(v2.j, 2.2)
        self.assertAlmostEqual(v2.k, 3.3)
        v2.setTo([5.5, 6.6, 7.7])
        self.assertAlmostEqual(v2.i, 5.5)
        self.assertAlmostEqual(v2.j, 6.6)
        self.assertAlmostEqual(v2.k, 7.7)
        v2.setTo(-2, v1)
        self.assertAlmostEqual(v2.i, -2.2)
        self.assertAlmostEqual(v2.j, -4.4)
        self.assertAlmostEqual(v2.k, -6.6)
        v2.setTo(1, [1.11, 2.22, 3.33, 4.44])
        self.assertAlmostEqual(v2.i, 2.22)
        self.assertAlmostEqual(v2.j, 3.33)
        self.assertAlmostEqual(v2.k, 4.44)

    def test_setToUnitized(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(3, 4, 5)
        v2.setToUnitized(v1)
        self.assertAlmostEqual(v2.i, 1/sqrt(3))
        self.assertAlmostEqual(v2.j, 1/sqrt(3))
        self.assertAlmostEqual(v2.k, 1/sqrt(3))

    def setToNegated(self):
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(4, 5, 6)
        v2.setToNegated(v1)
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

    def test_planeProject(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        v3 = VectorIJK.planeProject(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 1)
        self.assertAlmostEqual(v3.k, 1)

    def test_project(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        v3 = VectorIJK.project(v1, v2)
        self.assertAlmostEqual(v3.i, 1)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 0)

    def test_combine(self):
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(3, 4, 5)
        v3 = VectorIJK(5, 6, 7)
        v4 = VectorIJK.combine(1, v1, 2, v2, 3, v3)
        self.assertAlmostEqual(v4.i, 22)
        self.assertAlmostEqual(v4.j, 28)
        self.assertAlmostEqual(v4.k, 34)

    def test_uCross(self):
        v1 = VectorIJK(2, 0, 0)
        v2 = VectorIJK(0, 3, 0)
        v3 = VectorIJK.uCross(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)

    def test_cross(self):
        v1 = VectorIJK(1, 0, 0)
        v2 = VectorIJK(0, 1, 0)
        v3 = VectorIJK.cross(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)

    def test_pointwiseMultiply(self):
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(4, 5, 6)
        v3 = VectorIJK.pointwiseMultiply(v1, v2)
        self.assertAlmostEqual(v3.i, 4)
        self.assertAlmostEqual(v3.j, 10)
        self.assertAlmostEqual(v3.k, 18)

    def test_subtract(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 1, 0)
        v3 = VectorIJK.subtract(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)

    def test_add(self):
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 1, 0)
        v3 = VectorIJK.add(v1, v2)
        self.assertAlmostEqual(v3.i, 2)
        self.assertAlmostEqual(v3.j, 2)
        self.assertAlmostEqual(v3.k, 1)

    def test_addAll(self):
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(3, 4, 5)
        v3 = VectorIJK(5, 6, 7)
        v4 = VectorIJK.addAll([v1, v2, v3])
        self.assertAlmostEqual(v4.i, 9)
        self.assertAlmostEqual(v4.j, 12)
        self.assertAlmostEqual(v4.k, 15)

    def test_addRSS(self):
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(3, 4, 5)
        v3 = VectorIJK.addRSS(v1, v2)
        self.assertAlmostEqual(v3.i, sqrt(10))
        self.assertAlmostEqual(v3.j, sqrt(20))
        self.assertAlmostEqual(v3.k, sqrt(34))


if __name__ == '__main__':
    unittest.main()
