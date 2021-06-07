"""A 3-D rotation matrix."""


from emmpy.crucible.core.math.vectorspace.internaloperations import (
    checkRotation,
    computeNorm
)
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)
from emmpy.crucible.core.math.vectorspace.unwritablematrixijk import (
    UnwritableMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablerotationmatrixijk import (
    UnwritableRotationMatrixIJK
)


class RotationMatrixIJK(UnwritableRotationMatrixIJK):
    """A 3-D rotation matrix.

    A writable subclass of the unwritable 3D rotation matrix parent
    completing another link the weak-immutability design pattern.

    This class contains the mutator methods necessary to set or alter the
    internals of the parent classes fields. Wherever these mutations may alter
    the matrix to become one that no longer qualifies as a rotation, the
    methods on this class validate the resultant content. This is accomplished
    through the fact that each setTo method invokes one particular setTo
    method:
    {@link RotationMatrixIJK#setTo(double, double, double, double, double,
                                   double, double, double, double)}
    The validation code is confined to this method, allowing subclasses to
    override a single method on this class to remove the check code.

    Similarly each constructor, save the copy constructor and default
    constructor, validate input content to ensure that it is a rotation matrix.
    Validation is consistent with the {@link UnwritableMatrixIJK#isRotation()}
    method.

    @author F.S.Turner
    """

    # Instance of a rotation matrix capturing the content of the multiplicative
    # identity.
    IDENTITY = UnwritableRotationMatrixIJK(1, 0, 0, 0, 1, 0, 0, 0, 1)

    def __init__(self, *args):
        """Build a new object."""
        if len(args) == 0:
            # Creates a rotation matrix and sets it to the identity.
            UnwritableRotationMatrixIJK.__init__(self,
                                                 RotationMatrixIJK.IDENTITY)
        elif len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a matrix from the upper three by three block of a
                # two dimensional array of doubles.
                # @param data the array of doubles
                # @throws IndexOutOfBoundsException if the supplied data array
                # does not contain at least three arrays of arrays of length
                # three or greater.
                # @throws IllegalArgumentException if either the columns of the
                # supplied matrix have norms that are not within
                # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the
                # determinant is not within
                # {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
                (data,) = args
                UnwritableRotationMatrixIJK.__init__(self, data)
            elif isinstance(args[0], UnwritableRotationMatrixIJK):
                # Copy constructor, creates a matrix by copying the values of a
                # pre-existing instance of the parent unwritable matrix class.
                # @param matrix the matrix whose contents are to be copied.
                (matrix,) = args
                UnwritableRotationMatrixIJK.__init__(self, matrix)
            elif isinstance(args[0], UnwritableMatrixIJK):
                # Copy constructor, of sorts, creates a matrix by copying the
                # values of a pre-existing matrix.
                # Note: This constructor performs no validation on the input by
                # design.
                # @param matrix the rotation matrix whose contents are to be
                # copied.
                # @throws IllegalArgumentException if either the columns of the
                # supplied matrix have norms that are not within
                # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the
                # determinant is not within
                # {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
                (matrix,) = args
                UnwritableRotationMatrixIJK.__init__(self, matrix)
        elif len(args) == 2:
            # Scaling constructor, creates a new matrix by applying a scalar
            # multiple to the components of a pre-existing matrix.
            # @param scale the scale factor to apply
            # @param matrix the matrix whose components are to be scaled and
            # copied.
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (scale, matrix) = args
            UnwritableRotationMatrixIJK.__init__(self, scale, matrix)
        elif len(args) == 3:
            # Column vector constructor, creates a new matrix by populating the
            # columns of the rotation matrix with the supplied vectors.
            # @param ithColumn the vector containing the ith column
            # @param jthColumn the vector containing the jth column
            # @param kthColumn the vector containing the kth column
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (ithColumn, jthColumn, kthColumn) = args
            UnwritableRotationMatrixIJK.__init__(self, ithColumn, jthColumn,
                                                 kthColumn)
        elif len(args) == 4:
            # Column scaling constructor, creates a new rotation matrix by
            # applying scalar multiples to the columns of a pre-existing
            # matrix.
            # @param scaleI scale factor to apply to the ith column
            # @param scaleJ scale factor to apply to the jth column
            # @param scaleK scale factor to apply to the kth column
            # @param matrix the matrix whose components are to be scaled and
            # copied
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (scaleI, scaleJ, scaleK, matrix) = args
            UnwritableRotationMatrixIJK.__init__(self, scaleI, scaleJ, scaleK,
                                                 matrix)
        elif len(args) == 6:
            # Scaled column vector constructor, creates a new rotation matrix
            # by populating the columns of the matrix with scaled versions of
            # the supplied vectors
            # @param scaleI the scale factor to apply to the ith column
            # @param ithColumn the vector containing the ith column
            # @param scaleJ the scale factor to apply to the jth column
            # @param jthColumn the vector containing the jth column
            # @param scaleK the scale factor to apply to the kth column
            # @param kthColumn the vector containing the kth column
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            UnwritableRotationMatrixIJK.__init__(
                self, scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn)
        elif len(args) == 9:
            # Constructs a rotation matrix from the nine basic components.
            # @param ii ith row, ith column element
            # @param ji jth row, ith column element
            # @param ki kth row, ith column element
            # @param ij ith row, jth column element
            # @param jj jth row, jth column element
            # @param kj kth row, jth column element
            # @param ik ith row, kth column element
            # @param jk jth row, kth column element
            # @param kk kth row, kth column element
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            UnwritableRotationMatrixIJK.__init__(
                self, ii, ji, ki, ij, jj, kj, ik, jk, kk)

    def createSharpened(self):
        """Create a "sharpened" copy of the matrix.

        Note: this method is overridden to return an instance of the
        writable rotation subclass, rather than either of the two unwritable
        parents.
        """
        return RotationMatrixIJK(self).sharpen()

    def createTranspose(self):
        """Create a transposed copy of the matrix.

        Note: this method is overridden to return an instance of the
        writable rotation subclass, rather than either of the two unwritable
        parents.
        """
        return RotationMatrixIJK(self).transpose()

    def createInverse(self, *args):
        """Create an inverted copy of the matrix.

        Note: this method is overridden to return an instance of the
        writable rotation subclass, rather than either of the two unwritable
        parents.
        """
        if len(args) == 0:
            return self.createTranspose()
        elif len(args) == 1:
            # Note: this method is overridden to return an instance of the
            # writable rotation subclass, rather than either of the two
            # unwritable parents.
            (tolerance,) = args  # Unused
            return self.createTranspose()

    def sharpen(self):
        """Sharpen the contents of the rotation matrix in place.

        Sharpening is a process that starts with a rotation matrix and modifies
        its contents to bring it as close to a rotation as possible given the
        limits of floating point precision in the implementation. There are
        many possible rotation matrices that are &quot;sharpenings&quot; of the
        general rotation matrix. As such, the implementation is unspecified
        here. The only claims this method makes are that the resultant matrix
        is as close or closer to a rotation than what you start with.

        @return a reference to the instance for convenience.
        """
        # Normalize the first column vector of the matrix.
        norm = computeNorm(self.ii, self.ji, self.ki)
        self.ii /= norm
        self.ji /= norm
        self.ki /= norm

        # Define the third column of the matrix as the cross product of the
        # first with the second.
        self.ik = self.ji*self.kj - self.ki*self.jj
        self.jk = self.ki*self.ij - self.ii*self.kj
        self.kk = self.ii*self.jj - self.ji*self.ij

        # Normalize the result.
        norm = computeNorm(self.ik, self.jk, self.kk)
        self.ik /= norm
        self.jk /= norm
        self.kk /= norm

        # Lastly, cross the third vector with the first to replace the second.
        self.ij = self.jk*self.ki - self.kk*self.ji
        self.jj = self.kk*self.ii - self.ik*self.ki
        self.kj = self.ik*self.ji - self.jk*self.ii

        norm = computeNorm(self.ij, self.jj, self.kj)
        self.ij /= norm
        self.jj /= norm
        self.kj /= norm
        return self

    def transpose(self):
        """Transpose the matrix.

        @return a reference to the instance for convenience, which now contains
        the transpose
        """
        tmp = self.ij
        self.ij = self.ji
        self.ji = tmp
        tmp = self.ik
        self.ik = self.ki
        self.ki = tmp
        tmp = self.jk
        self.jk = self.kj
        self.kj = tmp
        return self

    def setTo(self, *args):
        """Set the components of the matrix."""
        if len(args) == 0:
            pass
        elif len(args) == 1:
            if isinstance(args[0], list):
                # Sets the contents of this matrix to the upper three by three
                # block of a supplied two dimensional array of doubles
                # @param data the array to copy to the components of this
                # instance
                # @return a reference to this instance for convenience
                # @throws IndexOutOfBoundsException if the supplied data array
                # does not contain at least three arrays of arrays of length
                # three or greater.
                # @throws IllegalArgumentException if either the columns of the
                # supplied matrix have norms that are not within
                # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the
                # determinant is not within
                # {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
                (data,) = args
                self.setTo(data[0][0], data[1][0], data[2][0],
                           data[0][1], data[1][1], data[2][1],
                           data[0][2], data[1][2], data[2][2])
                return self
            elif isinstance(args[0], UnwritableRotationMatrixIJK):
                # Sets the contents of this rotation matrix to match those of a
                # supplied rotation matrix
                # @param matrix the matrix to copy
                # @return a reference to this instance for convenience that
                # contains the supplied components
                (matrix,) = args
                self.ii = matrix.ii
                self.ji = matrix.ji
                self.ki = matrix.ki
                self.ij = matrix.ij
                self.jj = matrix.jj
                self.kj = matrix.kj
                self.ik = matrix.ik
                self.jk = matrix.jk
                self.kk = matrix.kk
                return self
            elif isinstance(args[0], UnwritableMatrixIJK):
                # Sets the contents of this matrix to match those of a
                # supplied matrix
                # @param matrix the matrix to copy
                # @return a reference to this instance for convenience that
                # contains the supplied components
                # @throws IllegalArgumentException if either the columns of the
                # supplied matrix have norms that are not within
                # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the
                # determinant is not within
                # {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
                (matrix,) = args
                return self.setTo(
                    matrix.ii, matrix.ji, matrix.ki,
                    matrix.ij, matrix.jj, matrix.kj,
                    matrix.ik, matrix.jk, matrix.kk)
        elif len(args) == 3:
            # Sets the columns of this matrix to the three specified vectors.
            # @param ithColumn the vector containing the contents to set the
            # ith column
            # @param jthColumn the vector containing the contents to set the
            # jth column
            # @param kthColumn the vector containing the contents to set the
            # kth column
            # @return a reference to the instance for convenience
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (ithColumn, jthColumn, kthColumn) = args
            return self.setTo(ithColumn.i, ithColumn.j, ithColumn.k,
                              jthColumn.i, jthColumn.j, jthColumn.k,
                              kthColumn.i, kthColumn.j, kthColumn.k)
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
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            return self.setTo(
                scaleI*ithColumn.i, scaleI*ithColumn.j, scaleI*ithColumn.k,
                scaleJ*jthColumn.i, scaleJ*jthColumn.j, scaleJ*jthColumn.k,
                scaleK*kthColumn.i, scaleK*kthColumn.j, scaleK*kthColumn.k)
        elif len(args) == 9:
            # Sets the components of this matrix to the supplied components
            # Note: Developers wishing to disable all of the "setTo" checking
            # performed by methods on this class need only override this
            # particular method and choose not to invoke the checkRotation
            # method.
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
            # @throws IllegalArgumentException if either the columns of the
            # supplied matrix have norms that are not within
            # {@link UnwritableMatrixIJK#NORM_TOLERANCE} or if the determinant
            # is not within {@link UnwritableMatrixIJK#DETERMINANT_TOLERANCE}.
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            try:
                checkRotation(
                    ii, ji, ki, ij, jj, kj, ik, jk, kk,
                    UnwritableRotationMatrixIJK.NORM_TOLERANCE,
                    UnwritableRotationMatrixIJK.DETERMINANT_TOLERANCE)
            except MalformedRotationException as e:
                raise Exception(
                    "Matrix components do not describe a rotation.", e)
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

    def setToSharpened(self, matrix):
        """Set this matrix to a sharpened version of a rotation matrix.

        @param matrix a rotation matrix to sharpen
        @return a reference to the instance, with the contents set to
        the sharpened version of matrix
        """
        if isinstance(matrix, UnwritableRotationMatrixIJK):
            self.setTo(matrix)
            return self.sharpen()
        elif isinstance(matrix, UnwritableMatrixIJK):
            self.setTo(matrix)
            return self.sharpen()

    def setToTranspose(self, matrix):
        """Set this matrix to the transpose of a rotation matrix.

        @param matrix a rotation matrix to transpose
        @return a reference to the instance, with the contents set to the
        tranposed version of matrix
        """
        if isinstance(matrix, UnwritableRotationMatrixIJK):
            self.setTo(matrix)
            return self.transpose()
        elif isinstance(matrix, UnwritableMatrixIJK):
            self.setTo(matrix)
            return self.transpose()

    @staticmethod
    def mxmt(*args):
        """Compute the product of the matrix with the transpose of another."""
        if len(args) == 2:
            # @param a the left hand rotation matrix
            # @param b the right hand rotation matrix to transpose, then
            # multiply
            # @return a new <code>MatrixIJK</code> containing the resultant
            # product
            # @see RotationMatrixIJK#mxmt(UnwritableRotationMatrixIJK,
            # UnwritableRotationMatrixIJK, RotationMatrixIJK)
            (a, b) = args
            return RotationMatrixIJK.mxmt(a, b, RotationMatrixIJK())
        elif len(args) == 3:
            # @param a the left hand rotation matrix
            # @param b the right hand rotation matrix to transpose, then
            # multiply
            # @param buffer the buffer to receive the product, a*transpose(b).
            # @return a reference to buffer for convenience.
            (a, b, buffer) = args
            ii = a.ii*b.ii + a.ij*b.ij + a.ik*b.ik
            ij = a.ii*b.ji + a.ij*b.jj + a.ik*b.jk
            ik = a.ii*b.ki + a.ij*b.kj + a.ik*b.kk
            ji = a.ji*b.ii + a.jj*b.ij + a.jk*b.ik
            jj = a.ji*b.ji + a.jj*b.jj + a.jk*b.jk
            jk = a.ji*b.ki + a.jj*b.kj + a.jk*b.kk
            ki = a.ki*b.ii + a.kj*b.ij + a.kk*b.ik
            kj = a.ki*b.ji + a.kj*b.jj + a.kk*b.jk
            kk = a.ki*b.ki + a.kj*b.kj + a.kk*b.kk
            buffer.ii = ii
            buffer.ij = ij
            buffer.ik = ik
            buffer.ji = ji
            buffer.jj = jj
            buffer.jk = jk
            buffer.ki = ki
            buffer.kj = kj
            buffer.kk = kk
            return buffer

    @staticmethod
    def mtxm(*args):
        """Compute the product of the transpose of a rotation with another."""
        if len(args) == 2:
            # @param a the left hand rotation matrix to transpose, then
            # multiply
            # @param b the right hand rotation matrix
            # @return a new <code>MatrixIJK</code> containing the product
            # @see RotationMatrixIJK#mtxm(UnwritableRotationMatrixIJK,
            # UnwritableRotationMatrixIJK, RotationMatrixIJK)
            (a, b) = args
            return RotationMatrixIJK.mtxm(a, b, RotationMatrixIJK())
        elif len(args) == 3:
            # @param a the left hand rotation matrix to transpose, then
            # multiply
            # @param b the right hand rotation matrix
            # @param buffer the buffer to receive the product, transpose(a)*b.
            # @return a reference to buffer for convenience
            (a, b, buffer) = args
            ii = a.ii*b.ii + a.ji*b.ji + a.ki*b.ki
            ij = a.ii*b.ij + a.ji*b.jj + a.ki*b.kj
            ik = a.ii*b.ik + a.ji*b.jk + a.ki*b.kk
            ji = a.ij*b.ii + a.jj*b.ji + a.kj*b.ki
            jj = a.ij*b.ij + a.jj*b.jj + a.kj*b.kj
            jk = a.ij*b.ik + a.jj*b.jk + a.kj*b.kk
            ki = a.ik*b.ii + a.jk*b.ji + a.kk*b.ki
            kj = a.ik*b.ij + a.jk*b.jj + a.kk*b.kj
            kk = a.ik*b.ik + a.jk*b.jk + a.kk*b.kk
            buffer.ii = ii
            buffer.ij = ij
            buffer.ik = ik
            buffer.ji = ji
            buffer.jj = jj
            buffer.jk = jk
            buffer.ki = ki
            buffer.kj = kj
            buffer.kk = kk
            return buffer

    @staticmethod
    def mxm(*args):
        """Compute the product of two rotation matrices."""
        if len(args) == 2:
            # @param a the left hand rotation matrix
            # @param b the right hand rotation matrix
            # @return a new <code>RotationMatrixIJK</code> containing the
            # product (ab)
            # @see RotationMatrixIJK#mxm(UnwritableRotationMatrixIJK,
            # UnwritableRotationMatrixIJK, RotationMatrixIJK)
            (a, b) = args
            return RotationMatrixIJK.mxm(a, b, RotationMatrixIJK())
        elif len(args) == 3:
            # @param a the left hand rotation matrix
            # @param b the right hand rotation matrix
            # @param buffer the buffer to receive the product, a*b.
            # @return a reference to buffer for convenience
            (a, b, buffer) = args
            ii = a.ii*b.ii + a.ij*b.ji + a.ik*b.ki
            ij = a.ii*b.ij + a.ij*b.jj + a.ik*b.kj
            ik = a.ii*b.ik + a.ij*b.jk + a.ik*b.kk
            ji = a.ji*b.ii + a.jj*b.ji + a.jk*b.ki
            jj = a.ji*b.ij + a.jj*b.jj + a.jk*b.kj
            jk = a.ji*b.ik + a.jj*b.jk + a.jk*b.kk
            ki = a.ki*b.ii + a.kj*b.ji + a.kk*b.ki
            kj = a.ki*b.ij + a.kj*b.jj + a.kk*b.kj
            kk = a.ki*b.ik + a.kj*b.jk + a.kk*b.kk
            buffer.ii = ii
            buffer.ij = ij
            buffer.ik = ik
            buffer.ji = ji
            buffer.jj = jj
            buffer.jk = jk
            buffer.ki = ki
            buffer.kj = kj
            buffer.kk = kk
            return buffer

    @staticmethod
    def static_createSharpened(ii, ji, ki, ij, jj, kj, ik, jk, kk):
        """Create a sharpened matrix from the supplied inputs.

        @throws IllegalArgumentException if, after sharpening, the resultant
        matrix is still not a rotation.
        """
        # This is necessary to be able to leave the variable names as
        # would be expected on this class, since they are shadowed by
        # the fields on the anonymous inner class used to subvert the
        # rotation check.
        aii = ii
        aji = ji
        aki = ki
        aij = ij
        ajj = jj
        akj = kj
        aik = ik
        ajk = jk
        akk = kk

        # Bypass the constructor check, and execute sharpen directly.
        source = RotationMatrixIJK(
            aii, aji, aki, aij, ajj, akj, aik, ajk, akk)

        # Check the determinant of source to see that it is at least
        # postiive.
        if source.getDeterminant() <= 0:
            raise Exception(
                "Source has a determinant that is not "
                "strictly positive.  Unable to sharpen source into "
                " a rotation matrix.")

        # Return an actual RotationMatrixIJK, not the anonymous
        # subclass.
        source.sharpen()
        return RotationMatrixIJK(
            source.ii, source.ji, source.ki,
            source.ij, source.jj, source.kj,
            source.ik, source.jk, source.kk)
