"""A 3-dimensional vector in latitudinal (r, lat, lon) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


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
        Latitude (radians).
    lon : float
        Longitude (radians).
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
