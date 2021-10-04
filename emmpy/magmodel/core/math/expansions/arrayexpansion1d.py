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
    array : list of float
        Expansion values.
    firstRadialExpansionNumber : int
        Index of first value in expansion.
    lastRadialExpansionNumber : int
        Index of last value in expansion.
    """

    def __init__(self, array, firstRadialExpansionNumber):
        """Initialize a new ArrayEpansion1D object.

        Initialize a new ArrayEpansion1D object.

        Parameters
        ----------
        array : list of float
            Expansion values.
        firstRadialExpansionNumber : int
            Index of first value in expansion.
        """
        self.array = array
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(array) - 1
        )

    def getLowerBoundIndex(self):
        """Return the lowest expansion value index.

        Return the lowest expansion value index.

        Parameters
        ----------
        None

        Returns
        -------
        self.firstRadialExpansionNumber : int
            Index of first expansion value.
        """
        return self.firstRadialExpansionNumber

    def getUpperBoundIndex(self):
        """Return the highest expansion value index.

        Return the highest expansion value index.

        Parameters
        ----------
        None

        Returns
        -------
        self.lastRadialExpansionNumber : int
            Index of last expansion value.
        """
        return self.lastRadialExpansionNumber

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
        return self.array[radialExpansion - self.firstRadialExpansionNumber]
