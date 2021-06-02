"""emmpy.magmodel.core.math.expansions.expansion1ds"""


# from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
#     CoefficientExpansion1D
# )
# from emmpy.utilities.isrealnumber import isRealNumber
from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import (
    VectorIJK
)
from emmpy.magmodel.core.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import CoefficientExpansion1D
from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D
from emmpy.magmodel.core.math.expansions.listexpansion1d import ListExpansion1D


class Expansion1Ds:

    @staticmethod
    def createFromList(aList, firstRadialExpansionNumber):
        """createFromList

        param list aList
        param int firstRadialExpansionNumber
        return Expansion1D
        """
        return ListExpansion1D(list, firstRadialExpansionNumber)

    @staticmethod
    def createFromArray(array, firstRadialExpansionNumber):
        """createFromArray

        param list array
        param int firstRadialExpansionNumber
        return Expansion1D
        """
        return ArrayExpansion1D(array, firstRadialExpansionNumber)

    class Vectors:
        """Vectors

        author stephgk1
        """

        @staticmethod
        def createConstant(firstRadialExpansionNumber, lastRadialExpansionNumber,
                        constant):
            """createConstant

            param int firstRadialExpansionNumber
            param int lastRadialExpansionNumber
            param UnwritableVectorIJK constant
            return Expansion1D<UnwritableVectorIJK>
            """

            # UnwritableVectorIJK constantCopy
            constantCopy = UnwritableVectorIJK.copyOf(constant)

            # Expansion1D e1d
            e1d = Expansion1D()
            e1d.getUpperBoundIndex = lambda: lastRadialExpansionNumber
            e1d.getLowerBoundIndex = lambda: firstRadialExpansionNumber
            e1d.getExpansion = lambda radialExpansion: constantCopy
            return e1d

        @staticmethod
        def add(a, b):
            """add

            param Expansion1D<UnwritableVectorIJK> a
            param Expansion1D<UnwritableVectorIJK> b
            return Expansion1D<UnwritableVectorIJK>
            """

            # int firstExpansion, lastExpansion
            firstExpansion = a.getLowerBoundIndex()
            lastExpansion = a.getUpperBoundIndex()

            # [UnwritableVectorIJK] array
            array = [None]*(lastExpansion - firstExpansion + 1)

            e1d = Expansion1D()
            e1d.getLowerBoundIndex = lambda: firstExpansion
            e1d.getUpperBoundIndex = lambda: lastExpansion

            # UnwritableVectorIJK getExpansion
            # int radialExpansion
            def my_getExpansion(radialExpansion):
                # UnwritableVectorIJK value
                value = array[radialExpansion - firstExpansion]
                if value is None:
                    value = VectorIJK.add(
                        a.getExpansion(radialExpansion),
                        b.getExpansion(radialExpansion)
                    )
                    array[radialExpansion - firstExpansion] = value
                    return value
                return value
            e1d.getExpansion = my_getExpansion

            return e1d

        @staticmethod
        def scale(*args):
            """scale"""
            if isinstance(args[1], float):
                (a, scaleFactor) = args
                # param Expansion1D<UnwritableVectorIJK> a
                # param float scaleFactor
                # return Expansion1D<UnwritableVectorIJK>
                # Expansion1D e1d
                e1d =  Expansion1D()
                e1d.getLowerBoundIndex = lambda: a.getLowerBoundIndex()
                e1d.getUpperBoundIndex = lambda: a.getUpperBoundIndex()
                e1d.getExpansion = (
                    lambda radialExpansion:
                    UnwritableVectorIJK(scaleFactor,
                                        a.getExpansion(radialExpansion))
                )
                return e1d
            elif isinstance(args[1], CoefficientExpansion1D):
                (a, scaleFactors) = args
                # param Expansion1D<UnwritableVectorIJK> a
                # param CoefficientExpansion1D scaleFactors
                # return Expansion1D<UnwritableVectorIJK>
                Preconditions.checkArgument(
                    a.getLowerBoundIndex() == scaleFactors.getLowerBoundIndex()
                )
                Preconditions.checkArgument(
                    a.getUpperBoundIndex() == scaleFactors.getUpperBoundIndex()
                )
                e1d =  Expansion1D()
                e1d.getLowerBoundIndex = lambda: a.getLowerBoundIndex()
                e1d.getUpperBoundIndex = lambda: a.getUpperBoundIndex()

                def my_getExpansion(radialExpansion):
                    # float scaleFactor
                    scaleFactor = scaleFactors.getCoefficient(radialExpansion)
                    return UnwritableVectorIJK(scaleFactor,
                                            a.getExpansion(radialExpansion))
                e1d.getExpansion = my_getExpansion
                return e1d
            else:
                raise Exception

        @staticmethod
        def computeSum(a):
            """computeSum

            param Expansion1D<UnwritableVectorIJK> a
            return UnwritableVectorIJK
            """

            # float bx, by, bz
            bx = 0.0
            by = 0.0
            bz = 0.0
            for rad in range(a.getLowerBoundIndex(), a.getUpperBoundIndex() + 1):
                # UnwritableVectorIJK vect
                vect = a.getExpansion(rad)
                bx += vect.getI()
                by += vect.getJ()
                bz += vect.getK()
            return UnwritableVectorIJK(bx, by, bz)
