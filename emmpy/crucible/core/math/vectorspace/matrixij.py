"""A square 2-D matrix in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


# from math import sqrt

import numpy as np

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.math.matrices.matrix2d import Matrix2D
from emmpy.utilities.isrealnumber import isRealNumber


# Map matrix component names to indices.
components = {'ii': (0, 0), 'ij': (0, 1),
              'ji': (1, 0), 'jj': (1, 1)}


class MatrixIJ(Matrix2D):
    """A square 2-D matrix in Cartesian (i, j) coordinates.

    The elements of the matrix are referred to by name as:

    ii ij
    ji jj
    """

    # # The matrix whose components are all zero.
    # ZEROS = UnwritableMatrixIJ(0, 0, 0, 0)

    # # The matrix whose components are all ones.
    # ONES = UnwritableMatrixIJ(1, 1, 1, 1)

    # # The multiplicative identity.
    # IDENTITY = UnwritableMatrixIJ(1, 0, 0, 1)

    def __init__(self, *args):
        """Initialize a new MatrixIJ object.

        Initialize a new MatrixIJ object.

        Parameters
        ----------
        a : 2x2 array-like of float, optional, default 2x2 None
            Values for matrix elements in row-major order.
        OR
        scale : float
            The scale factor to apply.
        a : 2x2 array-like of float
            The array whose components are to be scaled and copied.
        # OR
        # colI, colJ, colK : array-like of 3 float
        #     3-element array-likes containing the columns to use for the matrix.
        # OR
        # scaleI, scaleJ, scaleK : float
        #     Scale factors to apply to the ith, jth, kth columns.
        # a : 3x3 array-like of float
        #     The array whose components are to be scaled and copied.
        # OR
        # scaleI : float
        #     The scale factor to apply to the ith column.
        # colI : array-like of 3 float
        #     The vector containing the ith column.
        # scaleJ : float
        #     The scale factor to apply to the jth column.
        # colJ : array-like of 3 float
        #     The vector containing the jth column.
        # scaleK : float
        #     The scale factor to apply to the kth column.
        # colK : array-like of 3 float
        #     The vector containing the kth column.
        # OR
        # ii, ij, ik, ji, jj, jk, ki, kj, kk : float
        #     Elements of new matrix in row-major order.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Construct an empty matrix.
            self[:, :] = np.array((None,)*4).reshape((2, 2))
        elif len(args) == 1:
            # Initialize matrix from a 2x2 array-like of floats.
            (a,) = args
            self[:, :] = np.array(a)
        elif len(args) == 2:
            if isRealNumber(args[0]):
                # Scale an existing array-like.
                (scale, a) = args
                self[:, :] = scale*np.array(a)
            else:
                # Column vectors
                (ithColumn, jthColumn) = args
                self[:, 0] = ithColumn
                self[:, 1] = jthColumn
        elif len(args) == 3:
            # Column scaling constructor, creates a new matrix by applying
            # scalar multiples to each column of a pre-existing matrix.
            (scaleI, scaleJ, matrix) = args
            self[:, 0] = scaleI*matrix[:, 0]
            self[:, 1] = scaleJ*matrix[:, 1]
        elif len(args) == 4:
            if (isRealNumber(args[0]) and isRealNumber(args[1]) and
                isRealNumber(args[2]) and isRealNumber(args[3])):
                # Constructs a matrix from the four basic components.
                (ii, ij, ji, jj) = args
                self[:, :] = [[ii, ij], [ji, jj]]
            else:
                # Scaled column vector constructor, creates a new matrix by
                # populating the columns of the matrix with scaled versions of
                # the supplied vectors
                # @param scaleI the scale factor to apply to the ith column
                # @param ithColumn the vector containing the ith column
                # @param scaleJ the scale factor to apply to the jth column
                # @param jthColumn the vector containing the jth column
                (scaleI, ithColumn, scaleJ, jthColumn) = args
                self[:, 0] = scaleI*ithColumn[:]
                self[:, 1] = scaleJ*jthColumn[:]
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

        Returns
        -------
        None
        """
        self[components[name]] = value

    def setII(self, val):
        """Set the ith row, ith column component.

        Set the (i, i) = (0, 0) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self[0, 0] = val

    def setJI(self, val):
        """Set the jth row, ith column component.

        Set the (j, i) = (1, 0) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self[1, 0] = val

    def setIJ(self, val):
        """Set the ith row, jth column component.

        Set the (i, j) = (0, 1) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self[0, 1] = val

    def setJJ(self, val):
        """Set the jth row, jth column component.

        Set the (j, j) = (1, 1) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self[1, 1] = val

    def set(self, row, column, val):
        """Set the component for the specified row and column.

        Parameters
        ----------
        row : int
            Row of element to set
        column : int
            Column of element to set
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self[row, column] = val

    def setIthColumn(self, column):
        """Set the ith column to the supplied vector.

        Parameters
        ----------
        column : array-like of 2 float
            Vector whose components are to replace the ith column of this
            matrix

        Returns
        -------
        None
        """
        self[:, 0] = list(column)

    def setJthColumn(self, column):
        """Set the jth column to the supplied vector.

        Parameters
        ----------
        column : array-like of 2 float
            Vector whose components are to replace the jth column of this
            matrix

        Returns
        -------
        None
        """
        self[:, 1] = list(column)

    def setColumn(self, columnIndex, column):
        """Set the column at a specified index to the supplied vector.

        Parameters
        ----------
        columnIndex : integer
            Index of column to set.
        column : array-like of 2 float
            Vector whose components are to replace the specified column of
            this matrix

        Returns
        -------
        None
        """
        self[:, columnIndex] = list(column)

    def setTo(self, *args):
        """Set the matrix components.

        Parameters
        ----------
        a : array-like
            2x2 array of values to set the matrix.
        OR
        scale : float
            The scale factor to apply to array.
        a : array-like
            The 2x2 array to scale.
        OR
        colI, colJ : array-like
            2-element array-likes to use as matrix columns.
        OR
        scaleI, scaleJ : float
            Scale factors for cokumns in matrix.
        matrix : array-like
            2x2 array to scale.
        OR
        scaleI, colI
            Scale factor and vector for ith column.
        scaleJ, colJ
            Scale factor and vector for jth column.
        OR
        ii, ij, ji, jj : float
            Values to set matrix, row-major order.

        Returns
        -------
        self : MatrixIJ
            Current object, for convenience.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (a,) = args
            # Set to a 2x2 array-like of float.
            self[:, :] = np.array(a)
        elif len(args) == 2:
            if isRealNumber(args[0]):
                # Set to a scaled version of the 2x2 array-like.
                (scale, a) = args
                self[:, :] = scale*np.array(a)
            else:
                # Set the columns to 2 array-like.
                (colI, colJ) = args
                self[:, 0] = np.array(colI)
                self[:, 1] = np.array(colJ)
        elif len(args) == 3:
            # Scale the provided array-like by columns.
            (scaleI, scaleJ, a_in) = args
            a = np.array(a_in)
            self[:, 0] = scaleI*a[:, 0]
            self[:, 1] = scaleJ*a[:, 1]
        elif len(args) == 4:
            if isRealNumber(args[0]) and isRealNumber(args[1]) and isRealNumber(args[2]) and isRealNumber(args[3]):
                # Sets the components of this matrix to the supplied components
                (ii, ij, ji, jj) = args
                data = np.array((ii, ij, ji, jj)).reshape((2, 2)).T
                self[:, :] = data
            else:
                # Scale 2 array-likes for the columns.
                (scaleI, colI, scaleJ, colJ) = args
                self[:, 0] = scaleI*np.array(colI)
                self[:, 1] = scaleJ*np.array(colJ)
        else:
            raise ValueError
        return self

    def transposeInPlace(self):
        """Transpose the matrix in-place.

        Transpose the matrix in-place.

        Returns
        -------
        self : MatrixIJ
            The matrix, transposed.
        """
        self[:, :] = self.T
        return self

    def unitizeColumns(self):
        """Convert each column to a unit vector.

        Unitize the columns of the matrix in-place.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        for col in range(2):
            length = np.linalg.norm(self[:, col])
            self[:, col] /= length
        return self

    def invert(self):
        """Invert the matrix in-place.

        Invert the matrix in-place.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        self[:] = np.linalg.inv(self)
        return self

    def invort(self):
        """Invert, in place, this matrix whose columns are orthogonal.

        Invert the matrix in-place, assuming the columns are orthogonal.

        Note: No checks are done to verify that the columns are orthogonal.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        self.transposeInPlace()
        for row in range(2):
            length = computeNorm(self[row, 0], self[row, 1])
            self[row, :] /= length**2
        return self

    def scale(self, *args):
        """Scale the matrix in-place.

        Scale the matrix in-place, either as a unit, or by column.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic method.
        scale : float
            Scale factor to apply to all elements of the matrix.
        OR
        scaleI, scaleJ : float
            Scale factors to apply to columns i, j.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            # Scales each component of the matrix by the supplied factor.
            (scale,) = args
            self[:] *= scale
        elif len(args) == 2:
            # Scales each column of the matrix by the supplied factors.
            (scaleI, scaleJ) = args
            self[:, 0] *= scaleI
            self[:, 1] *= scaleJ
        else:
            raise ValueError
        return self

    def createTranspose(self):
        """Create a transposed copy of the matrix.

        Return the tranpose of the matrix.

        Returns
        -------
        m : MatrixIJ
            The transpose of the matrix.
        """
        m = MatrixIJ(self)
        m.transposeInPlace()
        return m

    def createUnitizedColumns(self):
        """Create a copy of the matrix with unitized columns.

        Create a copy of the matrix with unitized columns.

        Returns
        -------
        m : MatrixIJ
            A copy of the matrix with unitized columns.
        """
        m = MatrixIJ(self)
        m.unitizeColumns()
        return m

    def createInverse(self):
        """Create an inverted copy of the matrix.

        Create an inverted copy of the matrix.

        Returns
        -------
        m : MatrixIJ
            An inverted copy of the matrix.
        """
        m = MatrixIJ(self)
        m.invert()
        return m

    def createInvorted(self):
        """Create an invorted copy of the matrix.

        Create an invorted copy of the matrix.

        Returns
        -------
        m : MatrixIJ
            An invorted copy of the matrix.
        """
        m = MatrixIJ(self)
        m.invort()
        return m

    def setToTranspose(self, matrix):
        """Set this matrix to the transpose of another.

        Set this matrix to the transpose of another.

        Parameters
        ----------
        matrix : MatrixIJ
            Matrix to copy and transpose.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        self[:, :] = matrix.T
        return self

    def setToUnitizedColumns(self, matrix):
        """Set this matrix to the unitized columns of another.

        Set this matrix to the unitized columns of another.

        Parameters
        ----------
        matrix : MatrixIJ
            Matrix to copy and unitize.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        self.setTo(matrix)
        self.unitizeColumns()
        return self

    def setToInverse(self, matrix):
        """Set this matrix to the inverse of another.

        Set this matrix to the inverse of another.

        Parameters
        ----------
        matrix : MatrixIJ
            Matrix to copy and invert.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        self[:, :] = np.linalg.inv(matrix)
        return self

    def setToInvorted(self, matrix):
        """Set this matrix to the inverse of another, presumed orthogonal.

        Set this matrix to the inverse of another, presumed orthogonal.

        Parameters
        ----------
        matrix : MatrixIJ
            Matrix to copy and invert.

        Returns
        -------
        self : MatrixIJ
            The current object, for convenience.
        """
        self.setTo(matrix)
        self.invort()
        return self

    def add(self, *args):
        """Compute sum of this matrix with another.

        Compute the sum of this matrix with another.

        Parameters
        ----------
        matrix : MatrixIJ
            The matrix to add to this matrix.
        buffer : MatrixIJ, optional
            Buffer to hold the matrix sum.

        Returns
        -------
        buffer : MatrixIJ
            The matrix sum.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJ()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self + matrix
        return buffer

    def subtract(self, *args):
        """Subtract a matrix from this matrix.

        Subtract a matrix from this matrix.

        Parameters
        ----------
        matrix : MatrixIJ
            The matrix to subtract.
        buffer : MatrixIJ, optional
            Buffer to hold the matrix difference.

        Returns
        -------
        buffer : MatrixIJ
            The matrix difference.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJ()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self - matrix
        return buffer

    def mxm(self, *args):
        """Compute the matrix product of this matrix with another.

        Compute the product of this matrix with another.

        Parameters
        ----------
        matrix : MatrixIJ
            The second matrix.
        buffer : MatrixIJ, optional
            Buffer to hold the matrix product.

        Returns
        -------
        buffer : MatrixIJ
            The matrix product.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJ()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self.dot(matrix)
        return buffer

    def mxmt(self, *args):
        """Compute the matrix product of this matrix with the transpose of another.

        Compute the product of this matrix with the transpose of another.

        Parameters
        ----------
        matrix : MatrixIJ
            The second matrix.
        buffer : MatrixIJ, optional
            Buffer to hold the matrix product.

        Returns
        -------
        buffer : MatrixIJ
            The matrix product.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJ()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self.dot(matrix.T)
        return buffer

    def mtxm(self, *args):
        """Compute the matrix product of this transpose with another matrix.

        Compute the product of this transpose with another matrix.

        Parameters
        ----------
        matrix : MatrixIJ
            The second matrix.
        buffer : MatrixIJ, optional
            Buffer to hold the matrix product.

        Returns
        -------
        buffer : MatrixIJ
            The matrix product.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJ()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self.T.dot(matrix)
        return buffer

    @staticmethod
    def mxmadd(*args):
        """Compute the sum of the products of two pairs of matrices.

        Compute the sum of the products of two pairs of matrices.

        Parameters
        ----------
        a, b : MatrixIJ
            The first matrix pair.
        c, d : MatrixIJ
            The second matrix pair.
        buffer : MatrixIJ, optional
            Buffer to hold the sum.

        Returns
        -------
        buffer : MatrixIJ
            The sum of the matrix products.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 4:
            (a, b, c, d) = args
            buffer = MatrixIJ()
        elif len(args) == 5:
            (a, b, c, d, buffer) = args
        else:
            raise ValueError
        m1 = a.dot(b)
        m2 = c.dot(d)
        m3 = m1 + m2
        buffer[:, :] = m3
        return buffer

    @staticmethod
    def mxmtadd(*args):
        """Sum the products of two pairs of matrices, second transposed.

        Compute the sum of the products of two pairs of matrices, second
        transposed.

        Parameters
        ----------
        a, b : MatrixIJ
            The first matrix pair.
        c, d : MatrixIJ
            The second matrix pair.
        buffer : MatrixIJ, optional
            Buffer to hold the sum.

        Returns
        -------
        buffer : MatrixIJ
            The sum of the matrix products.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 4:
            (a, b, c, d) = args
            buffer = MatrixIJ()
        elif len(args) == 5:
            (a, b, c, d, buffer) = args
        else:
            raise ValueError
        m1 = a.dot(b.T)
        m2 = c.dot(d.T)
        m3 = m1 + m2
        buffer[:, :] = m3
        return buffer

    @staticmethod
    def mtxmadd(*args):
        """Sum of the products of two pairs of matrices, first transposed.

        Compute the sum of the products of two pairs of matrices, former
        transposed.

        Parameters
        ----------
        a, b : MatrixIJ
            The first matrix pair.
        c, d : MatrixIJ
            The second matrix pair.
        buffer : MatrixIJ, optional
            Buffer to hold the sum.

        Returns
        -------
        buffer : MatrixIJ
            The sum of the matrix products.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 4:
            (a, b, c, d) = args
            buffer = MatrixIJ()
        elif len(args) == 5:
            (a, b, c, d, buffer) = args
        else:
            raise ValueError
        m1 = a.T.dot(b)
        m2 = c.T.dot(d)
        m3 = m1 + m2
        buffer[:, :] = m3
        return buffer

    def mxv(self, *args):
        """Compute the product of this matrix with a vector.

        Compute the product of this matrix with a vector.

        Parameters
        ----------
        vector : VectorIJ
            The vector.
        buffer : VectorIJ, optional
            Buffer to hold the vector result.

        Returns
        -------
        buffer : VectorIJ
            The vector result.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (vector,) = args
            buffer = VectorIJ()
        elif len(args) == 2:
            (vector, buffer) = args
        else:
            raise ValueError
        v = self.dot(vector)
        buffer[:] = v
        return buffer

    def mtxv(self, *args):
        """Compute the product of this transpose with a vector.

        Compute the product of this transpose with a vector.

        Parameters
        ----------
        vector : VectorIJ
            The vector.
        buffer : VectorIJ, optional
            Buffer to hold the vector result.

        Returns
        -------
        buffer : VectorIJ
            The vector result.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (vector,) = args
            buffer = VectorIJ()
        elif len(args) == 2:
            (vector, buffer) = args
        else:
            raise ValueError
        v = self.T.dot(vector)
        buffer[:] = v
        return buffer
