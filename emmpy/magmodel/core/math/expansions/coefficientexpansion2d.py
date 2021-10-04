"""A 2-D array of expansion coefficients.

A 2-D array of expansion coefficients.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class CoefficientExpansion2D:
    """A 2-D array of expansion coefficients.

    An interface representing a two dimensional series expansion of
    coefficients (scalars i.e. doubles), that starts at a lower bound
    index (L) and ends at an upper bound index (U).

    This is similar to double[][] or List of Doubles, but with a non-zero
    starting index.
    """

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
        size = self.getIUpperBoundIndex() - self.getILowerBoundIndex() + 1
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
            Number of elements in 2nd dimesion of expansion.
        """
        size = self.getJUpperBoundIndex() - self.getJLowerBoundIndex() + 1
        return size

    def getILowerBoundIndex(self):
        """Return the lowest index of the 1st dimension of the expansion.
        
        Return the lowest index of the 1st dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Lowest index of 1st expansion dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getIUpperBoundIndex(self):
        """Return the highest index of the 1st dimension of the expansion.
        
        Return the highest index of the 1st dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Highest index of 1st expansion dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getJLowerBoundIndex(self):
        """Return the lowest index of the 2nd dimension of the expansion.
        
        Return the lowest index of the 2nd dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Lowest index of 2nd expansion dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getJUpperBoundIndex(self):
        """Return the highest index of the 2nd dimension of the expansion.
        
        Return the highest index of the 2nd dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Highest index of 2nd expansion dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getCoefficient(self, iIndex, jIndex):
        """Return i-jth coefficient for the expansion T_ij.

        Return i-jth coefficient for the expansion T_ij.

        Parameters
        ----------
        iIndex : int
            1st coefficient index.
        jIndex : int
            2nd coefficient index.
        
        Returns
        -------
        result : float
            i-jth coefficient for the expansion.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
