"""A 2-D array for a coefficient expansion.

A 2-D array of scalar expansion components. The index of the first valid
row (iLowerBoundIndex) and the first valid column (jLowerBoundIndex) are
not required to be 0. The stored array is padded with unused rows before
the first valid row, and unused columns in each row before the first valid
column. This allows the non-0-based indexing to work directly, at the
expense of some unused memory. This approach is faster than indexing with
offsets at each access, and allows the expansion to be used as a numpy
array directly using slicing, e.g.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.utilities.nones import nones


class ArrayCoefficientExpansion2D(np.ndarray):
    """A 2-D array of expansion coefficients.
    
    A 2-D array of scalar expansion components. The index of the first
    valid row (iLowerBoundIndex) and the first valid column
    (jLowerBoundIndex) are not required to be 0. The stored array is
    padded with unused rows before the first valid row, and unused
    columns in each row before the first valid column. This allows the
    non-0-based indexing to work directly, at the expense of some unused
    memory. This approach is faster than indexing with offsets at each
    access, and allows the expansion to be used as a numpy array directly
    using slicing, e.g.
    expansion[iJlowerBoundIndex:, jLowerBoundIndex:.]

    Attributes
    ----------
    iLowerBoundIndex, iUpperBoundIndex : int
        Logical index of first and last valid rows.
    jLowerBoundIndex, jUpperBoundIndex : int
        Logical index of first and last valid columns.
    iSize, jSize : int
        Number of logical rows and columns, respectively.
    """

    def __new__(cls, data, iLowerBoundIndex, jLowerBoundIndex):
        """Allocate a new ArrayCoefficient2D object.

        Allocate a new ArrayCoefficient2D object by allocating a new
        np.ndarray on which ArrayCoefficient2D will expand.

        Parameters
        ----------
        data : 2-D rectangular array-like of float
            The array of expansion coefficients.
        iLowerBoundIndex : int
            Logical index of first valid row of coefficients.
        jLowerBoundIndex : int
            Logical index of first valid column of coefficients.

        Returns
        -------
        ace2d : ArrayCoefficientExpansion2D
            The newly-allocated object.
        """
        nrows = len(data) + iLowerBoundIndex
        ncols = len(data[0]) + jLowerBoundIndex
        ace2d = super().__new__(cls, shape=(nrows, ncols), dtype=float)
        return ace2d

    def __init__(self,  data, iLowerBoundIndex, jLowerBoundIndex):
        """Initialize a new ArrayCoefficientExpansion2D object.

        Initialize a ArrayCoefficient2D object.

        Parameters
        ----------
        data : 2-D rectangular array of float
            The array of expansion coefficients.
        iLowerBoundIndex : int
            Index of first valid row of coefficients.
        jLowerBoundIndex : int
            Index of first valid column of coefficients.
        """
        self[iLowerBoundIndex:, jLowerBoundIndex:] = data
        self.iLowerBoundIndex = iLowerBoundIndex
        self.iSize = len(data)
        self.iUpperBoundIndex = self.iLowerBoundIndex + self.iSize - 1
        self.jLowerBoundIndex = jLowerBoundIndex
        self.jSize = len(data[0])
        self.jUpperBoundIndex = self.jLowerBoundIndex + self.jSize - 1

    def negate(self):
        """Return a negated copy of the expansion.

        Return a negated copy of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        negation : ArrayCoefficientExpansion2D
            A negated copy of this expansion.
        """
        iLowerBoundIndex = self.iLowerBoundIndex
        jLowerBoundIndex = self.jLowerBoundIndex
        data = -self[iLowerBoundIndex:, jLowerBoundIndex:]
        negation = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        return negation

    def scale(self, scale_factor):
        """Return a scaled copy of the expansion.

        Return a scaled copy of the expansion.

        Parameters
        ----------
        scale_factor : float
            Scale factor to apply to expansion.

        Returns
        -------
        scaled : ArrayCoefficientExpansion2D
            A scaled copy of this expansion.
        """
        iLowerBoundIndex = self.iLowerBoundIndex
        jLowerBoundIndex = self.jLowerBoundIndex
        data = scale_factor*self[iLowerBoundIndex:, jLowerBoundIndex:]
        scaled = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        return scaled

    @staticmethod
    def add(a, b):
        """Compute the sum of two expansions.

        Compute the sum of two expansions. The expansions are assumed to have
        the same shape and logical index limits.

        Parameters
        ----------
        a, b : ArrayCoefficientExpansion2D
            Expansions to add.

        Returns
        -------
        exp_sum : ArrayCoefficientExpansion2D
            Sum of the two expansions.
        """
        iLowerBoundIndex = a.iLowerBoundIndex
        jLowerBoundIndex = a.jLowerBoundIndex
        data = (
            a[iLowerBoundIndex:, jLowerBoundIndex:] +
            b[iLowerBoundIndex:, jLowerBoundIndex:]
        )
        exp_sum = ArrayCoefficientExpansion2D(data, iLowerBoundIndex, jLowerBoundIndex)
        return exp_sum

    @staticmethod
    def createNullExpansion(row_min, row_max, col_min, col_max):
        """Create an expansion of null coefficients.

        Create an expansion of null coefficients using the specified logical
        index limits.

        Parameters
        ----------
        row_min, row_max, col_min, col_max : int
            Lowest and highest logical indices for rows and columns.

        Returns
        -------
        null : ArrayCoefficientExpansion2D
            An expansion with null coefficients.
        """
        n_rows = row_max - row_min + 1
        n_cols = col_max - col_min + 1
        nulls = nones((n_rows, n_cols))
        data = np.array(nulls)
        null = ArrayCoefficientExpansion2D(data, row_min, col_min)
        return null

    @staticmethod
    def createUnity(row_min, row_max, col_min, col_max):
        """Create an expansion of unit coefficients.

        Create an expansion of unit coefficients using the specified logical
        index limits.

        Parameters
        ----------
        row_min, row_max, col_min, col_max : int
            Lowest and highest logical indices for rows and columns.

        Returns
        -------
        unity : ArrayCoefficientExpansion2D
            An expansion with unit coefficients.
        """
        n_rows = row_max - row_min + 1
        n_cols = col_max - col_min + 1
        data = np.ones((n_rows, n_cols))
        unity = ArrayCoefficientExpansion2D(data, row_min, col_min)
        return unity
