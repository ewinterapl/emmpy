"""emmpy.crucible.core.math.vectorspace.unwritablematrixij"""


import sys
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    checkRotation,
    computeDeterminant,
    computeNorm
)
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.utilities.doubletolongbits import doubleToLongBits
from emmpy.utilities.isrealnumber import isRealNumber


class UnwritableMatrixIJ:
    """A weakly immutable 2-dimensional matrix designed to properly support
    several writable subclasses.

    Note: Subclass implementers, you should only use the protected fields in
    this class to store the contents of the matrix components, otherwise all of
    the methods here and in the operations class may break.

    The basic data fields on this class are marked as protected to allow direct
    access to them through subclassing. This will get around any performance
    issues that one may have in utilizing this matrix arithmetic toolkit due to
    the enforcement of access to the component values through accessor methods.

    Note, the equals and hashcode implementations in this class support proper
    comparisons between subclasses of this class and this class. The reason
    this works is because by design the only member variables of this class
    live in the parent class. If one subclasses this class and defines
    additional members then this will most certainly break the implementation
    presented here.

    The protected fields in this matrix are arranged in the following manner:

    ii ij
    ji jj

    The class prefers column ordering, so when working with vectors and this
    class they are to be considered column vectors.

    @author G.K.Stephens copy and extension of F.S.Turner
    """

    # Default tolerance for determining if a matrix is invertible. The
    # determinant must be greater than this tolerance:
    # {@value #INVERSION_TOLERANCE}
    INVERSION_TOLERANCE = 1E-16

    # One of the two default tolerances that control how close to a rotation a
    # rotation matrix must be. This value determines how far off unity the norm
    # of the column vectors of a matrix must be. Currently it is set to:
    # {@value #NORM_TOLERANCE}
    NORM_TOLERANCE = 1E-4

    # The other of the two default tolerances that control how close to a
    # rotation a rotation matrix must be. This value determines how far off
    # unity the determinant of the matrix must be. Currently it is set to:
    # {@value #DETERMINANT_TOLERANCE}
    DETERMINANT_TOLERANCE = 1E-4

    # The bound defining the boundary length at which the invort procedure
    # works with double precision. Note: this is necessary because larger
    # negative exponents are captured by 64 IEEE doubles than positive ones.
    INVORSION_BOUND = sys.float_info.max

    def __init__(self, *args):
        """Constructor"""
        pass
        if len(args) == 0:
            # Protected, no argument, no initialization constructor for
            # subclasses to utilize.
            # The ith row, ith column component of the matrix.
            self.ii = None
            # The ith row, jth column component of the matrix.
            self.ij = None
            # The jth row, ith column component of the matrix.
            self.ji = None
            # The jth row, jth column component of the matrix.
            self.jj = None
        elif len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a matrix from the upper two by two block of a two
                # dimensional array of doubles.
                # The values from the data array are copied into the matrix as
                # follows:
                # data[0][0] data[0][1]
                # data[1][0] data[1][1]
                (data,) = args
                self.__init__(data[0][0], data[1][0], data[0][1], data[1][1])
            else:
                # Copy constructor, creates a matrix by copying the values of a
                # pre-existing one.
                (matrix,) = args
                self.__init__(matrix.ii, matrix.ji, matrix.ij, matrix.jj)
        elif len(args) == 2:
            if isRealNumber(args[0]):
                # Scaling constructor, creates a new matrix by applying a
                # scalar multiple to the components of a pre-existing matrix.
                (scale, matrix) = args
                self.__init__(scale*matrix.ii, scale*matrix.ji,
                              scale*matrix.ij, scale*matrix.jj)
            else:
                # Column vector constructor, creates a new matrix by populating
                # the columns of the matrix with the supplied vectors.
                (ithColumn, jthColumn) = args
                self.__init__(ithColumn.i, ithColumn.j,
                              jthColumn.i, jthColumn.j)
        elif len(args) == 3:
            # Column scaling constructor, creates a new matrix by applying
            # scalar multiples to the columns of a pre-existing matrix.
            (scaleI, scaleJ, matrix) = args
            self.__init__(scaleI*matrix.ii, scaleI*matrix.ji,
                          scaleJ*matrix.ij, scaleJ*matrix.jj)
        elif len(args) == 4:
            if (isRealNumber(args[0]) and isRealNumber(args[1]) and
                isRealNumber(args[2]) and isRealNumber(args[3])):
                # Constructs a matrix from the four basic components.
                (ii, ji, ij, jj) = args
                self.ii = ii
                self.ji = ji
                self.ij = ij
                self.jj = jj
            else:
                # Scaled column vector constructor, creates a new matrix by
                # populating the columns of the matrix with scaled versions of
                # the supplied vectors.
                (scaleI, ithColumn, scaleJ, jthColumn) = args
                self.__init__(scaleI*ithColumn.i, scaleI*ithColumn.j,
                              scaleJ*jthColumn.i, scaleJ*jthColumn.j)
        else:
            raise Exception

    def createTranspose(self):
        """Creates a new, transposed copy of the existing matrix.

        @return the transpose of the instance
        """
        return UnwritableMatrixIJ(self.ii, self.ij, self.ji, self.jj)

    def createUnitizedColumns(self):
        """Creates a new matrix whose columns are unitized versions of the
        columns of this matrix.

        @return the unitized column version of this matrix

        @throws UnsupportedOperationException if any of the columns are of
        length zero
        """
        return UnwritableMatrixIJ(
            VectorIJ(self.ii, self.ji).unitize(),
            VectorIJ(self.ij, self.jj).unitize())

    def createInverse(self, *args):
        """Creates a new, inverted copy of the existing matrix if possible.

        @param tolerance the absolute value of the determinant of the instance
        must be greater than this for inversion to proceed
        @return the multiplicative inverse of the instance
        @throws UnsupportedOperationException if the instance matrix has a
        determinant within {@value #INVERSION_TOLERANCE} of 0.0
        """
        if len(args) == 0:
            return self.createInverse(self.INVERSION_TOLERANCE)
        elif len(args) == 1:
            (tolerance,) = args
            det = self.getDeterminant()
            if abs(det) < tolerance:
                raise Exception(
                    "Matrix nearly singular, unable to invert.")
            return UnwritableMatrixIJ(self.jj/det, -self.ji/det,
                                      -self.ij/det, self.ii/det)

    def createInvorted(self):
        """Creates a new, inverted copy of the existing matrix with orthogonal
        columns.

        If this method is invoked on matrices whose columns are not orthogonal,
        the resultant matrix is likely not the inverse sought. Use the more
        general {@link UnwritableMatrixIJ#createInverse()}
        method instead.

        @return a newly created matrix, that is the inverse of this matrix if
        it meets the orthogonality condition

        @throws UnsupportedOperationException if the lengths of any of the
        columns are zero or too small to properly invert multiplicatively in
        the space available to double precision.
        """

        # First create the transpose, then all that's left is to scale the
        # rows appropriately.
        matrix = self.createTranspose()
        length = computeNorm(matrix.ii, matrix.ij)
        if length*self.INVORSION_BOUND < 1 or length == 0:
            raise Exception(
                "ith column of matrix has length %s, for which there is no "
                "inverse." % length)
        matrix.ii /= length
        matrix.ii /= length
        matrix.ij /= length
        matrix.ij /= length
        length = computeNorm(matrix.ji, matrix.jj)
        if length*self.INVORSION_BOUND < 1 or length == 0:
            raise Exception(
                "jth column of matrix has length, " + length +
                ", for which there is no inverse.")
        matrix.ji /= length
        matrix.ji /= length
        matrix.jj /= length
        matrix.jj /= length
        return matrix

    def getII(self):
        """Gets the ith row, ith column component."""
        return self.ii

    def getJI(self):
        """Gets the jth row, ith column component."""
        return self.ji

    def getIJ(self):
        """Gets the ith row, jth column component."""
        return self.ij

    def getJJ(self):
        """Gets the jth row, jth column component."""
        return self.jj

    def get(self, row, column):
        """Gets the component from the specified row and column.

        @param row a row index in [0,2].
        @param column a column index in [0,2]

        @return the desired matrix component value

        @throws IllegalArgumentException if either the supplied row or column
        index are outside their acceptable ranges of [0,2].
        """
        if row == 0:
            if column == 0:
                return self.ii
            elif column == 1:
                return self.ij
            else:
                raise Exception(
                    "Unable to retrieve element (%s, %s). Column index "
                    "invalid." % (row, column)
                )
        elif row == 1:
            if column == 0:
                return self.ji
            elif column == 1:
                return self.jj
            else:
                raise Exception(
                    "Unable to retrieve element (%s, %s). Column index "
                    "invalid." % (row, column))
        else:
            raise Exception(
                "Unable to retrieve element (%s, %s). Row index invalid." %
                (row, column))

    def getIthColumn(self, buffer):
        """Copies the ith column components into the supplied vector.

        @param buffer the vector to receive the components
        @return a reference to buffer for convenience
        """
        buffer.i = self.ii
        buffer.j = self.ji
        return buffer

    def getJthColumn(self, buffer):
        """Copies the jth column components into the supplied vector.

        @param buffer the vector to receive the components
        @return a reference to buffer for convenience
        """
        buffer.i = self.ij
        buffer.j = self.jj
        return buffer

    def getColumn(self, columnIndex, buffer):
        """Copies the desired column components into the supplied vector.

        @param columnIndex index of the column contents to copy. Must be in
        [0,2]
        @param buffer the vector to receive the components
        @return a reference to buffer for convenience
        @throws IllegalArgumentException if the supplied columnIndex lies
        outside the acceptable range
        """
        if columnIndex == 0:
            return self.getIthColumn(buffer)
        elif columnIndex == 1:
            return self.getJthColumn(buffer)
        else:
            raise Exception(
                "Unable to retrieve column. Index: %s is invalid." %
                columnIndex
            )

    def getDeterminant(self):
        """Computes the determinant of the matrix.

        @return the determinant of the instance
        """
        return computeDeterminant(self.ii, self.ji, self.ij, self.jj)

    def getTrace(self):
        """Computes the trace of the matrix.

        @return the trace of the instance
        """
        return self.ii + self.jj

    def isRotation(self, *args):
        """Do the components of the instance represent a rotation subject to
        the default norm {@link #NORM_TOLERANCE} and determinant
        {@value #DETERMINANT_TOLERANCE} tolerances.

        @param normTolerance specifies how far off unity the norms of the
        column vectors are allowed to be
        @param determinantTolerance specifies how far off unity the determinant
        of the instance is allowed to be

        @return true if the matrix components capture a rotation, false
        otherwise
        """
        if len(args) == 0:
            return self.isRotation(self.NORM_TOLERANCE,
                                   self.DETERMINANT_TOLERANCE)
        elif len(args) == 2:
            (normTolerance, determinantTolerance) = args
        try:
            checkRotation(self.ii, self.ji, self.ij, self.jj, normTolerance,
                          determinantTolerance)
            return True
        except MalformedRotationException:
            return False

    def isSymmetric(self):
        """Are the components of the instance symmetric?

        @return true if this.ji == this.ij, false otherwise.
        """
        return self.ji == self.ij

    def mxv(self, *args):
        """Compute the product of this matrix with a vector.

        @param v the vector
        @param buffer the buffer to receive the product, m*v.

        @return a new <code>VectorIJ</code> containing the result.

        @see mxv
        """
        if len(args) == 1:
            (v,) = args
            return self.mxv(v, VectorIJ())
        elif len(args) == 2:
            (v, buffer) = args
            i = self.ii*v.i + self.ij*v.j
            j = self.ji*v.i + self.jj*v.j
            buffer.i = i
            buffer.j = j
            return buffer

    def mtxv(self, *args):
        """Compute the product of the transpose of a matrix with a vector.

        @param v the vector
        @param buffer the buffer to receive the product, transpose(m)*v
        @return a new <code>VectorIJ</code> containing the result.

        @see mtxv
        """
        if len(args) == 1:
            (v,) = args
            return self.mtxv(v, VectorIJ())
        elif len(args) == 2:
            (v, buffer) = args
            i = self.ii*v.i + self.ji*v.j
            j = self.ij*v.i + self.jj*v.j
            buffer.i = i
            buffer.j = j
            return buffer

    @staticmethod
    def copyOf(matrix):
        """Makes an unwritable copy of the supplied matrix.

        This method makes an unwritable copy only if necessary. It tries to
        avoid making a copy wherever possible.

        @param matrix a matrix to copy.

        @return either a reference to matrix (if matrix is already only an
        instance of {@link UnwritableMatrixIJ}, otherwise an unwritable copy
        of matrix's contents
        """
        if isinstance(matrix, UnwritableMatrixIJ):
            return matrix
        return UnwritableMatrixIJ(matrix)

    def hashCode(self):
        """Compute and return hash code."""
        prime = 31
        result = 1
        temp = doubleToLongBits(self.ii)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.ij)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.ji)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.jj)
        result = prime*result + temp ^ (temp >> 32)
        result = prime*result + temp ^ (temp >> 32)
        return result

    def equals(self, obj):
        if self == obj:
            return True
        if obj is None:
            return False
        if not isinstance(obj, UnwritableMatrixIJ):
            return False
        other = obj
        if (doubleToLongBits(self.ii) !=
            doubleToLongBits(other.ii)):
            return False
        if (doubleToLongBits(self.ij) !=
            doubleToLongBits(other.ij)):
            return False
        if (doubleToLongBits(self.ji) !=
            doubleToLongBits(other.ji)):
            return False
        if (doubleToLongBits(self.jj) !=
            doubleToLongBits(other.jj)):
            return False
        return True

    def toString(self):
        return "[%s,%s;%s,%s]" % (self.ii, self.ji, self.ij, self.jj)
