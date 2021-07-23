import unittest

from emmpy.crucible.core.math.coords.latitudinaltocartesianjacobian import (
    LatitudinalToCartesianJacobian
)
from emmpy.crucible.core.math.coords.latitudinalvector import LatitudinalVector
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        l2cj = LatitudinalToCartesianJacobian()
        self.assertIsNotNone(l2cj)

    def test_getTransformation(self):
        l2cj = LatitudinalToCartesianJacobian()
        coordPosition = LatitudinalVector(1, 2, 3)
        buffer = MatrixIJK()
        b = l2cj.getTransformation(coordPosition, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(b.getII(), 0.411982245665683)
        self.assertAlmostEqual(b.getJI(), -0.05872664492762098)
        self.assertAlmostEqual(b.getKI(), 0.9092974268256817)
        self.assertAlmostEqual(b.getIJ(), 0.9001976297355174)
        self.assertAlmostEqual(b.getJJ(), -0.12832006020245673)
        self.assertAlmostEqual(b.getKJ(), -0.4161468365471424)
        self.assertAlmostEqual(b.getIK(), 0.05872664492762098)
        self.assertAlmostEqual(b.getJK(), 0.411982245665683)
        self.assertAlmostEqual(b.getKK(), 0)

    def test_getInverseTransformation(self):
        l2cj = LatitudinalToCartesianJacobian()
        coordPosition = LatitudinalVector(1, 2, 3)
        buffer = MatrixIJK()
        b = l2cj.getInverseTransformation(coordPosition, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(b.getII(), 0.411982245665683)
        self.assertAlmostEqual(b.getJI(), 0.9001976297355174)
        self.assertAlmostEqual(b.getKI(), 0.339111091726107)
        self.assertAlmostEqual(b.getIJ(), -0.05872664492762098)
        self.assertAlmostEqual(b.getJJ(), -0.12832006020245673)
        self.assertAlmostEqual(b.getKJ(), 2.378949951451322)
        self.assertAlmostEqual(b.getIK(), 0.9092974268256817)
        self.assertAlmostEqual(b.getJK(), -0.4161468365471424)
        self.assertAlmostEqual(b.getKK(), 0)

    def test_mxv(self):
        l2cj = LatitudinalToCartesianJacobian()
        r = 1.0
        lat = 2.0
        lon = 3.0
        lv = LatitudinalVector(r, lat, lon)
        mijk = MatrixIJK()
        l2cj.getTransformation(lv, mijk)
        latitudinalVelocity = LatitudinalVector(1, 1, 1)
        cartesianVelocity = l2cj.mxv(mijk, latitudinalVelocity)
        self.assertAlmostEqual(cartesianVelocity.i, 1.3709065203288213)
        self.assertAlmostEqual(cartesianVelocity.j, 0.22493554053560527)
        self.assertAlmostEqual(cartesianVelocity.getK(), 0.4931505902785393)
        l2cj.getInverseTransformation(lv, mijk)
        latitudinalalVelocity = l2cj.mxv(mijk, cartesianVelocity)
        self.assertAlmostEqual(latitudinalalVelocity.getI(), 1)
        self.assertAlmostEqual(latitudinalalVelocity.getJ(), 1)
        self.assertAlmostEqual(latitudinalalVelocity.getK(), 1)


if __name__ == '__main__':
    unittest.main()
