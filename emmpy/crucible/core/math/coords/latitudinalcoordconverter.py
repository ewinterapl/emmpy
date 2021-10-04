"""Convert to and from latitudinal coordinates.

This class provides methods that convert between latitudinal and Cartesian
coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


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
    """Convert to and from latitudinal coordinates.

    Convert to and from latitudinal coordinates.

    Attributes
    ----------
    JACOBIAN : 3x3 array-like of float
        Jacobian matrix to convert from latitudinal to Cartesian
        coordinates.
    """

    # Jacobian matrix to convert from latitudinal to Cartesian
    # coordinates.
    JACOBIAN = LatitudinalToCartesianJacobian()

    def __init__(self):
        """Initialize a new LatitudinalCoordConverter object.

        Initialize a new LatitudinalCoordConverter object.

        Parameters
        ----------
        None
        """
        AbstractCoordConverter.__init__(
            self, LatitudinalCoordConverter.JACOBIAN
        )

    def toCoordinate(self, cartesian):
        """Convert a Cartesian vector to latitudinal coordinates.

        Convert a Cartesian vector to latitudinal coordinates.

        Parameters
        ----------
        cartesian : VectorIJK
            Vector in Cartesian coordinates.

        Returns
        -------
        latitudinal : LatitudinalVector
            Input vector converted to latitudinal coordinates.
        """
        (x, y, z) = (cartesian.i, cartesian.j, cartesian.k)
        radius = sqrt(x**2 + y**2 + z**2)
        latitude = atan2(z, sqrt(x**2 + y**2))
        longitude = atan2(y, x)
        latitudinal = LatitudinalVector(radius, latitude, longitude)
        return latitudinal

    def toCartesian(self, latitudinal):
        """Convert a latitudinal vector to Cartesian coordinates.

        Convert a latitudinal vector to Cartesian coordinates.

        Parameters
        ----------
        latitudinal : LatitudinalVector
            Vector in latitudinal coordinates.

        Returns
        -------
        cartesian : VectorIJK
            Input vector converted to Cartesian coordinates.
        """
        radius = latitudinal.getRadius()
        latitude = latitudinal.getLatitude()
        longitude = latitudinal.getLongitude()
        x = radius*cos(latitude)*cos(longitude)
        y = radius*cos(latitude)*sin(longitude)
        z = radius*sin(latitude)
        cartesian = VectorIJK(x, y, z)
        return cartesian
