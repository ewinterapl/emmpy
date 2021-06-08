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

    def toString(self):
        """Convert the object to a string."""
        return (
            "ArrayCoefficientExpansion1D [array=%s, getLowerBoundIndex()=%s, "
            "getUpperBoundIndex()=%s]" %
            (self.array, self.getLowerBoundIndex(), self.getUpperBoundIndex()))

    def hashCode(self):
        """Compute the object hash code."""
        prime = 31
        result = 1
        result = prime*result + 0  # *self.array
        result = prime*result + self.firstExpansionNumber
        return result

    def equals(self, obj):
        """Check for equality with another object."""
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.array != other.array:
            return False
        if self.firstExpansionNumber != other.firstExpansionNumber:
            return False
        return True
