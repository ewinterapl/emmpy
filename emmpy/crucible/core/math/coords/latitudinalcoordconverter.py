"""Convert between latitudinal and cartesian coordinates."""


from math import atan2, cos, sin, sqrt

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)
from emmpy.crucible.core.math.coords.latitudinaltocartesianjacobian import (
    LatitudinalToCartesianJacobian
)
from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class LatitudinalCoordConverter(AbstractCoordConverter):
    """Convert between latitudinal and cartesian coordinates."""

    JACOBIAN = LatitudinalToCartesianJacobian()

    def __init__(self):
        """Build a new object."""
        AbstractCoordConverter.__init__(
            self, LatitudinalCoordConverter.JACOBIAN
        )

    def toCoordinate(self, cartesian):
        """From the SPICE routine reclat.f.

        BIG = MAX ( DABS(RECTAN(1)), DABS(RECTAN(2)), DABS(RECTAN(3)) )
        IF ( BIG .GT. 0 ) THEN
          X = RECTAN(1) / BIG Y = RECTAN(2) / BIG Z = RECTAN(3) / BIG
          RADIUS = BIG * DSQRT (X*X + Y*Y + Z*Z)
          LAT = DATAN2 ( Z, DSQRT(X*X + Y*Y) )
          X = RECTAN(1) Y = RECTAN(2)
          IF (X.EQ.0.D0 .AND. Y.EQ.0.D0) THEN LONG = 0.D0
          ELSE LONG=DATAN2(Y,X)
          END IF
        ELSE RADIUS = 0.0D0 LAT = 0.D0 LONG = 0.D0 END IF
        """
        x = cartesian.i
        y = cartesian.getJ()
        z = cartesian.getK()
        radius = 0
        latitude = 0
        longitude = 0
        big = max(abs(x), abs(y), abs(z))
        if big > 0:
            x /= big
            y /= big
            z /= big
            radius = big*sqrt(x*x + y*y + z*z)
            latitude = atan2(z, sqrt(x*x + y*y))
            x = cartesian.i
            y = cartesian.getJ()
            if x == 0 and y == 0:
                longitude = 0
            else:
                longitude = atan2(y, x)
        else:
            radius = 0
            latitude = 0
            longitude = 0
        return LatitudinalVector(radius, latitude, longitude)

    def toCartesian(self, coordinate):
        """From the SPICE routine latrec.f.

        X = RADIUS * DCOS(LONG) * DCOS(LAT)
        Y = RADIUS * DSIN(LONG) * DCOS(LAT)
        Z = RADIUS * DSIN(LAT)
        """
        i = (
            coordinate.getRadius()*cos(coordinate.getLongitude()) *
            cos(coordinate.getLatitude())
        )
        j = (
            coordinate.getRadius()*sin(coordinate.getLongitude()) *
            cos(coordinate.getLatitude())
        )
        k = coordinate.getRadius()*sin(coordinate.getLatitude())
        return VectorIJK(i, j, k)
