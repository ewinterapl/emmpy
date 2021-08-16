"""Basis transformation from spherical to Cartesian."""


from math import cos, sin
from re import T

import numpy as np

from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class SphericalToCartesianBasisTransformation(Transformation):
    """Basis transformation from spherical to Cartesian."""

    def __init__(self):
        """Build a new object."""

    def getTransformation(self, coordPosition, buffer):
        """Get the transformation matrix."""
        colat = coordPosition.theta
        lon = coordPosition.phi
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
        buffer[:, :] = [[xByR, xByColat, xByLong],
                        [yByR, yByColat, yByLong],
                        [zByR, zByColat, zByLong]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Get the inverse transformation matrix."""
        # I'm pretty confident that this exception can't be thrown, the columns
        # will always be non-zero
        self.getTransformation(coordPosition, buffer)
        buffer[:] = np.linalg.inv(buffer)
        return buffer

    def mxv(self, *args):
        """Multiply a vector by the transformation matrix."""
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
