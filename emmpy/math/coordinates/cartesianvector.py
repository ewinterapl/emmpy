"""A 3-dimensional vector in Cartesian (x, y, z) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'x': 0, 'y': 1, 'z': 2}


class CartesianVector(Vector3D):
    """A 3-dimensional vector in Cartesian (x, y, z) coordinates.

    This class implements a 3-dimensional vector in Cartesian (x, y, z)
    coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    x : float
        Value of x-coordinate.
    y : float
        Value of y-coordinate.
    z : float
        Value of z-coordinate.
    """

    def __new__(cls, x=None, y=None, z=None):
        """Create a new CartesianVector object.

        Allocate a new CartesianVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        x : float (optional)
            Value of x-coordinate.
        y : float (optional)
            Value of y-coordinate.
        y : float (optional)
            Value of z-coordinate.

        Returns
        -------
        v : CartesianVector
            The newly-created object.
        """
        v = Vector3D.__new__(cls, x, y, z)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (x, y, or z).
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
