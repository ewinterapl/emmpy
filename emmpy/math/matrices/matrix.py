"""Abstract base class for matrices (rank 2 tensors).

Note that we use __new__ in addition to __init__ to enforce the specified
size of the matrix.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class Matrix(np.ndarray):
    """Abstract base class for matrices (rank 2 tensors).

    This class is the base class for all matrix classes in all
    coordinate systems.

    This abstract class should not be instantiated directly. Doing so will
    usually raise an Exception of some type.

    A matrix is defined as a rank 2 tensor with an nrows rows and ncols
    columns. Indexing follows the Numpy row-major convention of [row, col]
    index ordering, i.e. matrix[i, j] (also matrix[i][j]) is the element
    in row i, column j.

    This class is derived from the numpy.ndarray class. This allows all of
    the numpy.ndarray methods to be available to subclasses of this class.
    """

    def __new__(cls, nrows, ncols, *args, **kargs):
        """Allocate a new Matrix object.

        Allocate a new Matrix object by allocating a new np.ndarray on
        which the Matrix will expand.

        The initial contents of the Matrix are undefined.

        Parameters
        ----------
        nrows, ncols : integer
            Number of rows and columns in the matrix.

        Returns
        -------
        m : Matrix
            The newly-created object.
        """
        m = super().__new__(cls, shape=(nrows, ncols), dtype=float)
        return m
