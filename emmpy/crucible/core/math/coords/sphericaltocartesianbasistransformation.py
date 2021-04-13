"""emmpy.crucible.core.math.coords.sphericaltocartesianbasistransformation"""


from math import cos, sin

from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class SphericalToCartesianBasisTransformation(Transformation):
    """SphericalToCartesianBasisTransformation"""

    def __init__(self):
        """Constructor"""
        pass

    def getTransformation(self, coordPosition, buffer):
        colat = coordPosition.getColatitude()
        lon = coordPosition.getLongitude()
        cosColat = cos(colat)
        sinColat = sin(colat)
        cosLong = cos(lon)
        sinLong = sin(lon)
        xByR = cosLong*sinColat
        yByR = sinLong*sinColat
        zByR = cosColat
        xByColat = cosLong*cosColat
        yByColat = sinLong*cosColat
        zByColat = -sinColat
        xByLong = -sinLong
        yByLong = cosLong
        zByLong = 0
        return buffer.setTo(
            xByR, yByR, zByR,
            xByColat, yByColat, zByColat,
            xByLong, yByLong, zByLong
        )

    def getInverseTransformation(self, coordPosition, buffer):
        # I'm pretty confident that this exception can't be thrown, the columns
        # will always be non-zero
        return self.getTransformation(coordPosition, buffer).invort()

    def mxv(self, *args):
        if isinstance(args[1], SphericalVector):
            (jacobian, coordVelocity) = args
            return MatrixIJK.mxv(jacobian, coordVelocity.getVectorIJK())
        else:
            (inverseJacobian, cartVelocity) = args
            vect = MatrixIJK.mxv(inverseJacobian, cartVelocity)
            return SphericalVector(vect.getI(), vect.getJ(), vect.getK())
