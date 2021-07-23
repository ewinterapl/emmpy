"""Jacobian for polar-Cartesian conversions."""


from math import cos, sin

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.polarvector import PolarVector
from emmpy.crucible.core.math.coords.transformationij import TransformationIJ
from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ


class PolarToCartesianJacobian(TransformationIJ):
    """Jacobian for polar-Cartesian conversions."""

    def __init__(self):
        """Jacobian for polar-Cartesian conversions."""

    def getTransformation(self, coordPosition, buffer):
        """Return the transformation matrix."""
        r = coordPosition.getRadius()
        angle = coordPosition.getAngle()
        cosAngle = cos(angle)
        sinAngle = sin(angle)
        return buffer.setTo(cosAngle, sinAngle, -r*sinAngle, r*cosAngle)

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the inverse transformation matrix."""
        try:
            return self.getTransformation(coordPosition, buffer).invort()
        except Exception as e:
            raise PointOnAxisException(e)

    def mxv(self, *args):
        """Multiply a vector by the Jacobian."""
        if isinstance(args[1], PolarVector):
            (jacobian, coordVelocity) = args
            return MatrixIJ.mxv(jacobian, coordVelocity.getVectorIJ())
        else:
            (inverseJacobian, cartVelocity) = args
            vect = MatrixIJ.mxv(inverseJacobian, cartVelocity)
            return PolarVector(vect.i, vect.j)
