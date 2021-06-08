"""A 2-D array of expansion coefficients."""


from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)


class ArrayCoefficientExpansion2D(CoefficientExpansion2D):
    """A 2-D array of expansion coefficients."""

    def __init__(self,  data, iLowerBoundIndex, jLowerBoundIndex):
        """Build a new object.

        Converts a 2D double array into a CoefficientExpansion2D by
        wrapping the array. Note, this is a view friendly implementation, so
        the returned CoefficientExpansion2D will change as the array changes.

        Note, the supplied array must be rectangular (not ragged). This check
        is performed on construction but not on subsequent retrievals. This
        makes this a potentially unsafe implementation, if the supplied array
        becomes ragged after construction.

        author G.K.Stephens
        """
        self.data = data
        self.iLowerBoundIndex = iLowerBoundIndex
        self.jLowerBoundIndex = jLowerBoundIndex

    def getILowerBoundIndex(self):
        """Return the lowest index in the first dimension."""
        return self.iLowerBoundIndex

    def getIUpperBoundIndex(self):
        """Return the highest index in the first dimension."""
        iUpperBoundIndex = self.iLowerBoundIndex + len(self.data) - 1
        return iUpperBoundIndex

    def getJLowerBoundIndex(self):
        """Return the lowest index in the second dimension."""
        return self.jLowerBoundIndex

    def getJUpperBoundIndex(self):
        """Return the highest index in the second dimension."""
        jUpperBoundIndex = self.jLowerBoundIndex + len(self.data[0]) - 1
        return jUpperBoundIndex

    def getCoefficient(self, azimuthalExpansion, radialExpansion):
        """Return the specified coefficient."""
        return (
            self.data[azimuthalExpansion - self.iLowerBoundIndex]
                     [radialExpansion - self.jLowerBoundIndex]
        )

    def toString(self):
        """Convert the object to a string."""
        return (
            "ArrayCoefficientExpansion2D [data=%s, getILowerBoundIndex()=%s, "
            "getIUpperBoundIndex()=%s, getJLowerBoundIndex()=%s, "
            "getJUpperBoundIndex()=%s]" %
            (self.data, self.getILowerBoundIndex(), self.getIUpperBoundIndex(),
             self.getJLowerBoundIndex(), self.getJUpperBoundIndex())
        )

    def hashCode(self):
        """Compute the object hash code."""
        prime = 31
        result = 1
        result = prime*result + 0  # * self.data
        result = prime*result + self.iLowerBoundIndex
        result = prime*result + self.jLowerBoundIndex
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
        if not self.data == other.data:
            return False
        if self.iLowerBoundIndex != other.iLowerBoundIndex:
            return False
        if self.jLowerBoundIndex != other.jLowerBoundIndex:
            return False
        return True
