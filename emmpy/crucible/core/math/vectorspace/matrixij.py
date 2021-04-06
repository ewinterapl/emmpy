"""matrixij.py
"""


from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
from emmpy.java.lang.illegalargumentexception import IllegalArgumentException
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)
from math import sqrt

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.utilities.isrealnumber import isRealNumber
from emmpy.crucible.core.math.vectorspace.unwritablematrixij import (
    UnwritableMatrixIJ
)


class MatrixIJ(UnwritableMatrixIJ):
    """A writable subclass of the unwritable 3D matrix parent completing one
    link in the weak-immutability design pattern.

    This class contains the mutator methods necessary to set or alter the
    internals of the parent classes fields.

    @author G.K.Stephens copy and extension of F.S.Turner
    """

    # The matrix whose components are all zero.
    ZEROS = UnwritableMatrixIJ(0, 0, 0, 0)

    # The matrix whose components are all ones.
    ONES = UnwritableMatrixIJ(1, 1, 1, 1)

    # The multiplicative identity.
    IDENTITY = UnwritableMatrixIJ(1, 0, 0, 1)

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 0:
            # Construct a matrix with an initial value of {@link #IDENTITY}.
            UnwritableMatrixIJ.__init__(self, self.IDENTITY)
        elif len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a matrix from the upper two by two block of a two
                # dimensional array of doubles.
                # @param data the array of doubles
                # @throws IndexOutOfBoundsException if the supplied data array
                # does not contain at least two arrays of arrays of length
                # two or greater.
                (data,) = args
                UnwritableMatrixIJ.__init__(self, data)
            elif isinstance(args[0], UnwritableMatrixIJ):
                # Copy constructor, creates a matrix by copying the values of a
                # pre-existing one.
                # @param matrix the matrix whose contents are to be copied.
                (matrix,) = args
                UnwritableMatrixIJ.__init__(self, matrix)
        elif len(args) == 2:
            if isRealNumber(args[0]) and isinstance(args[1],
                                                    UnwritableMatrixIJ):
                # Scaling constructor, creates a new matrix by applying a
                # scalar multiple to the components of a pre-existing matrix.
                # @param scale the scale factor to apply
                # @param matrix the matrix whose components are to be scaled
                # and copied
                (scale, matrix) = args
                UnwritableMatrixIJ.__init__(self, scale, matrix)
            elif (isinstance(args[0], UnwritableVectorIJ) and
                  isinstance(args[1], UnwritableVectorIJ)):
                # Column vector constructor, creates a new matrix by populating
                # the columns of the matrix with the supplied vectors.
                # @param ithColumn the vector containing the ith column
                # @param jthColumn the vector containing the jth column
                (ithColumn, jthColumn) = args
                UnwritableMatrixIJ.__init__(self, ithColumn, jthColumn)
        elif len(args) == 3:
            # Column scaling constructor, creates a new matrix by applying
            # scalar multiples to each column of a pre-existing matrix.
            # @param scaleI the scale factor to apply to the ith column
            # @param scaleJ the scale factor to apply to the jth column
            # @param matrix the matrix whose columns are to be scaled and
            # copied
            (scaleI, scaleJ, matrix) = args
            UnwritableMatrixIJ.__init__(self, scaleI, scaleJ, matrix)
        elif len(args) == 4:
            if (isRealNumber(args[0]) and isRealNumber(args[1]) and
                isRealNumber(args[2]) and isRealNumber(args[3])):
                # Constructs a matrix from the four basic components.
                # @param ii ith row, ith column element
                # @param ji jth row, ith column element
                # @param ij ith row, jth column element
                # @param jj jth row, jth column element
                (ii, ji, ij, jj) = args
                UnwritableMatrixIJ.__init__(self, ii, ji, ij, jj)
            elif (isRealNumber(args[0]) and
                  isinstance(args[1], UnwritableVectorIJ) and
                  isRealNumber(args[2]) and
                  isinstance(args[3], UnwritableVectorIJ)):
                # Scaled column vector constructor, creates a new matrix by
                # populating the columns of the matrix with scaled versions of
                # the supplied vectors
                # @param scaleI the scale factor to apply to the ith column
                # @param ithColumn the vector containing the ith column
                # @param scaleJ the scale factor to apply to the jth column
                # @param jthColumn the vector containing the jth column
                (scaleI, ithColumn, scaleJ, jthColumn) = args
                UnwritableMatrixIJ.__init__(self,
                                            scaleI, ithColumn,
                                            scaleJ, jthColumn)

    def createTranspose(self):
        """Note: this method is overridden to return an instance of the
        writable subclass rather than the unwritable parent."""
        return MatrixIJ(self).transpose()

    def createUnitizedColumns(self):
        """Note: this method is overridden to return an instance of the
        writable subclass rather than the unwritable parent."""
        return MatrixIJ(self).unitizeColumns()

    def createInverse(self, *args):
        """Create a new inverse matrix"""
        if len(args) == 0:
            # Note: this method is overridden to return an instance of the
            # writable subclass rather than the unwritable parent.
            return MatrixIJ(self).invert()
        elif len(args) == 1:
            # Note: this method is overridden to return an instance of the
            # writable subclass rather than the unwritable parent.
            (tolerance,) = args
            return MatrixIJ(self).invert(tolerance)

    def createInvorted(self):
        """Note: this method is overridden to return an instance of the
        writable subclass rather than the unwritable parent.
        """
        return MatrixIJ(self).invort()

    def transpose(self):
        """Transpose the matrix.

        @return a reference to the instance for convenience, which now
        contains the transpose
        """
        tmp = self.ij
        self.ij = self.ji
        self.ji = tmp
        return self

    def unitizeColumns(self):
        """Modifies the elements of this matrix so that each column in the
        matrix becomes a unit vector

        @return a reference to the instance for convenience
        @throws UnsupportedOperationException if any of the columns are of
        length zero
        """
        self.setTo(VectorIJ(self.ii, self.ji).unitize(),
                   VectorIJ(self.ij, self.jj).unitize())
        return self

    def invert(self, *args):
        """Invert the matrix."""
        if len(args) == 0:
            # Invert the matrix if the determinant is not within the default
            # tolerance of zero.
            # @return a reference to the instance for convenience, which now
            # contains the multiplicative inverse
            # @throws UnsupportedOperationException if the determinant of the
            # instance is within {@link UnwritableMatrixIJ#INVERSION_TOLERANCE}
            # of 0.0.
            return self.invert(UnwritableMatrixIJ.INVERSION_TOLERANCE)
        elif len(args) == 1:
            # Invert the matrix if the determinant is within the supplied
            # tolerance of zero.
            # @param tolerance the absolute value of the determinant of the
            # instance must be greater than this for inversion to proceed
            # @return a reference to the instance for convenience, which now
            # contains the multiplicative inverse
            # @throws UnsupportedOperationException if the determinant of the
            # instance is within the supplied tolerance of 0.0.
            (tolerance,) = args
            det = self.getDeterminant()
            if abs(det) < tolerance:
                raise UnsupportedOperationException(
                    "Matrix nearly singular, unable to invert.")
            cii = self.jj/det
            cij = -self.ij/det
            cji = -self.ji/det
            cjj = self.ii/det
            return self.setTo(cii, cji, cij, cjj)

    def invort(self):
        """Invert, in place, this matrix whose columns are orthogonal.

        Note: No checks are done to verify that the columns are orthogonal.

        @return a reference to the instance for convenience
        @throws UnsupportedOperationException if the lengths of any of the
        columns are zero or too small to properly invert multiplicatively in
        the space available to double precision
        """
        self.transpose()

        length = computeNorm(self.ii, self.ij)
        if length*UnwritableMatrixIJ.INVORSION_BOUND < 1 or length == 0:
            raise UnsupportedOperationException(
                "ith column of matrix has length, " + length +
                ", for which there is no inverse.")
        self.ii /= length
        self.ii /= length
        self.ij /= length
        self.ij /= length

        length = computeNorm(self.ji, self.jj)
        if length*MatrixIJ.INVORSION_BOUND < 1 or length == 0:
            raise UnsupportedOperationException(
                "jth column of matrix has length, " + length +
                ", for which there is no inverse.")
        self.ji /= length
        self.ji /= length
        self.jj /= length
        self.jj /= length

        return self

    def scale(self, *args):
        """Scales each component of the matrix by the supplied factor."""

        if len(args) == 1:
            # @param scale the scale factor to apply
            # @return a reference to the instance which now contains the scaled
            # matrix.
            (scale,) = args
            self.ii *= scale
            self.ji *= scale
            self.ij *= scale
            self.jj *= scale
            return self
        elif len(args) == 2:
            # Scales each column of the matrix by the supplied factors.
            # @param scaleI the ith column scale
            # @param scaleJ the jth column scale
            # @return a reference to the instance for convenience which
            # contains the scaled matrix.
            (scaleI, scaleJ) = args
            self.ii *= scaleI
            self.ji *= scaleI
            self.ij *= scaleJ
            self.jj *= scaleJ
            return self

    def setII(self, ii):
        """Sets the ith row, ith column component."""
        self.ii = ii

    def setJI(self, ji):
        """Sets the jth row, ith column component."""
        self.ji = ji

    def setIJ(self, ij):
        """Sets the ith row, jth column component."""
        self.ij = ij

    def setJJ(self, jj):
        """Sets the jth row, jth column component."""
        self.jj = jj

    def set(self, row, column, value):
        """Sets the component for the specified row and column.

        @param row a row index in [0,1].
        @param column a column index in [0,1]
        @param value the value to place into the matrix at (row,column).
        @throws IllegalArgumentException if either the supplied row or column
        index are outside their acceptable ranges of [0,1].
        """
        if row == 0:
            if column == 0:
                self.ii = value
            elif column == 1:
                self.ij = value
            else:
                raise IllegalArgumentException(
                    "Unable to set element (" + row + ", " + column +
                    "). Column index invalid.")
        elif row == 1:
            if column == 0:
                self.ji = value
            elif column == 1:
                self.jj = value
            else:
                raise IllegalArgumentException(
                    "Unable to set element (" + row + ", " + column +
                    "). Column index invalid.")
        else:
            raise IllegalArgumentException(
                "Unable to set element (" + row + ", " + column +
                "). Row index invalid.")

    def setIthColumn(self, column):
        """Sets the ith column to the supplied vector.

        @param column the vector whose components are to replace the ith column
        of this matrix
        """
        self.ii = column.i
        self.ji = column.j

    def setJthColumn(self, column):
        """Sets the jth column to the supplied vector.

        @param column the vector whose components are to replace the jth column
        of this matrix
        """
        self.ij = column.i
        self.jj = column.j

    def setColumn(self, columnIndex, column):
        """Sets the column at a specified index to the supplied vector.

        @param columnIndex a column index in [0,1].
        @param column the vector whose components are to replace the specified
        column of this matrix
        @throws IllegalArgumentException if the supplied columnIndex is not in
        [0,1].
        """
        if columnIndex == 0:
            self.setIthColumn(column)
        elif columnIndex == 1:
            self.setJthColumn(column)
        else:
            raise IllegalArgumentException(
                "Unable to set column. Index: " + columnIndex + " is invalid.")

    def setTo(self, *args):
        """Sets the components of this matrix to the supplied components"""

        if len(args) == 1:
            if isinstance(args[0], list):
                # Sets the contents of this matrix to the upper 2x2 block of a
                # supplied two dimensional array of doubles
                # @param data the array to copy to the components of this
                # instance
                # @return a reference to this instance for convenience
                # @throws IndexOutOfBoundsException if the supplied data array
                # does not contain at least two arrays of arrays of length two
                # or greater.
                (data,) = args
                self.setTo(data[0][0], data[1][0], data[0][1], data[1][1])
                return self
            elif isinstance(args[0], UnwritableMatrixIJ):
                # Sets the contents of this matrix to match those of a supplied
                # matrix
                # @param matrix the matrix to copy
                # @return a reference to this instance for convenience that
                # contains the supplied components
                (matrix,) = args
                self.setTo(matrix.ii, matrix.ji, matrix.ij, matrix.jj)
                return self
        elif len(args) == 2:
            if isRealNumber(args[0]) and isinstance(args[1],
                                                    UnwritableMatrixIJ):
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
            elif (isinstance(args[0], UnwritableVectorIJ) and
                  isinstance(args[1], UnwritableVectorIJ)):
                # Sets the columns of this matrix to the three specified
                # vectors.
                # @param ithColumn the vector containing the contents to set
                # the ith column
                # @param jthColumn the vector containing the contents to set
                # the jth column
                # @return a reference to the instance for convenience
                (ithColumn, jthColumn) = args
                self.setTo(ithColumn.i, ithColumn.j, jthColumn.i, jthColumn.j)
                return self
        elif len(args) == 3:
            # Sets the contents of this matrix to a column-wise scaled version
            # of the supplied matrix
            # @param scaleI the scale factor to apply to the ith column of
            # matrix
            # @param scaleJ the scale factor to apply to the jth column of
            # matrix
            # @param matrix the matrix to scale
            # @return a reference to this instance for convenience that
            # contains the column scaled version of matrix
            (scaleI, scaleJ, matrix) = args
            self.setTo(matrix)
            self.scale(scaleI, scaleJ)
            return self
        elif len(args) == 4:
            if (isRealNumber(args[0]) and isRealNumber(args[1]) and
                isRealNumber(args[2]) and isRealNumber(args[3])):
                # Sets the components of this matrix to the supplied components
                # @param ii ith row, ith column element
                # @param ji jth row, ith column element
                # @param ij ith row, jth column element
                # @param jj jth row, jth column element
                # @return a reference to the instance, for convenience, that
                # contains the newly set matrix
                (ii, ji, ij, jj) = args
                self.ii = ii
                self.ji = ji
                self.ij = ij
                self.jj = jj
                return self
            elif (isRealNumber(args[0]) and
                  isinstance(args[1], UnwritableVectorIJ) and
                  isRealNumber(args[2]) and
                  isinstance(args[3], UnwritableVectorIJ)):
                # Sets the columns of this matrix to the scaled versions of
                # the supplied vectors.
                # @param scaleI scale factor to apply to ithColumn
                # @param ithColumn the ith column vector
                # @param scaleJ scale factor to apply to jthColumn
                # @param jthColumn the jth column vector
                # @return a reference to the instance for convenience
                (scaleI, ithColumn, scaleJ, jthColumn) = args
                self.setTo(scaleI*ithColumn.i, scaleI*ithColumn.j,
                           scaleJ*jthColumn.i, scaleJ*jthColumn.j)
                return self

    def setToTranspose(self, matrix):
        """Sets this matrix components to the transpose of the supplied matrix.

        @param matrix the matrix whose transpose is to be copied into the
        instance
        @return a reference to the instance for convenience
        """
        self.setTo(matrix)
        self.transpose()
        return self

    def setToUnitizedColumns(self, matrix):
        """Modifies the elements of this matrix so that each column in the
        matrix becomes a unit vector

        @return a reference to the instance for convenience
        @throws UnsupportedOperationException if any of the columns are of
        length zero
        """
        return self.setTo(matrix).unitizeColumns()

    def setToInverse(self, *args):
        """Sets the matrix components to the inverse of the supplied matrix."""
        if len(args) == 1:
            # @param matrix the matrix to invert
            # @return a reference to the instance containing the inverse of
            # matrix for convenience
            # @throws IllegalArgumentException if the determinant of matrix is
            # within {@link UnwritableMatrixIJ#INVERSION_TOLERANCE} of 0.0.
            (matrix,) = args
            det = matrix.getDeterminant()
            if abs(det) < UnwritableMatrixIJ.DETERMINANT_TOLERANCE:
                raise IllegalArgumentException(
                    "Matrix nearly singular, unable to invert.")
            self.setTo(matrix)
            self.invert()
            return self
        elif len(args) == 2:
            # Sets the matrix components to the inverse of the supplied matrix.
            # @param matrix the matrix to invert
            # @param tolerance the tolerance
            # @return a reference to the instance containing the inverse of
            # matrix for convenience
            # @throws IllegalArgumentException if the determinant of matrix is
            # within tolerance of 0.0.
            (matrix, tolerance) = args
            det = matrix.getDeterminant()
            if abs(det) < tolerance:
                raise IllegalArgumentException(
                    "Matrix nearly singular, unable to invert.")
            self.setTo(matrix)
            self.invert(tolerance)
            return self

    def setToInvorted(self, matrix):
        """Sets the instance to the inverse of the supplied matrix, assuming
        this matrix has columns that are orthogonal.

        @param matrix a matrix to invert, with orthogonal columns.
        @return a reference to the instance for convenience
        @throws UnsupportedOperationException if any of the columns are zero or
        too small to properly invert multiplicatively in the space available to
        double precision
        """
        return self.setTo(matrix).invort()

    @staticmethod
    def mxmt(*args):
        """Compute the product of a matrix with the transpose of another
        matrix."""
        if len(args) == 2:
            # @param a the left hand matrix
            # @param b the right hand matrix to transpose, then multiply
            # @return a new <code>MatrixIJ</code> containing the product.
            # @see MatrixIJ#mxmt(UnwritableMatrixIJ, UnwritableMatrixIJ,
            # MatrixIJ)
            (a, b) = args
            return MatrixIJ.mxmt(a, b, MatrixIJ())
        elif len(args) == 3:
            # @param a the left hand matrix
            # @param b the right hand matrix to transpose, then multiply
            # @param buffer the buffer to receive the product, a*transpose(b).
            # @return a reference to buffer for convenience.
            (a, b, buffer) = args
            ii = a.ii*b.ii + a.ij*b.ij
            ij = a.ii*b.ji + a.ij*b.jj
            ji = a.ji*b.ii + a.jj*b.ij
            jj = a.ji*b.ji + a.jj*b.jj
            buffer.ii = ii
            buffer.ij = ij
            buffer.ji = ji
            buffer.jj = jj
            return buffer

    @staticmethod
    def mtxm(*args):
        """Compute the product of a transpose of a matrix with another matrix.
        """
        if len(args) == 2:
            # @param a the left hand matrix to transpose, then multiply
            # @param b the right hand matrix
            # @return a new <code>MatrixIJ</code> containing the product
            # @see MatrixIJ#mtxm(UnwritableMatrixIJ, UnwritableMatrixIJ,
            # MatrixIJ)
            (a, b) = args
            return MatrixIJ.mtxm(a, b, MatrixIJ())
        elif len(args) == 3:
            # Compute the product of a transpose of a matrix with another
            # matrix.
            # @param a the left hand matrix to transpose, then multiply
            # @param b the right hand matrix
            # @param buffer the buffer to receive the product, transpose(a)*b.
            # @return a reference to buffer for convenience
            (a, b, buffer) = args
            ii = a.ii*b.ii + a.ji*b.ji
            ij = a.ii*b.ij + a.ji*b.jj
            ji = a.ij*b.ii + a.jj*b.ji
            jj = a.ij*b.ij + a.jj*b.jj
            buffer.ii = ii
            buffer.ij = ij
            buffer.ji = ji
            buffer.jj = jj
            return buffer

    @staticmethod
    def mxm(*args):
        """Compute the product of two matrices."""
        if len(args) == 2:
            # @param a the left hand matrix
            # @param b the right hand matrix
            # @return a new <code>MatrixIJ</code> containing the product (ab).
            # @see MatrixIJ#mxm(UnwritableMatrixIJ, UnwritableMatrixIJ,
            # MatrixIJ)
            (a, b) = args
            return MatrixIJ.mxm(a, b, MatrixIJ())
        elif len(args) == 3:
            # @param a the left hand matrix
            # @param b the right hand matrix
            # @param buffer the buffer to receive the product, a*b
            # @return a reference to buffer for convenience
            (a, b, buffer) = args
            ii = a.ii*b.ii + a.ij*b.ji
            ij = a.ii*b.ij + a.ij*b.jj
            ji = a.ji*b.ii + a.jj*b.ji
            jj = a.ji*b.ij + a.jj*b.jj
            buffer.ii = ii
            buffer.ij = ij
            buffer.ji = ji
            buffer.jj = jj
            return buffer

    @staticmethod
    def mxmtadd(*args):
        """Compute the sum of a pair of matrices multipled with another matrix
        transposed"""
        if len(args) == 4:
            # @param a left hand matrix in the first product
            # @param b right hand matrix to transpose in the first product
            # @param c left hand matrix in the second product
            # @param d right hand matrix to transpose in the second product
            # @return a new <code>MatrixIJ</code> containing
            # (a x bt) + (c x dt)
            # @see MatrixIJ#mxmtadd(UnwritableMatrixIJ, UnwritableMatrixIJ,
            # UnwritableMatrixIJ, UnwritableMatrixIJ, MatrixIJ)
            (a, b, c, d) = args
            return MatrixIJ.mxmtadd(a, b, c, d, MatrixIJ())
        elif len(args) == 5:
            # @param a left hand matrix in the first product
            # @param b right hand matrix to transpose in the first product
            # @param c left hand matrix in the second product
            # @param d right hand matrix to transpose in the second product
            # @param buffer buffer to receive the results of
            # (a x bt) + (c x dt)
            # @return reference to buffer for convenience
            (a, b, c, d, buffer) = args
            ii = a.ii*b.ii + a.ij*b.ij
            ij = a.ii*b.ji + a.ij*b.jj
            ji = a.ji*b.ii + a.jj*b.ij
            jj = a.ji*b.ji + a.jj*b.jj
            ii += c.ii*d.ii + c.ij*d.ij
            ij += c.ii*d.ji + c.ij*d.jj
            ji += c.ji*d.ii + c.jj*d.ij
            jj += c.ji*d.ji + c.jj*d.jj
            buffer.ii = ii
            buffer.ij = ij
            buffer.ji = ji
            buffer.jj = jj
            return buffer

    @staticmethod
    def mtxmadd(*args):
        """Compute the sum of a pair of matrix transposes multipled with
        another matrix
        """
        if len(args) == 4:
            # @param a left hand matrix to transpose in the first product
            # @param b right hand matrix in the first product
            # @param c left hand matrix to transpose in the second product
            # @param d right hand matrix in the second product
            # @return a new <code>MatrixIJ</code> containing
            # (at x b) + (ct x d)
            # @see MatrixIJ#mtxmadd(UnwritableMatrixIJ, UnwritableMatrixIJ,
            # UnwritableMatrixIJ, UnwritableMatrixIJ, MatrixIJ)
            (a, b, c, d) = args
            return MatrixIJ.mtxmadd(a, b, c, d, MatrixIJ())
        elif len(args) == 5:
            # @param a left hand matrix to transpose in the first product
            # @param b right hand matrix in the first product
            # @param c left hand matrix to transpose in the second product
            # @param d right hand matrix in the second product
            # @param buffer buffer to receive the results of
            # (at x b) + (ct x d)
            # @return reference to buffer for convenience
            (a, b, c, d, buffer) = args
            ii = a.ii*b.ii + a.ji*b.ji
            ij = a.ii*b.ij + a.ji*b.jj
            ji = a.ij*b.ii + a.jj*b.ji
            jj = a.ij*b.ij + a.jj*b.jj
            ii += c.ii*d.ii + c.ji*d.ji
            ij += c.ii*d.ij + c.ji*d.jj
            ji += c.ij*d.ii + c.jj*d.ji
            jj += c.ij*d.ij + c.jj*d.jj
            buffer.ii = ii
            buffer.ij = ij
            buffer.ji = ji
            buffer.jj = jj
            return buffer

    @staticmethod
    def mxmadd(*args):
        """Compute the sum of the products of two pairs of matrices."""
        if len(args) == 4:
            # @param a left hand matrix in first product
            # @param b right hand matrix in first product
            # @param c left hand matrix in second product
            # @param d right hand matrix in second product
            # @return a new <code>MatrixIJ</code> containing
            # (a x b) + (c x d)
            # @see MatrixIJ#mxmadd(UnwritableMatrixIJ, UnwritableMatrixIJ,
            # UnwritableMatrixIJ, UnwritableMatrixIJ, MatrixIJ)
            (a, b, c, d) = args
            return MatrixIJ.mxmadd(a, b, c, d, MatrixIJ())
        elif len(args) == 5:
            # @param a left hand matrix in first product
            # @param b right hand matrix in first product
            # @param c left hand matrix in second product
            # @param d right hand matrix in second product
            # @param buffer buffer to receive the results of
            # (a x b) + (c x d)
            # @return a reference to buffer for convenience
            (a, b, c, d, buffer) = args
            ii = a.ii*b.ii + a.ij*b.ji
            ij = a.ii*b.ij + a.ij*b.jj
            ji = a.ji*b.ii + a.jj*b.ji
            jj = a.ji*b.ij + a.jj*b.jj
            ii += c.ii*d.ii + c.ij*d.ji
            ij += c.ii*d.ij + c.ij*d.jj
            ji += c.ji*d.ii + c.jj*d.ji
            jj += c.ji*d.ij + c.jj*d.jj
            buffer.ii = ii
            buffer.ij = ij
            buffer.ji = ji
            buffer.jj = jj
            return buffer

    @staticmethod
    def subtract(*args):
        """Compute the component-wise difference of two matrices.

        @param a the minuend matrix
        @param b the subtrahend matrix
        @param buffer the buffer to receive the results of the subtraction
        @see MatrixIJ#subtract(UnwritableMatrixIJ, UnwritableMatrixIJ,
        MatrixIJ)
        """
        if len(args) == 2:
            (a, b) = args
            return MatrixIJ.subtract(a, b, MatrixIJ())
        elif len(args) == 3:
            (a, b, buffer) = args
            buffer.ii = a.ii - b.ii
            buffer.ji = a.ji - b.ji
            buffer.ij = a.ij - b.ij
            buffer.jj = a.jj - b.jj
            return buffer

    @staticmethod
    def add(*args):
        """Compute component-wise sum of two matrices.

        @param a a matrix
        @param b another matrix
        @return a new <code>MatrixIJ</code> containing (a + b)
        @see MatrixIJ#add(UnwritableMatrixIJ, UnwritableMatrixIJ, MatrixIJ)
        """
        if len(args) == 2:
            (a, b) = args
            return MatrixIJ.add(a, b, MatrixIJ())
        elif len(args) == 3:
            (a, b, buffer) = args
            buffer.ii = a.ii + b.ii
            buffer.ji = a.ji + b.ji
            buffer.ij = a.ij + b.ij
            buffer.jj = a.jj + b.jj
            return buffer

    @staticmethod
    def diagonalizeSymmetricMatrix(symmetricMatrix, eigenvalueBuffer,
                                   eigenvectorBuffer):
        """Diagonalizes a symmetric matrix.

        NOTE: DOES NOT DIAGONALIZE symmetricMatrix. IT RETURNS THE
        EIGENVECTOR MATRIX THAT WOULD DIAGONALIZE IT.

        Diagonalization converts a matrix from its symmetric form to an
        equivalent representation:
        diagonalized = rotate  * symmetricMatrix * rotate

        where diagonlized is a matrix of the form:

                       [ a   0 ]
        diagonalized = [       ]
                       [ 0   b ]

        and (a,b) are the eigenvalues of the matrix, and the columns of rotate
        are the eigenvectors corresponding to (a,b) respectively.

        @param symmetricMatrix a symmetric matrix
        @param eigenvalueBuffer the buffer to capture the eigenvalues
        @param eigenvectorBuffer the buffer to capture the eigenvectors, may
        overwrite symmetricMatrix
        @return a reference to eigenvectorBuffer for convenience
        @throws IllegalArgumentException if symmetricMatrix is not symmetric,
        i.e. symmetricMatrix.isSymmetric() is false.
        """

        # THIS CODE DOES NOT CREATE A DIAGONAL MATRIX!
        Preconditions.checkArgument(
            symmetricMatrix.isSymmetric(),
            "Only able to diagonlize symmetric matrices")

        # Is the matrix already diagonal? If so, then don't do any heavy
        # lifting.
        if symmetricMatrix.ij == 0.0:  # NEEDS TO CHECK JI FOR 0
            eigenvalueBuffer.setTo(symmetricMatrix.ii, symmetricMatrix.jj)
            eigenvectorBuffer.setTo(MatrixIJ.IDENTITY)
            return eigenvectorBuffer

        # We only are going to use the upper triangle of the matrix. Determine
        # a scale factor to improve numerical robustness.
        scale = max(abs(symmetricMatrix.ii), max(abs(symmetricMatrix.ij),
                                                 abs(symmetricMatrix.jj)))
        a = symmetricMatrix.ii/scale
        b = symmetricMatrix.ij/scale
        c = symmetricMatrix.jj/scale

        # Compute the eigenvalues of the scaled version of symmetricMatrix. The
        # eigenvalues are simply the roots of the equation:

        # determinant
        # ( (1/scale) * symmetricMatrix - x * MatrixIJ.IDENTITY ) = 0

        # or equivalently:

        # x*x - (a+c) *x + (ac - b*b) = 0
        MatrixIJ.solveQuadratic(1.0, -(a + c), a*c - b*b, eigenvalueBuffer)
        eigval1 = eigenvalueBuffer.i
        eigval2 = eigenvalueBuffer.j

        # The ith component of the eigenvalueBuffer is the root corresponding
        # to the positive discriminant term; this is guaranteed by method used
        # to solve the quadratic equation. Now find the eigenvector
        # corresponding to the eigenvalue of the smaller magnitude. We can
        # unitize it and select an orthogonal unit vector so as to create the
        # desired rotation matrix.
        # There are two candidate eigenvectors, select the one involving the
        # eigenvector of the larger magnitude.
        if abs(eigval1 - a) >= (abs(eigval1) - c):  # CHECK THIS
            # In this case the second eigenvector component should be larger
            # than |b|. Use Math.max() below to guard against reversal of the
            # inequality due to round-off error. Abuse the eigenvalueBuffer
            # temporarily to hold the eigenvector.
            eigenvalueBuffer.setTo(b, max(eigval1 - a, abs(b)))
            eigenvalueBuffer.unitize()
            eigenvectorBuffer.setTo(eigenvalueBuffer.getJ(),
                                    -eigenvalueBuffer.getI(),
                                    eigenvalueBuffer.getI(),
                                    eigenvalueBuffer.getJ())
            # Swap the eigenvalues.
            eigenvalueBuffer.setTo(eigval2, eigval1)
        else:
            eigenvalueBuffer.setTo(max(eigval1 - c, abs(b)), b)
            eigenvalueBuffer.unitize()
            eigenvectorBuffer.setTo(eigenvalueBuffer.getI(),
                                    eigenvalueBuffer.getJ(),
                                    -eigenvalueBuffer.getJ(),
                                    eigenvalueBuffer.getI())
            # Restore the eigenvalues into their buffer.
            eigenvalueBuffer.setTo(eigval1, eigval2)

        # Scale the eigenvalues back up to their appropriate values.
        eigenvalueBuffer.scale(scale)
        return eigenvectorBuffer

    @staticmethod
    def solveQuadratic(a: float, b: float, c: float, buffer):
        """Solves a quadratic equation of the form:

             2
        a * x  + b * x + c = 0

        @param a the quadratic coefficient
        @param b the linear coefficient
        @param c the constant coefficient
        @param buffer the buffer to receive the real roots, the ith
        component will contain the positive discriminant term and the jth
        the negative.
        @return a reference to buffer for convenience
        @throws IllegalArgumentException if a and b are both 0.0, or if
        the roots are complex.
        """
        Preconditions.checkArgument(
            a != 0.0 or b != 0.0,
            "Both the linear and quadratic degree coefficients are zero.")
        scale = max(abs(a), max(abs(b), abs(c)))

        # If the coefficients can be scaled without zeroing any of them out,
        # do so. The expression below only evaluates to true when the input
        # variables can be safely scaled.
        if (not ((a != 0.0 and a/scale == 0.0) or
                 (b != 0.0 and b/scale == 0.0) or
                 (c != 0.0 and c/scale == 0.0))):
            a /= scale
            b /= scale
            c /= scale

        # If the second degree coefficient is non-zero then we have a quadratic
        # equation that needs factoring.
        if a != 0.0:
            discriminant = b*b - 4*a*c
            # Verify that the discriminant is positive or zero.
            Preconditions.checkArgument(discriminant >= 0.0,
                                        "Roots are not real.")
            # Take advantage of the fact that c/a is the product of the roots
            # to improve the accuracy of the root having the smaller magnitude.
            # Compute the larger root first and then divide by c/a by it to
            # obtain the smaller root.
            if b < 0.0:
                # The ith component will contain the root of the larger
                # magnitude.
                buffer.setI((-b + sqrt(discriminant))/(2.0*a))
                buffer.setJ((c/a)/buffer.getI())
            elif b > 0.0:
                # The jth component will contain the root of the larger
                # magnitude.
                buffer.setJ((-b - sqrt(discriminant))/(2.0*a))
                buffer.setI((c/a)/buffer.getJ())
            else:
                # The roots have the same magnitude.
                buffer.setI(sqrt(discriminant)/(2.0*a))
                buffer.setJ(-buffer.getI())

            return buffer

        # If we reach here, then the quadratic coefficient is zero, implying
        # this is a simple linear equation. Since there is only one solution,
        # set them both to the same value, the root.
        buffer.setI(-c/b)
        buffer.setJ(buffer.getI())
        return buffer

    @staticmethod
    def mtxv(*args):
        """Compute the product of the transpose of a matrix with a vector.

        @param m the matrix
        @param v the vector
        @return a new <code>VectorIJ</code> containing the result.
        @see UnwritableMatrixIJ#mtxv(UnwritableVectorIJ)
        OR
        @param m the matrix
        @param v the vector
        @param buffer the buffer to receive the product, transpose(m)*v
        @return a reference to buffer for convenience.
        @see UnwritableMatrixIJ#mtxv(UnwritableVectorIJ, VectorIJ)

        @Deprecated
        """
        if len(args) == 2:
            (m, v) = args
            return UnwritableMatrixIJ.mtxv(m, v, VectorIJ())
        elif len(args) == 3:
            (m, v, buffer) = args
            return UnwritableMatrixIJ.mtxv(m, v, buffer)

    @staticmethod
    def mxv(*args):
        """Compute the product of a matrix with a vector.

        @param m the matrix
        @param v the vector
        @return a new <code>VectorIJ</code> containing the result.
        OR
        @param m the matrix
        @param v the vector
        @param buffer the buffer to receive the product, m*v.
        @return a reference to buffer for convenience.

        @see UnwritableMatrixIJ#mxv(UnwritableVectorIJ)

        @Deprecated
        """
        if len(args) == 2:
            (m, v) = args
            return UnwritableMatrixIJ.mxv(m, v, VectorIJ())
        elif len(args) == 3:
            (m, v, buffer) = args
            return UnwritableMatrixIJ.mxv(m, v, buffer)
