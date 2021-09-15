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
        Expansion coefficiens.
    firstRadialExpansionNumber : int
        Index of first coefficient in expansion.
    lastRadialExpansionNumber : int
        Index of last coefficient in expansion.
    """

    def __init__(self, array, firstRadialExpansionNumber):
        """Initialize a new ArrayEpansion1D object.

        Initialize a new ArrayEpansion1D object.

        Parameters
        ----------
        array : list of float
            Expansion coefficiens.
        firstRadialExpansionNumber : int
            Index of first coefficient in expansion.
        """
        self.array = array
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(array) - 1
        )

    def getLowerBoundIndex(self):
        """Return the lowest expansion coefficient index.

        Return the lowest expansion coefficient index.

        Parameters
        ----------
        None

        Returns
        -------
        self.firstRadialExpansionNumber : int
            Index of first expansion coefficient.
        """
        return self.firstRadialExpansionNumber

    def getUpperBoundIndex(self):
        """Return the highest expansion coefficient index.

        Return the highest expansion coefficient index.

        Parameters
        ----------
        None

        Returns
        -------
        self.lastRadialExpansionNumber : int
            Index of last expansion coefficient.
        """
        return self.lastRadialExpansionNumber

    def getExpansion(self, radialExpansion):
        """Return the the specified expansion coefficient.
        
        Return the the specified expansion coefficient.

        Parameters
        ----------
        radialExpansion : int
            Index of expansion coefficient to retrieve.

        Returns
        -------
        result : float
            Value of expansion coefficient at specified index.
        """
        return self.array[radialExpansion - self.firstRadialExpansionNumber]
