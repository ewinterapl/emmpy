"""A 3-dimensional matrix in Cartesian (i, j, k) coordinates.

This class provides a 3-dimensional matrix in Cartesian (i, j, k)
coordinates.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
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
        OR
        ii, ji, ki, ij, jj, kj, ik, jk, kk : float
            Elements of new matrix in column-major order.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Construct an empty matrix (all NaN).
            self[:, :] = np.array((None,)*9).reshape((3, 3))
        elif len(args) == 1:
            # Initialize matrix from a 3x3 array-like of floats.
            (a,) = args
            self[:, :] = np.array(a)
        elif len(args) == 9:
            # Matrix elements in column-major order.
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            self[:, :] = [[ii, ij, ik], [ji, jj, jk], [ki, kj, kk]]
        else:
            raise ValueError

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

    def invert(self):
        """Invert the matrix in-place.

        Invert the matrix in-place.

        Parameters
        ----------
        None

        Returns
        -------
        self : MatrixIJK
            Current object.
        """
        self[:, :] = np.linalg.inv(self)
        return self

    def invort(self):
        """Invert, in place, this matrix whose columns are orthogonal.

        Invert, in place, this matrix whose columns are orthogonal. Note:
        No checks are done to verify that the columns are orthogonal.

        Parameters
        ----------
        None

        Returns
        -------
        self : MatrixIJK
            The current object after invorsion.
        """
        self.invert()
        return self

    def setTo(self, *args):
        """Set the matrix to the specified values.

        Set the matrix to the specified values.

        Parameters
        ----------
        a : 3x3 array-like of float
            Values for matrix elements.
        OR
        ii, ji, ki, ij, jj, kj, ik, jk, kk : float
            Elements of new matrix in column-major order.

        Returns
        -------
        self : MatrixIJK
            The current object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            # Initialize matrix from a 3x3 array-like of floats.
            (a,) = args
            m = np.array(a)
            self[:, :] = m
        elif len(args) == 9:
            # Assign the 9 components, in column-major order.
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            self[:, :] = [[ii, ij, ik], [ji, jj, jk], [ki, kj, kk]]
        else:
            raise TypeError
        return self

    def mtxv(*args):
        """Compute the product of a matrix transpose with a vector.

        Multiply a 3-D vector by a transposed 3-D matrix.

        Parameters
        ----------
        m : MatrixIJK
            The matrix to transpose and multiply.
        v : VectorIJK
            The vector to multiply.
        buffer : VectorIJK, optional
            Buffer to hold the result.

        Returns
        -------
        buffer : VectorIJK
            Vector product.

        Raises
        ------
        ValueError
            If incorrect parameters are supplied.
        """
        if len(args) == 2:
            (m, v) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (m, v, buffer) = args
        else:
            raise ValueError
        buffer[:] = m.T.dot(v)
        return buffer

    def mxv(self, *args):
        """Compute the product of this matrix with a vector.

        Multiply a 3-D vector by a 3-D matrix.

        Parameters
        ----------
        m : MatrixIJK
            The matrix to multiply.
        v : VectorIJK
            The vector to multiply.
        buffer : VectorIJK, optional
            Buffer to hold the result.

        Returns
        -------
        buffer : VectorIJK
            Vector product.

        Raises
        ------
        ValueError
            If incorrect parameters are supplied.
        """
        if len(args) == 1:
            (v,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (v, buffer) = args
        else:
            raise TypeError
        buffer[:] = self.dot(v)
        return buffer
