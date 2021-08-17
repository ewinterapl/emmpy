"""Convert to and from cylindrical coordinates.

This class provides methods that convert between cylindrical and Cartesian
coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)
from emmpy.crucible.core.math.coords.cylindricaltocartesianjacobian import (
    CylindricalToCartesianJacobian
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


class CylindricalCoordConverter(AbstractCoordConverter):
    """Convert to and from cylindrical coordinates.

    Convert to and from cylindrical coordinates.

    Attributes
    ----------
    JACOBIAN : 3x3 array-like of float
        Jacobian matrix to convert from cylindrical to Cartesian
        coordinates.
    """

    # Jacobian matrix to convert from cylindrical to Cartesian coordinates.
    JACOBIAN = CylindricalToCartesianJacobian()

    def __init__(self):
        """Initialize a new CylindricalCoordConverter object.

        Initialize a new CylindricalCoordConverter object.

        Parameters
        ----------
        None
        """
        AbstractCoordConverter.__init__(
            self, CylindricalCoordConverter.JACOBIAN
        )

    def toCoordinate(self, cartesian):
        """Convert a Cartesian vector to cylindrical coordinates.

        Convert a Cartesian vector to cylindrical coordinates.

        Parameters
        ----------
        cartesian : VectorIJK
            Vector in Cartesian coordinates.

        Returns
        -------
        cylindrical : CylindricalVector
            Input vector converted to cylindrical coordinates.
        """
        (x, y, z) = (cartesian.i, cartesian.j, cartesian.k)
        if x == y == 0:
            rho = 0
            phi = 0
        else:
            rho = sqrt(x**2 + y**2)
            phi = atan2(y, x)
            if phi < 0:
                phi += 2*pi
        cylindrical = CylindricalVector(rho, phi, z)
        return cylindrical

    def toCartesian(self, cylindrical):
        """Convert a cylindrical vector to Cartesian coordinates.

        Convert a cylindrical vector to Cartesian coordinates.

        Parameters
        ----------
        cylindrical : CylindricalVector
            Vector in cylindrical coordinates.

        Returns
        -------
        cartesian : VectorIJK
            Input vector converted to Cartesian coordinates.
        """
        (rho, phi, z) = (cylindrical.rho, cylindrical.phi, cylindrical.z)
        x = rho*cos(phi)
        y = rho*sin(phi)
        cartesian = VectorIJK(x, y, z)
        return cartesian
