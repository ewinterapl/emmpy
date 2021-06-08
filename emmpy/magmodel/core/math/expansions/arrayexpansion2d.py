"""A 2-D array of expansion values."""


# from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D
# from emmpy.utilities.isragged import isRagged


class ArrayExpansion2D(Expansion2D):
    """A 2-D array of expansion values."""

    def __init__(self, data, firstAzimuthalExpansionNumber,
                 firstRadialExpansionNumber):
        """Build a new object."""
        self.data = data
        self.firstAzimuthalExpansionNumber = firstAzimuthalExpansionNumber
        self.lastAzimuthalExpansionNumber = (
            firstAzimuthalExpansionNumber + len(data) - 1
        )
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(data[0]) - 1
        )

    def getJLowerBoundIndex(self):
        """Return the lowest second index."""
        return self.firstRadialExpansionNumber

    def getJUpperBoundIndex(self):
        """Return the highest second index."""
        return self.lastRadialExpansionNumber

    def getILowerBoundIndex(self):
        """Return the lowest first index."""
        return self.firstAzimuthalExpansionNumber

    def getIUpperBoundIndex(self):
        """Return the highest first index."""
        return self.lastAzimuthalExpansionNumber

    def getExpansion(self, azimuthalExpansion, radialExpansion):
        """Return the specified expansion component."""
        return (
            self.data[azimuthalExpansion - self.firstAzimuthalExpansionNumber]
            [radialExpansion - self.firstRadialExpansionNumber]
        )
