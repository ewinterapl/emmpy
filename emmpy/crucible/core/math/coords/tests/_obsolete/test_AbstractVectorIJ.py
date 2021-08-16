import unittest

from emmpy.crucible.core.math.coords.abstractvectorij import (
    AbstractVectorIJ
)


class TestBuilder(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
