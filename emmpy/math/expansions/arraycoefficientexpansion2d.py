"""A 2-D array for a coefficient expansion.

A 2-D array of scalar expansion coefficients. The index of the first valid
row (iLowerBoundIndex) and column (jLowerBoundIndex) is not required to be 0.
Indexing is adjusted to account for a non-0 first index.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class ArrayCoefficientExpansion2D(np.ndarray):
    """A 2-D array of expansion coefficients.
    
    A 2-D array of expansion coefficients. The index of the first valid
    row (iLowerBoundIndex) and column (jLowerBoundIndex) is not required
    to be 0. Indexing is adjusted to account for a non-0 first index.

    Attributes
    ----------
    iLowerBoundIndex, iUpperBoundIndex : int
        Logical index of first and last valid rows.
    jLowerBoundIndex, jUpperBoundIndex : int
        Logical index of first and last valid columns.
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
        ace2d : Matrix
            The newly-allocated object.
        """
        nrows = len(data)
        ncols = len(data[0])
        ace2d = super().__new__(cls, shape=(nrows, ncols), dtype=float)
        return ace2d

    def __init__(self,  data, iLowerBoundIndex, jLowerBoundIndex):
        """Initialize a new ArrayCoefficientExpansion2D object.

        Converts a 2D double array into a CoefficientExpansion2D by
        wrapping the array. Note, this is a view friendly implementation, so
        the returned CoefficientExpansion2D will change as the array changes.

        Note, the supplied array must be rectangular (not ragged). This check
        is performed on construction but not on subsequent retrievals. This
        makes this a potentially unsafe implementation, if the supplied array
        becomes ragged after construction.

        Parameters
        ----------
        data : 2-D rectangular array of float
            The array of expansion coefficients.
        iLowerBoundIndex : int
            Index of first coefficient in 1st dimension.
        jLowerBoundIndex : int
            Index of first coefficient in 2nd dimension.
        """
        self[:] = data
        self.iLowerBoundIndex = iLowerBoundIndex
        self.iUpperBoundIndex = self.iLowerBoundIndex + len(data) - 1
        self.iSize = self.iUpperBoundIndex - self.iLowerBoundIndex + 1
        self.jLowerBoundIndex = jLowerBoundIndex
        self.jUpperBoundIndex = self.jLowerBoundIndex + len(data[0]) - 1
        self.jSize = self.jUpperBoundIndex - self.jLowerBoundIndex + 1

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
        data = -self
        iLowerBoundIndex = self.iLowerBoundIndex
        jLowerBoundIndex = self.jLowerBoundIndex
        negation = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        return negation

    def getCoefficient(self, azimuthalExpansion, radialExpansion):
        """Return the specified coefficient.
        
        Return the specified coefficient.
        
        Parameters
        ----------
        azimuthalExpansion : int
            Index of first dimension of coefficient.
        radialExpansion : int
            Index of second dimension of coefficient.
        
        Returns
        -------
        result : float
            Coefficient at specified index.
        """
        return (
            self[azimuthalExpansion - self.iLowerBoundIndex]
                [radialExpansion - self.jLowerBoundIndex]
        )
