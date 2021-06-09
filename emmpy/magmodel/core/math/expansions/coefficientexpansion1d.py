"""A 1-D array of expansion coefficients."""


from emmpy.utilities.nones import nones


class CoefficientExpansion1D:
    """A 1-D array of expansion coefficients.

    An interface representing a series expansion of coefficients (scalars
    i.e. doubles), that starts at a lower bound index (L) and ends at an upper
    bound index (U).

    This is similar to double[] or List of Double, but with a non-zero starting
    index.

    author G.K.Stephens
    """

    def toArray(self):
        """Create a list containing the elements of the expansion."""
        size = self.size()
        anArray = nones((size,))
        for i in range(size):
            anArray[i] = self.getCoefficient(i + self.getLowerBoundIndex())
        return anArray

    def size(self):
        """Return the number of elements of the expansion."""
        size = self.getUpperBoundIndex() - self.getLowerBoundIndex() + 1
        return size

    def getLowerBoundIndex(self):
        """Return the lower bound index of the expansion (L)."""
        raise Exception

    def getUpperBoundIndex(self):
        """Return the upper bound index of the expansion (U)."""
        raise Exception

    def getCoefficient(self, index):
        """Return the ith coefficient for the expansion T_i.

        param index the index i
        return the ith coefficient for the expansion corresponding to the
        index T_i
        """
        raise Exception
