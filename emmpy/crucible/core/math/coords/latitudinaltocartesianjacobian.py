"""Jacobian for latitudinal-Cartesian transformation."""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.latitudinalvector import LatitudinalVector
from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class LatitudinalToCartesianJacobian(Transformation):
    """Jacobian for latitudinal-Cartesian transformation."""

    def __init__(self):
        """Build a new object."""

    def getTransformation(self, coordPosition, buffer):
        """Get the transformation.

        From SPICE's routine in drdlat.f:

        JACOBI (DX,DR) = DCOS( LONG ) * DCOS( LAT )
        JACOBI (DY,DR) = DSIN( LONG ) * DCOS( LAT )
        JACOBI (DZ,DR) = DSIN( LAT )
        JACOBI (DX,DLON) = -R * DSIN( LONG ) * DCOS( LAT )
        JACOBI (DY,DLON) = R * DCOS( LONG ) * DCOS( LAT )
        JACOBI (DZ,DLON) = 0.0D0
        JACOBI (DX,DLAT) = -R * DCOS( LONG ) * DSIN( LAT )
        JACOBI (DY,DLAT) = -R * DSIN( LONG ) * DSIN( LAT )
        JACOBI (DZ,DLAT) = R * DCOS( LAT )
        """
        r = coordPosition.getRadius()
        lat = coordPosition.getLatitude()
        lon = coordPosition.getLongitude()
        cosLat = cos(lat)
        sinLat = sin(lat)
        cosLong = cos(lon)
        sinLong = sin(lon)
        xByR = cosLong*cosLat
        yByR = sinLong*cosLat
        zByR = sinLat
        xByLat = -r*cosLong*sinLat
        yByLat = -r*sinLong*sinLat
        zByLat = r*cosLat
        xByLong = -r*sinLong*cosLat
        yByLong = r*cosLong*cosLat
        zByLong = 0
        buffer[:, :] = [[xByR, xByLat, xByLong],
                        [yByR, yByLat, yByLong],
                        [zByR, zByLat, zByLong]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Get the inverse transformation."""
        try:
            self.getTransformation(coordPosition, buffer)
            buffer[:] = np.linalg.inv(buffer)
            return buffer
        except Exception as e:
            raise PointOnAxisException(e)

    def mxv(self, *args):
        """Multiply a vector by the Jacobian."""
        if isinstance(args[1], LatitudinalVector):
            (jacobian, coordVelocity) = args
            vect = VectorIJK()
            vect[:] = jacobian.dot(coordVelocity.getVectorIJK())
            return vect
        else:
            (inverseJacobian, cartVelocity) = args
            vect = VectorIJK()
            vect[:] = inverseJacobian.dot(cartVelocity)
            return LatitudinalVector(vect.i, vect.j, vect.k)
