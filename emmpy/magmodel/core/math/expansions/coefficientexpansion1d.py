"""emmpy.magmodel.core.math.expansions.coefficientexpansion1d"""


class CoefficientExpansion1D:
    """An interface representing a series expansion of coefficients (scalars
    i.e. doubles), that starts at a lower bound index (L) and ends at an upper
    bound index (U).

    This is similar to double[] or {@link List} of {@link Double}s, but with a
    non-zero starting index.

    @author G.K.Stephens
    """

    def toArray(self):
        """@return a newly constructed double array containing the elements of
        the expansion"""
        size = self.size()
        anArray = [None]*size
        for i in range(size):
            anArray[i] = self.getCoefficient(i + self.getLowerBoundIndex())
        return anArray

    def size(self):
        """@return the number of elements of the expansion"""
        size = self.getUpperBoundIndex() - self.getLowerBoundIndex() + 1
        return size

    def getLowerBoundIndex(self):
        """@return the lower bound index of the expansion (L)"""
        raise Exception

    def getUpperBoundIndex(self):
        """@return the upper bound index of the expansion (U)"""
        raise Exception

    def getCoefficient(self, index):
        """gets ith coefficient for the expansion T<sub>i</sub> in &#8721;
        T<sub>i</sub>

        @param index the index i
        @return the ith coefficient for the expansion corresponding to the
        index T<sub>i</sub>
        """
        raise Exception
