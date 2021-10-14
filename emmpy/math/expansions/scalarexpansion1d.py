"""A 1-D array of scalar expansion components.

A 1-D array of scalar expansion components. The index of the first valid
component (firstExpansionNumber) is not required to be 0. Component access
by index is adjusted from the logical index to the physical index.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class ScalarExpansion1D(np.ndarray):
    """A 1-D array of scalar expansion components.

    This class represents a series expansion of scalars that starts at
    a lower bound index (L) and ends at an upper bound index (U).
    The index of the first valid component (firstExpansionNumber) is not
    required to be 0. Component access by index is adjusted from the
    logical index to the physical index.

    Attributes
    ----------
    firstExpansionNumber : int
        Logical index of first expansion coefficient. Maps to physical
        index 0 in the stored array.
    lastExpansionNumber : int
        Logical index of last expansion coefficient. Maps to last physical
        index in the stored array.
    """

    def __new__(cls, data, firstExpansionNumber):
        """Allocate a new ScalarExpansion1D object.

        Allocate a new ScalarExpansion1D object by allocating a new
        np.ndarray object on which this class will expand.

        Parameters
        ----------
        data : array-like of float
            1-D array of scalar expansion components.
        firstExpansionNumber : int
            Logical index of first expansion coefficient.

        Returns
        -------
        se1d : ScalarExpansion1D
            The newly-allocated object.
        """
        size = len(data)
        se1d = super().__new__(cls, shape=(size,))
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
        self[:] = np.array(data)
        self.firstExpansionNumber = firstExpansionNumber
        self.lastExpansionNumber = self.firstExpansionNumber + len(self) - 1

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
