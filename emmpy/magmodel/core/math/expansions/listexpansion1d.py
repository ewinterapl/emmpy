"""An expansion using a 1-D list.

An expansion using a 1-D list.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D


class ListExpansion1D(Expansion1D):
    """An expansion using a 1-D list.

    An expansion using a 1-D list.

    Attributes
    ----------
    aList : list
        List of expansion components.
    firstRadialExpansionNumber : int
        Index of first element in expansion.
    """

    def __init__(self, aList, firstRadialExpansionNumber):
        """Initialize a new ListExpansion1D object.

        Initialize a new ListExpansion1D object.

        Parameters
        ----------
        aList : list
            List of expansion components.
        firstRadialExpansionNumber : int
            Index of first element in expansion.
        """
        self.list = aList
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(aList) - 1
        )

    def getLowerBoundIndex(self):
        """Return the lowest expansion index.
        
        Return the lowest expansionindex.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Lowest expansion index.
        """
        return self.firstRadialExpansionNumber

    def getUpperBoundIndex(self):
        """Return the highest expansion index.
        
        Return the highest expansionindex.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Higest expansion index.
        """
        return self.lastRadialExpansionNumber

    def getExpansion(self, radialExpansion):
        """Return the specified expansion value.
        
        Return the specified expansion value.

        Parameters
        ----------
        radialExpansion : int
            Index of expansion component to return.
        
        Returns
        -------
        result : float
            Expansion component at specified index.
        """
        return self.list[radialExpansion - self.firstRadialExpansionNumber]
