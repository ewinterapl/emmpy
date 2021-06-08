"""A 1-D arrsy for a coefficient expansion."""


from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)


class ArrayCoefficientExpansion1D(CoefficientExpansion1D):
    """A 1-D arrsy for a coefficient expansion.

    author G.K.Stephens
    """

    def __init__(self, array, firstExpansionNumber):
        """Build a new object."""
        self.array = array
        self.firstExpansionNumber = firstExpansionNumber

    def getLowerBoundIndex(self):
        """Return the lower index bound for the expansion."""
        return self.firstExpansionNumber

    def getUpperBoundIndex(self):
        """Return the upper index bound for the expansion."""
        lastExpansionNumber = self.firstExpansionNumber + len(self.array) - 1
        return lastExpansionNumber

    def getCoefficient(self, index):
        """Return a coeeficient at the index."""
        return self.array[index - self.firstExpansionNumber]
