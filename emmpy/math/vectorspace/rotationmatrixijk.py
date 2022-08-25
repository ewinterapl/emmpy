"""A 3-D rotation matrix in Cartesian (i, j, k) coordinates.

A 3-D rotation matrix in Cartesian (i, j, k) coordinates.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectorspace.internaloperations import (
    checkRotation
)
from emmpy.math.matrices.matrixijk import MatrixIJK


# Tolerances for determinant and column norms, relative to unity, for a
# matrix to be a rotation matrix.
ROTATION_DETERMINANT_TOLERANCE = 1e-12
ROTATION_NORM_TOLERANCE = 1e-12


class RotationMatrixIJK(MatrixIJK):
    """A 3-D rotation matrix in Cartesian (i, j, k) coordinates.

    The arguments are checked to verify a valid rotation matrix.
    """

    def __init__(self, *args):
        """Initialize a new RotationMatrixIJK object.

        Initialize a new RotationMatrixIJK object.

        Parameters
        ----------
        a : 3x3 array-like of float, optional, default 3x3 identity matrix
            Values for matrix elements.
        OR
        ii, ji, ki, ij, jj, kj, ik, jk, kk : float
            Elements of new matrix in column-major order.

        Raises
        ------
        MalformedRotationException
            If the matrix is not a valid rotation matrix. Raised by
            checkRotation().
        """
        if len(args) == 0:
            # Create an identity rotation matrix.
            MatrixIJK.__init__(self, IDENTITY)
        else:
            MatrixIJK.__init__(self, *args)
        checkRotation(self, ROTATION_NORM_TOLERANCE,
                      ROTATION_DETERMINANT_TOLERANCE)


# Identity matrix (null rotation).
IDENTITY = RotationMatrixIJK([[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1]])
