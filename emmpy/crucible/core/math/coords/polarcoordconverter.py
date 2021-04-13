"""emmpy.crucible.core.math.coords.polarcoordconverter"""


# import static crucible.core.math.CrucibleMath.abs;
# import static crucible.core.math.CrucibleMath.atan2;
# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.max;
# import static crucible.core.math.CrucibleMath.sin;
# import static crucible.core.math.CrucibleMath.sqrt;
# import crucible.core.math.vectorspace.UnwritableVectorIJ;
from math import atan2, cos, sin, sqrt

from emmpy.crucible.core.math.coords.abstractcoordconverterij import (
    AbstractCoordConverterIJ
)
from emmpy.crucible.core.math.coords.polartocartesianjacobian import (
    PolarToCartesianJacobian
)
from emmpy.crucible.core.math.coords.polarvector import PolarVector
from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)


class PolarCoordConverter(AbstractCoordConverterIJ):

    JACOBIAN = PolarToCartesianJacobian()

    def __init__(self):
        """Constructor"""
        AbstractCoordConverterIJ.__init__(self, PolarCoordConverter.JACOBIAN)

    def toCoordinate(self, cartesian):
        """From the SPICE routine recsph.f, here is an algorithm for converting
        to polar polar coordinates from rectangular coordiantes:

        C Store rectangular coordinates in temporary variables
        C BIG = MAX ( DABS(RECTAN(1)), DABS(RECTAN(2)), DABS(RECTAN(3)) )
        IF ( BIG .GT. 0 ) THEN
          X = RECTAN(1) / BIG Y = RECTAN(2) / BIG Z = RECTAN(3) / BIG
          R = BIG * DSQRT (X*X + Y*Y + Z*Z)
          COLAT = DATAN2 ( DSQRT(X*X + Y*Y), Z )
          X = RECTAN(1) Y = RECTAN(2)
          IF (X.EQ.0.0D0 .AND. Y.EQ.0.0D0) THEN LONG = 0.0D0
          ELSE LONG = DATAN2 (Y,X) END IF
        ELSE R = 0.0D0 COLAT = 0.0D0 LONG = 0.0D0
        END IF
        RETURN END
        """
        x = cartesian.getI()
        y = cartesian.getJ()
        radius = 0
        angle = 0
        big = max(abs(x), abs(y))
        if big > 0:
            x /= big
            y /= big
            radius = big*sqrt(x*x + y*y)
            angle = atan2(y, x)
            x = cartesian.getI()
            y = cartesian.getJ()
        else:
            radius = 0
            angle = 0
        return PolarVector(radius, angle)

    def toCartesian(self, coordinate):
        """from the SPICE routine sphrec.f, here is a formula for converting from polar
        coordinates to rectangular coordinates:

        X = R * DCOS(LONG) * DSIN(COLAT)
        Y = R * DSIN(LONG) * * DSIN(COLAT)
        Z = R * DCOS(COLAT)
        """
        i = coordinate.getRadius()*cos(coordinate.getAngle())
        j = coordinate.getRadius()*sin(coordinate.getAngle())
        return UnwritableVectorIJ(i, j)
