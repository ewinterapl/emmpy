"""A 2-D array of expansion coefficients.

A 2-D array of expansion coefficients.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class ArrayCoefficientExpansion2D:
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
        self.data = np.array(data)
        self.iLowerBoundIndex = iLowerBoundIndex
        self.iUpperBoundIndex = self.iLowerBoundIndex + len(self.data) - 1
        self.iSize = self.iUpperBoundIndex - self.iLowerBoundIndex + 1
        self.jLowerBoundIndex = jLowerBoundIndex
        self.jUpperBoundIndex = self.jLowerBoundIndex + len(self.data[0]) - 1
        self.jSize = self.jUpperBoundIndex - self.jLowerBoundIndex + 1

    # def iSize(self):
    #     """Return the element count in the 1st dimension of the expansion.
        
    #     Return the element count in the 1st dimension of the expansion.

    #     Parameters
    #     ----------
    #     None

    #     Returns
    #     -------
    #     size : int
    #         Number of elements in 1st dimension of expansion.
    #     """
    #     size = self.iUpperBoundIndex - self.iLowerBoundIndex + 1
    #     return size

    # def jSize(self):
    #     """Return the element count in the 2nd dimension of the expansion.
        
    #     Return the element count in the 2nd dimension of the expansion.

    #     Parameters
    #     ----------
    #     None

    #     Returns
    #     -------
    #     size : int
    #         Number of elements in 2nd dimension of expansion.
    #     """
    #     size = self.jUpperBoundIndex - self.jLowerBoundIndex + 1
    #     return size

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
