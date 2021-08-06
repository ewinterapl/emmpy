"""Jacobian for spherical to Cartesian transformations."""


from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class SphericalToCartesianJacobian(Transformation):
    """Jacobian for spherical to Cartesian transformations."""

    def __init__(self):
        """Build a new object."""

    def getTransformation(self, coordPosition, buffer):
        """Get the transformation matrix.

        from SPICE's routine in drdsph.f:

        CCOLAT = DCOS(COLAT)
        SCOLAT = DSIN(COLAT)
        CLONG = DCOS(LONG)
        SLONG = DSIN(LONG)
        JACOBI(DX, DR) = CLONG*SCOLAT
        JACOBI(DY, DR) = SLONG*SCOLAT
        JACOBI(DZ, DR) = CCOLAT
        JACOBI(DX, DCOLAT) = R*CLONG*CCOLAT
        JACOBI(DY, DCOLAT) = R*SLONG*CCOLAT
        JACOBI(DZ, DCOLAT) = -R*SCOLAT
        JACOBI(DX, DLON) = -R*SLONG*SCOLAT
        JACOBI(DY, DLON) = R*CLONG*SCOLAT
        JACOBI(DZ, DLON) = 0.0D0
        """
        r = coordPosition.r
        colat = coordPosition.theta
        lon = coordPosition.phi
        cosColat = cos(colat)
        sinColat = sin(colat)
        cosLong = cos(lon)
        sinLong = sin(lon)
        xByR = cosLong*sinColat
        yByR = sinLong*sinColat
        zByR = cosColat
        xByColat = r*cosLong*cosColat
        yByColat = r*sinLong*cosColat
        zByColat = -r*sinColat
        xByLong = -r*sinLong*sinColat
        yByLong = r*cosLong*sinColat
        zByLong = 0
        buffer[:, :] = [[xByR, xByColat, xByLong],
                        [yByR, yByColat, yByLong],
                        [zByR, zByColat, zByLong]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Get the inverse transformation matrix."""
        try:
            self.getTransformation(coordPosition, buffer)
            buffer[:] = np.linalg.inv(buffer)
            return buffer
        except Exception as e:
            raise PointOnAxisException(e)

    def mxv(self, *args):
        """Multiply a vector by the Jacobian matrix."""
        if isinstance(args[1], SphericalVector):
            (jacobian, coordVelocity) = args
            vect = VectorIJK()
            vect[:] = jacobian.dot(coordVelocity)
            return vect
        else:
            (inverseJacobian, cartVelocity) = args
            vect = VectorIJK()
            vect[:] = inverseJacobian.dot(cartVelocity)
            return SphericalVector(vect.i, vect.j, vect.k)
