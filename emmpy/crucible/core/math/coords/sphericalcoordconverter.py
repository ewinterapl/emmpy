"""Convert to and from spherical coordinates.

This class provides methods that convert between spherical and Cartesian
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
from emmpy.crucible.core.math.coords.sphericaltocartesianjacobian import (
    SphericalToCartesianJacobian
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class SphericalCoordConverter(AbstractCoordConverter):
    """Convert to and from spherical coordinates.

    Convert to and from spherical coordinates.

    Attributes
    ----------
    JACOBIAN : 3x3 array-like of float
        Jacobian matrix to convert from spherical to Cartesian
        coordinates.
    """

    # Jacobian matrix to convert from spherical to Cartesian
    # coordinates.
    JACOBIAN = SphericalToCartesianJacobian()

    def __init__(self):
        """Initialize a new SphericalCoordConverter object.

        Initialize a new SphericalCoordConverter object.

        Parameters
        ----------
        None
        """
        AbstractCoordConverter.__init__(self, SphericalCoordConverter.JACOBIAN)

    def toCoordinate(self, cartesian):
        """Convert a Cartesian vector to spherical coordinates.

        Convert a Cartesian vector to spherical coordinates.

        Parameters
        ----------
        cartesian : VectorIJK
            Vector in Cartesian coordinates.

        Returns
        -------
        spherical : SphericalVector
            Input vector converted to spherical coordinates.
        """
        (x, y, z) = (cartesian.i, cartesian.j, cartesian.k)
        r = sqrt(x**2 + y**2 + z**2)
        theta = atan2(sqrt(x**2 + y**2), z)
        phi = atan2(y, x)
        spherical = SphericalVector(r, theta, phi)
        return spherical

    def toCartesian(self, spherical):
        """Convert a spherical vector to Cartesian coordinates.

        Convert a spherical vector to Cartesian coordinates.

        Parameters
        ----------
        spherical : SphericalVector
            Vector in spherical coordinates.

        Returns
        -------
        cartesian : VectorIJK
            Input vector converted to Cartesian coordinates.
        """
        r = spherical.r
        theta = spherical.theta
        phi = spherical.phi
        x = r*sin(theta)*cos(phi)
        y = r*sin(theta)*sin(phi)
        z = r*cos(theta)
        cartesian = VectorIJK(x, y, z)
        return cartesian
