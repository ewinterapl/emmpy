"""A 3-dimensional vector in cylindrical (rho, phi, z) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt

from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D
from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'rho': 0, 'phi': 1, 'z': 2}


class CylindricalVector(Vector3D):
    """A 3-dimensional vector in cylindrical (rho, phi, z) coordinates.

    This class implements a 3-dimensional vector in cylindrical
    (rho, phi, z) coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    rho : float
        Value of radius coordinate (unspecified units).
    phi : float
        Value of azimuthal angle (radians). The name is specified
        in ISO standard 31-11. The value is guaranteed to be in the range
        [-pi, pi].
    z : float
        Value of the axial position (unspecified units). The name is
        specified in ISO standard 31-11.

    References
    ----------
    https://en.wikipedia.org/wiki/ISO_31-11
    """

    def __new__(cls, rho=None, phi=None, z=None):
        """Create a new CylindricalVector object.

        Allocate a new CylindricalVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        rho : float (optional)
            Value of radius coordinate (unspecified units).
        phi : float (optional)
            Value of azimuthal angle (radians).
        z : float (optional)
            Value of the axial position (unspecified units).

        Returns
        -------
        v : CylindricalVector
            The newly-created object.
        """
        v = Vector3D.__new__(cls, rho, phi, z)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (rho, phi, or z).
        """
        return self[components[name]]

    def __setattr__(self, name, value):
        """Set the value of a computed attribute.

        Set the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.
    
        Returns
        -------
        None
        """
        self[components[name]] = value


def cylindricalToCartesian(cylindrical):
    """Convert a cylindrical vector to Cartesian coordinates.

    Convert a cylindrical vector to Cartesian coordinates.

    Parameters
    ----------
    cylindrical : CylindricalVector
        Cylindrical vector to convert to Cartesian coordinates.

    Returns
    -------
    cartesian : CartesianVector3D
        Input cylindrical vector converted to Cartesian coordinates.
    """
    (rho, phi, z) = (cylindrical.rho, cylindrical.phi, cylindrical.z)
    x = rho*cos(phi)
    y = rho*sin(phi)
    cartesian = CartesianVector3D(x, y, z)
    return cartesian


def cartesianToCylindrical(cartesian):
    """Convert a Cartesian vector to cylindrical coordinates.

    Convert a Cartesian vector to cylindrical.

    The angle phi is guaranteed to be in the range [0, 2*pi).

    Parameters
    ----------
    cartesian : CartesianVector3D
        Cartesian vector to convert to cylindrical coordinates.

    Returns
    -------
    cylindrical : CylindricalVector
        Input Cartesian vector converted to cylindrical coordinates.
    """
    (x, y, z) = (cartesian.x, cartesian.y, cartesian.z)
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
