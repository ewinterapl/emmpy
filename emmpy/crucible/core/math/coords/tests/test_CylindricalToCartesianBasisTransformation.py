import unittest

from emmpy.crucible.core.math.coords.cylindricaltocartesianbasistransformation import (
    CylindricalToCartesianBasisTransformation
)
from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        c2cbt = CylindricalToCartesianBasisTransformation()
        self.assertIsNotNone(c2cbt)

    def test_getTransformation(self):
        c2cbt = CylindricalToCartesianBasisTransformation()
        cyl = CylindricalVector(1, 2, 3)
        buffer = MatrixIJK()
        b = c2cbt.getTransformation(cyl, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(buffer.getII(), -0.4161468365471424)
        self.assertAlmostEqual(buffer.getJI(), 0.9092974268256817)
        self.assertAlmostEqual(buffer.getKI(), 0)
        self.assertAlmostEqual(buffer.getIJ(), -0.9092974268256817)
        self.assertAlmostEqual(buffer.getJJ(), -0.4161468365471424)
        self.assertAlmostEqual(buffer.getKJ(), 0)
        self.assertAlmostEqual(buffer.getIK(), 0)
        self.assertAlmostEqual(buffer.getJK(), 0)
        self.assertAlmostEqual(buffer.getKK(), 1)

    def test_getInverseTransformation(self):
        c2cbt = CylindricalToCartesianBasisTransformation()
        cyl = CylindricalVector(1, 2, 3)
        buffer = MatrixIJK()
        b = c2cbt.getInverseTransformation(cyl, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(buffer.getII(), -0.4161468365471424)
        self.assertAlmostEqual(buffer.getJI(), -0.9092974268256817)
        self.assertAlmostEqual(buffer.getKI(), 0)
        self.assertAlmostEqual(buffer.getIJ(), 0.9092974268256817)
        self.assertAlmostEqual(buffer.getJJ(), -0.4161468365471424)
        self.assertAlmostEqual(buffer.getKJ(), 0)
        self.assertAlmostEqual(buffer.getIK(), 0)
        self.assertAlmostEqual(buffer.getJK(), 0)
        self.assertAlmostEqual(buffer.getKK(), 1)

    def test_mxv(self):
        c2cbt = CylindricalToCartesianBasisTransformation()
        jacobian = MatrixIJK(
            -0.4161468365471424, 0.9092974268256817, 0,
            -0.9092974268256817, -0.4161468365471424, 0,
            0, 0, 1
        )
        cyl = CylindricalVector(1, 2, 3)
        v = c2cbt.mxv(jacobian, cyl)
        self.assertAlmostEqual(v.getI(), -2.234741690198506)
        self.assertAlmostEqual(v.getJ(), 0.0770037537313969)
        self.assertAlmostEqual(v.getK(), 3)
        jacobianInverse = jacobian.createInverse()
        cartVelocity = VectorIJK(1, 2, 3)
        v = c2cbt.mxv(jacobianInverse, cartVelocity)
        self.assertAlmostEqual(v.getI(), 1.402448017104221)
        self.assertAlmostEqual(v.getJ(), -1.7415910999199666)
        self.assertAlmostEqual(v.getK(), 3)


if __name__ == '__main__':
    unittest.main()
