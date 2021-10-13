"""A 1-D array for a coefficient expansion.

A 1-D array for a coefficient expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.vectors.vector import Vector


class ArrayCoefficientExpansion1D(Vector):
    """A 1-D array for a coefficient expansion.

    A 1-D array for a coefficient expansion.
    """

    def __new__(cls, array, firstExpansionNumber):
        """Allocate a new ArrayCoefficientExpansion1D object.

        Allocate a new ArrayCoefficientExpansion1D object by allocating a
        new Vector object with the same length.

        Parameters
        ----------
        array : list of double
            List of expansion coefficients.
        firstExpansionNumber : int
            Index of first expansion coefficient.

        Returns
        -------
        v : Vector3D
            The newly-created object.
        """
        v = super().__new__(cls, length=len(array))
        return v

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
