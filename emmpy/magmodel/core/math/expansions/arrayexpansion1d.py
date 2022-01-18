"""A 1-D array of expansion values.

A 1-D array of expansion values.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D


class ArrayExpansion1D(Expansion1D):
    """A 1-D array of expansion values.

    A 1-D array of expansion values.

    Attributes
    ----------
    array : array-like of float
        Expansion values.
    """

    def __init__(self, array):
        """Initialize a new ArrayEpansion1D object.

        Initialize a new ArrayEpansion1D object.

        Parameters
        ----------
        array : list of float
            Expansion values.
        """
        self.array = array

    def getExpansion(self, radialExpansion):
        """Return the the specified expansion value.
        
        Return the the specified expansion value.

        Parameters
        ----------
        radialExpansion : int
            Index of expansion value to retrieve.

        Returns
        -------
        result : float
            Value of expansion at specified index.
        """
        return self.array[radialExpansion]
