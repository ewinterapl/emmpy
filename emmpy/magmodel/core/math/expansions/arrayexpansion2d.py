"""A 2-D array of expansion values.

A 2-D array of expansion values.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D


class ArrayExpansion2D(Expansion2D):
    """A 2-D array of expansion values.
    
    A 2-D array of expansion values.

    Attributes
    ----------
    data : 2-D list of float
        Expansion values.
    firstAzimuthalExpansionNumber, lastAzimuthalExpansionNumber : int
        First and last index of expansion values in 1st dimension.
    firstRadialExpansionNumber, lastRadialExpansionNumber : int
        First and last index of expansion values in 2nd dimension.
    """

    def __init__(self, data, firstAzimuthalExpansionNumber,
                 firstRadialExpansionNumber):
        """Initialize a new ArrayExpansion2D object.

        Initialize a new ArrayExpansion2D object.

        Parameters
        ----------
        data : 2-D list of float
            Expansion values.
        firstAzimuthalExpansionNumber : int
            First index of expansion values in 1st dimension.
        firstRadialExpansionNumber : int
            First index of expansion values in 2nd dimension.
        """
        self.data = data
        self.firstAzimuthalExpansionNumber = firstAzimuthalExpansionNumber
        self.lastAzimuthalExpansionNumber = (
            firstAzimuthalExpansionNumber + len(data) - 1
        )
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(data[0]) - 1
        )

    def getJLowerBoundIndex(self):
        """Return the lowest second index.
        
        Return the lowest second index.

        Parameters
        ----------
        None

        Returns
        -------
        self.firstRadialExpansionNumber : int
            Lowest index of 2nd expansion dimension.
        """
        return self.firstRadialExpansionNumber

    def getJUpperBoundIndex(self):
        """Return the highest second index.
        
        Return the highest second index.

        Parameters
        ----------
        None

        Returns
        -------
        self.lastRadialExpansionNumber : int
            Highest index of 2nd expansion dimension.
        """
        return self.lastRadialExpansionNumber

    def getIUpperBoundIndex(self):
        """Return the highest first index.
        
        Return the highest first index.

        Parameters
        ----------
        None

        Returns
        -------
        self.lastAzimuthalExpansionNumber : int
            Highest index of first expansion dimension.
        """
        return self.lastAzimuthalExpansionNumber

    def getExpansion(self, azimuthalExpansion, radialExpansion):
        """Return the specified expansion component.
        
        Return the specified expansion component.

        Parameters
        ----------
        azimuthalExpansion : int
            Expansion index in first dimension.
        radialExpansion : int
            Expansion index in second dimension.
        
        Returns
        -------
        result : float
            Value of expansion at specified index.
        """
        return (
            self.data[azimuthalExpansion - self.firstAzimuthalExpansionNumber]
            [radialExpansion - self.firstRadialExpansionNumber]
        )
