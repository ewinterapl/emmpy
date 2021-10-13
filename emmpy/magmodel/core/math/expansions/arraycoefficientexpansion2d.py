"""A 2-D array of expansion coefficients.

A 2-D array of expansion coefficients.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)


class ArrayCoefficientExpansion2D(CoefficientExpansion2D):
    """A 2-D array of expansion coefficients.
    
    A 2-D array of expansion coefficients.
    """

    def __init__(self,  data, iLowerBoundIndex, jLowerBoundIndex):
        """Initialize a new ArrayCoefficientExpansion2D object.

        Converts a 2D double array into a CoefficientExpansion2D by
        wrapping the array. Note, this is a view friendly implementation, so
        the returned CoefficientExpansion2D will change as the array changes.

        Note, the supplied array must be rectangular (not ragged). This check
        is performed on construction but not on subsequent retrievals. This
        makes this a potentially unsafe implementation, if the supplied array
        becomes ragged after construction.

        Parameters
        ----------
        data : 2-D rectangular array of float
            The array of expansion coefficients.
        iLowerBoundIndex : int
            Index of first coefficient in 1st dimension.
        jLowerBoundIndex : int
            Index of first coefficient in 2nd dimension.
        """
        self.data = data
        self.iLowerBoundIndex = iLowerBoundIndex
        self.iUpperBoundIndex = self.iLowerBoundIndex + len(self.data) - 1
        self.jLowerBoundIndex = jLowerBoundIndex
        self.jUpperBoundIndex = self.jLowerBoundIndex + len(self.data[0]) - 1

    def iSize(self):
        """Return the element count in the 1st dimension of the expansion.
        
        Return the element count in the 1st dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        size : int
            Number of elements in 1st dimension of expansion.
        """
        size = self.iUpperBoundIndex - self.iLowerBoundIndex + 1
        return size

    def jSize(self):
        """Return the element count in the 2nd dimension of the expansion.
        
        Return the element count in the 2nd dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        size : int
            Number of elements in 2nd dimension of expansion.
        """
        size = self.jUpperBoundIndex - self.jLowerBoundIndex + 1
        return size

    # def getILowerBoundIndex(self):
    #     """Return the lowest index in the first dimension.
        
    #     Return the lowest index in the first dimension.

    #     Parameters
    #     ----------
    #     None

    #     Returns
    #     -------
    #     self.iLowerBoundIndex : int
    #         Index of first coefficient in 1st dimension.
    #     """
    #     return self.iLowerBoundIndex

    # def getIUpperBoundIndex(self):
    #     """Return the highest index in the first dimension.
        
    #     Return the highest index in the first dimension.

    #     Parameters
    #     ----------
    #     None

    #     Returns
    #     -------
    #     iUpperBoundIndex : int
    #         Index of last coefficient in 1st dimension.
    #     """
    #     iUpperBoundIndex = self.iLowerBoundIndex + len(self.data) - 1
    #     return iUpperBoundIndex

    # def getJLowerBoundIndex(self):
    #     """Return the lowest index in the second dimension.
        
    #     Return the lowest index in the second dimension.

    #     Parameters
    #     ----------
    #     None

    #     Returns
    #     -------
    #     self.jLowerBoundIndex : int
    #         Index of first coefficient in 2nd dimension.
    #     """
    #     return self.jLowerBoundIndex

    def getJUpperBoundIndex(self):
        """Return the highest index in the second dimension.
        
        Return the highest index in the second dimension.

        Parameters
        ----------
        None

        Returns
        -------
        jUpperBoundIndex : int
            Index of last coefficient in 2nd dimension.
        """
        jUpperBoundIndex = self.jLowerBoundIndex + len(self.data[0]) - 1
        return jUpperBoundIndex

    def getCoefficient(self, azimuthalExpansion, radialExpansion):
        """Return the specified coefficient.
        
        Return the specified coefficient.
        
        Parameters
        ----------
        azimuthalExpansion : int
            Index of first dimension of coefficient.
        radialExpansion : int
            Index of second dimension of coefficient.
        
        Returns
        -------
        result : float
            Coefficient at specified index.
        """
        return (
            self.data[azimuthalExpansion - self.iLowerBoundIndex]
                     [radialExpansion - self.jLowerBoundIndex]
        )
