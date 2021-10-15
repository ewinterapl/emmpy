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

    def negate(self):
        """Return a negated copy of the expansion.

        Return a negated copy of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        negation : ArrayCoefficientExpansion1D
            Expansion containing the negative of each original component.
        """
        data = -self
        negation = ArrayCoefficientExpansion1D(data, self.firstExpansionNumber)
        return negation
