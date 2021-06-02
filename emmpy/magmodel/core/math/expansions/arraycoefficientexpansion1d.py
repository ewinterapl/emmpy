"""emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.java.util.arrays import Arrays
from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)


class ArrayCoefficientExpansion1D(CoefficientExpansion1D):
    """author G.K.Stephens"""

    def __init__(self, array, firstExpansionNumber):
        self.array = array
        self.firstExpansionNumber = firstExpansionNumber

    def getLowerBoundIndex(self):
        return self.firstExpansionNumber

    def getUpperBoundIndex(self):
        lastExpansionNumber = self.firstExpansionNumber + len(self.array) - 1
        return lastExpansionNumber

    def getCoefficient(self, index):
        return self.array[index - self.firstExpansionNumber]

    def toString(self):
        return (
            "ArrayCoefficientExpansion1D [array=%s, getLowerBoundIndex()=%s, "
            "getUpperBoundIndex()=%s]" %
            (self.array, self.getLowerBoundIndex(), self.getUpperBoundIndex()))

    def hashCode(self):
        prime = 31
        result = 1
        result = prime*result + Arrays.hashCode(self.array)
        result = prime*result + self.firstExpansionNumber
        return result

    def equals(self, obj):
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
