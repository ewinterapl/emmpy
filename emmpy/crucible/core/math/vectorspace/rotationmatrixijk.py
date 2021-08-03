"""A 3-D rotation matrix."""


from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class RotationMatrixIJK(MatrixIJK):
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

    def __init__(self, *args):
        """Build a new object."""
        if len(args) == 0:
            # Creates a rotation matrix and sets it to the identity.
            data = (1, 0, 0, 0, 1, 0, 0, 0, 1)
            self.__init__(*data)
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
                self.__init__(data[0][0], data[1][0], data[2][0],
                              data[0][1], data[1][1], data[2][1],
                              data[0][2], data[1][2], data[2][2])
            elif isinstance(args[0], RotationMatrixIJK):
                # Copy constructor, creates a matrix by copying the values of a
                # pre-existing instance of the parent unwritable matrix class.
                # @param matrix the matrix whose contents are to be copied.
                (m,) = args
                self.__init__(m.ii, m.ji, m.ki,
                              m.ij, m.jj, m.kj,
                              m.ik, m.jk, m.kk)
            elif isinstance(args[0], MatrixIJK):
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
                (m,) = args
                self.__init__(m.ii, m.ji, m.ki,
                              m.ij, m.jj, m.kj,
                              m.ik, m.jk, m.kk)
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
            (s, m) = args
            self.__init__(s*m.ii, s*m.ji, s*m.ki,
                          s*m.ij, s*m.jj, s*m.kj,
                          s*m.ik, s*m.jk, s*m.kk)
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
            (colI, colJ, colK) = args
            self.__init__(colI.i, colI.j, colI.k,
                          colJ.i, colJ.j, colJ.k,
                          colK.i, colK.j, colK.k)
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
            (sI, sJ, sK, m) = args
            self.__init__(sI*m.ii, sI*m.ji, sI*m.ki,
                          sJ*m.ij, sJ*m.jj, sJ*m.kj,
                          sK*m.ik, sK*m.jk, sK*m.kk)
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
            (sI, colI, sJ, colJ, sK, colK) = args
            self.__init__(sI*colI.i, sI*colI.j, sI*colI.k,
                          sJ*colJ.i, sJ*colJ.j, sJ*colJ.k,
                          sK*colK.i, sK*colK.j, sK*colK.k)
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
            self.ii = ii
            self.ji = ji
            self.ki = ki
            self.ij = ij
            self.jj = jj
            self.kj = kj
            self.ik = ik
            self.jk = jk
            self.kk = kk
