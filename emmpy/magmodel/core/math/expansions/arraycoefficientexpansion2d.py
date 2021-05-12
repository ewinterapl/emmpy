"""emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d"""


# from emmpy.com.google.common.base.preconditions import Preconditions
# from emmpy.java.util.arrays import Arrays
from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)
# from emmpy.utilities.isragged import isRagged


class ArrayCoefficientExpansion2D(CoefficientExpansion2D):
    pass

    # def __init__(self,  data, iLowerBoundIndex, jLowerBoundIndex):
    #     """Converts a 2D double array into a {@link CoefficientExpansion2D} by
    #     wrapping the array. Note, this is a view friendly implementation, so
    #     the returned {@link CoefficientExpansion2D} will change as the array
    #     changes.

    #     Note, the supplied array must be rectangular (not ragged). This check
    #     is performed on construction but not on subsequent retrievals. This
    #     makes this a potentially unsafe implementation, if the supplied array
    #     becomes ragged after construction.

    #     @author G.K.Stephens
    #     """
    #     self.data = Preconditions.checkNotNull(data)
    #     Preconditions.checkArgument(not isRagged(data))
    #     self.iLowerBoundIndex = iLowerBoundIndex
    #     self.jLowerBoundIndex = jLowerBoundIndex

    # def getILowerBoundIndex(self):
    #     return self.iLowerBoundIndex

    # def getIUpperBoundIndex(self):
    #     iUpperBoundIndex = self.iLowerBoundIndex + len(self.data) - 1
    #     return iUpperBoundIndex

    # def getJLowerBoundIndex(self):
    #     return self.jLowerBoundIndex

    # def getJUpperBoundIndex(self):
    #     jUpperBoundIndex = self.jLowerBoundIndex + len(self.data[0]) - 1
    #     return jUpperBoundIndex

    # def getCoefficient(self, azimuthalExpansion, radialExpansion):
    #     return (
    #         self.data[azimuthalExpansion - self.iLowerBoundIndex]
    #                  [radialExpansion - self.jLowerBoundIndex]
    #     )

    # def toString(self):
    #     return (
    #         "ArrayCoefficientExpansion2D [data=%s, getILowerBoundIndex()=%s, "
    #         "getIUpperBoundIndex()=%s, getJLowerBoundIndex()=%s, "
    #         "getJUpperBoundIndex()=%s]" %
    #         (self.data, self.getILowerBoundIndex(), self.getIUpperBoundIndex(),
    #          self.getJLowerBoundIndex(), self.getJUpperBoundIndex())
    #     )

    # def hashCode(self):
    #     prime = 31
    #     result = 1
    #     result = prime*result + Arrays.deepHashCode(self.data)
    #     result = prime*result + self.iLowerBoundIndex
    #     result = prime*result + self.jLowerBoundIndex
    #     return result

    # def equals(self, obj):
    #     if self is obj:
    #         return True
    #     if obj is None:
    #         return False
    #     if self.__class__ != obj.__class__:
    #         return False
    #     other = obj
    #     if not self.data == other.data:
    #         return False
    #     if self.iLowerBoundIndex != other.iLowerBoundIndex:
    #         return False
    #     if self.jLowerBoundIndex != other.jLowerBoundIndex:
    #         return False
    #     return True
