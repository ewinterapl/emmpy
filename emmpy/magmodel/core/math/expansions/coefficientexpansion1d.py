"""A 1-D array of expansion coefficients.

A 1-D array of expansion coefficients.

This class was generated from a Java interface, and therfore most of the
methods defined here raise an exception when invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.utilities.nones import nones


class CoefficientExpansion1D:
    """A 1-D array of expansion coefficients.

    An interface representing a series expansion of coefficients (scalars
    i.e. doubles), that starts at a lower bound index (L) and ends at an
    upper bound index (U).

    This is similar to double[] or List of Double, but with a non-zero starting
    index.
    """

    def size(self):
        """Return the number of elements of the expansion.
        
        Return the number of elements of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        size : int
            Number of elements in the expansion coefficient list.
        """
        size = self.getUpperBoundIndex() - self.getLowerBoundIndex() + 1
        return size
