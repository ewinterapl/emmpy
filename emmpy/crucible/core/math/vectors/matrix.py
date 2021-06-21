"""Abstract base class for matrices.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class Matrix(np.ndarray):
    """Abstract base class for 2-dimensional, n-component matrices.

    This class is the base class for all matrix classes in all
    coordinate systems.

    This abstract class must not be instantiated directly. Doing so will
    usually raise an Exception of some type.

    A matrix is defined as a two-dimensional tensor with n rows and n
    columns. Indexing follows row-major ordering, i.e. matrix[i,j] is the
    element in row i, column j.

    This class is derived from the numpy.ndarray class, to allow a single
    entry point for Numpy code to be used in the matrix classes.
    Therefore, if we decide to use a new representation for matrices
    (other than numpy), fewer classes will need to be changed. This
    approach also allows all of the numpy.ndarray methods to be available
    to subclasses of Matrix.
    """

    def __new__(cls, *args, **kargs):
        """Create a new Matrix object.

        Allocate a new Matrix object by allocating a new ndarray
        on which the Matrix will expand.

        Note that this method should only be called from the __new__()
        method of subclasses.

        Parameters
        ----------
        args : Tuple of objects
            Positional arguments.
        kargs : Dictionary of str->object pairs
            Keyword arguments.

        Returns
        -------
        m : Matrix
            The newly-created object.
        """
        m = np.ndarray.__new__(cls, *args, **kargs)
        return m
