"""emmpy.magmodel.core.math.expansions.expansion2d"""


class Expansion2D:
    """An interface representing an arbitrary two dimensional series
    expansion, that starts at a lower bound index (L) and ends at an upper
    bound index (U), where T is any Object.

    This is similar to a 2-D array or List of Ts, but with a non-zero
    starting index. If the object is a Double, the interface
    CoefficientExpansion2D can be used instead to avoid autoboxing.

    author G.K.Stephens
    param <T> some arbitrary object that is represented in the expansion
    (common examples would include math objects like Vectors VectorIJK)
    """
    pass

    # def iSize(self):
    #     """@return the number of elements of the expansion"""
    #     size = self.getIUpperBoundIndex() - self.getILowerBoundIndex() + 1
    #     return size

    # def jSize(self):
    #     """@return the number of elements of the expansion"""
    #     size = self.getJUpperBoundIndex() - self.getJLowerBoundIndex() + 1
    #     return size

    # def getILowerBoundIndex(self):
    #     """@return the lower bound index of the expansion (L)"""
    #     raise Exception

    # def getIUpperBoundIndex(self):
    #     """@return the upper bound index of the expansion (U<sub>i</sub>)"""
    #     raise Exception

    # def getJLowerBoundIndex(self):
    #     """@return the lower bound index of the expansion (L<sub>j</sub>)"""
    #     raise Exception

    # def getJUpperBoundIndex(self):
    #     """@return the upper bound index of the expansion (U<sub>j</sub>)"""
    #     raise Exception

    # def getExpansion(self, mIndex, nIndex):
    #     """gets i-jth coefficient for the expansion T<sub>ij</sub> in &#8721;
    #     T<sub>ij</sub>

    #     @param iIndex the index i
    #     @param jIndex the index j
    #     @return the i-jth coefficient for the expansion corresponding to the
    #     index T<sub>ij</sub>
    #     """
    #     raise Exception
