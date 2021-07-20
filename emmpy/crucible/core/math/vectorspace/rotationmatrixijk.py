"""A 3-D rotation matrix in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


# One of the two default tolerances that control how close to a rotation a
# rotation matrix must be. This value determines how far off unity the norm of
# the column vectors of a matrix must be.
NORM_TOLERANCE = 1E-4

# The other of the two default tolerances that control how close to a
# rotation a rotation matrix must be. This value determines how far off
# unity the determinant of the matrix must be.
DETERMINANT_TOLERANCE = 1E-4


class RotationMatrixIJK(MatrixIJK):
    """A 3-D rotation matrix in Cartesian (i, j, k) coordinates."""

    def __init__(self, *args):
        """Initialize a new RotationMatrixIJK object.

        Initialize a new RotationMatrixIJK object.

        Parameters
        ----------
        data : array-like
            3x3 array of values for matrix elements in row-major order.
        OR
        ithColumn, jthColumn, kthColumn : VectorIJK
            Vectors containing the 3 columns to use for the matrix.
        OR
        ii, ij, ik, ji, jj, jk, ki, kj, kk : float
            Elements of new matrix, in row-major order.

        Returns
        -------
        m : RotationMatrixIJK
            The newly-created object.

        Raises
        ------
        MalformedRotationException
            If the matrix is not a rotation matrix.
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Construct an identity matrix.
            self[:, :] = IDENTITY
        elif len(args) == 1:
            # Initialize matrix from a 3x3 array-like of floats.
            (a,) = args
            self[:, :] = np.array(a)
        elif len(args) == 3:
            # Initialize matrix by populating the columns of the matrix
            # with the supplied vectors.
            (colI, colJ, colK) = args
            self[:, 0] = np.array(colI)
            self[:, 1] = np.array(colJ)
            self[:, 2] = np.array(colK)
        elif len(args) == 9:
            # Constructs a matrix from the nine basic components, in row-
            # major order.
            self[:, :] = np.array(args).reshape((3, 3))
        else:
            raise ValueError
        if not self.isRotation():
            raise MalformedRotationException

    def isRotation(self, *args):
        """Check if this is a rotation matrix.

        Do the components of the instance represent a rotation?

        Parameters
        ----------
        normTolerance, determinantTolerance : float (optional)
            Tolerance values used to verify matrix is a rotation matrix.

        Returns
        -------
        bool
            True if a rotation matrix, else False.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Use default tolerances.
            normTolerance = NORM_TOLERANCE
            determinantTolerance = DETERMINANT_TOLERANCE
        elif len(args) == 2:
            (normTolerance, determinantTolerance) = args
        else:
            raise ValueError('Incorrect arguments for method!')

        # Check that columns are sufficiently close to unit vectors.
        for col in range(3):
            length = np.linalg.norm(self[:, col])
            if abs(length - 1) > normTolerance:
                return False

        # Check that the determinant is sufficiently close to unity.
        det = np.linalg.det(self)
        if abs(det - 1) > determinantTolerance:
            return False

        return True

    def sharpen(self):
        """Sharpen the contents of the rotation matrix in place.

        Sharpening is a process that starts with a rotation matrix and
        modifies its contents to bring it as close to a rotation as
        possible given the limits of floating point precision in the
        implementation. There are many possible rotation matrices that are
        "sharpenings" of the general rotation matrix. As such, the
        implementation is unspecified here. The only claims this method
        makes are that the resultant matrix is as close or closer to a
        rotation than what you start with.

        Returns
        -------
        self : RotationMatrixIJK
            The current object, for convenience.
        """

        # Normalize the first column vector of the matrix.
        norm = np.linalg.norm(self[:, 0])
        self[:, 0] /= norm

        # Define the third column of the matrix as the cross product of
        # the first with the second. Normalize the result.
        self[:, 2] = np.cross(self[:, 0], self[:, 1])
        norm = np.linalg.norm(self[:, 2])
        self[:, 2] /= norm

        # Cross the third vector with the first to replace the second,
        # then normalize.
        self[:, 1] = np.cross(self[:, 2], self[:, 0])
        norm = np.linalg.norm(self[:, 1])
        self[:, 1] /= norm

        return self

    def createSharpened(self):
        """Create a "sharpened" copy of the matrix.

        See the sharpen() method for details.

        Returns
        -------
        m : RotationMatrixIJK
            Sharpened copy of the matrix.
        """
        m = RotationMatrixIJK(self)
        m.sharpen()
        return m

    def createTranspose(self):
        """Create a transposed copy of the matrix.

        Create a transposed copy of the matrix.

        Returns
        -------
        m : RotationMatrixIJK
            Transposed copy of matrix.
        """
        m = RotationMatrixIJK(self)
        m.transposeInPlace()
        return m

    def createInverse(self):
        """Create an inverted copy of the matrix.

        Create an inverted copy of the matrix.

        Returns
        -------
        m : RotationMatrixIJK
            Inverted copy of matrix.
        """
        m = RotationMatrixIJK(self)
        m.invert()
        return m

    def setToSharpened(self, matrix):
        """Set this matrix to a sharpened version of a rotation matrix.

        Set this matrix to a sharpened version of a rotation matrix.

        Parameters
        ----------
        matrix : RotationMatrixIJK
            A rotation matrix to sharpen

        Returns
        -------
        self : RotationMatrixIJK
            The current object, for convenience.
        """
        self[:, :] = matrix[:, :]
        self.sharpen()
        return self


# Identity matrix.
IDENTITY = MatrixIJK(1, 0, 0, 0, 1, 0, 0, 0, 1)
