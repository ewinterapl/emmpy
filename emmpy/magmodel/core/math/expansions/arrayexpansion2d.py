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
    lastAzimuthalExpansionNumber : int
        First and last index of expansion values in 1st dimension.
    firstRadialExpansionNumber, lastRadialExpansionNumber : int
        First and last index of expansion values in 2nd dimension.
    """

    def __init__(self, data, firstRadialExpansionNumber):
        """Initialize a new ArrayExpansion2D object.

        Initialize a new ArrayExpansion2D object.

        Parameters
        ----------
        data : 2-D list of float
            Expansion values.
        firstRadialExpansionNumber : int
            First index of expansion values in 2nd dimension.
        """
        self.data = data
        self.lastAzimuthalExpansionNumber = len(data) - 1
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(data[0]) - 1
        )

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
            self.data[azimuthalExpansion][radialExpansion - self.firstRadialExpansionNumber]
        )
