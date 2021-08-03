import unittest

from emmpy.crucible.core.math.coords.sphericaltocartesianbasistransformation import (
    SphericalToCartesianBasisTransformation
)
from emmpy.crucible.core.math.coords.sphericalvector import (
    SphericalVector
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        s2cbt = SphericalToCartesianBasisTransformation()
        self.assertIsNotNone(s2cbt)

    def test_getTransformation(self):
        s2cbt = SphericalToCartesianBasisTransformation()
        spherical = SphericalVector(1, 2, 3)
        buffer = MatrixIJK()
        b = s2cbt.getTransformation(spherical, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(buffer.ii, -0.9001976297355174)
        self.assertAlmostEqual(buffer.ji, 0.12832006020245673)
        self.assertAlmostEqual(buffer.ki, -0.4161468365471424)
        self.assertAlmostEqual(buffer.ij, 0.411982245665683)
        self.assertAlmostEqual(buffer.jj, -0.05872664492762098)
        self.assertAlmostEqual(buffer.kj, -0.9092974268256817)
        self.assertAlmostEqual(buffer.ik, -0.1411200080598672)
        self.assertAlmostEqual(buffer.jk, -0.9899924966004454)
        self.assertAlmostEqual(buffer.kk, 0)

    def test_getInverseTransformation(self):
        s2cbt = SphericalToCartesianBasisTransformation()
        spherical = SphericalVector(1, 2, 3)
        buffer = MatrixIJK()
        b = s2cbt.getInverseTransformation(spherical, buffer)
        self.assertIs(b, buffer)
        self.assertAlmostEqual(buffer.ii, -0.9001976297355174)
        self.assertAlmostEqual(buffer.ji, 0.411982245665683)
        self.assertAlmostEqual(buffer.ki, -0.14112000805986727)
        self.assertAlmostEqual(buffer.ij, 0.12832006020245673)
        self.assertAlmostEqual(buffer.jj, -0.05872664492762098)
        self.assertAlmostEqual(buffer.kj, -0.9899924966004456)
        self.assertAlmostEqual(buffer.ik, -0.4161468365471424)
        self.assertAlmostEqual(buffer.jk, -0.9092974268256817)
        self.assertAlmostEqual(buffer.kk, 0)

    def test_mxv(self):
        s2cbt = SphericalToCartesianBasisTransformation()
        jacobian = MatrixIJK(
            -0.4161468365471424, -0.9092974268256817, 0,
            0.9092974268256817, -0.4161468365471424, 0,
            0, 0, 1
        )
        spherical = SphericalVector(1, 2, 3)
        v = s2cbt.mxv(jacobian, spherical)
        self.assertAlmostEqual(v.i, 1.402448017104221)
        self.assertAlmostEqual(v.j, -1.7415910999199666)
        self.assertAlmostEqual(v.k, 3)


if __name__ == '__main__':
    unittest.main()
