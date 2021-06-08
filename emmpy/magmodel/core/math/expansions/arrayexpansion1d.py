"""A 1-D array of expansion values."""


from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D


class ArrayExpansion1D(Expansion1D):
    """A 1-D array of expansion values."""

    def __init__(self, array, firstRadialExpansionNumber):
        """Build a new object."""
        self.array = array
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(array) - 1
        )

    def getLowerBoundIndex(self):
        """Return the lowest index."""
        return self.firstRadialExpansionNumber

    def getUpperBoundIndex(self):
        """Returnn the highest index."""
        return self.lastRadialExpansionNumber

    def getExpansion(self, radialExpansion):
        """Return the specified expansion."""
        return self.array[radialExpansion - self.firstRadialExpansionNumber]

    def toString(self):
        """Convert the object to a string."""
        return (
            "ArraySymmetricScalarCylindricalExpansion [array=%s"
            ", firstRadialExpansionNumber=%s, lastRadialExpansionNumber=%s]" %
            (self.array, self.firstRadialExpansionNumber,
             self.lastRadialExpansionNumber)
        )

    def hashCode(self):
        """Compute the object hash code."""
        prime = 31
        result = 1
        result = prime*result + 0  # *self.array
        result = prime*result + self.firstRadialExpansionNumber
        result = prime*result + self.lastRadialExpansionNumber
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
        if self.firstRadialExpansionNumber != other.firstRadialExpansionNumber:
            return False
        if self.lastRadialExpansionNumber != other.lastRadialExpansionNumber:
            return False
        return True
