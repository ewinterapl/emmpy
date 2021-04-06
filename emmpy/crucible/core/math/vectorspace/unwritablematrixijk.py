"""unwritablematrixijk.py
"""


from emmpy.crucible.core.math.vectorspace.internaloperations import (
    checkRotation,
    computeDeterminant,
    computeNorm
)
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.java.lang.double import Double
from emmpy.java.lang.illegalargumentexception import IllegalArgumentException
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)


class UnwritableMatrixIJK:
    """A weakly immutable 3-dimensional matrix designed to properly support
    several writable subclasses.

    Note: Subclass implementers, you should only use the protected fields in
    this class to store the contents of the matrix components, otherwise all
    of the methods here and in the operations class may break.

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

    | ii ij ik |
    | ji jj jk |
    | ki kj kk |

    The class prefers column ordering, so when working with vectors and this
    class they are to be considered "column" vectors.

    @author F.S.Turner
    """

    # Default tolerance for determining if a matrix is invertible. The
    # determinant must be greater than this tolerance:
    # {@value #INVERSION_TOLERANCE}
    INVERSION_TOLERANCE = 1E-16

    # One of the two default tolerances that control how close to a rotation
    # a rotation matrix must be. This value determines how far off unity the
    # norm of the column vectors of a matrix must be. Currently it is set to:
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
    INVORSION_BOUND = Double.MAX_VALUE

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 0:
            # Protected, no argument, no initialization constructor for
            # subclasses to utilize.
            self.ii = None
            self.ij = None
            self.ik = None
            self.ji = None
            self.jj = None
            self.jk = None
            self.ki = None
            self.kj = None
            self.kk = None
        elif len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a matrix from the upper three by three block of a
                # two dimensional array of doubles.
                # The values from the data array are copied into the matrix as
                # follows:
                # | data[0][0] data[0][1] data[0][2] |
                # | data[1][0] data[1][1] data[1][2] |
                # | data[2][0] data[2][1] data[2][2] |
                # @param data the array of doubles
                # @throws IndexOutOfBoundsException if the supplied data array
                # does not contain at least three arrays of arrays of length
                # three or greater.
                (data,) = args
                self.__init__(data[0][0], data[1][0], data[2][0],
                              data[0][1], data[1][1], data[2][1],
                              data[0][2], data[1][2], data[2][2])
            else:
                # Copy constructor, creates a matrix by copying the values of a
                # pre-existing one.
                # @param matrix the matrix whose contents are to be copied.
                (matrix,) = args
                self.__init__(matrix.ii, matrix.ji, matrix.ki,
                              matrix.ij, matrix.jj, matrix.kj,
                              matrix.ik, matrix.jk, matrix.kk)
        elif len(args) == 2:
            # Scaling constructor, creates a new matrix by applying a
            # scalar multiple to the components of a pre-existing matrix.
            # @param scale the scale factor to apply
            # @param matrix the matrix whose components are to be scaled
            # and copied
            (scale, matrix) = args
            self.__init__(
                scale*matrix.ii, scale*matrix.ji, scale*matrix.ki,
                scale*matrix.ij, scale*matrix.jj, scale*matrix.kj,
                scale*matrix.ik, scale*matrix.jk, scale*matrix.kk)
        elif len(args) == 3:
            # Column vector constructor, creates a new matrix by populating
            # the columns of the matrix with the supplied vectors.
            # @param ithColumn the vector containing the ith column
            # @param jthColumn the vector containing the jth column
            # @param kthColumn the vector containing the kth column
            (ithColumn, jthColumn, kthColumn) = args
            self.__init__(ithColumn.i, ithColumn.j, ithColumn.k,
                          jthColumn.i, jthColumn.j, jthColumn.k,
                          kthColumn.i, kthColumn.j, kthColumn.k)
        elif len(args) == 4:
            # Column scaling constructor, creates a new matrix by applying
            # scalar multiples to the columns of a pre-existing matrix.
            # @param scaleI scale factor to apply to the ith column
            # @param scaleJ scale factor to apply to the jth column
            # @param scaleK scale factor to apply to the kth column
            # @param matrix the matrix whose components are to be scaled
            # and copied
            (scaleI, scaleJ, scaleK, matrix) = args
            self.__init__(
                scaleI*matrix.ii, scaleI*matrix.ji, scaleI*matrix.ki,
                scaleJ*matrix.ij, scaleJ*matrix.jj, scaleJ*matrix.kj,
                scaleK*matrix.ik, scaleK*matrix.jk, scaleK*matrix.kk)
        elif len(args) == 6:
            # Scaled column vector constructor, creates a new matrix by
            # populating the columns of the matrix with scaled versions of
            # the supplied vectors
            # @param scaleI the scale factor to apply to the ith column
            # @param ithColumn the vector containing the ith column
            # @param scaleJ the scale factor to apply to the jth column
            # @param jthColumn the vector containing the jth column
            # @param scaleK the scale factor to apply to the kth column
            # @param kthColumn the vector containing the kth column
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK,
                kthColumn) = args
            self.__init__(
                scaleI*ithColumn.i, scaleI*ithColumn.j, scaleI*ithColumn.k,
                scaleJ*jthColumn.i, scaleJ*jthColumn.j, scaleJ*jthColumn.k,
                scaleK*kthColumn.i, scaleK*kthColumn.j, scaleK*kthColumn.k)
        elif len(args) == 9:
            # Constructs a matrix from the nine basic components.
            # @param ii ith row, ith column element
            # @param ji jth row, ith column element
            # @param ki kth row, ith column element
            # @param ij ith row, jth column element
            # @param jj jth row, jth column element
            # @param kj kth row, jth column element
            # @param ik ith row, kth column element
            # @param jk jth row, kth column element
            # @param kk kth row, kth column element
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
        else:
            raise Exception

    def createTranspose(self):
        """Creates a new, transposed copy of the existing matrix.

        @return the transpose of the instance
        """
        return UnwritableMatrixIJK(
            self.ii, self.ij, self.ik,
            self.ji, self.jj, self.jk,
            self.ki, self.kj, self.kk)

    def createUnitizedColumns(self):
        """Creates a new matrix whose columns are unitized versions of the
        columns of this matrix.

        @return the unitized column version of this matrix
        @throws UnsupportedOperationException if any of the columns are of
        length zero
        """
        return UnwritableMatrixIJK(
            VectorIJK(self.ii, self.ji, self.ki).unitize(),  # first column
            VectorIJK(self.ij, self.jj, self.kj).unitize(),  # second column
            VectorIJK(self.ik, self.jk, self.kk).unitize())  # third column

    def createInverse(self, *args):
        """Creates a new, inverted copy of the existing matrix if possible."""
        if len(args) == 0:
            # @return the multiplicative inverse of the instance
            # @throws UnsupportedOperationException if the instance matrix has
            # a determinant within {@value #INVERSION_TOLERANCE} of 0.0
            return self.createInverse(UnwritableMatrixIJK.INVERSION_TOLERANCE)
        elif len(args) == 1:
            # Creates a new, inverted copy of the existing matrix.
            # @param tolerance the absolute value of the determinant of the
            # instance must be greater than this for inversion to proceed
            # @return the multiplicative inverse of the instance
            # @throws UnsupportedOperationException if the instance matrix has
            # a determinant within tolerance of 0.0
            (tolerance,) = args
            det = self.getDeterminant()
            if abs(det) < tolerance:
                raise UnsupportedOperationException(
                    "Matrix nearly singular, unable to invert.")
            return UnwritableMatrixIJK(
                (self.jj*self.kk - self.kj*self.jk)/det,
                -(self.ji*self.kk - self.ki*self.jk)/det,
                (self.ji*self.kj - self.ki*self.jj)/det,
                -(self.ij*self.kk - self.kj*self.ik)/det,
                (self.ii*self.kk - self.ki*self.ik)/det,
                -(self.ii*self.kj - self.ki*self.ij)/det,
                (self.ij*self.jk - self.jj*self.ik)/det,
                -(self.ii*self.jk - self.ji*self.ik)/det,
                (self.ii*self.jj - self.ji*self.ij)/det)

    def createInvorted(self):
        """Creates a new, inverted copy of the existing matrix with orthogonal
        columns.

        If this method is invoked on matrices whose columns are not orthogonal,
        the resultant matrix is likely not the inverse sought. Use the more
        general {@link UnwritableMatrixIJK#createInverse()} method instead.

        @return a newly created matrix, that is the inverse of this matrix if
        it meets the orthogonality condition
        @throws UnsupportedOperationException if the lengths of any of the
        columns are zero or too small to properly invert multiplicatively in
        the space available to double precision.
        """

        # First create the transpose, then all that's left is to scale the rows
        # appropriately.
        matrix = self.createTranspose()

        length = computeNorm(matrix.ii, matrix.ij, matrix.ik)
        if length*self.INVORSION_BOUND < 1 or length == 0:
            raise UnsupportedOperationException(
                "ith column of matrix has length, %s, for which there is no "
                "inverse." % length)
        matrix.ii /= length
        matrix.ii /= length
        matrix.ij /= length
        matrix.ij /= length
        matrix.ik /= length
        matrix.ik /= length

        length = computeNorm(
            matrix.ji, matrix.jj, matrix.jk)
        if length*self.INVORSION_BOUND < 1 or length == 0:
            raise UnsupportedOperationException(
                "jth column of matrix has length, %s, for which there is no "
                "inverse." % length)
        matrix.ji /= length
        matrix.ji /= length
        matrix.jj /= length
        matrix.jj /= length
        matrix.jk /= length
        matrix.jk /= length

        length = computeNorm(
            matrix.ki, matrix.kj, matrix.kk)
        if length*self.INVORSION_BOUND < 1 or length == 0:
            raise UnsupportedOperationException(
                "kth column of matrix has length, %s, for which there is no "
                "inverse." % length)
        matrix.ki /= length
        matrix.ki /= length
        matrix.kj /= length
        matrix.kj /= length
        matrix.kk /= length
        matrix.kk /= length

        return matrix

    def getII(self):
        """Gets the ith row, ith column component.

        @return the ith row, ith column value
        """
        return self.ii

    def getJI(self):
        """Gets the jth row, ith column component.

        @return the jth row, ith column value
        """
        return self.ji

    def getKI(self):
        """Gets the kth row, ith column component.

        @return the kth row, ith column value
        """
        return self.ki

    def getIJ(self):
        """Gets the ith row, jth column component.

        @return the ith row, jth column value
        """
        return self.ij

    def getJJ(self):
        """Gets the jth row, jth column component.

        @return the jth row, jth column value
        """
        return self.jj

    def getKJ(self):
        """Gets the kth row, jth column component.

        @return the kth row, jth column value
        """
        return self.kj

    def getIK(self):
        """Gets the ith row, kth column component.

        @return the ith row, kth column value
        """
        return self.ik

    def getJK(self):
        """Gets the jth row, kth column value.

        @return the jth row, kth column value.
        """
        return self.jk

    def getKK(self):
        """Gets the kth row, kth column component.

        @return kth row, kth column value
        """
        return self.kk

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
            elif column == 2:
                return self.ik
            else:
                raise IllegalArgumentException(
                    "Unable to retrieve element (%s,%s). Column index invalid."
                    % (row, column))
        elif row == 1:
            if column == 0:
                return self.ji
            elif column == 1:
                return self.jj
            elif column == 2:
                return self.jk
            else:
                raise IllegalArgumentException(
                    "Unable to retrieve element (%s,%s). Column index invalid."
                    % (row, column))
        elif row == 2:
            if column == 0:
                return self.ki
            elif column == 1:
                return self.kj
            elif column == 2:
                return self.kk
            else:
                raise IllegalArgumentException(
                    "Unable to retrieve element (%s,%s). Column index invalid."
                    % (row, column))
        else:
            raise IllegalArgumentException(
                "Unable to retrieve element (%s,%s). Column index invalid."
                % (row, column))

    def getIthColumn(self, *args):
        """Copies the ith column components into the supplied vector."""
        if len(args) == 0:
            # @return ith column vector
            return self.getIthColumn(VectorIJK())
        elif len(args) == 1:
            # @param buffer the vector to receive the components
            # @return a reference to buffer for convenience
            (buffer,) = args
            buffer.i = self.ii
            buffer.j = self.ji
            buffer.k = self.ki
            return buffer

    def getJthColumn(self, *args):
        """Copies the jth column components into the supplied vector."""
        if len(args) == 0:
            # @return jth column vector
            return self.getJthColumn(VectorIJK())
        elif len(args) == 1:
            # @param buffer the vector to receive the components
            # @return a reference to buffer for convenience
            (buffer,) = args
            buffer.i = self.ij
            buffer.j = self.jj
            buffer.k = self.kj
            return buffer

    def getKthColumn(self, *args):
        """Copies the kth column components into the supplied vector."""
        if len(args) == 0:
            # @return kth column vector
            return self.getKthColumn(VectorIJK())
        elif len(args) == 1:
            # @param buffer the vector to receive the components
            # @return a reference to buffer for convenience
            (buffer,) = args
            buffer.i = self.ik
            buffer.j = self.jk
            buffer.k = self.kk
            return buffer

    def getColumn(self, *args):
        """Copies the desired column components into the supplied vector."""
        if len(args) == 1:
            # Extracts the desired column components as a vector.
            # @param columnIndex index of the column contents to extract. Must
            # be in [0,2]
            # @return desired column vector
            # @throws IllegalArgumentException if the supplied columnIndex lies
            # outside the acceptable range
            (columnIndex,) = args
            return self.getColumn(columnIndex, VectorIJK())
        elif len(args) == 2:
            # @param columnIndex index of the column contents to copy. Must be
            # in [0,2]
            # @param buffer the vector to receive the components
            # @return a reference to buffer for convenience
            # @throws IllegalArgumentException if the supplied columnIndex lies
            # outside the acceptable range
            (columnIndex, buffer) = args
            if columnIndex == 0:
                return self.getIthColumn(buffer)
            elif columnIndex == 1:
                return self.getJthColumn(buffer)
            elif columnIndex == 2:
                return self.getKthColumn(buffer)
            else:
                raise IllegalArgumentException(
                    "Unable to retrieve column. Index: %s is invalid." %
                    columnIndex)
        else:
            raise Exception

    def getDeterminant(self):
        """Computes the determinant of the matrix.

        @return the determinant of the instance
        """
        return computeDeterminant(
            self.ii, self.ji, self.ki,
            self.ij, self.jj, self.kj,
            self.ik, self.jk, self.kk)

    def getTrace(self):
        """Computes the trace of the matrix.

        @return the trace of the instance
        """
        return self.ii + self.jj + self.kk

    def isRotation(self, *args):
        """Do the components of the instance represent a rotation?"""
        if len(args) == 0:
            # Subject to the default norm {@link #NORM_TOLERANCE} and
            # determinant {@value #DETERMINANT_TOLERANCE} tolerances.
            # @return true if the matrix components capture a rotation, false
            # otherwise
            return self.isRotation(self.NORM_TOLERANCE,
                                   self.DETERMINANT_TOLERANCE)
        elif len(args) == 2:
            #  @param normTolerance specifies how far off unity the norms of
            # the column vectors are allowed to be
            # @param determinantTolerance specifies how far off unity the
            # determinant of the instance is allowed to be
            # @return true if the matrix components capture a rotation, false
            # otherwise
            (normTolerance, determinantTolerance) = args
            try:
                checkRotation(
                    self.ii, self.ji, self.ki,
                    self.ij, self.jj, self.kj,
                    self.ik, self.jk, self.kk,
                    normTolerance, determinantTolerance)
                return True
            except MalformedRotationException:
                return False

    def mxv(self, *args):
        """Compute the product of this matrix with a vector."""

        if len(args) == 1:
            # @param v the vector
            # @return a new <code>VectorIJK</code> containing the result.
            # @see UnwritableMatrixIJK#mxv(UnwritableVectorIJK, VectorIJK)
            (v,) = args
            return self.mxv(v, VectorIJK())
        elif len(args) == 2:
            # Compute the product of this matrix with a vector.
            # @param v the vector
            # @param buffer the buffer to receive the product, m*v.
            # @return a reference to buffer for convenience.
            (v, buffer) = args
            i = self.ii*v.i + self.ij*v.j + self.ik*v.k
            j = self.ji*v.i + self.jj*v.j + self.jk*v.k
            buffer.k = self.ki*v.i + self.kj*v.j + self.kk*v.k
            buffer.i = i
            buffer.j = j
            return buffer

    def mtxv(self, *args):
        """Compute the product of the transpose of a matrix with a vector."""
        if len(args) == 1:
            # @param v the vector
            # @return a new <code>VectorIJK</code> containing the result.
            # @see UnwritableMatrixIJK#mtxv(UnwritableVectorIJK, VectorIJK)
            (v,) = args
            return self.mtxv(v, VectorIJK())
        elif len(args) == 2:
            # Compute the product of the transpose of a matrix with a vector.
            # @param v the vector
            # @param buffer the buffer to receive the product, transpose(m)*v
            # @return a reference to buffer for convenience.
            (v, buffer) = args
            i = self.ii*v.i + self.ji*v.j + self.ki*v.k
            j = self.ij*v.i + self.jj*v.j + self.kj*v.k
            buffer.k = self.ik*v.i + self.jk*v.j + self.kk*v.k
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
        instance of
        {@link UnwritableMatrixIJK}, otherwise an unwritable copy of matrix's
        contents
        """
        if isinstance(matrix, UnwritableMatrixIJK):
            return matrix
        return UnwritableMatrixIJK(matrix)

    def hashCode(self):
        """Compute the hash code."""
        prime = 31
        result = 1
        temp = Double.doubleToLongBits(self.ii)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.ij)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.ik)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.ji)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.jj)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.jk)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.ki)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.kj)
        result = prime*result + temp ^ (temp >> 32)
        temp = Double.doubleToLongBits(self.kk)
        result = prime*result + temp ^ (temp >> 32)
        return result

    def equals(self, obj):
        """Test for equality."""
        if self is obj:
            return True
        if obj is None:
            return False
        if not isinstance(obj, UnwritableMatrixIJK):
            return False
        other = obj
        if (Double.doubleToLongBits(self.ii) !=
            Double.doubleToLongBits(other.ii)):
            return False
        if (Double.doubleToLongBits(self.ij) !=
            Double.doubleToLongBits(other.ij)):
            return False
        if (Double.doubleToLongBits(self.ik) !=
            Double.doubleToLongBits(other.ik)):
            return False
        if (Double.doubleToLongBits(self.ji) !=
            Double.doubleToLongBits(other.ji)):
            return False
        if (Double.doubleToLongBits(self.jj) !=
            Double.doubleToLongBits(other.jj)):
            return False
        if (Double.doubleToLongBits(self.jk) !=
            Double.doubleToLongBits(other.jk)):
            return False
        if (Double.doubleToLongBits(self.ki) !=
            Double.doubleToLongBits(other.ki)):
            return False
        if (Double.doubleToLongBits(self.kj) !=
            Double.doubleToLongBits(other.kj)):
            return False
        if (Double.doubleToLongBits(self.kk) !=
            Double.doubleToLongBits(other.kk)):
            return False
        return True

    def toString(self):
        return ("[%s,%s,%s;%s,%s,%s;%s,%s,%s]" %
                (self.ii, self.ji, self.ki,
                 self.ij, self.jj, self.kj,
                 self.ik, self.jk, self.kk))
