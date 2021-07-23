import unittest

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.sphericaltocartesianjacobian import (
    SphericalToCartesianJacobian
)
from emmpy.crucible.core.math.coords.sphericalvector import (
    SphericalVector
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        s2cj = SphericalToCartesianJacobian()
        self.assertIsNotNone(s2cj)

    def test_getTransformation(self):
        s2cj = SphericalToCartesianJacobian()
        spherical = SphericalVector(1, 2, 3)
        mijk = MatrixIJK()
        b = s2cj.getTransformation(spherical, mijk)
        self.assertIs(b, mijk)
        self.assertAlmostEqual(mijk.getII(), -0.9001976297355174)
        self.assertAlmostEqual(mijk.getJI(), 0.12832006020245673)
        self.assertAlmostEqual(mijk.getKI(), -0.4161468365471424)
        self.assertAlmostEqual(mijk.getIJ(), 0.411982245665683)
        self.assertAlmostEqual(mijk.getJJ(), -0.058726644927620980)
        self.assertAlmostEqual(mijk.getKJ(), -0.9092974268256817)
        self.assertAlmostEqual(mijk.getIK(), -0.12832006020245673)
        self.assertAlmostEqual(mijk.getJK(), -0.9001976297355174)
        self.assertAlmostEqual(mijk.getKK(), 0)

    def test_getInverseTransformation(self):
        s2cj = SphericalToCartesianJacobian()
        spherical = SphericalVector(1, 2, 3)
        mijk = MatrixIJK()
        b = s2cj.getInverseTransformation(spherical, mijk)
        self.assertIs(b, mijk)
        self.assertAlmostEqual(mijk.getII(), -0.9001976297355174)
        self.assertAlmostEqual(mijk.getJI(), 0.411982245665683)
        self.assertAlmostEqual(mijk.getKI(), -0.15519675289581672)
        self.assertAlmostEqual(mijk.getIJ(), 0.12832006020245673)
        self.assertAlmostEqual(mijk.getJJ(), -0.058726644927620980)
        self.assertAlmostEqual(mijk.getKJ(), -1.0887444167267328)
        self.assertAlmostEqual(mijk.getIK(), -0.4161468365471424)
        self.assertAlmostEqual(mijk.getJK(), -0.9092974268256817)
        self.assertAlmostEqual(mijk.getKK(), 0)
        with self.assertRaises(PointOnAxisException):
            s2cj.getInverseTransformation(SphericalVector(0, 0, 0), mijk)

    def test_mxv(self):
        s2cj = SphericalToCartesianJacobian()
        spherical = SphericalVector(1, 2, 3)
        mijk = MatrixIJK()
        s2cj.getTransformation(spherical, mijk)
        sphericalVelocity = SphericalVector(1, 1, 1)
        cartesianVelocity = s2cj.mxv(mijk, sphericalVelocity)
        self.assertAlmostEqual(cartesianVelocity.i, -0.6165354442722912)
        self.assertAlmostEqual(cartesianVelocity.j, -0.8306042144606817)
        self.assertAlmostEqual(cartesianVelocity.getK(), -1.325444263372824)
        s2cj.getInverseTransformation(spherical, mijk)
        sphericalVelocity = s2cj.mxv(mijk, cartesianVelocity)
        self.assertAlmostEqual(sphericalVelocity.getI(), 1)
        self.assertAlmostEqual(sphericalVelocity.getJ(), 1)
        self.assertAlmostEqual(sphericalVelocity.getK(), 1)


if __name__ == '__main__':
    unittest.main()
