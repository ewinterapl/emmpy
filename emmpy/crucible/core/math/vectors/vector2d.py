"""Generic class for 2-dimensional vectors."""


import numpy as np

from emmpy.crucible.core.math.vectors.vector import Vector


class Vector2D(np.ndarray):
    """Generic class for 2-dimensional vectors.

    This class implements a generic 2-dimensional vector. No coordinate
    system information is assumed. The x and y attribute names were chosen
    for convenience.

    Since this class inherits from `ndarray`, all of the functionality of
    Numpy is immediately available.

    Attributes
    ----------
    v : `ndarray`
        A 2-element `ndarray` containing the 2 vector elements.

    author Eric Winter (eric.winter@jhuapl.edu)

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
        return np.array((x, y))
