"""Convert between spherical and Cartesian coordinates."""


from math import atan2, cos, sin, sqrt

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)
from emmpy.crucible.core.math.coords.sphericaltocartesianjacobian import (
    SphericalToCartesianJacobian
)
from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class SphericalCoordConverter(AbstractCoordConverter):
    """Convert between spherical and Cartesian coordinates."""

    JACOBIAN = SphericalToCartesianJacobian()

    def __init__(self):
        """Build a new object."""
        AbstractCoordConverter.__init__(self, SphericalCoordConverter.JACOBIAN)

    def toCoordinate(self, cartesian):
        """Convert Cartesian to spherical coordinates.

        From the SPICE routine recsph.f,

        here is an algorithm for converting to spherical polar coordinates from
        rectangular coordiantes:
        C Store rectangular coordinates in temporary variables
        BIG = MAX(DABS(RECTAN(1)), DABS(RECTAN(2)), DABS(RECTAN(3)))
        IF (BIG .GT. 0) THEN
          X = RECTAN(1)/BIG
          Y = RECTAN(2)/BIG
          Z = RECTAN(3)/BIG
          R = BIG*DSQRT(X*X + Y*Y + Z*Z)
          COLAT = DATAN2(DSQRT(X*X + Y*Y), Z)
          X = RECTAN(1)
          Y = RECTAN(2)
          IF (X.EQ.0.0D0 .AND. Y.EQ.0.0D0) THEN
            LONG = 0.0D0
          ELSE
            LONG = DATAN2 (Y, X)
          END IF
        ELSE
          R = 0.0D0
          COLAT = 0.0D0
          LONG = 0.0D0
        END IF
        RETURN
        END
        """
        x = cartesian.getI()
        y = cartesian.getJ()
        z = cartesian.getK()
        radius = 0
        colatitude = 0
        longitude = 0
        big = max(abs(x), abs(y), abs(z))
        if big > 0:
            x /= big
            y /= big
            z /= big
            radius = big*sqrt(x*x + y*y + z*z)
            colatitude = atan2(sqrt(x*x + y*y), z)
            x = cartesian.getI()
            y = cartesian.getJ()
            if x == 0 and y == 0:
                longitude = 0
            else:
                longitude = atan2(y, x)
        else:
            radius = 0
            colatitude = 0
            longitude = 0
        return SphericalVector(radius, colatitude, longitude)

    def toCartesian(self, coordinate):
        """Convert spherical to Cartesian coordinates.

        From the SPICE routine sphrec.f, here is a formula for converting
        from spherical polar coordinates to rectangular coordinates:

        X = R*DCOS(LONG)*DSIN(COLAT)
        Y = R*DSIN(LONG)*DSIN(COLAT)
        Z = R*DCOS(COLAT)
        """
        r = coordinate.getRadius()
        cosLong = cos(coordinate.getLongitude())
        sinLong = sin(coordinate.getLongitude())
        cosColat = cos(coordinate.getColatitude())
        sinColat = sin(coordinate.getColatitude())
        i = r * cosLong*sinColat
        j = r*sinLong*sinColat
        k = r*cosColat
        return UnwritableVectorIJK(i, j, k)
