import unittest

from emmpy.crucible.core.math.coords.abstractvector import (
    AbstractVector
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        av = AbstractVector(0.0, 1.1, 2.2)
        self.assertAlmostEqual(av.ijkCoordinate.i, 0.0)
        self.assertAlmostEqual(av.ijkCoordinate.j, 1.1)
        self.assertAlmostEqual(av.ijkCoordinate.k, 2.2)

    def test_getI(self):
        av = AbstractVector(0.1, 1.2, 2.3)
        self.assertAlmostEqual(av.getI(), 0.1)

    def test_getJ(self):
        av = AbstractVector(0.1, 1.2, 2.3)
        self.assertAlmostEqual(av.getJ(), 1.2)

    def test_getK(self):
        av = AbstractVector(0.1, 1.2, 2.3)
        self.assertAlmostEqual(av.getK(), 2.3)

    def test_getVectorIJK(self):
        av = AbstractVector(0.1, 1.2, 2.3)
        vijk = av.getVectorIJK()
        self.assertAlmostEqual(vijk.i, 0.1)
        self.assertAlmostEqual(vijk.j, 1.2)
        self.assertAlmostEqual(vijk.k, 2.3)


if __name__ == '__main__':
    unittest.main()
