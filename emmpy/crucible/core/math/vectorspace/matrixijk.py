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


# One of the two default tolerances that control how close to a rotation a
# rotation matrix must be. This value determines how far off unity the norm
# of the column vectors of a matrix must be.
NORM_TOLERANCE = 1E-4

# The other of the two default tolerances that control how close to a
# rotation a rotation matrix must be. This value determines how far off
# unity the determinant of the matrix must be.
DETERMINANT_TOLERANCE = 1E-4


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
        scale : float
            The scale factor to apply.
        a : 3x3 array-like of float
            The array whose components are to be scaled and copied.
        OR
        colI, colJ, colK : array-like of 3 float
            3-element array-likes containing the columns to use for the matrix.
        OR
        scaleI, scaleJ, scaleK : float
            Scale factors to apply to the ith, jth, kth columns.
        a : 3x3 array-like of float
            The array whose components are to be scaled and copied.
        OR
        scaleI : float
            The scale factor to apply to the ith column.
        colI : array-like of 3 float
            The vector containing the ith column.
        scaleJ : float
            The scale factor to apply to the jth column.
        colJ : array-like of 3 float
            The vector containing the jth column.
        scaleK : float
            The scale factor to apply to the kth column.
        colK : array-like of 3 float
            The vector containing the kth column.
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
        elif len(args) == 2:
            # Initialize matrix by applying a scale factor to the
            # components of an existing array-like.
            (scale, a) = args
            self[:, :] = scale*np.array(a)
        elif len(args) == 3:
            # Initialize matrix by populating the columns of the matrix
            # with the supplied vectors.
            (colI, colJ, colK) = args
            self[:, 0] = np.array(colI)
            self[:, 1] = np.array(colJ)
            self[:, 2] = np.array(colK)
        elif len(args) == 4:
            # Initialize matrix by applying scalar multiples to each
            # column of an existing array-like.
            (scaleI, scaleJ, scaleK, a) = args
            scales = (scaleI, scaleJ, scaleK)
            self[:, :] = scales*np.array(a)
        elif len(args) == 6:
            # Initialize matrix by applying individual scale factors to
            # columns.
            (scaleI, colI, scaleJ, colJ, scaleK, colK) = args
            self[:, 0] = scaleI*np.array(colI)
            self[:, 1] = scaleJ*np.array(colJ)
            self[:, 2] = scaleK*np.array(colK)
        elif len(args) == 9:
            # Constructs a matrix from the nine basic components, in column-
            # major order.
            self[:, :] = np.array(args).reshape((3, 3)).T
        else:
            raise ValueError

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
        scale : float
            The scale factor to apply.
        a : 3x3 array-like of float
            The array whose components are to be scaled and copied.
        OR
        colI, colJ, colK : array-like of 3 float
            3-element array-likes containing the columns to use for the matrix.
        # OR
        # scaleI, scaleJ : float
        #     Scale factors to apply to the ith and jth columns of a.
        # a : 2x2 array-like of float
        #     The array whose components are to be scaled and copied.
        # OR
        # ii, ji, ij, jj : float
        #     Elements of new matrix in column-major order.
        # OR
        # scaleI : float
        #     The scale factor to apply to the ith column.
        # colI : array-like of 2 float
        #     The vector containing the ith column.
        # scaleJ : float
        #     The scale factor to apply to the jth column.
        # colJ : array-like of 2 float
        #     The vector containing the jth column.

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
            # Initialize matrix from a 3x3 array-like of floats.
            (a,) = args
            m = np.array(a)
            self[:, :] = m
        elif len(args) == 2:
            # Scale an existing 3x3 array-like of floats.
            (scale, a) = args
            m = np.array(a)
            self[:, :] = scale*m
        elif len(args) == 3:
                # Assign array-like vectors to columns.
                (ithColumn, jthColumn, kthColumn) = args
                self[:, 0] = np.array(ithColumn)
                self[:, 1] = np.array(jthColumn)
                self[:, 2] = np.array(kthColumn)
        elif len(args) == 4:
            # Apply separate scale factors to the columns of an existing
            # 3x3 array-like of floats.
            (scaleI, scaleJ, scaleK, a) = args
            self.setTo(a)
            self[:, 0] *= scaleI
            self[:, 1] *= scaleJ
            self[:, 2] *= scaleK
        elif len(args) == 6:
            # Scale a set of 3-element array-like of floats to use as
            # columns.
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            c1 = scaleI*np.array(ithColumn)
            c2 = scaleJ*np.array(jthColumn)
            c3 = scaleK*np.array(kthColumn)
            self.setTo(c1, c2, c3)
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
