from math import cos, sin
import unittest


from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablematrixijk import (
    UnwritableMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablerotationmatrixijk import (
    UnwritableRotationMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class TestRotationMatrixIJK(unittest.TestCase):

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
        m = UnwritableMatrixIJK(cos(a), 0, sin(a),
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
        v1 = UnwritableVectorIJK(cos(a), 0, sin(a))
        v2 = UnwritableVectorIJK(0, 1, 0)
        v3 = UnwritableVectorIJK(-sin(a), 0, cos(a))
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
        m = UnwritableMatrixIJK(cos(a)/2, 0, sin(a)/2,
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
        v1 = UnwritableVectorIJK(cos(a)/2, 0, sin(a)/2)
        v2 = UnwritableVectorIJK(0, 1/3, 0)
        v3 = UnwritableVectorIJK(-sin(a)/4, 0, cos(a)/4)
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

    def test_createSharpened(self):
        a = 1
        m = RotationMatrixIJK(cos(a), 0, sin(a),
                              0, 1, 0,
                              -sin(a), 0, cos(a))
        m2 = m.createSharpened()
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))

    def test_createTranspose(self):
        a = 1
        m = RotationMatrixIJK(cos(a), 0, sin(a),
                              0, 1, 0,
                              -sin(a), 0, cos(a))
        m2 = m.createTranspose()
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, -sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))

    def test_createInverse(self):
        a = 1
        m = RotationMatrixIJK(cos(a), 0, sin(a),
                              0, 1, 0,
                              -sin(a), 0, cos(a))
        m2 = m.createInverse()
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, -sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))

    def test_sharpen(self):
        a = 1
        m = RotationMatrixIJK(cos(a), 0, sin(a),
                              0, 1, 0,
                              -sin(a), 0, cos(a))
        m.sharpen()
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, -sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))

    def test_transpose(self):
        a = 1
        m = RotationMatrixIJK(cos(a), 0, sin(a),
                              0, 1, 0,
                              -sin(a), 0, cos(a))
        m.transpose()
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, -sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))

    def test_setTo(self):
        a = 1
        # 1 2-D list arg
        m = RotationMatrixIJK()
        m.setTo([[cos(a), 0, -sin(a), 99],
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
        # 1 UnwritbleRotationMatrixIJK arg
        m = UnwritableRotationMatrixIJK(
            cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
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
        m = UnwritableMatrixIJK(
            cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
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
        # 3 args: all vectors
        v1 = UnwritableVectorIJK(cos(a), 0, sin(a))
        v2 = UnwritableVectorIJK(0, 1, 0)
        v3 = UnwritableVectorIJK(-sin(a), 0, cos(a))
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
        # 6 args: 3 x (scale, vector)
        v1 = UnwritableVectorIJK(cos(a)/2, 0, sin(a)/2)
        v2 = UnwritableVectorIJK(0, 1/3, 0)
        v3 = UnwritableVectorIJK(-sin(a)/4, 0, cos(a)/4)
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
        m = RotationMatrixIJK()
        m.setTo(cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        self.assertAlmostEqual(m.ii, cos(a))
        self.assertAlmostEqual(m.ji, 0)
        self.assertAlmostEqual(m.ki, sin(a))
        self.assertAlmostEqual(m.ij, 0)
        self.assertAlmostEqual(m.jj, 1)
        self.assertAlmostEqual(m.kj, 0)
        self.assertAlmostEqual(m.ik, -sin(a))
        self.assertAlmostEqual(m.jk, 0)
        self.assertAlmostEqual(m.kk, cos(a))

    def test_setToSharpened(self):
        a = 1
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
                                        0, 1, 0,
                                        -sin(a), 0, cos(a))
        m2 = RotationMatrixIJK()
        m2.setToSharpened(m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))
        a = 2
        m = UnwritableMatrixIJK(cos(a), 0, sin(a),
                                0, 1, 0,
                                -sin(a), 0, cos(a))
        m2 = RotationMatrixIJK()
        m2.setToSharpened(m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))

    def setToTransposed(self):
        a = 1
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
                                        0, 1, 0,
                                        -sin(a), 0, cos(a))
        m2 = RotationMatrixIJK()
        m2.setToTranspose(m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, -sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))
        a = 2
        m = UnwritableMatrixIJK(cos(a), 0, sin(a),
                                0, 1, 0,
                                -sin(a), 0, cos(a))
        m2 = RotationMatrixIJK()
        m2.setToTranspose(m)
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, -sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))

    def test_mxmt(self):
        a = 1
        m1 = RotationMatrixIJK(cos(a), 0, sin(a),
                               0, 1, 0,
                               -sin(a), 0, cos(a))
        b = 2
        m2 = UnwritableRotationMatrixIJK(cos(b), 0, sin(b),
                                         0, 1, 0,
                                         -sin(b), 0, cos(b))
        m3 = RotationMatrixIJK.mxmt(m1, m2)
        # | cos(a) 0 -sin(a) | | cos(b) 0 -sin(b) |T
        # |    0   1     0   |*|    0   1     0   | =
        # | sin(a) 0  cos(a) | | sin(b) 0  cos(b) |
        #
        # | cos(a) 0 -sin(a) | | cos(b) 0  sin(b) |
        # |    0   1     0   |*|    0   1     0   |
        # | sin(a) 0  cos(a) | |-sin(b) 0  cos(b) |
        self.assertAlmostEqual(m3.ii, cos(a)*cos(b) + sin(a)*sin(b))
        self.assertAlmostEqual(m3.ji, 0)
        self.assertAlmostEqual(m3.ki, sin(a)*cos(b) - cos(a)*sin(b))
        self.assertAlmostEqual(m3.ij, 0)
        self.assertAlmostEqual(m3.jj, 1)
        self.assertAlmostEqual(m3.kj, 0)
        self.assertAlmostEqual(m3.ik, cos(a)*sin(b) - sin(a)*cos(b))
        self.assertAlmostEqual(m3.jk, 0)
        self.assertAlmostEqual(m3.kk, sin(a)*sin(b) + cos(a)*cos(b))

    def test_mtxm(self):
        a = 1
        m1 = RotationMatrixIJK(cos(a), 0, sin(a),
                               0, 1, 0,
                               -sin(a), 0, cos(a))
        b = 2
        m2 = UnwritableRotationMatrixIJK(cos(b), 0, sin(b),
                                         0, 1, 0,
                                         -sin(b), 0, cos(b))
        m3 = RotationMatrixIJK.mtxm(m1, m2)
        # | cos(a) 0 -sin(a) |T| cos(b) 0 -sin(b) |
        # |    0   1     0   |*|    0   1     0   | =
        # | sin(a) 0  cos(a) | | sin(b) 0  cos(b) |
        #
        # | cos(a) 0  sin(a) | | cos(b) 0 -sin(b) |
        # |    0   1     0   |*|    0   1     0   |
        # |-sin(a) 0  cos(a) | | sin(b) 0  cos(b) |
        self.assertAlmostEqual(m3.ii, cos(a)*cos(b) + sin(a)*sin(b))
        self.assertAlmostEqual(m3.ji, 0)
        self.assertAlmostEqual(m3.ki, -sin(a)*cos(b) + cos(a)*sin(b))
        self.assertAlmostEqual(m3.ij, 0)
        self.assertAlmostEqual(m3.jj, 1)
        self.assertAlmostEqual(m3.kj, 0)
        self.assertAlmostEqual(m3.ik, -cos(a)*sin(b) + sin(a)*cos(b))
        self.assertAlmostEqual(m3.jk, 0)
        self.assertAlmostEqual(m3.kk, sin(a)*sin(b) + cos(a)*cos(b))

    def test_mxm(self):
        a = 1
        m1 = RotationMatrixIJK(cos(a), 0, sin(a),
                               0, 1, 0,
                               -sin(a), 0, cos(a))
        b = 2
        m2 = UnwritableRotationMatrixIJK(cos(b), 0, sin(b),
                                         0, 1, 0,
                                         -sin(b), 0, cos(b))
        m3 = RotationMatrixIJK.mxm(m1, m2)
        # | cos(a) 0 -sin(a) | | cos(b) 0 -sin(b) |
        # |    0   1     0   |*|    0   1     0   |
        # | sin(a) 0  cos(a) | | sin(b) 0  cos(b) |
        self.assertAlmostEqual(m3.ii, cos(a)*cos(b) - sin(a)*sin(b))
        self.assertAlmostEqual(m3.ji, 0)
        self.assertAlmostEqual(m3.ki, sin(a)*cos(b) + cos(a)*sin(b))
        self.assertAlmostEqual(m3.ij, 0)
        self.assertAlmostEqual(m3.jj, 1)
        self.assertAlmostEqual(m3.kj, 0)
        self.assertAlmostEqual(m3.ik, -cos(a)*sin(b) - sin(a)*cos(b))
        self.assertAlmostEqual(m3.jk, 0)
        self.assertAlmostEqual(m3.kk, -sin(a)*sin(b) + cos(a)*cos(b))

    def test_static_createSharpened(self):
        a = 1
        m2 = RotationMatrixIJK.static_createSharpened(
            cos(a), 0, sin(a), 0, 1, 0, -sin(a), 0, cos(a))
        self.assertAlmostEqual(m2.ii, cos(a))
        self.assertAlmostEqual(m2.ji, 0)
        self.assertAlmostEqual(m2.ki, sin(a))
        self.assertAlmostEqual(m2.ij, 0)
        self.assertAlmostEqual(m2.jj, 1)
        self.assertAlmostEqual(m2.kj, 0)
        self.assertAlmostEqual(m2.ik, -sin(a))
        self.assertAlmostEqual(m2.jk, 0)
        self.assertAlmostEqual(m2.kk, cos(a))


if __name__ == '__main__':
    unittest.main()
