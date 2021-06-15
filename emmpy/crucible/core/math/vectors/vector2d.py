"""Generic class for 2-dimensional vectors."""


import numpy as np


class Vector2D(np.ndarray):
    """Generic class for 2-dimensional vectors.

    This class implements a generic 2-dimensional vector. No coordinate
    system information is assumed. The x and y attribute names were chosen
    for convenience.

    Since this class inherits from ndarray, all of the functionality of
    Numpy is immediately available.

    Attributes
    ----------
    x : float
        First vector element.
    y : float
        Second vector element.

    Authors
    -------
    Eric Winter (eric.winter@jhuapl.edu)

    """

    def __new__(cls, x, y):
        """Create a new `Vector2D` object.

        Allocate a new `Vector2D` object by allocating a new `ndarray`
        on which the `Vector2D` will expand.

        Parameters
        ----------
        x : float
            First vector element.
        y : float
            Second vector element.

        Returns
        -------
        self : `Vector2D`
            The newly-created object.
        """
        v = np.ndarray.__new__(cls, shape=(2,))
        v[0] = x
        v[1] = y
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
            Value of specified attribute (`x` or `y`).
        """
        if name == 'x':
            return self[0]
        elif name == 'y':
            return self[1]
        else:
            raise AttributeError
