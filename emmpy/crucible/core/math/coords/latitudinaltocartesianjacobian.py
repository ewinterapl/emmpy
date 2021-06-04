"""emmpy.crucible.core.math.coords.latitudinaltocartesianjacobian"""


from math import cos, sin

from emmpy.crucible.core.math.coords.latitudinalvector import LatitudinalVector
from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class LatitudinalToCartesianJacobian(Transformation):
    """LatitudinalToCartesianJacobian"""

    def __init__(self):
        """Constructor"""
        pass

    def getTransformation(self, coordPosition, buffer):
        """from SPICE's routine in drdlat.f:

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
        return buffer.setTo(
            xByR, yByR, zByR,
            xByLat, yByLat, zByLat,
            xByLong, yByLong, zByLong
        )

    def getInverseTransformation(self, coordPosition, buffer):
        try:
            return self.getTransformation(coordPosition, buffer).invort()
        except Exception as e:
            raise PointOnAxisException(e)

    def mxv(self, *args):
        if isinstance(args[1], LatitudinalVector):
            (jacobian, coordVelocity) = args
            return MatrixIJK.mxv(jacobian, coordVelocity.getVectorIJK())
        else:
            (inverseJacobian, cartVelocity) = args
            vect = MatrixIJK.mxv(inverseJacobian, cartVelocity)
            return LatitudinalVector(vect.getI(), vect.getJ(), vect.getK())
