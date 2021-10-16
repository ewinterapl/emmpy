"""A 1-D array for a coefficient expansion.

A 1-D array for a coefficient expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class ArrayCoefficientExpansion1D(np.ndarray):
    """A 1-D array for a coefficient expansion.

    A 1-D array for a coefficient expansion.
    """

    def __new__(cls, data, firstExpansionNumber):
        """Allocate a new ArrayCoefficientExpansion1D object.

        Allocate a new ArrayCoefficientExpansion1D object by allocating a
        new Vector object with the same length.

        Parameters
        ----------
        data : array-like of float
            List of expansion coefficients.
        firstExpansionNumber : int
            Index of first expansion coefficient.

        Returns
        -------
        ace1d : ArrayCoefficientExpansion1D
            The newly-created object.
        """
        nrows = len(data)
        ace1d = super().__new__(cls, shape=(nrows,), dtype=float)
        return ace1d

    def __init__(self, array, firstExpansionNumber):
        """Initialize a new ArrayCoefficientExpansion1D object.

        Initialize a new ArrayCoefficientExpansion1D object.

        Parameters
        ----------
        array : list of double
            List of expansion coefficients.
        firstExpansionNumber : int
            Index of first expansion coefficient.
        """
        self[:] = array
        self.firstExpansionNumber = firstExpansionNumber
        self.lastExpansionNumber = firstExpansionNumber + len(array) - 1

    def invert(self):
        """Return an inverted copy of the expansion.

        Return an inverted copy of the expansion. Note that no checks for
        0 coefficients are performed.

        Parameters
        ----------
        None

        Returns
        -------
        inverse : ArrayCoefficientExpansion1D
            Expansion containing the inverse of each original component.
        """
        data = 1/self
        inverse = ArrayCoefficientExpansion1D(data, self.firstExpansionNumber)
        return inverse

    def scale(self, scaleFactor):
        """Create a scaled copy of the expansion.

        Create a scaled copy of the expansion.

        Parameters
        ----------
        scaleFactor : float
            Scale factor to apply to expansion.

        Returns
        -------
        scaled : ArrayCoefficientExpansion1D
            Scaled copy of the expansion.
        """
        data = scaleFactor*self
        scaled = ArrayCoefficientExpansion1D(data, self.firstExpansionNumber)
        return scaled

    def getCoefficient(self, index):
        """Return the coefficient at the specified index.

        Return the coefficient at the specified index.

        Parameters
        ----------
        index : int
            Index of coefficient to return.
        
        Returns
        -------
        result : float
            Desired expansion coefficient.
        """
        return self[index - self.firstExpansionNumber]


def createUnity(i_min, i_max):
    """Create an expansion of unit coefficients.

    Create an expansion of unit coefficients using the specified logical
    index limits.

    Parameters
    ----------
    i_min, i_max : int
        Lowest and highest logical indices for expansion.

    Returns
    -------
    unity : ArrayCoefficientExpansion1D
        An expansion with unit coefficients.
    """
    length = i_max - i_min + 1
    data = np.ones(length)
    unity = ArrayCoefficientExpansion1D(data, i_min)
    return unity
