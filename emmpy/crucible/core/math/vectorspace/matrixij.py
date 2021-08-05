"""A 2-dimensional matrix in Cartesian (i, j) coordinates.

This class provides a 2-dimensional matrix in Cartesian (i, j)
coordinates.

Authors
-------
G.K. Stephens
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.math.matrices.matrix2d import Matrix2D


# Map matrix component names to indices.
components = {'ii': (0, 0), 'ij': (0, 1),
              'ji': (1, 0), 'jj': (1, 1)}


class MatrixIJ(Matrix2D):
    """A 2-dimensional matrix in Cartesian (i, j) coordinates.

    This class implements a 2-dimensional vector in Cartesian (i, j)
    coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    ii, ji, ij, jj : float
        Value of matrix components (listed in column-major order).
    """

    def __init__(self, *args):
        """Initialize a new MatrixIJ object.

        Initialize a new MatrixIJ object.

        Parameters
        ----------
        a : 2x2 array-like of float, optional, default 2x2 None
            Values for matrix elements.
        OR
        ii, ji, ij, jj : float
            Elements of new matrix in column-major order.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Construct an empty matrix (all NaN).
            self[:, :] = np.array((None,)*4).reshape((2, 2))
        elif len(args) == 1:
            # Initialize matrix from a 2x2 array-like of floats.
            (a,) = args
            self[:, :] = np.array(a)
        elif len(args) == 4:
            # Matrix elements in column-major order.
            (ii, ji, ij, jj) = args
            self[:, :] = [[ii, ij], [ji, jj]]
        else:
            raise TypeError

    def __getattr__(self, name):
        """Return the value of an attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Parameters
        ----------
        name : str
            Name of attribute to get.

        Returns
        -------
        self[components[name]] : float
            Value of element at location for components[name].
        """
        return self[components[name]]

    def __setattr__(self, name, value):
        """Set the value of an attribute.

        Set the value of an attribute not found by the standard attribute
        search process. The valid attributes are listed in the components
        dictionary.

        Parameters
        ----------
        name : str
            Name of attribute to set.
        value : obj
            Value for attribute to be set.

        Returns
        -------
        None
        """
        self[components[name]] = value
