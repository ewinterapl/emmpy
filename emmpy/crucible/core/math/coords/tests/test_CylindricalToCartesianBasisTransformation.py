import unittest

from emmpy.crucible.core.math.coords.cylindricaltocartesianbasistransformation import (
    CylindricalToCartesianBasisTransformation
)
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
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
        self.assertAlmostEqual(buffer.ii, -0.4161468365471424)
        self.assertAlmostEqual(buffer.ji, 0.9092974268256817)
        self.assertAlmostEqual(buffer.ki, 0)
        self.assertAlmostEqual(buffer.ij, -0.9092974268256817)
        self.assertAlmostEqual(buffer.jj, -0.4161468365471424)
        self.assertAlmostEqual(buffer.kj, 0)
        self.assertAlmostEqual(buffer.ik, 0)
        self.assertAlmostEqual(buffer.jk, 0)
        self.assertAlmostEqual(buffer.kk, 1)

    def test_getInverseTransformation(self):
        c2cbt = CylindricalToCartesianBasisTransformation()
        cyl = CylindricalVector(1, 2, 3)
        buffer = MatrixIJK()
        b = c2cbt.getInverseTransformation(cyl, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(buffer.ii, -0.4161468365471424)
        self.assertAlmostEqual(buffer.ji, -0.9092974268256817)
        self.assertAlmostEqual(buffer.ki, 0)
        self.assertAlmostEqual(buffer.ij, 0.9092974268256817)
        self.assertAlmostEqual(buffer.jj, -0.4161468365471424)
        self.assertAlmostEqual(buffer.kj, 0)
        self.assertAlmostEqual(buffer.ik, 0)
        self.assertAlmostEqual(buffer.jk, 0)
        self.assertAlmostEqual(buffer.kk, 1)

    def test_mxv(self):
        c2cbt = CylindricalToCartesianBasisTransformation()
        jacobian = MatrixIJK(
            -0.4161468365471424, 0.9092974268256817, 0,
            -0.9092974268256817, -0.4161468365471424, 0,
            0, 0, 1
        )
        cyl = CylindricalVector(1, 2, 3)
        v = c2cbt.mxv(jacobian, cyl)
        self.assertAlmostEqual(v.i, -2.234741690198506)
        self.assertAlmostEqual(v.j, 0.0770037537313969)
        self.assertAlmostEqual(v.k, 3)


if __name__ == '__main__':
    unittest.main()
