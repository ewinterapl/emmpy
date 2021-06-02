from math import cos, sin
import unittest


from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
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


class TestBuilder(unittest.TestCase):

    def test_checkRotation(self):
        a = 1
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
                                        0, 1, 0,
                                        -sin(a), 0, cos(a))
        self.assertIsNone(UnwritableRotationMatrixIJK.checkRotation(m))
        m = UnwritableMatrixIJK(1, 2, 3, 4, 5, 6, 7, 8, 9)
        with self.assertRaises(MalformedRotationException):
            UnwritableRotationMatrixIJK.checkRotation(m)

    def test___init__(self):
        a = 1
        # 0 args
        m = UnwritableRotationMatrixIJK()
        # 1 2-D list arg
        m = UnwritableRotationMatrixIJK([[cos(a), 0, -sin(a), 99],
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
        # 1 UnwritbleRotationMatrixIJK arg
        m2 = UnwritableRotationMatrixIJK(m)
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
        m2 = UnwritableRotationMatrixIJK(m)
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
        m = UnwritableMatrixIJK(cos(a)/2, 0, sin(a)/2,
                                0, 1/2, 0,
                                -sin(a)/2, 0, cos(a)/2)
        m2 = UnwritableRotationMatrixIJK(2.0, m)
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
        m = UnwritableRotationMatrixIJK(v1, v2, v3)
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
        m2 = UnwritableRotationMatrixIJK(2, 3, 4, m)
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
        m = UnwritableRotationMatrixIJK(2, v1, 3, v2, 4, v3)
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
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
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
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
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
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
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
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
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

    def test_copyOf(self):
        a = 1
        m = UnwritableRotationMatrixIJK(cos(a), 0, sin(a),
                                        0, 1, 0,
                                        -sin(a), 0, cos(a))
        m2 = UnwritableRotationMatrixIJK.copyOf(m)
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
