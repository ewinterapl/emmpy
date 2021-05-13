"""emmpy.magmodel.core.math.expansions.coefficientexpansion2d"""


class CoefficientExpansion2D:
    """An interface representing a two dimensional series expansion of
    coefficients (scalars i.e. doubles), that starts at a lower bound index
    (L) and ends at an upper bound index (U).

    This is similar to double[][] or {@link List} of {@link Double}s, but with
    a non-zero starting index.

    @author G.K.Stephens
    """
    pass

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
        """return the number of elements of the expansion"""
        size = self.getIUpperBoundIndex() - self.getILowerBoundIndex() + 1
        return size

    def jSize(self):
        """return the number of elements of the expansion"""
        size = self.getJUpperBoundIndex() - self.getJLowerBoundIndex() + 1
        return size

    def getILowerBoundIndex(self):
        """return the lower bound index of the expansion (L_i)"""
        raise Exception

    def getIUpperBoundIndex(self):
        """return the upper bound index of the expansion (U_i)"""
        raise Exception

    def getJLowerBoundIndex(self):
        """return the lower bound index of the expansion (L<sub>j</sub>)"""
        raise Exception

    def getJUpperBoundIndex(self):
        """return the upper bound index of the expansion (U<sub>j</sub>)"""
        raise Exception

    def getCoefficient(self, iIndex, jIndex):
        """gets i-jth coefficient for the expansion T_ij

        param iIndex the index i
        param jIndex the index j
        return the i-jth coefficient for the expansion corresponding to the
        index T_ij
        """
        raise Exception
