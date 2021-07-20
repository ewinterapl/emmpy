"""Convert to and from cylindrical coordinates."""


from math import atan2, cos, pi, sin, sqrt

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)
from emmpy.crucible.core.math.coords.cylindricaltocartesianjacobian import (
    CylindricalToCartesianJacobian
)
from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class CylindricalCoordConverter(AbstractCoordConverter):
    """Convert to and from cylindrical coordinates."""

    JACOBIAN = CylindricalToCartesianJacobian()

    def __init__(self):
        """Build a new object."""
        AbstractCoordConverter.__init__(
            self, CylindricalCoordConverter.JACOBIAN
        )

    def toCoordinate(self, cartesian):
        """Use temporary variables for computing R.

        BIG = MAX( DABS(RECTAN(1)), DABS(RECTAN(2)) )
        Convert to cylindrical coordinates C Z = RECTAN(3 )
        IF ( BIG .EQ. 0 ) THEN R = 0.D0 LONG = 0.D0
        ELSE X = RECTAN(1) / BIG Y = RECTAN(2) / BIG
        R = BIG * DSQRT (X*X + Y*Y)
        LONG = DATAN2 (Y,X) END IF
        IF ( LONG .LT. 0.D0) THEN LONG = LONG + TWOPI() END IF
        """
        # Use temporary variables for computing R.
        big = max(abs(cartesian.getI()), abs(cartesian.getJ()))

        # Convert to cylindrical coordinates
        height = cartesian.getK()
        cylindricalRadius = 0
        longitude = 0
        if big == 0.0:
            cylindricalRadius = 0.0
            longitude = 0.0
        else:
            x = cartesian.getI()/big
            y = cartesian.getJ()/big
            cylindricalRadius = big*sqrt(x*x + y*y)
            longitude = atan2(y, x)
        if longitude < 0.0:
            longitude += 2*pi

        return CylindricalVector(cylindricalRadius, longitude, height)

    def toCartesian(self, coordinate):
        """From the SPICE routine cylrec.f.

        Convert to rectangular coordinates, storing the results in C temporary
        variables.
        X = R * DCOS(LONG) Y = R * DSIN(LONG)
        Move the results to the output variables.
        RECTAN(1) = X RECTAN(2) = Y RECTAN(3) = Z
        """
        # r = coordinate.getCylindricalRadius()
        # lon = coordinate.getLongitude()
        # z = coordinate.getHeight()
        return VectorIJK(
            coordinate.getCylindricalRadius()*cos(coordinate.getLongitude()),
            coordinate.getCylindricalRadius()*sin(coordinate.getLongitude()),
            coordinate.getHeight()
        )
