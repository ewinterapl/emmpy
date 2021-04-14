"""emmpy.crucible.core.math.coords.cylindricaltocartesianbasistransformation"""


from math import cos, sin
from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class CylindricalToCartesianBasisTransformation(Transformation):
    """CylindricalToCartesianBasisTransformation"""

    def __init__(self):
        """Constructor"""
        pass

    def getTransformation(self, coordPosition, buffer):
        """getTransformation

        return
              .-                                  -.
              |  cos(long)  -sin(long)      0      |
              |                                    |
              |  sin(long)   cos(long)      0      |
              |                                    |
              |     0           0           1      |
              `-                                  -'
        """
        lon = coordPosition.getLongitude()
        cosLon = cos(lon)
        sinLon = sin(lon)
        j_DX_DR = cosLon
        j_DY_DR = sinLon
        j_DZ_DR = 0.0
        j_DX_DLON = -sinLon
        j_DY_DLON = cosLon
        j_DZ_DLON = 0.0
        j_DX_DZ = 0.0
        j_DY_DZ = 0.0
        j_DZ_DZ = 1.0
        return buffer.setTo(
            j_DX_DR, j_DY_DR, j_DZ_DR,
            j_DX_DLON, j_DY_DLON, j_DZ_DLON,
            j_DX_DZ, j_DY_DZ, j_DZ_DZ
        )

    def getInverseTransformation(self, coordPosition, buffer):
        return self.getTransformation(coordPosition, buffer).invort()

    def mxv(self, *args):
        if isinstance(args[1], CylindricalVector):
            (jacobian, coordValue) = args
            return jacobian.mxv(coordValue.getVectorIJK())
        else:
            (inverseTransformation, cartVelocity) = args
            vect = MatrixIJK.mxv(inverseTransformation, cartVelocity)
            return CylindricalVector(vect.getI(), vect.getJ(), vect.getK())
