"""A 2-dimensional vector in Cartesian (x, y) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectors.vector2d import Vector2D


class CartesianVector2D(Vector2D):
    """A 2-dimensional vector in Cartesian (x, y) coordinates.

    This class implements a 2-dimensional vector in Cartesian (x, y)
    coordinates.

    Attributes
    ----------
    x : float
        Value of x-coordinate.
    y : float
        Value of y-coordinate.
    """

    def __new__(cls, x, y):
        """Create a new CartesianVector2D object.

        Allocate a new CartesianVector2D object by allocating a Vector2D
        object which will be expanded upon.

        Parameters
        ----------
        x : float
            Value of x-coordinate.
        y : float
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
        attribute search process. The valid attributes are

        x : float
            First vector element.
        y : float
            Second vector element.

        Returns
        -------
        self[0|1] : float
            Value of specified attribute (x or y).

        Raises
        ------
        AttributeError
            If an illegal attribute name is specified.
        """
        if name == 'x':
            return self[0]
        elif name == 'y':
            return self[1]
        else:
            raise AttributeError
