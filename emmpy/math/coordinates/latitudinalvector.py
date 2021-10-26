"""A 3-dimensional vector in latitudinal (r, lat, lon) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, sin, sqrt

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'r': 0, 'lat': 1, 'lon': 2}


class LatitudinalVector(Vector3D):
    """A 3-dimensional vector in latitudinal (r, lat, lon) coordinates.

    This class implements a 3-dimensional vector in latitudinal
    (r, lat, lon) coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    r : float
        Value of radius coordinate (unspecified units).
    lat : float
        Latitude (radians). The value is guaranteed to be in the range
        [-pi/2, pi/2].
    lon : float
        Longitude (radians). The value is guaranteed to be in the range
        [-pi, pi].
    """

    def __new__(cls, r, lat, lon):
        """Allocate a new LatitudinalVector object.

        Allocate a new LatitudinalVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        r : float
            Value of radius coordinate (unspecified units).
        lat : float
            Latitude (radians).
        lon : float
            Longitude (radians).

        Returns
        -------
        v : LatitudinalVector
            The newly-created object.
        """
        v = Vector3D.__new__(cls, r, lat, lon)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (r, lat, or lon).
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


def latitudinalToCartesian(latitudinal):
    """Convert a latitudinal vector to Cartesian coordinates.

    Convert a latitudinal vector to Cartesian coordinates.

    Parameters
    ----------
    latitudinal : LatitudinalVector
        Latitudinal vector to convert to Cartesian coordinates.

    Returns
    -------
    cartesian : CartesianVector
        Input latitudinal vector converted to Cartesian coordinates.
    """
    (r, lat, lon) = (latitudinal.r, latitudinal.lat, latitudinal.lon)
    x = r*cos(lat)*cos(lon)
    y = r*cos(lat)*sin(lon)
    z = r*sin(lat)
    cartesian = CartesianVector(x, y, z)
    return cartesian


def cartesianToLatitudinal(cartesian):
    """Convert a Cartesian vector to latitudinal coordinates.

    Convert a Cartesian vector to latitudinal coordinates.

    The longitude is guaranteed to be in the range [-pi, pi).

    Parameters
    ----------
    cartesian : CartesianVector
        Cartesian vector to convert to latitudinal coordinates.

    Returns
    -------
    latitudinal : LatitudinalVector
        Input Cartesian vector converted to latitudinal coordinates.
    """
    (x, y, z) = (cartesian.x, cartesian.y, cartesian.z)
    r = sqrt(x**2 + y**2 + z**2)
    lat = atan2(z, sqrt(x**2 + y**2))
    lon = atan2(y, x)
    latitudinal = LatitudinalVector(r, lat, lon)
    return latitudinal
