"""Generic class for 2-dimensional vectors."""


import numpy as np


class Vector2D(np.ndarray):
    """Generic class for 2-dimensional vectors.

    This class implements a generic 2-dimensional vector. No coordinate
    system information is assumed.

    Since this class inherits from ndarray, all of the functionality of
    Numpy is immediately available.

    Authors
    -------
    Eric Winter (eric.winter@jhuapl.edu)

    """

    def __new__(cls, *args):
        """Create a new Vector2D object.

        Allocate a new Vector2D object by allocating a new ndarray
        on which the Vector2D will expand.

        Parameters
        ----------
        args : Tuple of 2 floats
            First and second vector elements. If more than 2 arguments are
            provided, only the first 2 are used.

        Returns
        -------
        v : Vector2D
            The newly-created object.
        """
        v = np.ndarray.__new__(cls, shape=(2,))
        v[0] = args[0]
        v[1] = args[1]
        return v
