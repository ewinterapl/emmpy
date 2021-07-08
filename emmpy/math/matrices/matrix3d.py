"""Generic class for 3-dimensional (3x3) square matrices.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.matrices.squarematrix import SquareMatrix


# Number of elements in each dimension of a 3-D matrix.
N = 3


class Matrix3D(SquareMatrix):
    """Generic class for 3-dimensional (3x3) square matrices.

    This class implements a generic 3-dimensional square matrix. No
    coordinate system information is assumed.
    """

    def __new__(cls, *args, **kargs):
        """Allocate a new Matrix3D object.

        Allocate a new Matrix3D object by allocating a new 3x3
        SquareMatrix object on which the Matrix3D will expand.

        Initial contents are undefined.

        Returns
        -------
        m : Matrix3D
            The newly-created object.
        """
        m = SquareMatrix.__new__(cls, length=N)
        return m

    def __init__(self, *args, **kargs):
        """Initialize a new Matrix3D object.

        Initialize a new Matrix3D object.

        Parameters
        ----------
        data : array-like, optional, default all None.
            Values for array elements in array order.
        OR
        data[:9] : float, optional.
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
