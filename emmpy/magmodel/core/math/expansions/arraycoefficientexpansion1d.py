"""A 1-D array for a coefficient expansion.

A 1-D array for a coefficient expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class ArrayCoefficientExpansion1D:
    """A 1-D array for a coefficient expansion.

    A 1-D array for a coefficient expansion.
    """

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
        self.array = np.array(array)
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
        return self.array[index - self.firstExpansionNumber]
