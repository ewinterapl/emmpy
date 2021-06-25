"""A 2-dimensional vector in Cartesian (x, y) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector2d import Vector2D


# Map vector component names to indices.
components = {'x': 0, 'y': 1}


class CartesianVector2D(Vector2D):
    """A 2-dimensional vector in Cartesian (x, y) coordinates.

    This class implements a 2-dimensional vector in Cartesian (x, y)
    coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    x : float
        Value of x-coordinate.
    y : float
        Value of y-coordinate.
    """

    def __new__(cls, x=None, y=None):
        """Create a new CartesianVector2D object.

        Allocate a new CartesianVector2D object by allocating a Vector2D
        object which will be expanded upon.

        Parameters
        ----------
        x : float (optional)
            Value of x-coordinate.
        y : float (optional)
            Value of y-coordinate.

        Returns
        -------
        v : CartesianVector2D
            The newly-created object.
        """
        v = Vector2D.__new__(cls, x, y)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1] : float
            Value of specified attribute (x or y).
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
