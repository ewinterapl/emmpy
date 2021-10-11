"""Useful coordinate conversion methods.

This class contains several useful coordinate conversion methods.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D
from emmpy.math.coordinates.cylindricalvector import (
    CylindricalVector, cylindricalToCartesian, cartesianToCylindrical
)
from emmpy.math.coordinates.sphericalvector import (
    SphericalVector, sphericalToCartesian, cartesianToSpherical
)


class CoordConverters:
    """Useful coordinate conversion methods.

    This class contains several useful coordinate conversion methods.

    Attributes
    ----------
    None
    """

    @staticmethod
    def convert(position):
        """Convert an input vector to Cartesian coordinates.

        Convert a cylindrical or spherical vector to Cartesian
        coordinates.

        Parameters
        -----------
        position : Vector
            A vector in cylindrical or spherical coordinates.

        Returns
        -------
        cartesian : VectorIJK
            Input vector converted to Cartesian coordinates.
        """
        if isinstance(position, CylindricalVector):
            cartesian = VectorIJK(cylindricalToCartesian(position))
        elif isinstance(position, SphericalVector):
            cartesian = VectorIJK(sphericalToCartesian(position))
        else:
            raise ValueError
        return cartesian
