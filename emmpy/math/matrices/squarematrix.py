"""Abstract base class for square matrices (rank 2 square tensors).

Note that we use __new__ in addition to __init__ to enforce the specified
size of the matrix.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.matrices.matrix import Matrix


class SquareMatrix(Matrix):
    """Abstract base class for square matrices (rank 2 square tensors).

    A square matrix is defined as a rank 2 square tensor with an equal
    number of rows and columns. Indexing follows the Numpy row-major
    convention of [row, col] index ordering, i.e. matrix[i, j] (also
    matrix[i][j]) is the element in row i, column j.
    """

    def __new__(cls, length, *args, **kargs):
        """Allocate a new SquareMatrix object.

        Allocate a new SquareMatrix object by allocating a new np.ndarray
        on which the SquareMatrix will expand.

        The initial contents of the SquareMatrix are undefined.

        Parameters
        ----------
        length : integer
            Number of elements in each matrix dimesion.

        Returns
        -------
        m : SquareMatrix
            The newly-created object.
        """
        m = super().__new__(cls, nrows=length, ncols=length, dtype=float)
        return m
