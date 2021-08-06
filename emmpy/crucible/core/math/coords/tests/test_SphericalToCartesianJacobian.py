import unittest

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.sphericaltocartesianjacobian import (
    SphericalToCartesianJacobian
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
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
        self.assertAlmostEqual(mijk.ii, -0.9001976297355174)
        self.assertAlmostEqual(mijk.ji, 0.12832006020245673)
        self.assertAlmostEqual(mijk.ki, -0.4161468365471424)
        self.assertAlmostEqual(mijk.ij, 0.411982245665683)
        self.assertAlmostEqual(mijk.jj, -0.058726644927620980)
        self.assertAlmostEqual(mijk.kj, -0.9092974268256817)
        self.assertAlmostEqual(mijk.ik, -0.12832006020245673)
        self.assertAlmostEqual(mijk.jk, -0.9001976297355174)
        self.assertAlmostEqual(mijk.kk, 0)

    def test_getInverseTransformation(self):
        s2cj = SphericalToCartesianJacobian()
        spherical = SphericalVector(1, 2, 3)
        mijk = MatrixIJK()
        b = s2cj.getInverseTransformation(spherical, mijk)
        self.assertIs(b, mijk)
        self.assertAlmostEqual(mijk.ii, -0.9001976297355174)
        self.assertAlmostEqual(mijk.ji, 0.411982245665683)
        self.assertAlmostEqual(mijk.ki, -0.15519675289581672)
        self.assertAlmostEqual(mijk.ij, 0.12832006020245673)
        self.assertAlmostEqual(mijk.jj, -0.058726644927620980)
        self.assertAlmostEqual(mijk.kj, -1.0887444167267328)
        self.assertAlmostEqual(mijk.ik, -0.4161468365471424)
        self.assertAlmostEqual(mijk.jk, -0.9092974268256817)
        self.assertAlmostEqual(mijk.kk, 0)
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
        self.assertAlmostEqual(cartesianVelocity.k, -1.325444263372824)
        s2cj.getInverseTransformation(spherical, mijk)
        sphericalVelocity = s2cj.mxv(mijk, cartesianVelocity)
        self.assertAlmostEqual(sphericalVelocity.r, 1)
        self.assertAlmostEqual(sphericalVelocity.theta, 1)
        self.assertAlmostEqual(sphericalVelocity.phi, 1)


if __name__ == '__main__':
    unittest.main()
