"""Generic class for 2-dimensional (2x2) square matrices.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.matrices.squarematrix import SquareMatrix


# Number of elements in each dimension of a 2-D matrix.
N = 2


class Matrix2D(SquareMatrix):
    """Generic class for 2-dimensional (2x2) square matrices.

    This class implements a generic 2-dimensional square matrix. No
    coordinate system information is assumed.
    """

    def __new__(cls, *args, **kargs):
        """Allocate a new Matrix2D object.

        Allocate a new Matrix2D object by allocating a new 2x2
        SquareMatrix object on which the Matrix2D will expand.

        Initial contents are undefined.

        Returns
        -------
        m : Matrix2D
            The newly-created object.
        """
        m = SquareMatrix.__new__(cls, length=N)
        return m

    def __init__(self, *args, **kargs):
        """Initialize a new Matrix2D object.

        Initialize a new Matrix2D object.

        Parameters
        ----------
        data : array-like, optional, default all None.
            Values for array elements in array order.
        OR
        data[:3] : float, optional.
            Values for array elements, in row-major order.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = np.array((None,)*N*N).reshape((N, N))
        elif len(args) == 1:
            (data,) = args
        elif len(args) == N*N:
            data = np.array(args).reshape((N, N))
        else:
            raise ValueError
        self[:, :] = data
