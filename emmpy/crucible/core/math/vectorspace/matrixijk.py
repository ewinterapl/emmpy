"""A square 3-D matrix in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.matrices.matrix3d import Matrix3D

# Map matrix component names to indices.
components = {'ii': (0, 0), 'ij': (0, 1), 'ik': (0, 2),
              'ji': (1, 0), 'jj': (1, 1), 'jk': (1, 2),
              'ki': (2, 0), 'kj': (2, 1), 'kk': (2, 2)}


class MatrixIJK(Matrix3D):
    """A square 3-D matrix in Cartesian (i, j, k) coordinates.

    The elements of the matrix are referred to by name as:

    ii ij ik
    ji jj jk
    ki kj kk
    """

    def __new__(cls, *args):
        """Create a new MatrixIJK object.

        Allocate a new MatrixIJK object by allocating a new Matrix3D
        object on which the MatrixIJK will expand.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic constructor.
        data : list or tuple of (list or tuple) of float
            Values for matrix elements in row-major order. Array must
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
        ii, ij, ik, ji, jj, jk, ki, kj, kk : float
            Elements of new matrix in row-major order.

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
            elif isinstance(args[0], np.ndarray):
                # Initialize the matrix by copying the values from the
                # upper 3x3 block of an existing Numpy array.
                (matrix,) = args
                data = matrix[:3, :3].flatten()
            else:
                raise ValueError
        elif len(args) == 2:
            # Create a new matrix by applying a scalar factor to the
            # components of an existing matrix.
            (scale, matrix) = args
            data = matrix.flatten()*scale
        elif len(args) == 3:
            # Creates a new matrix by populating the columns of the matrix
            # with the supplied vectors.
            (ithColumn, jthColumn, kthColumn) = args
            data = np.vstack([ithColumn, jthColumn, kthColumn]).T.flatten()
        elif len(args) == 4:
            # Creates a new matrix by applying scalar multiples to each
            # column of an existing matrix.
            (scaleI, scaleJ, scaleK, matrix) = args
            scales = (scaleI, scaleJ, scaleK)
            data = (scales*matrix).flatten()
        elif len(args) == 6:
            # Creates a new matrix by populating the columns of the matrix
            # with scaled versions of the supplied vectors
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            scales = (scaleI, scaleJ, scaleK)
            matrix = np.vstack([ithColumn, jthColumn, kthColumn]).T
            data = (scales*matrix).flatten()
        elif len(args) == 9:
            # Constructs a matrix from the nine basic components.
            data = args
        else:
            raise ValueError
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
        self.ii = val

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
        self.ji = val

    def setKI(self, val):
        """Set the kth row, ith column component.

        Set the (k, i) = (2, 0) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self.ki = val

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
        self.ij = val

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
        self.jj = val

    def setKJ(self, val):
        """Set the kth row, jth column component.

        Set the (k, j) = (2, 1) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self.kj = val

    def setIK(self, val):
        """Set the ith row, kth column component.

        Set the (i, k) = (0, 2) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self.ik = val

    def setJK(self, val):
        """Set the jth row, kth column component.

        Set the (j, k) = (1, 2) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self.jk = val

    def setKK(self, val):
        """Set the kth row, kth column component.

        Set the (k, k) = (2, 2) element of the matrix.

        Parameters
        ----------
        val : int or float
            Value to assign to the element.

        Returns
        -------
        None
        """
        self.kk = val

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
        column : VectorIJK
            Vector whose components are to replace the ith column of this
            matrix

        Returns
        -------
        None
        """
        self[:, 0] = column[:]

    def setJthColumn(self, column):
        """Set the jth column to the supplied vector.

        Parameters
        ----------
        column : VectorIJK
            Vector whose components are to replace the jth column of this
            matrix

        Returns
        -------
        None
        """
        self[:, 1] = column[:]

    def setKthColumn(self, column):
        """Set the kth column to the supplied vector.

        Parameters
        ----------
        column : VectorIJK
            Vector whose components are to replace the kth column of this
            matrix

        Returns
        -------
        None
        """
        self[:, 2] = column[:]

    def setColumn(self, columnIndex, column):
        """Set the column at a specified index to the supplied vector.

        Parameters
        ----------
        columnIndex : integer
            Index of column to set.
        column : VectorIJK
            Vector whose components are to replace the specified column of
            this matrix

        Returns
        -------
        None
        """
        self[:, columnIndex] = column[:]

    def setTo(self, *args):
        """Set the matrix components.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic method.
        data : (list or tuple) of (list or tuple) of int or float, or MatrixIJK
            Array of values to set the matrix; upper 3x3 block used.
        column : VectorIJK
            Vector whose components are to replace the specified column of
            this matrix
        OR
        scale : float
            The scale factor to apply to matrix.
        matrix : MatrixIJK
            The matrix to scale.
        OR
        ithColumn, jthColumn, kthColumn : VectorIJK
            Vectors to use as matrix columns.
        OR
        scaleI, scaleJ, scaleK : float
            Scale factors for cokumns in matrix.
        matrix : MatrixIJK
            The matrix to scale.
        OR
        scaleI, ithColumn
            Scale factor and vector for ith column.
        scaleJ, jthColumn
            Scale factor and vector for jth column.
        scaleK, kthColumn
            Scale factor and vector for kth column.
        OR
        ii, ji, ki, ij, jj, kj, ik, jk, kk : float
            Values to set matrix.

        Returns
        -------
        self : MatrixIJK
            Current object, for convenience.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (data,) = args
            # Use the upper 3x3 block of values - list, tuple, or MatrixIJK
            data = np.array(data[:3][:3])
            self[:] = data[:]
        elif len(args) == 2:
            # Sets the contents of this matrix to a scaled version of the
            # supplied matrix
            (scale, matrix) = args
            self[:] = scale*matrix[:]
        elif len(args) == 3:
            # Sets the columns of this matrix to the three specified vectors.
            (ithColumn, jthColumn, kthColumn) = args
            self[:, 0] = ithColumn[:]
            self[:, 1] = jthColumn[:]
            self[:, 2] = kthColumn[:]
        elif len(args) == 4:
            # Sets the contents of this matrix to a column-wise scaled version
            # of the supplied matrix
            (scaleI, scaleJ, scaleK, matrix) = args
            self[:, 0] = scaleI*matrix[:, 0]
            self[:, 1] = scaleJ*matrix[:, 1]
            self[:, 2] = scaleK*matrix[:, 2]
        elif len(args) == 6:
            # Sets the columns of this matrix to the scaled versions of the
            # supplied vectors.
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            self[:, 0] = scaleI*ithColumn[:]
            self[:, 1] = scaleJ*jthColumn[:]
            self[:, 2] = scaleK*kthColumn[:]
        elif len(args) == 9:
            # Sets the components of this matrix to the supplied components
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            data = np.array((ii, ji, ki, ij, jj, kj, ik, jk, kk)
                            ).reshape((3, 3)).T
            self[:, :] = data[:, :]
        else:
            raise ValueError
        return self

    def transposeInPlace(self):
        """Transpose the matrix in-place.

        Transpose the matrix in-place.

        Returns
        -------
        self : MatrixIJK
            The matrix, transposed.
        """
        self[:, :] = self.T[:, :]
        return self

    def unitizeColumns(self):
        """Convert each column to a unit vector.

        Unitize the columns of the matrix in-place.

        Returns
        -------
        self : MatrixIJK
            The current object, for convenience.
        """
        for col in range(3):
            length = np.linalg.norm(self[:, col])
            self[:, col] /= length
        return self

    def invert(self):
        """Invert the matrix in-place.

        Invert the matrix in-place.

        Returns
        -------
        self : MatrixIJK
            The current object, for convenience.
        """
        self[:] = np.linalg.inv(self)[:]
        return self

    def invort(self):
        """Invert, in place, this matrix whose columns are orthogonal.

        Invert the matrix in-place, assuming the columns are orthogonal.

        Note: No checks are done to verify that the columns are orthogonal.

        Returns
        -------
        self : MatrixIJK
            The current object, for convenience.
        """
        self.transposeInPlace()
        for row in range(3):
            length = computeNorm(self[row, 0], self[row, 1], self[row, 2])
            self[row, :] /= length**2
        return self

    def scale(self, *args):
        """Scale the matrix.

        Scale the matrix in-place, either as a unit, or by column.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic method.
        scale : float
            Scale factor to apply to all elements of the matrix.
        OR
        scaleI, scaleJ, scaleK : float
            Scale factors to apply to columns i, j, k.

        Returns
        -------
        self : MatrixIJK
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
        elif len(args) == 3:
            # Scales each column of the matrix by the supplied factors.
            (scaleI, scaleJ, scaleK) = args
            self[:, 0] *= scaleI
            self[:, 1] *= scaleJ
            self[:, 2] *= scaleK
        else:
            raise ValueError
        return self

    def createTranspose(self):
        """Create a transposed copy of the matrix.

        Return the tranpose of the matrix.

        Returns
        -------
        m : MatrixIJK
            The transpose of the matrix.
        """
        m = MatrixIJK(self)
        m.transposeInPlace()
        return m

    def createUnitizedColumns(self):
        """Create a copy of the matrix with unitized columns.

        Create a copy of the matrix with unitized columns.

        Returns
        -------
        m : MatrixIJK
            A copy of the matrix with unitized columns.
        """
        m = MatrixIJK(self)
        m.unitizeColumns()
        return m

    def createInverse(self):
        """Create an inverted copy of the matrix.

        Create an inverted copy of the matrix.

        Returns
        -------
        m : MatrixIJK
            An inverted copy of the matrix.
        """
        m = MatrixIJK(self)
        m.invert()
        return m

    def createInvorted(self):
        """Create an invorted copy of the matrix.

        Create an invorted copy of the matrix.

        Returns
        -------
        m : MatrixIJK
            An invorted copy of the matrix.
        """
        m = MatrixIJK(self)
        m.invort()
        return m

    def setToTranspose(self, matrix):
        """Set this matrix to the transpose of another.

        Set this matrix to the transpose of another.

        Parameters
        ----------
        matrix : MatrixIJK
            Matrix to copy and transpose.

        Returns
        -------
        self : MatrixIJK
            The current object, for convenience.
        """
        self.setTo(matrix)
        self.transposeInPlace()
        return self

    def setToUnitizedColumns(self, matrix):
        """Set this matrix to the unitized columns of another.

        Set this matrix to the unitized columns of another.

        Parameters
        ----------
        matrix : MatrixIJK
            Matrix to copy and unitize.

        Returns
        -------
        self : MatrixIJK
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
        matrix : MatrixIJK
            Matrix to copy and invert.

        Returns
        -------
        self : MatrixIJK
            The current object, for convenience.
        """
        self.setTo(matrix)
        self.invert()
        return self

    def setToInvorted(self, matrix):
        """Set this matrix to the inverse of another, presumed orthogonal.

        Set this matrix to the inverse of another, presumed orthogonal.

        Parameters
        ----------
        matrix : MatrixIJK
            Matrix to copy and invert.

        Returns
        -------
        self : MatrixIJK
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
        matrix : MatrixIJK
            The matrix to add to this matrix.
        buffer : MatrixIJK (optional)
            Buffer to hold the matrix sum.

        Returns
        -------
        buffer : MatrixIJK
            The matrix sum.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJK()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = (self + matrix)[:, :]
        return buffer

    def subtract(self, *args):
        """Subtract a matrix from this matrix.

        Subtract a matrix from this matrix.

        Parameters
        ----------
        matrix : MatrixIJK
            The matrix to subtract.
        buffer : MatrixIJK (optional)
            Buffer to hold the matrix difference.

        Returns
        -------
        buffer : MatrixIJK
            The matrix difference.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJK()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = (self - matrix)[:, :]
        return buffer

    def mxm(self, *args):
        """Compute the product of this matrix with another.

        Compute the product of this matrix with another.

        Parameters
        ----------
        matrix : MatrixIJK
            The second matrix.
        buffer : MatrixIJK (optional)
            Buffer to hold the matrix product.

        Returns
        -------
        buffer : MatrixIJK
            The matrix product.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJK()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self.dot(matrix)[:, :]
        return buffer

    def mxmt(self, *args):
        """Compute the product of this matrix with the transpose of another.

        Compute the product of this matrix with the transpose of another.

        Parameters
        ----------
        matrix : MatrixIJK
            The second matrix.
        buffer : MatrixIJK (optional)
            Buffer to hold the matrix product.

        Returns
        -------
        buffer : MatrixIJK
            The matrix product.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJK()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self.dot(matrix.T)[:, :]
        return buffer

    def mtxm(self, *args):
        """Compute the product of this transpose with another matrix.

        Compute the product of this transpose with another matrix.

        Parameters
        ----------
        matrix : MatrixIJK
            The second matrix.
        buffer : MatrixIJK (optional)
            Buffer to hold the matrix product.

        Returns
        -------
        buffer : MatrixIJK
            The matrix product.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (matrix,) = args
            buffer = MatrixIJK()
        elif len(args) == 2:
            (matrix, buffer) = args
        else:
            raise ValueError
        buffer[:, :] = self.T.dot(matrix)[:, :]
        return buffer

    @staticmethod
    def mxmadd(*args):
        """Compute the sum of the products of two pairs of matrices.

        Compute the sum of the products of two pairs of matrices.

        Parameters
        ----------
        a, b : MatrixIJK
            The first matrix pair.
        c, d : MatrixIJK
            The second matrix pair.
        buffer : MatrixIJK (optional)
            Buffer to hold the sum.

        Returns
        -------
        buffer : MatrixIJK
            The sum of the matrix products.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 4:
            (a, b, c, d) = args
            buffer = MatrixIJK()
        elif len(args) == 5:
            (a, b, c, d, buffer) = args
        else:
            raise ValueError
        m1 = a.dot(b)
        m2 = c.dot(d)
        m3 = m1 + m2
        buffer[:, :] = m3[:, :]
        return buffer

    @staticmethod
    def mxmtadd(*args):
        """Sum the products of two pairs of matrices, second transposed.

        Compute the sum of the products of two pairs of matrices, second
        transposed.

        Parameters
        ----------
        a, b : MatrixIJK
            The first matrix pair.
        c, d : MatrixIJK
            The second matrix pair.
        buffer : MatrixIJK (optional)
            Buffer to hold the sum.

        Returns
        -------
        buffer : MatrixIJK
            The sum of the matrix products.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 4:
            (a, b, c, d) = args
            buffer = MatrixIJK()
        elif len(args) == 5:
            (a, b, c, d, buffer) = args
        else:
            raise ValueError
        m1 = a.dot(b.T)
        m2 = c.dot(d.T)
        m3 = m1 + m2
        buffer[:, :] = m3[:, :]
        return buffer

    @staticmethod
    def mtxmadd(*args):
        """Sum of the products of two pairs of matrices, first transposed.

        Compute the sum of the products of two pairs of matrices, former
        transposed.

        Parameters
        ----------
        a, b : MatrixIJK
            The first matrix pair.
        c, d : MatrixIJK
            The second matrix pair.
        buffer : MatrixIJK (optional)
            Buffer to hold the sum.

        Returns
        -------
        buffer : MatrixIJK
            The sum of the matrix products.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 4:
            (a, b, c, d) = args
            buffer = MatrixIJK()
        elif len(args) == 5:
            (a, b, c, d, buffer) = args
        else:
            raise ValueError
        m1 = a.T.dot(b)
        m2 = c.T.dot(d)
        m3 = m1 + m2
        buffer[:, :] = m3[:, :]
        return buffer

    def mxv(self, *args):
        """Compute the product of this matrix with a vector.

        Compute the product of this matrix with a vector.

        Parameters
        ----------
        vector : VectorIJK
            The vector.
        buffer : VectorIJK
            Buffer to hold the vector result.

        Returns
        -------
        buffer : VectorIJK
            The vector result.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (vector,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (vector, buffer) = args
        else:
            raise ValueError
        v = self.dot(vector)
        buffer[:] = v[:]
        return buffer

    def mtxv(self, *args):
        """Compute the product of this transpose with a vector.

        Compute the product of this transpose with a vector.

        Parameters
        ----------
        vector : VectorIJK
            The vector.
        buffer : VectorIJK
            Buffer to hold the vector result.

        Returns
        -------
        buffer : VectorIJK
            The vector result.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (vector,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (vector, buffer) = args
        else:
            raise ValueError
        v = self.T.dot(vector)
        buffer[:] = v[:]
        return buffer
