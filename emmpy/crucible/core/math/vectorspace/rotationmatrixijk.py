"""A 3-D rotation matrix in Cartesian (i, j, k) coordinates.

A 3-D rotation matrix in Cartesian (i, j, k) coordinates.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectorspace.internaloperations import (
    checkRotation
)
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


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
            If the matrix is not a valid rotation matrix.
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            # Creates an identity rotation matrix.
            data = (1, 0, 0, 0, 1, 0, 0, 0, 1)
            MatrixIJK.__init__(self, *data)
        elif len(args) == 1:
            # Initialize matrix from a 3x3 array-like of floats.
            (a,) = args
            MatrixIJK.__init__(self, a)
        elif len(args) == 9:
            # Matrix elements in column-major order.
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            data = [ii, ji, ki, ij, jj, jk, ik, jk, kk]
            MatrixIJK.__init__(self, *data)
        else:
            raise ValueError
        checkRotation(self, ROTATION_NORM_TOLERANCE,
                      ROTATION_DETERMINANT_TOLERANCE)
