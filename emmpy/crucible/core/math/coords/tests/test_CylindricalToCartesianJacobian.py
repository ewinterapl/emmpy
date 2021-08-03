from math import cos, sin
import unittest

from emmpy.crucible.core.math.coords.cylindricaltocartesianjacobian import (
    CylindricalToCartesianJacobian
)
from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        CylindricalToCartesianJacobian()

    def test_getTransformation(self):
        c2cj = CylindricalToCartesianJacobian()
        r = 1.0
        lon = 2.0
        z = 3.0
        cv = CylindricalVector(r, lon, z)
        mijk = MatrixIJK()
        c2cj.getTransformation(cv, mijk)
        self.assertAlmostEqual(mijk.getII(), cos(lon))
        self.assertAlmostEqual(mijk.getJI(), sin(lon))
        self.assertAlmostEqual(mijk.getKI(), 0)
        self.assertAlmostEqual(mijk.getIJ(), -r*sin(lon))
        self.assertAlmostEqual(mijk.getJJ(), r*cos(lon))
        self.assertAlmostEqual(mijk.getKJ(), 0)
        self.assertAlmostEqual(mijk.getIK(), 0)
        self.assertAlmostEqual(mijk.getJK(), 0)
        self.assertAlmostEqual(mijk.kk, 1)

    def test_getInverseTransformation(self):
        c2cj = CylindricalToCartesianJacobian()
        r = 1.0
        lon = 2.0
        z = 3.0
        cv = CylindricalVector(r, lon, z)
        mijk = MatrixIJK()
        c2cj.getInverseTransformation(cv, mijk)
        self.assertAlmostEqual(mijk.getII(), cos(lon))
        self.assertAlmostEqual(mijk.getJI(), -r*sin(lon))
        self.assertAlmostEqual(mijk.getKI(), 0)
        self.assertAlmostEqual(mijk.getIJ(), sin(lon))
        self.assertAlmostEqual(mijk.getJJ(), r*cos(lon))
        self.assertAlmostEqual(mijk.getKJ(), 0)
        self.assertAlmostEqual(mijk.getIK(), 0)
        self.assertAlmostEqual(mijk.getJK(), 0)
        self.assertAlmostEqual(mijk.kk, 1)
        cv0 = CylindricalVector(0, 0, 0)
        with self.assertRaises(PointOnAxisException):
            c2cj.getInverseTransformation(cv0, mijk)

    def test_mxv(self):
        c2cj = CylindricalToCartesianJacobian()
        r = 1.0
        lon = 2.0
        z = 3.0
        cv1 = CylindricalVector(r, lon, z)
        mijk = MatrixIJK()
        c2cj.getTransformation(cv1, mijk)
        cylindricalVelocity = CylindricalVector(1, 1, 1)
        cartesianVelocity = c2cj.mxv(mijk, cylindricalVelocity)
        self.assertAlmostEqual(cartesianVelocity.i, -1.325444263372824)
        self.assertAlmostEqual(cartesianVelocity.j, 0.4931505902785393)
        self.assertAlmostEqual(cartesianVelocity.k, 1)
        c2cj.getInverseTransformation(cv1, mijk)
        cylindricalVelocity = c2cj.mxv(mijk, cartesianVelocity)
        self.assertAlmostEqual(cylindricalVelocity.getI(), 1)
        self.assertAlmostEqual(cylindricalVelocity.getJ(), 1)
        self.assertAlmostEqual(cylindricalVelocity.getK(), 1)
        with self.assertRaises(Exception):
            c2cj.mxv(mijk, [])


if __name__ == '__main__':
    unittest.main()
