"""A 2-D array of expansion coefficients."""


class CoefficientExpansion2D:
    """A 2-D array of expansion coefficients.

    An interface representing a two dimensional series expansion of
    coefficients (scalars i.e. doubles), that starts at a lower bound index
    (L) and ends at an upper bound index (U).

    This is similar to double[][] or {@link List} of {@link Double}s, but with
    a non-zero starting index.

    @author G.K.Stephens
    """

    # def toArray(self):
    #     """@return a newly constructed double array containing the elements of
    #     the expansion"""
    #     iSize = self.iSize()
    #     jSize = self.jSize()
    #     a = [None]*jSize
    #     anArray = [a]*iSize
    #     for i in range(iSize):
    #         for j in range(jSize):
    #             anArray[i][j] = self.getCoefficient(
    #                 i + self.getILowerBoundIndex(),
    #                 j + self.getJLowerBoundIndex())
    #     return anArray

    def iSize(self):
        """Return the element count in the 1st dimension of the expansion."""
        size = self.getIUpperBoundIndex() - self.getILowerBoundIndex() + 1
        return size

    def jSize(self):
        """Return the element count in the 2nd dimension of the expansion."""
        size = self.getJUpperBoundIndex() - self.getJLowerBoundIndex() + 1
        return size

    def getILowerBoundIndex(self):
        """Return the lowest index of the 1st dimension of the expansion."""
        raise Exception

    def getIUpperBoundIndex(self):
        """Return the highest index of the 1st dimension of the expansion."""
        raise Exception

    def getJLowerBoundIndex(self):
        """Return the lowest index of the 2nd dimension of the expansion."""
        raise Exception

    def getJUpperBoundIndex(self):
        """Return the lowest index of the 2nd dimension of the expansion."""
        raise Exception

    def getCoefficient(self, iIndex, jIndex):
        """Return i-jth coefficient for the expansion T_ij.

        param iIndex the index i
        param jIndex the index j
        return the i-jth coefficient for the expansion corresponding to the
        index T_ij
        """
        raise Exception
