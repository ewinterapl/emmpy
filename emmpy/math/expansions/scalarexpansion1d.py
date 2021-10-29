"""A 1-D array of scalar expansion components.

A 1-D array of scalar expansion components. The index of the first valid
component (firstExpansionNumber) is not required to be 0. The stored array
is padded with unused elements at the head of the array, to allow for the
desired indexing to work properly.

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
    required to be 0. To permit this, the stored array is padded with
    unused elements at the head of the array. For example, if
    firstExpansionNumber is 2, then elements 0 and 1 in the array are
    allocated, but ignored. This is more efficient than recomputing
    the index on every access, since firstExpansionNumber is usually a
    small integer. It also allows the expansion to be used directly as a
    numpy array, by using slicing of the form:

    valid_components = expansion[firstExpansionNumber:]

    Attributes
    ----------
    firstExpansionNumber : int
        Index of first expansion component.
    lastExpansionNumber : int
        Index of last expansion component.
    """

    def __new__(cls, data, firstExpansionNumber):
        """Allocate a new ScalarExpansion1D object.

        Allocate a new ScalarExpansion1D object by allocating a new
        np.ndarray object on which this class will expand. Extra, unused
        elements are padded at the head of the array to allow for non-0-
        based indexing.

        Parameters
        ----------
        data : array-like of float
            1-D array of scalar expansion components.
        firstExpansionNumber : int
            Logical index of first expansion component.

        Returns
        -------
        se1d : ScalarExpansion1D
            The newly-allocated object.
        """
        size = len(data) + firstExpansionNumber
        se1d = super().__new__(cls, shape=(size,))
        return se1d

    def __init__(self, data, firstExpansionNumber):
        """Initialize a new ScalarExpansion1D object.

        Initialize a new ScalarExpansion1D object. Note that the padding
        elements (equal to firstExpansionNumber elements) are ignored.

        Parameters
        ----------
        data : array-like of float
            1-D array of scalar expansion components.
        firstExpansionNumber : int
            Index of first valid expansion component.
        """
        self[firstExpansionNumber:] = np.array(data)
        self.firstExpansionNumber = firstExpansionNumber
        self.lastExpansionNumber = self.firstExpansionNumber + len(data) - 1

    def invert(self):
        """Return an inverted copy of the expansion.

        Return an inverted copy of the expansion. Note that no checks for
        0 coefficients are performed.

        Parameters
        ----------
        None

        Returns
        -------
        inverse : ScalarExpansion1D
            Expansion containing the inverse of each original component.
        """
        data = 1/self[self.firstExpansionNumber:]
        inverse = ScalarExpansion1D(data, self.firstExpansionNumber)
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
        scaled : ScalarExpansion1D
            Scaled copy of the expansion.
        """
        data = scaleFactor*self[self.firstExpansionNumber:]
        scaled = ScalarExpansion1D(data, self.firstExpansionNumber)
        return scaled


def createUnity(firstExpansionNumber, lastExpansionNumber):
    """Create an expansion of unit scalars.

    Create an expansion of unit scalars using the specified logical
    index limits.

    Parameters
    ----------
    firstExpansionNumber, lastExpansionNumber : int
        Lowest and highest logical indices for expansion.

    Returns
    -------
    unity : ScalarExpansion1D
        An expansion with unit coefficients.
    """
    length = lastExpansionNumber - firstExpansionNumber + 1
    data = np.ones(length)
    unity = ScalarExpansion1D(data, firstExpansionNumber)
    return unity
