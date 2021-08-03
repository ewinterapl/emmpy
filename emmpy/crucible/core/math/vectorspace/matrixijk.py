"""A writable 3-D matrix.

A writable subclass of the unwritable 3D matrix parent completing one link in
the weak-immutability design pattern.

This class contains the mutator methods necessary to set or alter the
internals of the parent classes fields.

@author F.S.Turner
"""


import sys

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
    """A writable 3-D matrix."""

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

    def scale(self, *args):
        """Scale the matrix as a unit, or by columns.
        
        Scale the matrix as a unit, or by columns.
        
        Parameters
        ----------
        scale : float
            Scale factor to apply to each matrix element.
        OR
        scaleI, scaleJ, scaleK : float
            Scale factors for columns i, j, k

        Returns
        -------
        self : MatrixIJK
            The current object, after scaling.
        """
        if len(args) == 1:
            # Apply a single scale factor.
            (scale,) = args
            self[:, :] *= scale
        elif len(args) == 3:
            # Apply a different scale factor to each column.
            (scaleI, scaleJ, scaleK) = args
            self[:, 0] *= scaleI
            self[:, 1] *= scaleJ
            self[:, 2] *= scaleK
        return self

    def setTo(self, *args):
        """Set the matrix components."""
        if len(args) == 1:
            if isinstance(args[0], list):
                # Sets the contents of this matrix to the upper three by three
                # block of a supplied two dimensional array of doubles.
                # @param data the array to copy to the components of this
                # instance
                # @return a reference to this instance for convenience
                # @throws IndexOutOfBoundsException if the supplied data array
                # does not contain at least three arrays of arrays of length
                # three or greater.
                (data,) = args
                self.setTo(data[0][0], data[1][0], data[2][0],
                           data[0][1], data[1][1], data[2][1],
                           data[0][2], data[1][2], data[2][2])
                return self
            else:
                # Sets the contents of this matrix to match those of a supplied
                # matrix
                # @param matrix the matrix to copy
                # @return a reference to this instance for convenience that
                # contains the supplied components
                (matrix,) = args
                self.setTo(matrix.ii, matrix.ji, matrix.ki,
                           matrix.ij, matrix.jj, matrix.kj,
                           matrix.ik, matrix.jk, matrix.kk)
                return self
        elif len(args) == 2:
            # Sets the contents of this matrix to a scaled version of the
            # supplied matrix
            # @param scale the scale factor to apply to matrix
            # @param matrix the matrix to scale
            # @return a reference to this instance for convenience that
            # contains the scaled version of matrix
            (scale, matrix) = args
            self.setTo(matrix)
            self.scale(scale)
            return self
        elif len(args) == 3:
            # Sets the columns of this matrix to the three specified vectors.
            # @param ithColumn the vector containing the contents to set the
            # ith column
            # @param jthColumn the vector containing the contents to set the
            # jth column
            # @param kthColumn the vector containing the contents to set the
            # kth column
            # @return a reference to the instance for convenience
            (ithColumn, jthColumn, kthColumn) = args
            self.setTo(ithColumn.i, ithColumn.j, ithColumn.k,
                       jthColumn.i, jthColumn.j, jthColumn.k,
                       kthColumn.i, kthColumn.j, kthColumn.k)
            return self
        elif len(args) == 4:
            # Sets the contents of this matrix to a column-wise scaled version
            # of the supplied matrix
            # @param scaleI the scale factor to apply to the ith column of
            # matrix
            # @param scaleJ the scale factor to apply to the jth column of
            # matrix
            # @param scaleK the scale factor to apply to the kth column of
            # matrix
            # @param matrix the matrix to scale
            # @return a reference to this instance for convenience that
            # contains the column scaled version of matrix
            (scaleI, scaleJ, scaleK, matrix) = args
            self.setTo(matrix)
            self.scale(scaleI, scaleJ, scaleK)
            return self
        elif len(args) == 6:
            # Sets the columns of this matrix to the scaled versions of the
            # supplied vectors.
            # @param scaleI scale factor to apply to ithColumn
            # @param ithColumn the ith column vector
            # @param scaleJ scale factor to apply to jthColumn
            # @param jthColumn the jth column vector
            # @param scaleK scale factor to apply to kthColumn
            # @param kthColumn the kth column vector
            # @return a reference to the instance for convenience
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            self.setTo(
                scaleI*ithColumn.i, scaleI*ithColumn.j, scaleI*ithColumn.k,
                scaleJ*jthColumn.i, scaleJ*jthColumn.j, scaleJ*jthColumn.k,
                scaleK*kthColumn.i, scaleK*kthColumn.j, scaleK*kthColumn.k)
            return self
        elif len(args) == 9:
            # Sets the components of this matrix to the supplied components
            # @param ii ith row, ith column element
            # @param ji jth row, ith column element
            # @param ki kth row, ith column element
            # @param ij ith row, jth column element
            # @param jj jth row, jth column element
            # @param kj kth row, jth column element
            # @param ik ith row, kth column element
            # @param jk jth row, kth column element
            # @param kk kth row, kth column element
            # @return a reference to the instance, for convenience, that
            # contains the newly set matrix
            # COLUMN-MAJOR ORDER
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            self.ii = ii
            self.ji = ji
            self.ki = ki
            self.ij = ij
            self.jj = jj
            self.kj = kj
            self.ik = ik
            self.jk = jk
            self.kk = kk
            return self
        else:
            raise Exception


    def mtxv(*args):
        """Compute the product of the transpose of a matrix with a vector."""
        if len(args) == 2:
            # @param m the matrix
            # @param v the vector
            # @return a new <code>VectorIJK</code> containing the result.
            # @see UnwritableMatrixIJK#mtxv(UnwritableVectorIJK)
            (m, v) = args
            return MatrixIJK.mtxv(m, v, VectorIJK())
        elif len(args) == 3:
            # @param m the matrix
            # @param v the vector
            # @param buffer the buffer to receive the product, transpose(m)*v
            # @return a reference to buffer for convenience.
            # @see UnwritableMatrixIJK#mtxv(UnwritableVectorIJK, VectorIJK)
            (m, v, buffer) = args
            i = m.ii*v.i + m.ji*v.j + m.ki*v.k
            j = m.ij*v.i + m.jj*v.j + m.kj*v.k
            k = m.ik*v.i + m.jk*v.j + m.kk*v.k
            buffer.i = i
            buffer.j = j
            buffer.k = k
            return buffer

    def mxv(self, *args):
        """Compute the product of a matrix with a vector."""
        if len(args) == 1:
            (v,) = args
            return self.mxv(v, VectorIJK())
        elif len(args) == 2:
            # @param m the matrix
            # @param v the vector
            # @return a new <code>VectorIJK</code> containing the result.
            # @see UnwritableMatrixIJK#mxv(UnwritableVectorIJK)
            (v, buffer) = args
            i = self.ii*v.i + self.ij*v.j + self.ik*v.k
            j = self.ji*v.i + self.jj*v.j + self.jk*v.k
            k = self.ki*v.i + self.kj*v.j + self.kk*v.k
            buffer.i = i
            buffer.j = j
            buffer.k = k
            return buffer
        else:
            raise Exception
