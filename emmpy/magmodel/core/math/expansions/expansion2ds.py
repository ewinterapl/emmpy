"""emmpy.magmodel.core.math.expansions.expansion2ds"""


# from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
#     UnwritableVectorIJK
# )
# from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
# from emmpy.magmodel.core.math.expansions.arrayexpansion2d import (
#     ArrayExpansion2D
# )
# from emmpy.java.lang.unsupportedoperationexception import (
#     UnsupportedOperationException
# )
# from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
#     CoefficientExpansion2D
# )
from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D
# from emmpy.utilities.isrealnumber import isRealNumber


class Expansion2Ds:

    @staticmethod
    def createNull(firstAzimuthalExpansionNumber, firstRadialExpansionNumber,
                   lastRadialExpansionNumber):
        expansion2D = Expansion2D()
        expansion2D.getJLowerBoundIndex = lambda: firstRadialExpansionNumber
        expansion2D.getJUpperBoundIndex = lambda: lastRadialExpansionNumber
        expansion2D.getILowerBoundIndex = lambda: firstAzimuthalExpansionNumber
        expansion2D.getIUpperBoundIndex = firstAzimuthalExpansionNumber - 1
        def getExpansionWrapper(ignoredSelf):
            raise UnsupportedOperationException()
        expansion2D.getExpansion = getExpansionWrapper
        return expansion2D

    # @staticmethod
    # def createFromArray(
    #     data, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
    # ):
    #     return ArrayExpansion2D(
    #         data, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
    #     )

    # # N.B. NESTED CLASS UNUSED!
    # # @author stephgk1
    # class Vectors:

    #     @staticmethod
    #     def add(a, b):
    #         firstAzimuthalExpansion = a.getILowerBoundIndex()
    #         lastAzimuthalExpansion = a.getIUpperBoundIndex()
    #         firstRadialExpansion = a.getJLowerBoundIndex()
    #         lastRadialExpansion = a.getJUpperBoundIndex()
    #         array = [
    #             [UnwritableVectorIJK([0, 0, 0])
    #              for j in range(lastRadialExpansion - firstRadialExpansion +
    #                             1 + 1)]
    #             for i in range(
    #                 lastAzimuthalExpansion - firstAzimuthalExpansion + 1 + 1
    #             )
    #         ]
    #         expansion2D = Expansion2D()

    #         def getILowerBoundIndexWrapper(ignoredSelf):
    #             return firstAzimuthalExpansion
    #         expansion2D.getILowerBoundIndex = getILowerBoundIndexWrapper

    #         def getIUpperBoundIndexWrapper(ignoredSelf):
    #             return lastAzimuthalExpansion
    #         expansion2D.getIUpperBoundIndex = getIUpperBoundIndexWrapper

    #         def getJLowerBoundIndexWrapper(ignoredSelf):
    #             return firstRadialExpansion
    #         expansion2D.getJLowerBoundIndex = getJLowerBoundIndexWrapper

    #         def getJUpperBoundIndexWrapper(ignoredSelf):
    #             return lastRadialExpansion
    #         expansion2D.getJUpperBoundIndex = getJUpperBoundIndexWrapper

    #         def getExpansionWrapper(
    #             ignoredSelf, azimuthalExpansion, radialExpansion
    #         ):
    #             value = (
    #                 array[azimuthalExpansion - firstAzimuthalExpansion]
    #                      [radialExpansion - firstRadialExpansion]
    #             )
    #             if value is None:
    #                 value = VectorIJK.add(
    #                     a.getExpansion(azimuthalExpansion, radialExpansion),
    #                     b.getExpansion(azimuthalExpansion, radialExpansion)
    #                 )
    #                 array[azimuthalExpansion -
    #                       firstAzimuthalExpansion][radialExpansion -
    #                                                firstRadialExpansion] = (
    #                                                 value
    #                                                )
    #                 return value
    #             return value
    #         expansion2D.getExpansion = getExpansionWrapper
    #         return expansion2D

    # @staticmethod
    # def scale(*args):
    #     if isRealNumber(args[1]):
    #         (a, scaleFactor) = args
    #         expansion2D = Expansion2D()

    #         def getILowerBoundIndexWrapper(ignoredSelf):
    #             return a.getILowerBoundIndex()
    #         expansion2D.getILowerBoundIndex = getILowerBoundIndexWrapper

    #         def getIUpperBoundIndexWrapper(ignoredSelf):
    #             return a.getIUpperBoundIndex()
    #         expansion2D.getIUpperBoundIndex = getIUpperBoundIndexWrapper

    #         def getJLowerBoundIndexWrapper(ignoredSelf):
    #             return a.getJLowerBoundIndex()
    #         expansion2D.getJLowerBoundIndex = getJLowerBoundIndexWrapper

    #         def getJUpperBoundIndexWrapper(ignoredSelf):
    #             return a.getJUpperBoundIndex()
    #         expansion2D.getJUpperBoundIndex = getJUpperBoundIndexWrapper

    #         def getExpansionWrapper(
    #             ignoredSelf, azimuthalExpansion, radialExpansion
    #         ):
    #             return UnwritableVectorIJK(
    #                 scaleFactor,
    #                 a.getExpansion(azimuthalExpansion, radialExpansion)
    #             )
    #     elif isinstance(args[1], CoefficientExpansion2D):
    #         (a, scaleFactors) = args
    #         expansion2D = Expansion2D()

    #         def getILowerBoundIndexWrapper(ignoredSelf):
    #             return a.getILowerBoundIndex()
    #         expansion2D.getILowerBoundIndex = getILowerBoundIndexWrapper

    #         def getIUpperBoundIndexWrapper(ignoredSelf):
    #             return a.getIUpperBoundIndex()
    #         expansion2D.getIUpperBoundIndex = getIUpperBoundIndexWrapper

    #         def getJLowerBoundIndexWrapper(ignoredSelf):
    #             return a.getJLowerBoundIndex()
    #         expansion2D.getJLowerBoundIndex = getJLowerBoundIndexWrapper

    #         def getJUpperBoundIndexWrapper(ignoredSelf):
    #             return a.getJUpperBoundIndex()
    #         expansion2D.getJUpperBoundIndex = getJUpperBoundIndexWrapper

    #         def getExpansionWrapper(
    #             ignoredSelf, azimuthalExpansion, radialExpansion
    #         ):
    #             scaleFactor = scaleFactors.getCoefficient(
    #                 azimuthalExpansion, radialExpansion
    #             )
    #             return UnwritableVectorIJK(
    #                 scaleFactor,
    #                 a.getExpansion(azimuthalExpansion, radialExpansion)
    #             )

    #         return expansion2D

    # @staticmethod
    # def computeSum(a):
    #     bx = 0.0
    #     by = 0.0
    #     bz = 0.0
    #     for az in range(a.getILowerBoundIndex(), a.getIUpperBoundIndex + 1):
    #         for rad in range(
    #             a.getJLowerBoundIndex(), a.getJUpperBoundIndex() + 1
    #         ):
    #             vect = a.getExpansion(az, rad)
    #             bx += vect.getI()
    #             by += vect.getJ()
    #             bz += vect.getK()
    #     return UnwritableVectorIJK(bx, by, bz)
