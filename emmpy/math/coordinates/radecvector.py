"""A 3-dimensional vector in celestial (r, ra, dec) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


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
        Value of radius coordinate (unspecified units).
    ra : float
        Right ascension (radians).
    dec : float
        Declination (radians).
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
