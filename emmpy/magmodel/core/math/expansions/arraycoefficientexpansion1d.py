"""A 1-D array for a coefficient expansion.

A 1-D array for a coefficient expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)


class ArrayCoefficientExpansion1D(CoefficientExpansion1D):
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
        self.array = array
        self.firstExpansionNumber = firstExpansionNumber

    def getLowerBoundIndex(self):
        """Return the lower index bound for the expansion.
        
        Return the lower index bound for the expansion.

        Returns
        -------
        self.firstExpansionNumber : int
            Index of first expansion coefficient.
        """
        return self.firstExpansionNumber

    def getUpperBoundIndex(self):
        """Return the upper index bound for the expansion.
        
        Return the upper index bound for the expansion.

        Returns
        -------
        lastExpansionNumber : int
            Index of last expansion coefficient.
        """
        lastExpansionNumber = self.firstExpansionNumber + len(self.array) - 1
        return lastExpansionNumber

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
