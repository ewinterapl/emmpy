"""Interface for a 2-D expansion.

Interface for a 2-D expansion.

This class was created based on a Java interface, and therefore many of
the methods will raise an exception if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class Expansion2D:
    """Interface for a 2-D expansion.

    An interface representing an arbitrary two dimensional series
    expansion, that starts at a lower bound index (L) and ends at an upper
    bound index (U), where T is any Object.

    This is similar to a 2-D array or List of Ts, but with a non-zero
    starting index. If the object is a Double, the interface
    CoefficientExpansion2D can be used instead to avoid autoboxing.
    """

    def iSize(self):
        """Return count of elements in the 1st dimension of the expansion.
        
        Return count of elements in the 1st dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        size : int
            Number of elements in 1st dimension.
        """
        size = self.getIUpperBoundIndex() - self.getILowerBoundIndex() + 1
        return size

    def jSize(self):
        """Return count of elements in the 2nd dimension of the expansion.
        
        Return count of elements in the 2nd dimension of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        size : int
            Number of elements in 2nd dimension.
        """
        size = self.getJUpperBoundIndex() - self.getJLowerBoundIndex() + 1
        return size

    def getILowerBoundIndex(self):
        """Return the lowest index along the 1st dimension.
        
        Return the lowest index along the 1st dimension.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Lowest expansion index along 1st dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getIUpperBoundIndex(self):
        """Return the highest index along the 1st dimension.
        
        Return the highest index along the 1st dimension.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Highest expansion index along 1st dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getJLowerBoundIndex(self):
        """Return the lowest index along the 2nd dimension.
        
        Return the lowest index along the 2nd dimension.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Lowest expansion index along 2nd dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getJUpperBoundIndex(self):
        """Return the highest index along the 2nd dimension.
        
        Return the highest index along the 2nd dimension.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Highest expansion index along 2nd dimension.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise Exception
