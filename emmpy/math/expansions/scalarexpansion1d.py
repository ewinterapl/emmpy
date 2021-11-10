"""A 1-D array of scalar expansion components.

A 1-D array of scalar expansion components. This is just a lightweight
extension of a 1-D np.ndarray.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class ScalarExpansion1D(np.ndarray):
    """A 1-D array of scalar expansion components.

    This class represents a 1-D expansion of scalars. This class can be
    used directly as an np.ndarray.

    Attributes
    ----------
    None
    """

    def __new__(cls, data):
        """Allocate a new ScalarExpansion1D object.

        Allocate a new ScalarExpansion1D object by allocating a new
        np.ndarray object on which this class will expand.

        Parameters
        ----------
        data : array-like of float
            1-D array of scalar expansion components.

        Returns
        -------
        se1d : ScalarExpansion1D
            The newly-allocated object.
        """
        se1d = super().__new__(cls, shape=(len(data),))
        return se1d

    def __init__(self, data):
        """Initialize a new ScalarExpansion1D object.

        Initialize a new ScalarExpansion1D object.

        Parameters
        ----------
        data : array-like of float
            1-D array of scalar expansion components.
        """
        self[...] = np.array(data)

    def invert(self):
        """Return an inverted copy of the expansion.

        Return an inverted copy of the expansion. Note that no checks for
        0-valued components are performed.

        Parameters
        ----------
        None

        Returns
        -------
        inverse : ScalarExpansion1D
            Expansion containing the inverse of each original component.
        """
        inverse = ScalarExpansion1D(1.0/self)
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
        scaled = ScalarExpansion1D(scaleFactor*self)
        return scaled

    @staticmethod
    def createUnity(length):
        """Create an expansion of unit scalars.

        Create an expansion of unit scalars of the specified size.

        Parameters
        ----------
        length : int
            Number of components in expansion.

        Returns
        -------
        unity : ScalarExpansion1D
            An expansion with unit coefficients.
        """
        data = np.ones(length)
        unity = ScalarExpansion1D(data)
        return unity
