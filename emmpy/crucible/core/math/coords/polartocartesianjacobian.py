"""emmpy.crucible.core.math.coords.polartocartesianjacobian"""


# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.sin;
# import crucible.core.math.vectorspace.MatrixIJ;
# import crucible.core.math.vectorspace.UnwritableMatrixIJ;
# import crucible.core.math.vectorspace.UnwritableVectorIJ;
from math import cos, sin

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.polarvector import PolarVector
from emmpy.crucible.core.math.coords.transformationij import TransformationIJ
from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ


class PolarToCartesianJacobian(TransformationIJ):

    def __init__(self):
        """Constructor"""
        pass

    def getTransformation(self, coordPosition, buffer):
        """getTransformation"""
        r = coordPosition.getRadius()
        angle = coordPosition.getAngle()
        cosAngle = cos(angle)
        sinAngle = sin(angle)
        return buffer.setTo(cosAngle, sinAngle, -r*sinAngle, r*cosAngle)

    def getInverseTransformation(self, coordPosition, buffer):
        try:
            return self.getTransformation(coordPosition, buffer).invort()
        except Exception as e:
            raise PointOnAxisException(e)

    def mxv(self, *args):
        if isinstance(args[1], PolarVector):
            (jacobian, coordVelocity) = args
            return MatrixIJ.mxv(jacobian, coordVelocity.getVectorIJ())
        else:
            (inverseJacobian, cartVelocity) = args
            vect = MatrixIJ.mxv(inverseJacobian, cartVelocity)
            return PolarVector(vect.getI(), vect.getJ())
