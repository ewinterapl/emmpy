"""emmpy.magmodel.core.math.expansions.expansion1d"""


class Expansion1D:
    """An interface representing an arbitrary series expansion, that starts at
    a lower bound index (L) and ends at an upper bound index (U), where T is
    any {@link Object}.

    This is similar to an array or {@link List} of Ts, but with a non-zero
    starting index. If the object is a {@link Double}, the interface
    {@link CoefficientExpansion1D} can be used instead to avoid autoboxing.

    @author G.K.Stephens
    @param <T> some arbitrary object that is represented in the expansion
    (common examples would include math objects like Vectors {@link VectorIJK})
    """

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

    def getExpansion(self):
        """gets ith expansion T<sub>i</sub> in &#8721; T<sub>i</sub>

        @param index the index i
        @return the ith expansion corresponding to the index T<sub>i</sub>
        """
        raise Exception
