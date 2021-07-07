"""Generic class for 3-dimensional (3x3) square matrices.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.matrices.matrix import Matrix


class Matrix3D(Matrix):
    """Generic class for 3-dimensional (3x3) square matrices.

    This class implements a generic 3-dimensional square matrix. No coordinate
    system information is assumed.

    This object may be directly used as a Numpy array.
    """

    def __new__(cls, *args):
        """Create a new Matrix3D object.

        Allocate a new Matrix3D object by allocating a new Matrix object
        on which the Matrix3D will expand.

        Parameters
        ----------
        args : tuple of 9 float (optional, defaults None)
            Matrix elements in row-major order (ii, ij, ik, ji, ...).

        Returns
        -------
        m : Matrix3D
            The newly-created object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = [None]*9
        elif len(args) == 9:
            data = args
        else:
            raise ValueError
        m = Matrix.__new__(cls, shape=(3, 3))
        m[:, :] = np.array(data).reshape((3, 3))
        return m
