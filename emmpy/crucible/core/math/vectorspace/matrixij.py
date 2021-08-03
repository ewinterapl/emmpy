"""A 2-dimensional matrix in Cartesian (i, j) coordinates.

This class provides a 2-dimensional matrix in Cartesian (i, j)
coordinates.

Authors
-------
G.K. Stephens
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import sys

import numpy as np

from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.math.matrices.matrix2d import Matrix2D
from emmpy.utilities.isrealnumber import isRealNumber


# Default tolerance for determining if a matrix is invertible. The
# determinant must be greater than this tolerance.
INVERSION_TOLERANCE = 1E-16

# The other of the two default tolerances that control how close to a
# rotation a rotation matrix must be. This value determines how far off
# unity the determinant of the matrix must be.
DETERMINANT_TOLERANCE = 1E-4

# The bound defining the boundary length at which the invort procedure
# works with double precision. Note: this is necessary because larger
# negative exponents are captured by 64 IEEE doubles than positive ones.
INVORSION_BOUND = sys.float_info.max


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
        scale : float
            The scale factor to apply.
        a : 2x2 array-like of float
            The array whose components are to be scaled and copied.
        OR
        colI, colJ : array-like of 2 float
            2-element array-likes containing the columns to use for the matrix.
        OR
        scaleI, scaleJ : float
            Scale factors to apply to the ith and jth columns of a.
        a : 2x2 array-like of float
            The array whose components are to be scaled and copied.
        OR
        ii, ji, ij, jj : float
            Elements of new matrix in column-major order.
        OR
        scaleI : float
            The scale factor to apply to the ith column.
        colI : array-like of 2 float
            The vector containing the ith column.
        scaleJ : float
            The scale factor to apply to the jth column.
        colJ : array-like of 2 float
            The vector containing the jth column.

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
        elif len(args) == 2:
            if isRealNumber(args[0]):
                # Scale an existing 2x2 array-like of floats.
                (scale, a) = args
                self[:, :] = scale*np.array(a)
            else:
                # Assign vectors to columns.
                (ithColumn, jthColumn) = args
                self[:, 0] = np.array(ithColumn)
                self[:, 1] = np.array(jthColumn)
        elif len(args) == 3:
            # Apply separate scale factors to the columns of an existing
            # 2x2 array-like of floats.
            (scaleI, scaleJ, matrix) = args
            self[:, 0] = scaleI*np.array(matrix)[:, 0]
            self[:, 1] = scaleJ*np.array(matrix)[:, 1]
        elif len(args) == 4:
            if (isRealNumber(args[0]) and isRealNumber(args[1]) and
                isRealNumber(args[2]) and isRealNumber(args[3])):
                # Assign the 4 components, in column-major order.
                (ii, ji, ij, jj) = args
                self[:, :] = [[ii, ij], [ji, jj]]
            else:
                # Scale a pair of 2-element array-like of floats to use as
                # columns.
                (scaleI, ithColumn, scaleJ, jthColumn) = args
                self[:, 0] = scaleI*np.array(ithColumn)
                self[:, 1] = scaleJ*np.array(jthColumn)
        else:
            raise TypeError

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Parameters
        ----------
        name : str
            Name of attribute to get.

        Returns
        -------
        self[i, j] : float
            Value of specified element (i, j).
        """
        return self[components[name]]

    def __setattr__(self, name, value):
        """Set the value of a computed attribute.

        Set the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

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

    def transpose(self):
        """Transpose the matrix in-place.

        Transpose the matrix in-place.

        Parameters
        ----------
        None
    
        Returns
        -------
        self : MatrixIJ
            The current object.
        """
        self[:, :] = self.T
        return self

    def invort(self):
        """Invert, in place, this matrix whose columns are orthogonal.

        Note: No checks are done to verify that the columns are orthogonal.

        Parameters
        ----------
        None

        Returns
        -------
        self : MatrixIJ
            The current object
        """
        self[:, :] = np.linalg.inv(self)
        return self

    def scale(self, *args):
        """Scale each component of the matrix by the supplied factors.

        Scale the matrix components with a single scale factor, or a
        separate scale factor for each column.

        Parameters
        ----------
        scale : float
            Scale factor to apply to entire matrix.
        OR
        scaleI, scaleJ : float
            Scale factors to apply to 1st and 2nd columns.

        Returns
        -------
        self : MatrixIJ
            The current object.
        
        Raises
        ------
        ValueError
            If incorrect parameters are provided.
        """
        if len(args) == 1:
            # Apply a single scale factor to the entire matrix.
            (scale,) = args
            self[:, :] *= scale
        elif len(args) == 2:
            # Scale each column of the matrix by a separate factor.
            (scaleI, scaleJ) = args
            self[:, 0] *= scaleI
            self[:, 1] *= scaleJ
        else:
            raise ValueError
        return self

    def setTo(self, *args):
        """Set the matrix to the specified values.

        Set the matrix to the specified values.

        Parameters
        ----------
        a : 2x2 array-like of float, optional, default 2x2 None
            Values for matrix elements.
        OR
        scale : float
            The scale factor to apply.
        a : 2x2 array-like of float
            The array whose components are to be scaled and copied.
        OR
        colI, colJ : array-like of 2 float
            2-element array-likes containing the columns to use for the matrix.
        OR
        scaleI, scaleJ : float
            Scale factors to apply to the ith and jth columns of a.
        a : 2x2 array-like of float
            The array whose components are to be scaled and copied.
        OR
        ii, ji, ij, jj : float
            Elements of new matrix in column-major order.
        OR
        scaleI : float
            The scale factor to apply to the ith column.
        colI : array-like of 2 float
            The vector containing the ith column.
        scaleJ : float
            The scale factor to apply to the jth column.
        colJ : array-like of 2 float
            The vector containing the jth column.

        Returns
        -------
        self : MatrixIJ
            The current object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            # Initialize matrix from a 2x2 array-like of floats.
            # Initialize matrix from a 2x2 array-like of floats.
            (a,) = args
            self[:, :] = np.array(a)
        elif len(args) == 2:
            if isRealNumber(args[0]):
                # Scale an existing 2x2 array-like of floats.
                (scale, a) = args
                self[:, :] = scale*np.array(a)
            else:
                # Assign vectors to columns.
                (ithColumn, jthColumn) = args
                self[:, 0] = np.array(ithColumn)
                self[:, 1] = np.array(jthColumn)
        elif len(args) == 3:
            # Apply separate scale factors to the columns of an existing
            # 2x2 array-like of floats.
            (scaleI, scaleJ, matrix) = args
            self[:, 0] = scaleI*np.array(matrix)[:, 0]
            self[:, 1] = scaleJ*np.array(matrix)[:, 1]
        elif len(args) == 4:
            if (isRealNumber(args[0]) and isRealNumber(args[1]) and
                isRealNumber(args[2]) and isRealNumber(args[3])):
                # Assign the 4 components, in column-major order.
                (ii, ji, ij, jj) = args
                self[:, :] = [[ii, ij], [ji, jj]]
            else:
                # Scale a pair of 2-element array-like of floats to use as
                # columns.
                (scaleI, ithColumn, scaleJ, jthColumn) = args
                self[:, 0] = scaleI*np.array(ithColumn)
                self[:, 1] = scaleJ*np.array(jthColumn)
        else:
            raise ValueError
        return self

    @staticmethod
    def mxv(*args):
        """Compute the product of a matrix with a vector.

        Multiply a 2-D vector by a 2-D matrix.

        Parameters
        ----------
        m : MatrixIJ
            The matrix to multiply.
        v : VectorIJ
            The vector to multiply.
        buffer : VectorIJ, optional
            Buffer to hold the result.

        Returns
        -------
        buffer : VectorIJ
            Vector product.

        Raises
        ------
        ValueError
            If incorrect parameters are supplied.
        """
        if len(args) == 2:
            (m, v) = args
            buffer = VectorIJ()
        elif len(args) == 3:
            (m, v, buffer) = args
        else:
            raise ValueError
        buffer[:] = m.dot(v)
        return buffer
