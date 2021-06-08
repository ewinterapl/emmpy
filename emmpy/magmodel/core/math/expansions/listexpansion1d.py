"""An expansion using a 1-D list."""


from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D


class ListExpansion1D(Expansion1D):
    """An expansion using a 1-D list."""

    def __init__(self, aList, firstRadialExpansionNumber):
        """Build a new object."""
        self.list = aList
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(aList) - 1)

    def getLowerBoundIndex(self):
        """Return the lowest index."""
        return self.firstRadialExpansionNumber

    def getUpperBoundIndex(self):
        """Return the highest index."""
        return self.lastRadialExpansionNumber

    def getExpansion(self, radialExpansion):
        """Return the specified expansion value."""
        return self.list[radialExpansion - self.firstRadialExpansionNumber]
