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
