"""emmpy.magmodel.core.math.expansions.expansion1ds"""


from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import (
    VectorIJK
)
from emmpy.magmodel.core.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D
from emmpy.magmodel.core.math.expansions.listexpansion1d import ListExpansion1D
from emmpy.utilities.isrealnumber import isRealNumber


class Expansion1Ds:

    @staticmethod
    def createFromList(aList, firstRadialExpansionNumber):
        return ListExpansion1D(aList, firstRadialExpansionNumber)

    @staticmethod
    def createFromArray(array, firstRadialExpansionNumber):
        return ArrayExpansion1D(array, firstRadialExpansionNumber)

    # N.B.: EMBEDDED CLASS!
    class Vectors:
        """@author stephgk1"""

        @staticmethod
        def createConstant(
            firstRadialExpansionNumber, lastRadialExpansionNumber,
            constant
        ):
            constantCopy = UnwritableVectorIJK.copyOf(constant)
            expansion1D = Expansion1D()

            def getUpperBoundIndexWrapper(*args2):
                return lastRadialExpansionNumber
            expansion1D.getUpperBoundIndex = getUpperBoundIndexWrapper

            def getLowerBoundIndexWrapper(*args2):
                return firstRadialExpansionNumber
            expansion1D.getLowerBoundIndex = getLowerBoundIndexWrapper

            def getExpansionWrapper(*args2):
                return constantCopy
            expansion1D.getExpansion = getExpansionWrapper

            return expansion1D

        @staticmethod
        def add(a, b):
            firstExpansion = a.getLowerBoundIndex()
            lastExpansion = a.getUpperBoundIndex()
            array = [
                UnwritableVectorIJK([0, 0, 0])
                for i in range(lastExpansion - firstExpansion + 1)
            ]
            expansion1D = Expansion1D()

            def getLowerBoundIndexWrapper(*args):
                return firstExpansion
            expansion1D.getLowerBoundIndex = getLowerBoundIndexWrapper

            def getUpperBoundIndexWrapper(*args):
                return lastExpansion
            expansion1D.getUpperBoundIndex = getUpperBoundIndexWrapper

            def getExpansionWrapper(*args):
                radialExpansion = args[1]
                value = array[radialExpansion - firstExpansion]
                if value is None:
                    value = VectorIJK.add(
                        a.getExpansion(radialExpansion),
                        b.getExpansion(radialExpansion)
                    )
                    array[radialExpansion - firstExpansion] = value
                    return value
                return value
            expansion1D.getExpansion = getExpansionWrapper
            return expansion1D

    @staticmethod
    def scale(*args):
        if isRealNumber(args[1]):
            (a, scaleFactor) = args
            expansion1D = Expansion1D()

            def getLowerBoundIndexWrapper(*args):
                return a.getLowerBoundIndex()
            expansion1D.getLowerBoundIndex = getLowerBoundIndexWrapper

            def getUpperBoundIndexWrapper(*args):
                return a.getUpperBoundIndex()
            expansion1D.getUpperBoundIndex = getUpperBoundIndexWrapper

            def getExpansionWrapper(*args2):
                radialExpansion = args2[1]
                return UnwritableVectorIJK(
                    scaleFactor, a.getExpansion(radialExpansion)
                )
            expansion1D.getExpansion = getExpansionWrapper

            return expansion1D
        elif isinstance(args[1], CoefficientExpansion1D):
            (a, scaleFactors) = args
            expansion1D = Expansion1D()

            def getLowerBoundIndexWrapper(*args):
                return a.getLowerBoundIndex()
            expansion1D.getLowerBoundIndex = getLowerBoundIndexWrapper

            def getUpperBoundIndexWrapper(*args):
                return a.getUpperBoundIndex()
            expansion1D.getUpperBoundIndex = getUpperBoundIndexWrapper

            def getExpansionWrapper(*args2):
                radialExpansion = args2[1]
                scaleFactor = scaleFactors.getCoefficient(radialExpansion)
                return UnwritableVectorIJK(
                    scaleFactor, a.getExpansion(radialExpansion)
                )
            expansion1D.getExpansion = getExpansionWrapper
            return expansion1D

    @staticmethod
    def computeSum(a):
        bx = 0.0
        by = 0.0
        bz = 0.0
        for rad in range(a.getLowerBoundIndex(), a.getUpperBoundIndex() + 1):
            vect = a.getExpansion(rad)
            bx += vect.getI()
            by += vect.getJ()
            bz += vect.getK()
        return UnwritableVectorIJK(bx, by, bz)
