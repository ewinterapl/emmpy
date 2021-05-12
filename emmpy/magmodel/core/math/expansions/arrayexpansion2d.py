"""emmpy.magmodel.core.math.expansions.arrayexpansion2d"""


# from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D
# from emmpy.utilities.isragged import isRagged


class ArrayExpansion2D(Expansion2D):
    pass

    def __init__(self, data, firstAzimuthalExpansionNumber,
                 firstRadialExpansionNumber):
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
        return self.firstRadialExpansionNumber

    def getJUpperBoundIndex(self):
        return self.lastRadialExpansionNumber

    def getILowerBoundIndex(self):
        return self.firstAzimuthalExpansionNumber

    def getIUpperBoundIndex(self):
        return self.lastAzimuthalExpansionNumber

    def getExpansion(self, azimuthalExpansion, radialExpansion):
        return (
            self.data[azimuthalExpansion - self.firstAzimuthalExpansionNumber]
            [radialExpansion - self.firstRadialExpansionNumber]
        )
