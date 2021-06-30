"""A square 3-D matrix in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import sqrt

import numpy as np

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
from emmpy.crucible.core.math.vectorspace.unwritablematrixijk import (
    UnwritableMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.matrices.matrix3d import Matrix3D


# Map vector component names to indices.
components = {'ii': (0, 0), 'ji': (1, 0), 'ki': (2, 0),
              'ij': (0, 1), 'jj': (1, 1), 'kj': (1, 2),
              'ik': (0, 2), 'jk': (1, 2), 'kk': (2, 2)}


class MatrixIJK(Matrix3D):
    """A square 3-D matrix in Cartesian (i, j, k) coordinates.

    The elements of the matrix are referred to by name as:

    ii ij ik
    ji jj jk
    ki kj kk

    The primary difference between this class and a rank-2 Numpy array
    is the flatten behavior:

    MatrixIJK:   (ii, ji, ki, ij, jj, kj, ik, jk, kk)
    Numpy Array: (ii, ij, ik, ji, jj, jk, ki, kj, kk)
    """

    # # The matrix whose components are all zero.
    # ZEROS = UnwritableMatrixIJK(0, 0, 0, 0, 0, 0, 0, 0, 0)

    # # The matrix whose components are all ones.
    # ONES = UnwritableMatrixIJK(1, 1, 1, 1, 1, 1, 1, 1, 1)

    # # The multiplicative identity.
    # IDENTITY = UnwritableMatrixIJK(1, 0, 0, 0, 1, 0, 0, 0, 1)

    def __new__(cls, *args):
        """Create a new MatrixIJK object.
        
        Allocate a new MatrixIJK object by allocating a new Matrix3D
        object on which the MatrixIJK will expand.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic constructor.
        data : list of list of float, or tuple or tuple of tuple of float
            Values for matrix elements in column-major order. Array must
            be at least 3x3 in size.
        OR
        matrix : MatrixIJK
            Matrix to copy values from.
        OR
        scale : float
            The scale factor to apply.
        matrix : MatrixIJK
            The matrix whose components are to be scaled and copied.
        OR
        ithColumn, jthColumn, kthColumn : VectorIJK
            Vectors containing the 3 columns to use for the matrix.
        OR
        scaleI, scaleJ, scaleK : float
            The scale factors to apply to the ith, jth, kth columns.
        matrix : MatrixIJK
            The matrix whose components are to be scaled and copied.
        OR
        scaleI : float
            The scale factor to apply to the ith column.
        ithColumn : VectorIJK
            The vector containing the ith column.
        scaleJ : float
            The scale factor to apply to the jth column.
        jthColumn : VectorIJK
            The vector containing the jth column.
        scaleK : float
            The scale factor to apply to the kth column.
        kthColumn : VectorIJK
            The vector containing the kth column.
        OR
        ii, ji, ki, ij, jj, kj, ik, jk, kk : Float
            Elements of new vector.

        Returns
        -------
        m : MatrixIJK
            The newly-created object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Construct an empty matrix.
            data = [None]*9
        elif len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                # Initialize matrix from the upper 3x3 block of a two
                # dimensional array of floats.
                (data,) = args
                data = data[0][:3] + data[1][:3] + data[2][:3]
            elif isinstance(args[0], MatrixIJK):
                # Initialize the matrix by copying the values from an
                # existing 3x3 Numpy array.
                (matrix,) = args
                data = matrix.T.flatten()
            else:
                raise ValueError('Bad arguments for constructor!')
        elif len(args) == 2:
            # Create a new matrix by applying a scalar factor to the
            # components of an existing matrix.
            (scale, matrix) = args
            data = matrix.T.flatten()*scale
        elif len(args) == 3:
            # Creates a new matrix by populating the columns of the matrix
            # with the supplied vectors.
            (ithColumn, jthColumn, kthColumn) = args
            data = np.hstack([ithColumn, jthColumn, kthColumn])
        elif len(args) == 4:
            # Creates a new matrix by applying scalar multiples to each
            # column of an existing matrix.
            (scaleI, scaleJ, scaleK, matrix) = args
            data = np.hstack((
                scaleI*matrix[:, 0], scaleJ*matrix[:, 1], scaleK*matrix[:, 2]
            ))
        elif len(args) == 6:
            # Creates a new matrix by populating the columns of the matrix
            # with scaled versions of the supplied vectors
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            data = np.hstack((scaleI*ithColumn, scaleJ*jthColumn,
                              scaleK*kthColumn))
        elif len(args) == 9:
            # Constructs a matrix from the nine basic components.
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            data = (ii, ji, ki, ij, jj, kj, ik, jk, kk)
        else:
            raise ValueError('Bad arguments for constructor!')
        m = Matrix3D.__new__(cls, *data)
        return m

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

        Returns
        -------
        None
        """
        self[components[name]] = value

    def createTranspose(self):
        """Create a transposed copy of the matrix.

        Return the tranpose of the matrix.

        Returns
        -------
        m : MatrixIJK
            The transpose of the matrix.
        """
        m = MatrixIJK()
        m[:, :] = self.T[:, :]
        return m

    def createUnitizedColumns(self):
        """Create a copy of the matrix with unitized columns.

        Create a copy of the matrix with unitized columns.

        Returns
        -------
        m : MatrixIJK
            A copy of the matrix with unitized columns.
        """
        lengths = [np.linalg.norm(self[:, i]) for i in range(3)]
        u = np.array([self[:, i]/lengths[i] for i in range(3)])
        # data = np.hstack(c)
        m = MatrixIJK(u)
        return m

    def createInverse(self, *args):
        """Create an inverted copy of the matrix.

        Create an inverted copy of the matrix.

        Returns
        -------
        m : MatrixIJK
            An inverted copy of the matrix.
        """
        m = MatrixIJK()
        m[:] = np.linalg.inv(self)[:]
        return m

    # def createInvorted(self):
    #     """Create an invorted copy of the matrix.

    #     Note: this method is overridden to return an instance of the
    #     writable subclass rather than the unwritable parent.
    #     """
    #     return MatrixIJK(self).invort()

    def transpose(self):
        """Transpose the matrix in-place.

        Transpose the matrix in-place.

        Returns
        -------
        self : MatrixIJK
            The matrix, transposed.
        """
        self[:] = self.T[:]
        return self

    def unitizeColumns(self):
        """Convert each column to a unit vector.

        Unitize the columns of the matrix in-place.

        Returns
        -------
        self : MatrixIJK
            The current object, for convenience.
        """
        lengths = [np.linalg.norm(self[:, i]) for i in range(3)]
        u = np.array([self[:, i]/lengths[i] for i in range(3)]).T
        self[:, :] = u[:, :]
        return self

    def invert(self, *args):
        """Invert the matrix in-place.

        Invert the matrix in-place.

        Returns
        -------
        self : MatrixIJK
            The current object, for convenience.
        """
        self[:] = np.linalg.inv(self)[:]
        return self

    # def invort(self):
    #     """Invert, in place, this matrix whose columns are orthogonal.

    #     Note: No checks are done to verify that the columns are orthogonal.

    #     @return a reference to the instance for convenience
    #     @throws UnsupportedOperationException if the lengths of any of the
    #     columns are zero or too small to properly invert multiplicatively in
    #     the space available to double precision
    #     """
    #     self.transpose()
    #     length = computeNorm(self.ii, self.ij, self.ik)
    #     if length*MatrixIJK.INVORSION_BOUND < 1 or length == 0:
    #         raise Exception(
    #             "ith column of matrix has length, %s, for which there is no "
    #             "inverse." % length)
    #     self.ii /= length
    #     self.ii /= length
    #     self.ij /= length
    #     self.ij /= length
    #     self.ik /= length
    #     self.ik /= length
    #     length = computeNorm(self.ji, self.jj, self.jk)
    #     if length*MatrixIJK.INVORSION_BOUND < 1 or length == 0:
    #         raise Exception(
    #             "jth column of matrix has length, %s, for which there is no "
    #             "inverse." % length)
    #     self.ji /= length
    #     self.ji /= length
    #     self.jj /= length
    #     self.jj /= length
    #     self.jk /= length
    #     self.jk /= length
    #     length = computeNorm(self.ki, self.kj, self.kk)
    #     if length*MatrixIJK.INVORSION_BOUND < 1 or length == 0:
    #         raise Exception(
    #             "kth column of matrix has length, %s, for which there is no "
    #             "inverse." % length)
    #     self.ki /= length
    #     self.ki /= length
    #     self.kj /= length
    #     self.kj /= length
    #     self.kk /= length
    #     self.kk /= length
    #     return self

    # def scale(self, *args):
    #     """Scale the matrix."""
    #     if len(args) == 1:
    #         # Scales each component of the matrix by the supplied factor.
    #         # @param scale the scale factor to apply
    #         # @return a reference to the instance which now contains the scaled
    #         # matrix.
    #         (scale,) = args
    #         self.ii *= scale
    #         self.ji *= scale
    #         self.ki *= scale
    #         self.ij *= scale
    #         self.jj *= scale
    #         self.kj *= scale
    #         self.ik *= scale
    #         self.jk *= scale
    #         self.kk *= scale
    #         return self
    #     elif len(args) == 3:
    #         # Scales each column of the matrix by the supplied factors.
    #         # @param scaleI the ith column scale
    #         # @param scaleJ the jth column scale
    #         # @param scaleK the kth column scale
    #         # @return a reference to the instance for convenience which
    #         # contains the scaled matrix.
    #         (scaleI, scaleJ, scaleK) = args
    #         self.ii *= scaleI
    #         self.ji *= scaleI
    #         self.ki *= scaleI
    #         self.ij *= scaleJ
    #         self.jj *= scaleJ
    #         self.kj *= scaleJ
    #         self.ik *= scaleK
    #         self.jk *= scaleK
    #         self.kk *= scaleK
    #         return self

    # def setII(self, ii):
    #     """Set the ith row, ith column component."""
    #     self.ii = ii

    # def setJI(self, ji):
    #     """Set the jth row, ith column component."""
    #     self.ji = ji

    # def setKI(self, ki):
    #     """Set the kth row, ith column component."""
    #     self.ki = ki

    # def setIJ(self, ij):
    #     """Set the ith row, jth column component."""
    #     self.ij = ij

    # def setJJ(self, jj):
    #     """Set the jth row, jth column component."""
    #     self.jj = jj

    # def setKJ(self, kj):
    #     """Set the kth row, jth column component."""
    #     self.kj = kj

    # def setIK(self, ik):
    #     """Set the ith row, kth column component."""
    #     self.ik = ik

    # def setJK(self, jk):
    #     """Set the jth row, kth column component."""
    #     self.jk = jk

    # def setKK(self, kk):
    #     """Set the kth row, kth column component."""
    #     self.kk = kk

    # def set(self, row, column, value):
    #     """Set the component for the specified row and column.

    #     @param row a row index in [0,2].
    #     @param column a column index in [0,2]
    #     @param value the value to place into the matrix at (row,column).
    #     @throws IllegalArgumentException if either the supplied row or column
    #     index are outside their acceptable ranges of [0,2].
    #     """
    #     if row == 0:
    #         if column == 0:
    #             self.ii = value
    #         elif column == 1:
    #             self.ij = value
    #         elif column == 2:
    #             self.ik = value
    #         else:
    #             raise Exception(
    #                 "Unable to set element (%s, %s). Column index invalid." %
    #                 (row, column))
    #     elif row == 1:
    #         if column == 0:
    #             self.ji = value
    #         elif column == 1:
    #             self.jj = value
    #         elif column == 2:
    #             self.jk = value
    #         else:
    #             raise Exception(
    #                 "Unable to set element (%s, %s). Column index invalid." %
    #                 (row, column))
    #     elif row == 2:
    #         if column == 0:
    #             self.ki = value
    #         elif column == 1:
    #             self.kj = value
    #         elif column == 2:
    #             self.kk = value
    #         else:
    #             raise Exception(
    #                 "Unable to set element (%s, %s). Column index invalid." %
    #                 (row, column))
    #     else:
    #         raise Exception(
    #             "Unable to set element (%s, %s). Column index invalid." %
    #             (row, column))

    # def setIthColumn(self, column):
    #     """Set the ith column to the supplied vector.

    #     @param column the vector whose components are to replace the ith column
    #     of this matrix
    #     """
    #     self.ii = column.i
    #     self.ji = column.j
    #     self.ki = column.k

    # def setJthColumn(self, column):
    #     """Set the jth column to the supplied vector.

    #     @param column the vector whose components are to replace the jth column
    #     of this matrix
    #     """
    #     self.ij = column.i
    #     self.jj = column.j
    #     self.kj = column.k

    # def setKthColumn(self, column):
    #     """Set the kth column to the supplied vector.

    #     @param column the vector whose components are to replace the kth column
    #     of this matrix
    #     """
    #     self.ik = column.i
    #     self.jk = column.j
    #     self.kk = column.k

    # def setColumn(self, columnIndex, column):
    #     """Set the column at a specified index to the supplied vector.

    #     @param columnIndex a column index in [0,2].
    #     @param column the vector whose components are to replace the specified
    #     column of this matrix
    #     @throws IllegalArgumentException if the supplied columnIndex is not in
    #     [0,2].
    #     """
    #     if columnIndex == 0:
    #         self.setIthColumn(column)
    #     elif columnIndex == 1:
    #         self.setJthColumn(column)
    #     elif columnIndex == 2:
    #         self.setKthColumn(column)
    #     else:
    #         raise Exception(
    #             "Unable to set column. Index: %s is invalid." % columnIndex)

    # def setTo(self, *args):
    #     """Set the matrix components."""
    #     if len(args) == 1:
    #         if isinstance(args[0], list):
    #             # Sets the contents of this matrix to the upper three by three
    #             # block of a supplied two dimensional array of doubles.
    #             # @param data the array to copy to the components of this
    #             # instance
    #             # @return a reference to this instance for convenience
    #             # @throws IndexOutOfBoundsException if the supplied data array
    #             # does not contain at least three arrays of arrays of length
    #             # three or greater.
    #             (data,) = args
    #             self.setTo(data[0][0], data[1][0], data[2][0],
    #                        data[0][1], data[1][1], data[2][1],
    #                        data[0][2], data[1][2], data[2][2])
    #             return self
    #         else:
    #             # Sets the contents of this matrix to match those of a supplied
    #             # matrix
    #             # @param matrix the matrix to copy
    #             # @return a reference to this instance for convenience that
    #             # contains the supplied components
    #             (matrix,) = args
    #             self.setTo(matrix.ii, matrix.ji, matrix.ki,
    #                        matrix.ij, matrix.jj, matrix.kj,
    #                        matrix.ik, matrix.jk, matrix.kk)
    #             return self
    #     elif len(args) == 2:
    #         # Sets the contents of this matrix to a scaled version of the
    #         # supplied matrix
    #         # @param scale the scale factor to apply to matrix
    #         # @param matrix the matrix to scale
    #         # @return a reference to this instance for convenience that
    #         # contains the scaled version of matrix
    #         (scale, matrix) = args
    #         self.setTo(matrix)
    #         self.scale(scale)
    #         return self
    #     elif len(args) == 3:
    #         # Sets the columns of this matrix to the three specified vectors.
    #         # @param ithColumn the vector containing the contents to set the
    #         # ith column
    #         # @param jthColumn the vector containing the contents to set the
    #         # jth column
    #         # @param kthColumn the vector containing the contents to set the
    #         # kth column
    #         # @return a reference to the instance for convenience
    #         (ithColumn, jthColumn, kthColumn) = args
    #         self.setTo(ithColumn.i, ithColumn.j, ithColumn.k,
    #                    jthColumn.i, jthColumn.j, jthColumn.k,
    #                    kthColumn.i, kthColumn.j, kthColumn.k)
    #         return self
    #     elif len(args) == 4:
    #         # Sets the contents of this matrix to a column-wise scaled version
    #         # of the supplied matrix
    #         # @param scaleI the scale factor to apply to the ith column of
    #         # matrix
    #         # @param scaleJ the scale factor to apply to the jth column of
    #         # matrix
    #         # @param scaleK the scale factor to apply to the kth column of
    #         # matrix
    #         # @param matrix the matrix to scale
    #         # @return a reference to this instance for convenience that
    #         # contains the column scaled version of matrix
    #         (scaleI, scaleJ, scaleK, matrix) = args
    #         self.setTo(matrix)
    #         self.scale(scaleI, scaleJ, scaleK)
    #         return self
    #     elif len(args) == 6:
    #         # Sets the columns of this matrix to the scaled versions of the
    #         # supplied vectors.
    #         # @param scaleI scale factor to apply to ithColumn
    #         # @param ithColumn the ith column vector
    #         # @param scaleJ scale factor to apply to jthColumn
    #         # @param jthColumn the jth column vector
    #         # @param scaleK scale factor to apply to kthColumn
    #         # @param kthColumn the kth column vector
    #         # @return a reference to the instance for convenience
    #         (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
    #         self.setTo(
    #             scaleI*ithColumn.i, scaleI*ithColumn.j, scaleI*ithColumn.k,
    #             scaleJ*jthColumn.i, scaleJ*jthColumn.j, scaleJ*jthColumn.k,
    #             scaleK*kthColumn.i, scaleK*kthColumn.j, scaleK*kthColumn.k)
    #         return self
    #     elif len(args) == 9:
    #         # Sets the components of this matrix to the supplied components
    #         # @param ii ith row, ith column element
    #         # @param ji jth row, ith column element
    #         # @param ki kth row, ith column element
    #         # @param ij ith row, jth column element
    #         # @param jj jth row, jth column element
    #         # @param kj kth row, jth column element
    #         # @param ik ith row, kth column element
    #         # @param jk jth row, kth column element
    #         # @param kk kth row, kth column element
    #         # @return a reference to the instance, for convenience, that
    #         # contains the newly set matrix
    #         (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
    #         self.ii = ii
    #         self.ji = ji
    #         self.ki = ki
    #         self.ij = ij
    #         self.jj = jj
    #         self.kj = kj
    #         self.ik = ik
    #         self.jk = jk
    #         self.kk = kk
    #         return self
    #     else:
    #         raise Exception

    # def setToTranspose(self, matrix):
    #     """Set the matrix components to the transpose of the supplied matrix.

    #     @param matrix the matrix whose transpose is to be copied into the
    #     instance
    #     @return a reference to the instance for convenience
    #     """
    #     self.setTo(matrix)
    #     self.transpose()
    #     return self

    # def setToUnitizedColumns(self, matrix):
    #     """Set to the unitized columns of a matrix.

    #     @return a reference to the instance for convenience
    #     @throws UnsupportedOperationException if any of the columns are of
    #     length zero
    #     """
    #     return self.setTo(matrix).unitizeColumns()

    # def setToInverse(self, *args):
    #     """Set the matrix components to the inverse of the supplied matrix."""
    #     if len(args) == 1:
    #         # @param matrix the matrix to invert
    #         # @return a reference to the instance containing the inverse of
    #         # matrix for convenience
    #         # @throws IllegalArgumentException if the determinant of matrix is
    #         # within {@link UnwritableMatrixIJK#INVERSION_TOLERANCE} of 0.0.
    #         (matrix,) = args
    #         det = matrix.getDeterminant()
    #         if abs(det) < UnwritableMatrixIJK.DETERMINANT_TOLERANCE:
    #             raise Exception(
    #                 "Matrix nearly singular, unable to invert.")
    #         self.setTo(matrix)
    #         self.invert()
    #         return self
    #     elif len(args) == 2:
    #         # Sets the matrix components to the inverse of the supplied matrix.
    #         # @param matrix the matrix to invert
    #         # @param tolerance the tolerance
    #         # @return a reference to the instance containing the inverse of
    #         # matrix for convenience
    #         # @throws IllegalArgumentException if the determinant of matrix is
    #         # within tolerance of 0.0.
    #         (matrix, tolerance) = args
    #         det = matrix.getDeterminant()
    #         if abs(det) < tolerance:
    #             raise Exception(
    #                 "Matrix nearly singular, unable to invert.")
    #         self.setTo(matrix)
    #         self.invert(tolerance)
    #         return self

    # def setToInvorted(self, matrix):
    #     """Set to the invorse of the specified matrix.

    #     @param matrix a matrix to invert, with orthogonal columns.
    #     @return a reference to the instance for convenience
    #     @throws UnsupportedOperationException if any of the columns are zero or
    #     too small to properly invert multiplicatively in the space available to
    #     double precision
    #     """
    #     return self.setTo(matrix).invort()

    # @staticmethod
    # def mxmt(*args):
    #     """Compute the product of a matrix with the transpose of another."""
    #     if len(args) == 2:
    #         # @param a the left hand matrix
    #         # @param b the right hand matrix to transpose, then multiply
    #         # @return a new <code>MatrixIJK</code> containing the product.
    #         # @see MatrixIJK#mxmt(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # MatrixIJK)
    #         (a, b) = args
    #         return MatrixIJK.mxmt(a, b, MatrixIJK())
    #     elif len(args) == 3:
    #         # @param a the left hand matrix
    #         # @param b the right hand matrix to transpose, then multiply
    #         # @param buffer the buffer to receive the product, a*transpose(b).
    #         # @return a reference to buffer for convenience.
    #         (a, b, buffer) = args
    #         ii = a.ii*b.ii + a.ij*b.ij + a.ik*b.ik
    #         ij = a.ii*b.ji + a.ij*b.jj + a.ik*b.jk
    #         ik = a.ii*b.ki + a.ij*b.kj + a.ik*b.kk
    #         ji = a.ji*b.ii + a.jj*b.ij + a.jk*b.ik
    #         jj = a.ji*b.ji + a.jj*b.jj + a.jk*b.jk
    #         jk = a.ji*b.ki + a.jj*b.kj + a.jk*b.kk
    #         ki = a.ki*b.ii + a.kj*b.ij + a.kk*b.ik
    #         kj = a.ki*b.ji + a.kj*b.jj + a.kk*b.jk
    #         kk = a.ki*b.ki + a.kj*b.kj + a.kk*b.kk
    #         buffer.ii = ii
    #         buffer.ij = ij
    #         buffer.ik = ik
    #         buffer.ji = ji
    #         buffer.jj = jj
    #         buffer.jk = jk
    #         buffer.ki = ki
    #         buffer.kj = kj
    #         buffer.kk = kk
    #         return buffer

    # @staticmethod
    # def mtxm(*args):
    #     """Compute the product of a transpose of a matrix with another."""
    #     if len(args) == 2:
    #         # @param a the left hand matrix to transpose, then multiply
    #         # @param b the right hand matrix
    #         # @return a new <code>MatrixIJK</code> containing the product
    #         # @see MatrixIJK#mtxm(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # MatrixIJK)
    #         (a, b) = args
    #         return MatrixIJK.mtxm(a, b, MatrixIJK())
    #     elif len(args) == 3:
    #         # @param a the left hand matrix to transpose, then multiply
    #         # @param b the right hand matrix
    #         # @param buffer the buffer to receive the product, transpose(a)*b.
    #         # @return a reference to buffer for convenience
    #         (a, b, buffer) = args
    #         ii = a.ii*b.ii + a.ji*b.ji + a.ki*b.ki
    #         ij = a.ii*b.ij + a.ji*b.jj + a.ki*b.kj
    #         ik = a.ii*b.ik + a.ji*b.jk + a.ki*b.kk
    #         ji = a.ij*b.ii + a.jj*b.ji + a.kj*b.ki
    #         jj = a.ij*b.ij + a.jj*b.jj + a.kj*b.kj
    #         jk = a.ij*b.ik + a.jj*b.jk + a.kj*b.kk
    #         ki = a.ik*b.ii + a.jk*b.ji + a.kk*b.ki
    #         kj = a.ik*b.ij + a.jk*b.jj + a.kk*b.kj
    #         kk = a.ik*b.ik + a.jk*b.jk + a.kk*b.kk
    #         buffer.ii = ii
    #         buffer.ij = ij
    #         buffer.ik = ik
    #         buffer.ji = ji
    #         buffer.jj = jj
    #         buffer.jk = jk
    #         buffer.ki = ki
    #         buffer.kj = kj
    #         buffer.kk = kk
    #         return buffer

    # @staticmethod
    # def mxm(*args):
    #     """Compute the product of two matrices."""
    #     if len(args) == 2:
    #         # @param a the left hand matrix
    #         # @param b the right hand matrix
    #         # @return a new <code>MatrixIJK</code> containing the product (ab).
    #         # @see MatrixIJK#mxm(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # MatrixIJK)
    #         (a, b) = args
    #         return MatrixIJK.mxm(a, b, MatrixIJK())
    #     elif len(args) == 3:
    #         # @param a the left hand matrix
    #         # @param b the right hand matrix
    #         # @param buffer the buffer to receive the product, a*b
    #         # @return a reference to buffer for convenience
    #         (a, b, buffer) = args
    #         ii = a.ii*b.ii + a.ij*b.ji + a.ik*b.ki
    #         ij = a.ii*b.ij + a.ij*b.jj + a.ik*b.kj
    #         ik = a.ii*b.ik + a.ij*b.jk + a.ik*b.kk
    #         ji = a.ji*b.ii + a.jj*b.ji + a.jk*b.ki
    #         jj = a.ji*b.ij + a.jj*b.jj + a.jk*b.kj
    #         jk = a.ji*b.ik + a.jj*b.jk + a.jk*b.kk
    #         ki = a.ki*b.ii + a.kj*b.ji + a.kk*b.ki
    #         kj = a.ki*b.ij + a.kj*b.jj + a.kk*b.kj
    #         kk = a.ki*b.ik + a.kj*b.jk + a.kk*b.kk
    #         buffer.ii = ii
    #         buffer.ij = ij
    #         buffer.ik = ik
    #         buffer.ji = ji
    #         buffer.jj = jj
    #         buffer.jk = jk
    #         buffer.ki = ki
    #         buffer.kj = kj
    #         buffer.kk = kk
    #         return buffer

    # @staticmethod
    # def mxmtadd(*args):
    #     """Compute the sum of 2 matrices multipled with another transposed."""
    #     if len(args) == 4:
    #         # @param a left hand matrix in the first product
    #         # @param b right hand matrix to transpose in the first product
    #         # @param c left hand matrix in the second product
    #         # @param d right hand matrix to transpose in the second product
    #         # @return a new <code>MatrixIJK</code> containing
    #         # (a x bt) + (c x dt)
    #         # @see MatrixIJK#mxmtadd(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # UnwritableMatrixIJK, UnwritableMatrixIJK, MatrixIJK)
    #         (a, b, c, d) = args
    #         return MatrixIJK.mxmtadd(a, b, c, d, MatrixIJK())
    #     elif len(args) == 5:
    #         # @param a left hand matrix in the first product
    #         # @param b right hand matrix to transpose in the first product
    #         # @param c left hand matrix in the second product
    #         # @param d right hand matrix to transpose in the second product
    #         # @param buffer buffer to receive the results of
    #         # (a x bt) + (c x dt)
    #         # @return reference to buffer for convenience
    #         (a, b, c, d, buffer) = args
    #         ii = a.ii*b.ii + a.ij*b.ij + a.ik*b.ik
    #         ij = a.ii*b.ji + a.ij*b.jj + a.ik*b.jk
    #         ik = a.ii*b.ki + a.ij*b.kj + a.ik*b.kk
    #         ji = a.ji*b.ii + a.jj*b.ij + a.jk*b.ik
    #         jj = a.ji*b.ji + a.jj*b.jj + a.jk*b.jk
    #         jk = a.ji*b.ki + a.jj*b.kj + a.jk*b.kk
    #         ki = a.ki*b.ii + a.kj*b.ij + a.kk*b.ik
    #         kj = a.ki*b.ji + a.kj*b.jj + a.kk*b.jk
    #         kk = a.ki*b.ki + a.kj*b.kj + a.kk*b.kk
    #         ii += c.ii*d.ii + c.ij*d.ij + c.ik*d.ik
    #         ij += c.ii*d.ji + c.ij*d.jj + c.ik*d.jk
    #         ik += c.ii*d.ki + c.ij*d.kj + c.ik*d.kk
    #         ji += c.ji*d.ii + c.jj*d.ij + c.jk*d.ik
    #         jj += c.ji*d.ji + c.jj*d.jj + c.jk*d.jk
    #         jk += c.ji*d.ki + c.jj*d.kj + c.jk*d.kk
    #         ki += c.ki*d.ii + c.kj*d.ij + c.kk*d.ik
    #         kj += c.ki*d.ji + c.kj*d.jj + c.kk*d.jk
    #         kk += c.ki*d.ki + c.kj*d.kj + c.kk*d.kk
    #         buffer.ii = ii
    #         buffer.ij = ij
    #         buffer.ik = ik
    #         buffer.ji = ji
    #         buffer.jj = jj
    #         buffer.jk = jk
    #         buffer.ki = ki
    #         buffer.kj = kj
    #         buffer.kk = kk
    #         return buffer

    # @staticmethod
    # def mtxmadd(*args):
    #     """Compute the sum of 2 matrix transposes multipled with another."""
    #     if len(args) == 4:
    #         # @param a left hand matrix to transpose in the first product
    #         # @param b right hand matrix in the first product
    #         # @param c left hand matrix to transpose in the second product
    #         # @param d right hand matrix in the second product
    #         # @return a new <code>MatrixIJK</code> containing
    #         # (at x b) + (ct x d)
    #         # @see MatrixIJK#mtxmadd(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # UnwritableMatrixIJK, UnwritableMatrixIJK, MatrixIJK)
    #         (a, b, c, d) = args
    #         return MatrixIJK.mtxmadd(a, b, c, d, MatrixIJK())
    #     elif len(args) == 5:
    #         # @param a left hand matrix to transpose in the first product
    #         # @param b right hand matrix in the first product
    #         # @param c left hand matrix to transpose in the second product
    #         # @param d right hand matrix in the second product
    #         # @param buffer buffer to receive the results of
    #         # (at x b) + (ct x d)
    #         # @return reference to buffer for convenience
    #         (a, b, c, d, buffer) = args
    #         ii = a.ii*b.ii + a.ji*b.ji + a.ki*b.ki
    #         ij = a.ii*b.ij + a.ji*b.jj + a.ki*b.kj
    #         ik = a.ii*b.ik + a.ji*b.jk + a.ki*b.kk
    #         ji = a.ij*b.ii + a.jj*b.ji + a.kj*b.ki
    #         jj = a.ij*b.ij + a.jj*b.jj + a.kj*b.kj
    #         jk = a.ij*b.ik + a.jj*b.jk + a.kj*b.kk
    #         ki = a.ik*b.ii + a.jk*b.ji + a.kk*b.ki
    #         kj = a.ik*b.ij + a.jk*b.jj + a.kk*b.kj
    #         kk = a.ik*b.ik + a.jk*b.jk + a.kk*b.kk
    #         ii += c.ii*d.ii + c.ji*d.ji + c.ki*d.ki
    #         ij += c.ii*d.ij + c.ji*d.jj + c.ki*d.kj
    #         ik += c.ii*d.ik + c.ji*d.jk + c.ki*d.kk
    #         ji += c.ij*d.ii + c.jj*d.ji + c.kj*d.ki
    #         jj += c.ij*d.ij + c.jj*d.jj + c.kj*d.kj
    #         jk += c.ij*d.ik + c.jj*d.jk + c.kj*d.kk
    #         ki += c.ik*d.ii + c.jk*d.ji + c.kk*d.ki
    #         kj += c.ik*d.ij + c.jk*d.jj + c.kk*d.kj
    #         kk += c.ik*d.ik + c.jk*d.jk + c.kk*d.kk
    #         buffer.ii = ii
    #         buffer.ij = ij
    #         buffer.ik = ik
    #         buffer.ji = ji
    #         buffer.jj = jj
    #         buffer.jk = jk
    #         buffer.ki = ki
    #         buffer.kj = kj
    #         buffer.kk = kk
    #         return buffer

    # @staticmethod
    # def mxmadd(*args):
    #     """Compute the sum of the products of two pairs of matrices."""
    #     if len(args) == 4:
    #         # @param a left hand matrix in first product
    #         # @param b right hand matrix in first product
    #         # @param c left hand matrix in second product
    #         # @param d right hand matrix in second product
    #         # @return a new <code>MatrixIJK</code> containing (a x b) + (c x d)
    #         # @see MatrixIJK#mxmadd(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # UnwritableMatrixIJK, UnwritableMatrixIJK, MatrixIJK)
    #         (a, b, c, d) = args
    #         return MatrixIJK.mxmadd(a, b, c, d, MatrixIJK())
    #     elif len(args) == 5:
    #         # @param a left hand matrix in first product
    #         # @param b right hand matrix in first product
    #         # @param c left hand matrix in second product
    #         # @param d right hand matrix in second product
    #         # @param buffer buffer to receive the results of (a x b) + (c x d)
    #         # @return a reference to buffer for convenience
    #         (a, b, c, d, buffer) = args
    #         ii = a.ii*b.ii + a.ij*b.ji + a.ik*b.ki
    #         ij = a.ii*b.ij + a.ij*b.jj + a.ik*b.kj
    #         ik = a.ii*b.ik + a.ij*b.jk + a.ik*b.kk
    #         ji = a.ji*b.ii + a.jj*b.ji + a.jk*b.ki
    #         jj = a.ji*b.ij + a.jj*b.jj + a.jk*b.kj
    #         jk = a.ji*b.ik + a.jj*b.jk + a.jk*b.kk
    #         ki = a.ki*b.ii + a.kj*b.ji + a.kk*b.ki
    #         kj = a.ki*b.ij + a.kj*b.jj + a.kk*b.kj
    #         kk = a.ki*b.ik + a.kj*b.jk + a.kk*b.kk
    #         ii += c.ii*d.ii + c.ij*d.ji + c.ik*d.ki
    #         ij += c.ii*d.ij + c.ij*d.jj + c.ik*d.kj
    #         ik += c.ii*d.ik + c.ij*d.jk + c.ik*d.kk
    #         ji += c.ji*d.ii + c.jj*d.ji + c.jk*d.ki
    #         jj += c.ji*d.ij + c.jj*d.jj + c.jk*d.kj
    #         jk += c.ji*d.ik + c.jj*d.jk + c.jk*d.kk
    #         ki += c.ki*d.ii + c.kj*d.ji + c.kk*d.ki
    #         kj += c.ki*d.ij + c.kj*d.jj + c.kk*d.kj
    #         kk += c.ki*d.ik + c.kj*d.jk + c.kk*d.kk
    #         buffer.ii = ii
    #         buffer.ij = ij
    #         buffer.ik = ik
    #         buffer.ji = ji
    #         buffer.jj = jj
    #         buffer.jk = jk
    #         buffer.ki = ki
    #         buffer.kj = kj
    #         buffer.kk = kk
    #         return buffer

    # @staticmethod
    # def subtract(*args):
    #     """Compute the component-wise difference of two matrices."""
    #     if len(args) == 2:
    #         # @param a the minuend matrix
    #         # @param b the subtrahend matrix
    #         # @return a new <code>MatrixIJK</code> which contains (a - b)
    #         # @see MatrixIJK#subtract(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # MatrixIJK)
    #         (a, b) = args
    #         return MatrixIJK.subtract(a, b, MatrixIJK())
    #     elif len(args) == 3:
    #         # @param a the minuend matrix
    #         # @param b the subtrahend matrix
    #         # @param buffer the buffer to receive the results of the
    #         # subtraction
    #         # @return a reference to buffer for convenience which now contains
    #         # (a - b)
    #         (a, b, buffer) = args
    #         buffer.ii = a.ii - b.ii
    #         buffer.ji = a.ji - b.ji
    #         buffer.ki = a.ki - b.ki
    #         buffer.ij = a.ij - b.ij
    #         buffer.jj = a.jj - b.jj
    #         buffer.kj = a.kj - b.kj
    #         buffer.ik = a.ik - b.ik
    #         buffer.jk = a.jk - b.jk
    #         buffer.kk = a.kk - b.kk
    #         return buffer

    # @staticmethod
    # def add(*args):
    #     """Compute component-wise sum of two matrices."""
    #     if len(args) == 2:
    #         # @param a a matrix
    #         # @param b another matrix
    #         # @return a new <code>MatrixIJK</code> containing (a + b)
    #         # @see MatrixIJK#add(UnwritableMatrixIJK, UnwritableMatrixIJK,
    #         # MatrixIJK)
    #         (a, b) = args
    #         return MatrixIJK.add(a, b, MatrixIJK())
    #     elif len(args) == 3:
    #         # @param a a matrix
    #         # @param b another matrix
    #         # @param buffer the buffer to receive a + b
    #         # @return a reference to buffer for convenience
    #         (a, b, buffer) = args
    #         buffer.ii = a.ii + b.ii
    #         buffer.ji = a.ji + b.ji
    #         buffer.ki = a.ki + b.ki
    #         buffer.ij = a.ij + b.ij
    #         buffer.jj = a.jj + b.jj
    #         buffer.kj = a.kj + b.kj
    #         buffer.ik = a.ik + b.ik
    #         buffer.jk = a.jk + b.jk
    #         buffer.kk = a.kk + b.kk
    #         return buffer

    # @staticmethod
    # def mtxv(*args):
    #     """Compute the product of the transpose of a matrix with a vector."""
    #     if len(args) == 2:
    #         # @param m the matrix
    #         # @param v the vector
    #         # @return a new <code>VectorIJK</code> containing the result.
    #         # @see UnwritableMatrixIJK#mtxv(UnwritableVectorIJK)
    #         (m, v) = args
    #         return UnwritableMatrixIJK.mtxv(m, v, VectorIJK())
    #     elif len(args) == 3:
    #         # @param m the matrix
    #         # @param v the vector
    #         # @param buffer the buffer to receive the product, transpose(m)*v
    #         # @return a reference to buffer for convenience.
    #         # @see UnwritableMatrixIJK#mtxv(UnwritableVectorIJK, VectorIJK)
    #         (m, v, buffer) = args
    #         return UnwritableMatrixIJK.mtxv(m, v, buffer)

    # def mxv(self, *args):
    #     """Compute the product of a matrix with a vector."""
    #     if len(args) == 1:
    #         (v,) = args
    #         return UnwritableMatrixIJK.mxv(self, v)
    #     elif len(args) == 2:
    #         # @param m the matrix
    #         # @param v the vector
    #         # @return a new <code>VectorIJK</code> containing the result.
    #         # @see UnwritableMatrixIJK#mxv(UnwritableVectorIJK)
    #         (v, buffer) = args
    #         return UnwritableMatrixIJK.mxv(self, v, buffer)
    #     # elif len(args) == 3:
    #     #     # @param m the matrix
    #     #     # @param v the vector
    #     #     # @param buffer the buffer to receive the product, m*v.
    #     #     # @return a reference to buffer for convenience.
    #     #     # @see UnwritableMatrixIJK#mxv(UnwritableVectorIJK, VectorIJK)
    #     #     (m, v, buffer) = args
    #     #     return UnwritableMatrixIJK.mxv(m, v, buffer)
    #     else:
    #         raise Exception
