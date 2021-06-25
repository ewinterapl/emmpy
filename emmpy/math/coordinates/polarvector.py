"""A 2-dimensional vector in polar (r, phi) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector2d import Vector2D


# Map vector component names to indices.
components = {'r': 0, 'phi': 1}


class PolarVector(Vector2D):
    """A 2-dimensional vector in polar (r, phi) coordinates.

    This class implements a 2-dimensional vector in polar (r, phi)
    coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    r : float
        Value of radius coordinate (unspecified units).
    phi : float
        Value of angle coordinate (radians). The name is specified
        in ISO standard 31-11.

    References
    ----------
    https://en.wikipedia.org/wiki/ISO_31-11
    """

    def __new__(cls, r=None, phi=None):
        """Create a new PolarVector object.

        Allocate a new PolarVector object by allocating a Vector2D
        object which will be expanded upon.

        Parameters
        ----------
        r : float (optional)
            Value of radius coordinate (unspecified units).
        phi : float (optional)
            Value of angle coordinate (radians).

        Returns
        -------
        v : PolarVector
            The newly-created object.
        """
        v = Vector2D.__new__(cls, r, phi)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1] : float
            Value of specified attribute (r or phi).
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
