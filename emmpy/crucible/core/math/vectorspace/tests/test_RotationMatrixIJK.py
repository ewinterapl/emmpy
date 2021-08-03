from math import cos, sin
import unittest


from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        a = 1
        # 0 args
        m = RotationMatrixIJK()
        self.assertAlmostEqual(m.ii, 1)
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, 0)
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, 0)
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, 1)
        # 1 2-D list arg
        m = RotationMatrixIJK([[cos(a), 0, -sin(a), 99],
                               [0, 1, 0, 99],
                               [sin(a), 0, cos(a), 99],
                               [99, 99, 99, 99]])
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, -sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))
        # 1 RotationMatrixIJK arg
        m2 = RotationMatrixIJK(m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))
        # 1 UnwritbleMatrixIJK arg
        a = 2
        m = MatrixIJK(cos(a), 0, sin(a),
                                0, 1, 0,
                                -sin(a), 0, cos(a))
        m2 = RotationMatrixIJK(m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))
        # 2 args: scale and matrix
        m = RotationMatrixIJK(cos(a), 0, sin(a),
                              0, 1, 0,
                              -sin(a), 0, cos(a))
        m2 = RotationMatrixIJK(1, m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))
        # 3 args: all vectors
        v1 = VectorIJK(cos(a), 0, sin(a))
        v2 = VectorIJK(0, 1, 0)
        v3 = VectorIJK(-sin(a), 0, cos(a))
        m = RotationMatrixIJK(v1, v2, v3)
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, -sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))
        # 4 args: 3 scale factors, matrix
        m = MatrixIJK(cos(a)/2, 0, sin(a)/2,
                                0, 1/3, 0,
                                -sin(a)/4, 0, cos(a)/4)
        m2 = RotationMatrixIJK(2, 3, 4, m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))
        # 6 args: 3 x (scale, vector)
        v1 = VectorIJK(cos(a)/2, 0, sin(a)/2)
        v2 = VectorIJK(0, 1/3, 0)
        v3 = VectorIJK(-sin(a)/4, 0, cos(a)/4)
        m = RotationMatrixIJK(2, v1, 3, v2, 4, v3)
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, -sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))
        # 9 args
        m = RotationMatrixIJK(cos(a), 0, sin(a),
                              0, 1, 0,
                              -sin(a), 0, cos(a))
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, -sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))


if __name__ == '__main__':
    unittest.main()
