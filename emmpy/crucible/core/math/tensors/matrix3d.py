"""Generic class for 3-dimensional (3x3) matrices.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.tensors.matrix import Matrix


class Matrix3D(Matrix):
    """Generic class for 3-dimensional (3x3) matrices.

    This class implements a generic 3-dimensional matrix. No coordinate
    system information is assumed.
    """

    def __new__(cls, *args):
        """Create a new Matrix3D object.

        Allocate a new Matrix3D object by allocating a new Matrix object
        on which the Matrix3D will expand.

        Parameters
        ----------
        args : Tuple of 9 floats
            Matrix elements in row-major order (ii, ji, ki, ij, ...).

        Returns
        -------
        m : Matrix3D
            The newly-created object.

        Raises
        ------
        ValueError
            If other than 9 arguments are provided.
        """
        if len(args) != 9:
            raise ValueError('Exactly 9 numeric arguments are required!')
        m = Matrix.__new__(cls, shape=(3, 3))
        m[:] = np.array(args).reshape((3, 3)).T
        return m
