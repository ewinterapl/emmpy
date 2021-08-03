import unittest

from emmpy.crucible.core.math.coords.polartocartesianjacobian import (
    PolarToCartesianJacobian
)
from emmpy.crucible.core.math.coords.polarvector import (
    PolarVector
)
from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        PolarToCartesianJacobian()

    def test_getTransformation(self):
        p2cj = PolarToCartesianJacobian()
        polarv = PolarVector(1, 2)
        buffer = MatrixIJ()
        b = p2cj.getTransformation(polarv, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(b.ii, -0.4161468365471424)
        self.assertAlmostEqual(b.ji, 0.9092974268256817)
        self.assertAlmostEqual(b.ij, -0.9092974268256817)
        self.assertAlmostEqual(b.jj, -0.4161468365471424)

    def test_getInverseTransformation(self):
        p2cj = PolarToCartesianJacobian()
        polarv = PolarVector(1, 2)
        buffer = MatrixIJ()
        b = p2cj.getInverseTransformation(polarv, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(b.ii, -0.4161468365471424)
        self.assertAlmostEqual(b.ji, -0.9092974268256817)
        self.assertAlmostEqual(b.ij, 0.9092974268256817)
        self.assertAlmostEqual(b.jj, -0.4161468365471424)

    def test_mxv(self):
        p2cj = PolarToCartesianJacobian()
        pv = PolarVector(1, 2)
        mij = MatrixIJ()
        p2cj.getTransformation(pv, mij)
        polarVelocity = PolarVector(1, 1)
        cartesianVelocity = p2cj.mxv(mij, polarVelocity)
        self.assertAlmostEqual(cartesianVelocity.i, -1.325444263372824)
        self.assertAlmostEqual(cartesianVelocity.j, 0.4931505902785393)
        p2cj.getInverseTransformation(pv, mij)
        polarVelocity = p2cj.mxv(mij, cartesianVelocity)
        self.assertAlmostEqual(polarVelocity.getI(), 1)
        self.assertAlmostEqual(polarVelocity.getJ(), 1)


if __name__ == '__main__':
    unittest.main()
