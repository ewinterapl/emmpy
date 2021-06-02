"""emmpy.magmodel.core.math.expansions.arrayexpansion1d"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.java.util.arrays import Arrays
from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D


class ArrayExpansion1D(Expansion1D):

    def __init__(self, array, firstRadialExpansionNumber):
        self.array = array
        self.firstRadialExpansionNumber = firstRadialExpansionNumber
        self.lastRadialExpansionNumber = (
            firstRadialExpansionNumber + len(array) - 1
        )

    def getLowerBoundIndex(self):
        return self.firstRadialExpansionNumber

    def getUpperBoundIndex(self):
        return self.lastRadialExpansionNumber

    def getExpansion(self, radialExpansion):
        return self.array[radialExpansion - self.firstRadialExpansionNumber]

    def toString(self):
        return (
            "ArraySymmetricScalarCylindricalExpansion [array=%s"
            ", firstRadialExpansionNumber=%s, lastRadialExpansionNumber=%s]" %
            (self.array, self.firstRadialExpansionNumber,
             self.lastRadialExpansionNumber)
        )

    def hashCode(self):
        prime = 31
        result = 1
        result = prime*result + Arrays.hashCode(self.array)
        result = prime*result + self.firstRadialExpansionNumber
        result = prime*result + self.lastRadialExpansionNumber
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
        if self.firstRadialExpansionNumber != other.firstRadialExpansionNumber:
            return False
        if self.lastRadialExpansionNumber != other.lastRadialExpansionNumber:
            return False
        return True
