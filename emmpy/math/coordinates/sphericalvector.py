"""A 3-dimensional vector in spherical (r, theta, phi) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, sin, sqrt

from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D
from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'r': 0, 'theta': 1, 'phi': 2}


class SphericalVector(Vector3D):
    """A 3-dimensional vector in spherical (r, theta, phi) coordinates.

    This class implements a 3-dimensional vector in spherical
    (r, theta, phi) coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    r : float
        Value of radius coordinate (unspecified units).
    theta : float
        Value of the polar angle (radians). The name is specified
        in ISO standard 31-11.
    phi : float
        Value of azimuthal angle (radians). The name is specified
        in ISO standard 31-11.

    References
    ----------
    https://en.wikipedia.org/wiki/ISO_31-11
    """

    def __new__(cls, r=None, theta=None, phi=None):
        """Create a new SphericalVector object.

        Allocate a new SphericalVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        r : float (optional)
            Value of radius coordinate (unspecified units).
        theta : float (optional)
            Value of the polar angle (radians).
        phi : float (optional)
            Value of azimuthal angle (radians).

        Returns
        -------
        v : SphericalVector
            The newly-created object.
        """
        v = Vector3D.__new__(cls, r, theta, phi)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (r, theta, or phi).
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


def sphericalToCartesian(spherical):
    """Convert a spherical coordinate vector to Cartesian coordinates.

    Convert a spherical coordinate vector to Cartesian coordinates.

    Parameters
    ----------
    spherical : SphericalVector
        Spherical coordinate vector to convert to Cartesian coordinates.

    Returns
    -------
    cartesian : CartesianVector3D
        Input spherical coordinate vector converted to Cartesian coordinates.
    """
    (r, theta, phi) = (spherical.r, spherical.theta, spherical.phi)
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(theta)
    cartesian = CartesianVector3D(x, y, z)
    return cartesian


def cartesianToSpherical(cartesian):
    """Convert a Cartesian vector to spherical coordinates.

    Convert a Cartesian vector to spherical coordinates.

    The angle phi is guaranteed to be in the range [-pi, pi).

    Parameters
    ----------
    cartesian : CartesianVector3D
        Cartesian vector to convert to spherical coordinates.

    Returns
    -------
    spherical : SphericalVector
        Input Cartesian vector converted to spherical coordinates.
    """
    (x, y, z) = (cartesian.x, cartesian.y, cartesian.z)
    r = sqrt(x**2 + y**2 + z**2)
    theta = atan2(sqrt(x**2 + y**2), z)
    phi = atan2(y, x)
    spherical = SphericalVector(r, theta, phi)
    return spherical
