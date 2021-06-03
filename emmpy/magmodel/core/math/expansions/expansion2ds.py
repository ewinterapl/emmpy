"""emmpy.magmodel.core.math.expansions.expansion2ds"""


from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablematrixijk import (
    UnwritableMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.expansions.arrayexpansion2d import (
    ArrayExpansion2D
)
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)
from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D
from emmpy.utilities.isrealnumber import isRealNumber


class Expansion2Ds:

    @staticmethod
    def createNull(firstAzimuthalExpansionNumber, firstRadialExpansionNumber,
                   lastRadialExpansionNumber):
        e2d = Expansion2D()
        e2d.getJLowerBoundIndex = lambda: firstRadialExpansionNumber
        e2d.getJUpperBoundIndex = lambda: lastRadialExpansionNumber
        e2d.getILowerBoundIndex = lambda: firstAzimuthalExpansionNumber
        e2d.getIUpperBoundIndex = firstAzimuthalExpansionNumber - 1

        def my_getExpansion():
            raise UnsupportedOperationException
        e2d.getExpansion = my_getExpansion
        return e2d

    @staticmethod
    def createFromArray(data, firstAzimuthalExpansionNumber,
                        firstRadialExpansionNumber):
        return ArrayExpansion2D(
            data, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
        )

    class Vectors:
        """author stephgk1"""

        @staticmethod
        def add(a, b):
            """add

            param Expansion2D<UnwritableVectorIJK> a
            param Expansion2D<UnwritableVectorIJK> b
            return Expansion2D<UnwritableVectorIJK>
            """
            # int firstAzimuthalExpansion, lastAzimuthalExpansion,
            # firstRadialExpansion, lastRadialExpansion
            firstAzimuthalExpansion = a.getILowerBoundIndex()
            lastAzimuthalExpansion = a.getIUpperBoundIndex()
            firstRadialExpansion = a.getJLowerBoundIndex()
            lastRadialExpansion = a.getJUpperBoundIndex()
            # [[UnwritableVectorIJK]] array
            array = []
            for i in range(lastAzimuthalExpansion - firstAzimuthalExpansion + 1):
                array.append([])
                for j in range(lastRadialExpansion -
                               firstRadialExpansion + 1):
                    array[i].append(None)
            e2d = Expansion2D()
            e2d.getILowerBoundIndex = lambda: firstAzimuthalExpansion
            e2d.getIUpperBoundIndex = lambda: lastAzimuthalExpansion
            e2d.getJLowerBoundIndex = lambda: firstRadialExpansion
            e2d.getJUpperBoundIndex = lambda: lastRadialExpansion

            def my_getExpansion(azimuthalExpansion, radialExpansion):
                value = (
                    array[azimuthalExpansion - firstAzimuthalExpansion]
                         [radialExpansion - firstRadialExpansion]
                )
                if value is None:
                    value = VectorIJK.add(
                        a.getExpansion(azimuthalExpansion, radialExpansion),
                        b.getExpansion(azimuthalExpansion, radialExpansion)
                    )
                    array[azimuthalExpansion - firstAzimuthalExpansion][radialExpansion - firstRadialExpansion] = value
                    return value
                return value
            e2d.getExpansion = my_getExpansion
            return e2d

        @staticmethod
        def scale(*args):
            if isRealNumber(args[1]):
                (a, scaleFactor) = args
                # param Expansion2D a
                # param float scaleFactor
                # return Expansion2D
                e2d = Expansion2D()
                e2d.getILowerBoundIndex = lambda: a.getILowerBoundIndex()
                e2d.getIUpperBoundIndex = lambda: a.getIUpperBoundIndex()
                e2d.getJLowerBoundIndex = lambda: a.getJLowerBoundIndex()
                e2d.getJUpperBoundIndex = lambda: a.getJUpperBoundIndex()
                e2d.getExpansion = (
                    lambda azimuthalExpansion, radialExpansion:
                    UnwritableVectorIJK(
                        scaleFactor,
                        a.getExpansion(azimuthalExpansion, radialExpansion)
                    )
                )
                return e2d
            elif isinstance(args[1], CoefficientExpansion2D):
                (a, scaleFactors) = args
                # Expansion2D a
                # CoefficientExpansion2D scaleFactors
                # return Expansion2D
                e2d = Expansion2D()
                e2d.getILowerBoundIndex = lambda: a.getILowerBoundIndex()
                e2d.getIUpperBoundIndex = lambda: a.getIUpperBoundIndex()
                e2d.getJLowerBoundIndex = lambda: a.getJLowerBoundIndex()
                e2d.getJUpperBoundIndex = lambda: a.getJUpperBoundIndex()

                def my_getExpansion(azimuthalExpansion, radialExpansion):
                    scaleFactor = scaleFactors.getCoefficient(
                        azimuthalExpansion, radialExpansion
                    )
                    return UnwritableVectorIJK(
                        scaleFactor,
                        a.getExpansion(azimuthalExpansion, radialExpansion)
                    )
                e2d = my_getExpansion
                return e2d
            else:
                raise Exception

        @staticmethod
        def computeSum(a):
            # float bx, by, bz
            bx = 0.0
            by = 0.0
            bz = 0.0
            for az in range(a.getILowerBoundIndex(), a.getIUpperBoundIndex + 1):
                for rad in range(
                    a.getJLowerBoundIndex(), a.getJUpperBoundIndex() + 1
                ):
                    vect = a.getExpansion(az, rad)
                    bx += vect.getI()
                    by += vect.getJ()
                    bz += vect.getK()
            return UnwritableVectorIJK(bx, by, bz)
