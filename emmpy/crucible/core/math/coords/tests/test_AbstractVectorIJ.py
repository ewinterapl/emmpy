import unittest

from emmpy.crucible.core.math.coords.abstractvectorij import (
    AbstractVectorIJ
)


class TestAbstractVectorIJ(unittest.TestCase):

    def test___init__(self):
        avij = AbstractVectorIJ(0.0, 0.1)
        self.assertAlmostEqual(avij.ijCoordinate.i, 0.0)
        self.assertAlmostEqual(avij.ijCoordinate.j, 0.1)

    def test_getI(self):
        avij = AbstractVectorIJ(0.0, 0.1)
        self.assertAlmostEqual(avij.getI(), 0.0)

    def test_getJ(self):
        avij = AbstractVectorIJ(0.0, 0.1)
        self.assertAlmostEqual(avij.getJ(), 0.1)

    def test_getVectorIJ(self):
        avij = AbstractVectorIJ(0.0, 0.1)
        uvij = avij.getVectorIJ()
        self.assertAlmostEqual(uvij.i, 0.0)
        self.assertAlmostEqual(uvij.j, 0.1)

    def test_hashCode(self):
        avij = AbstractVectorIJ(0.0, 0.1)
        self.assertEqual(avij.hashCode(), 1036832941)

    def test_equals(self):
        avij1 = AbstractVectorIJ(0.0, 0.1)
        avij2 = AbstractVectorIJ(0.0, 0.1)
        avij3 = AbstractVectorIJ(0.0, 0.2)
        self.assertTrue(avij1.equals(avij1))
        self.assertFalse(avij1.equals(None))
        self.assertFalse(avij1.equals([0.0, 0.1]))
        self.assertTrue(avij1.equals(avij2))
        self.assertFalse(avij1.equals(avij3))

    def test_toString(self):
        with self.assertRaises(Exception):
            AbstractVectorIJ.toString(None)


if __name__ == '__main__':
    unittest.main()
