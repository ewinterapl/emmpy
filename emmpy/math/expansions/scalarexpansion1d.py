"""A 1-D array of scalar expansion components.

A 1-D array of scalar expansion components. In effect, this class provides
an n-dimensional vector with a starting index that is logically not 0.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.vectors.vector import Vector


class ScalarExpansion1D(Vector):
    """A 1-D array of scalar expansion components.

    This class represents a series expansion of scalars that starts at
    a lower bound index (L) and ends at an upper bound index (U).
    L represents index 0 in the array, and U the index (len-1), where
    len = U - L + 1. In effect, this class provides an n-dimensional
    vector with a starting index that is not 0.
    """

    def __new__(cls, array, firstExpansionNumber):
        """Allocate a new ScalarExpansion1D object.

        Allocate a new ScalarExpansion1D object by allocating a new Vector
        object on which this class will expand.

        Parameters
        ----------
        array : array-like of float
            1-D array of scalar expansion components.
        firstExpansionNumber : int
            Index of first expansion coefficient.

        Returns
        -------
        se1d : ScalarExpansion1D
            The newly-created object.
        """
        se1d = super().__new__(cls, length=len(array))
        return se1d

    def __init__(self, data, firstExpansionNumber):
        """Initialize a new ScalarExpansion1D object.

        Initialize a new ScalarExpansion1D object.

        Parameters
        ----------
        data : array-like of float
            1-D array of scalar expansion components.
        firstExpansionNumber : int
            Index of first expansion coefficient.
        """
        self[:] = np.array(data)[:]
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
        lastExpansionNumber = self.firstExpansionNumber + len(self) - 1
        return lastExpansionNumber

    def getComponent(self, index):
        """Return the component at the specified index.

        Return the component at the specified index.

        Parameters
        ----------
        index : int
            Index of component to return.
        
        Returns
        -------
        result : float
            Desired expansion component.
        """
        return self[index - self.firstExpansionNumber]
