"""Convert to and from polar coordinates.

This class provides methods that convert between polar and Cartesian
coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, sin, sqrt

from emmpy.crucible.core.math.coords.abstractcoordconverterij import (
    AbstractCoordConverterIJ
)
from emmpy.crucible.core.math.coords.polartocartesianjacobian import (
    PolarToCartesianJacobian
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.math.coordinates.polarvector import PolarVector


class PolarCoordConverter(AbstractCoordConverterIJ):
    """Convert to and from polar coordinates.

    Convert to and from polar coordinates.

    Attributes
    ----------
    JACOBIAN : MatrixIJK
        Jacobian matrix to convert from polar to Cartesian
        coordinates.
    """

    JACOBIAN = PolarToCartesianJacobian()

    def __init__(self):
        """Initialize a new PolarCoordConverter object.

        Initialize a new PolarCoordConverter object.

        Parameters
        ----------
        None
        """
        AbstractCoordConverterIJ.__init__(
            self, PolarCoordConverter.JACOBIAN
        )

    def toCoordinate(self, cartesian):
        """Convert a Cartesian vector to polar coordinates.

        Convert a Cartesian vector to polar coordinates.

        Parameters
        ----------
        cartesian : VectorIJK
            Vector in Cartesian coordinates.

        Returns
        -------
        polar : polar
            Input vector converted to polar coordinates.
        """
        (x, y) = (cartesian.i, cartesian.j)
        radius = sqrt(x**2 + y**2)
        angle = atan2(y, x)
        polar = PolarVector(radius, angle)
        return polar

    def toCartesian(self, polar):
        """Convert a polar vector to Cartesian coordinates.

        Convert a polar vector to Cartesian coordinates.

        Parameters
        ----------
        polar : PolarlVector
            Vector in polar coordinates.

        Returns
        -------
        cartesian : VectorIJK
            Input vector converted to Cartesian coordinates.
        """
        (radius, angle) = (polar.r, polar.phi)
        x = radius*cos(angle)
        y = radius*sin(angle)
        cartesian = VectorIJ(x, y)
        return cartesian
