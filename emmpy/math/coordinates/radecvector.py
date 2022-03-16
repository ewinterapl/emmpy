"""A 3-dimensional vector in celestial (r, ra, dec) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'r': 0, 'ra': 1, 'dec': 2}


class RaDecVector(Vector3D):
    """A 3-dimensional vector in celestial (r, ra, dec) coordinates.

    This class implements a 3-dimensional vector in celestial
    (r, ra, dec) coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    r : float
        Value of radius coordinate (unspecified units). r >= 0.
    ra : float
        Right ascension (radians), 0 <= ra < 2*pi. The value is guaranteed
        to be in the range [0, 2*pi].
    dec : float
        Declination (radians). The value is guaranteed to be in the range
        [-pi/2, pi/2].
    """

    def __new__(cls, r, ra, dec):
        """Allocate a new RaDecVector object.

        Allocate a new RaDecVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        r : float
            Value of radius coordinate (unspecified units).
        ra : float
            Right ascension (radians).
        dec : float
            Declination (radians).

        Returns
        -------
        v : RaDecVector
            The newly-created object.
        """
        v = Vector3D.__new__(cls, r, ra, dec)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (r, ra, or dec).
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


def raDecToCartesian(celestial):
    """Convert a celestial coordinate vector to Cartesian coordinates.

    Convert a celestial coordinate vector to Cartesian coordinates.

    Parameters
    ----------
    celestial : RaDecVector
        Celestial coordinate vector to convert to Cartesian coordinates.

    Returns
    -------
    cartesian : CartesianVector
        Input celestial coordinate vector converted to Cartesian coordinates.
    """
    (r, ra, dec) = (celestial.r, celestial.ra, celestial.dec)
    x = r*cos(dec)*cos(ra)
    y = r*cos(dec)*sin(ra)
    z = r*sin(dec)
    cartesian = CartesianVector(x, y, z)
    return cartesian


def cartesianToRaDec(cartesian):
    """Convert a Cartesian vector to celestial coordinates.

    Convert a Cartesian vector to celestial coordinates.

    The declination is guaranteed to be in the range [0, 2*pi).

    Parameters
    ----------
    cartesian : CartesianVector
        Cartesian vector to convert to celestial coordinates.

    Returns
    -------
    celestial : RaDecVector
        Input Cartesian vector converted to celestial coordinates.
    """
    (x, y, z) = (cartesian.x, cartesian.y, cartesian.z)
    r = sqrt(x**2 + y**2 + z**2)
    ra = atan2(y, x)
    if ra < 0.0:
        ra += 2*pi
    dec = atan2(z, sqrt(x**2 + y**2))
    celestial = RaDecVector(r, ra, dec)
    return celestial
