"""A 2-D rotation matrix in Cartesian coordinates.

This class provides methods for a 2-D rotation matrix in Cartesian (x, y)
coordinates. This class was designed as a lightweight extension to
the Matrix2D class, adding code to process 2-D rotations. Since this class
ultimately derives from np.ndarray, objects of this class may be used
directly as np.ndarray objects to take advantage of Numpy operations.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.matrices.matrix2d import Matrix2D


class RotationMatrix2D(Matrix2D):
    """A 2-D rotation matrix in Cartesian coordinates.

    The 2-D rotation matrix is a standard 2-D Cartesian matrix, with
    additional code to ensure the matrix represents a valid 2-D rotation.

    Attributes
    ----------
    None
    """

    def __init__(self, *args, **kargs):
        """Initialize a new RotationMatrix2D object.

        Initialize a new RotationMatrix2D object. All this method does
        is verify that the new matrix is a valid 2-D rotation. If no
        matrix is provided, a 2x2 identity matrix is created, which is
        always a valid rotation matrix.

        Parameters
        ----------
        As for Matrix2D.__init__().

        Raises
        ------
        TypeError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            super().__init__(np.eye(2), **kargs)
        else:
            super().__init__(*args, **kargs)
        if not self.isValidRotation(self):
            raise TypeError

    @staticmethod
    def isValidRotation(m):
        """Verify a matrix represents a valid 2-D rotation.

        Verify the provided matrix represents a valid 2-D rotation. A
        matrix m is a valid 2-D rotation matrix if and only if:
        
        0. The shape of the matrix is (2, 2).
        1. The matrix has unit determinant.
        2. The matrix inverse is equal to the matrix transpose.

        Note that this method can be used on any np.ndarray-derived
        object, not just RotationMatrix2D objects.

        Parameters
        ----------
        m : np.ndarray
            The matrix to check for valid rotation.

        Returns
        -------
        _isValidRotation : bool
            True if m is a valid 2-D rotation matrix, otherwise False.
        """
        _isValidRotation = True

        # Check that the matrix has the correct shape.
        if m.shape != (2, 2):
            _isValidRotation = False

        # Check that the matrix has unit determinant.
        if not np.isclose(np.linalg.det(m), 1.0):
            _isValidRotation = False

        # Check that the matrix transpose and inverse are equal.
        if not np.isclose(m.T, np.linalg.inv(m)).all():
            _isValidRotation = False

        return _isValidRotation
