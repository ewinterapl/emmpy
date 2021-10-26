"""A 3-dimensional matrix in Cartesian (i, j, k) coordinates.

This class provides a 3-dimensional matrix in Cartesian (i, j, k)
coordinates.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.matrices.matrix3d import Matrix3D


# Map matrix component names to indices.
components = {'ii': (0, 0), 'ij': (0, 1), 'ik': (0, 2),
              'ji': (1, 0), 'jj': (1, 1), 'jk': (1, 2),
              'ki': (2, 0), 'kj': (2, 1), 'kk': (2, 2)}


class MatrixIJK(Matrix3D):
    """A 3-dimensional matrix in Cartesian (i, j, k) coordinates.

    This class implements a 3-dimensional vector in Cartesian (i, j, k)
    coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    ii, ji, ki, ij, jj, kj, ik, jk, kk : float
        Value of matrix components (listed in column-major order).
    """

    def __init__(self, *args):
        """Initialize a new MatrixIJK object.

        Initialize a new MatrixIJK object.

        Parameters
        ----------
        a : 3x3 array-like of float, optional, default 3x3 None
            Values for matrix elements.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Construct an empty matrix (all NaN).
            data = np.array((None,)*9).reshape((3, 3))
        elif len(args) == 1:
            # Initialize matrix from a 3x3 array-like of floats.
            (a,) = args
            data = np.array(a)
        else:
            raise ValueError
        self[:] = data[:]

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
