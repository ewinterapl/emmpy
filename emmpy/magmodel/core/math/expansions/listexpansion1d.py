"""emmpy.magmodel.core.math.expansions.listexpansion1d"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D


class ListExpansion1D(Expansion1D):
    """ListExpansion1D"""

    def __init__(self, aList, firstRadialExpansionNumber):
        """Constructor"""
        self.list = Preconditions.checkNotNull(aList)
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(aList) - 1)

    def getLowerBoundIndex(self):
        return self.firstRadialExpansionNumber

    def getUpperBoundIndex(self):
        return self.lastRadialExpansionNumber

    def getExpansion(self, radialExpansion):
        return self.list[radialExpansion - self.firstRadialExpansionNumber]
