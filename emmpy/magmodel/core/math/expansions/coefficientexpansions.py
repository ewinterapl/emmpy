"""emmpy.magmodel.core.math.expansions.coefficientexpansions"""


from math import floor

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)


class CoefficientExpansion1DView:

    def __init__(self, e):
        self.e = e

    def getLowerBoundIndex(self):
        return self.e.getLowerBoundIndex()

    def getUpperBoundIndex(self):
        return self.e.getUpperBoundIndex()

    def getCoefficient(self, index):
        return self.e.getCoefficient(index)


class CoefficientExpansion2DView:

    def __init__(self, e):
        self.e = e

    def getILowerBoundIndex(self):
        return self.e.getILowerBoundIndex()

    def getIUpperBoundIndex(self):
        return self.e.getIUpperBoundIndex()

    def getJLowerBoundIndex(self):
        return self.e.getJLowerBoundIndex()

    def getJUpperBoundIndex(self):
        return self.e.getJUpperBoundIndex()

    def iSize(self):
        return self.e.iSize()

    def jSize(self):
        return self.e.jSize()

    def getCoefficient(self, iIndex, jIndex):
        return self.e.getCoefficient(iIndex, jIndex)


class CoefficientExpansions:

    @staticmethod
    def createExpansionFromArray(*args):
        """Wraps an array and returns a view of the array as a
        {@link CoefficientExpansion1D}."""
        if len(args) == 2:
            # @param data the array that backs the
            # {@link CoefficientExpansion1D}
            # @param firstExpansionNumber the first index to be used in the
            # expansion
            # @return a newly created {@link CoefficientExpansion1D} that is a
            # view of the input array
            (data, firstExpansionNumber) = args
            return ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        elif len(args) == 3:
            # @param data the 2D array that backs the
            # {@link CoefficientExpansion2D}
            # @param firstIexpansionNumber the first index to be used in the
            # first dimension of the expansion
            # @param firstJexpansionNumber the first index to be used in the
            # second dimensions of the expansion
            # @return a newly created {@link CoefficientExpansion2D} that is a
            # view of the input array
            (data, firstIexpansionNumber, firstJexpansionNumber) = args
            return ArrayCoefficientExpansion2D(data, firstIexpansionNumber,
                                               firstJexpansionNumber)

    @staticmethod
    def invert(p):
        """Returns an inverted view of the supplied expansion coefficients.

        p[i] = 1/p[i]
        @param p the set of coefficients p<sub>i</sub> to invert
        @return the inverted set of coefficients p'<sub>i</sub>
        """

        # Create a view object to wrap the expansion.
        v = CoefficientExpansion1DView(p)

        # Replace the getCoefficient() method with a method that inverts the
        # coefficient, as a closure.
        v.getCoefficient = lambda index: 1/p.getCoefficient(index)

        # Return the view.
        return v

    @staticmethod
    def negate(a):

        # Create the appropriate view object to wrap the expansion.
        # Then replace the getCoefficient() method with a method that negates
        # the coefficient, as a closure.
        if isinstance(a, CoefficientExpansion1D):
            v = CoefficientExpansion1DView(a)
            v.getCoefficient = lambda index: -a.getCoefficient(index)
        elif isinstance(a, CoefficientExpansion2D):
            v = CoefficientExpansion2DView(a)
            v.getCoefficient = lambda iExpansion, kExpansion: (
                -a.getCoefficient(iExpansion, kExpansion)
            )

        # Return the view.
        return v

    @staticmethod
    def createUnity(*args):
        """createUnity()

        @param firstRadialExpansionNumber
        @param lastRadialExpansionNumber
        @return
        """
        if len(args) == 2:
            (firstRadialExpansionNumber, lastRadialExpansionNumber) = args

            # Create a dummy expansion of the appropriate size.
            n = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            p = ArrayCoefficientExpansion1D(
                [None]*n, firstRadialExpansionNumber
            )

            # Create a view object to wrap the expansion.
            v = CoefficientExpansion1DView(p)

            # Replace the getCoefficient() method with a method that always
            # returns unity, as a closure.
            v.getCoefficient = lambda index: 1

        elif len(args) == 4:
            (firstAzimuthalExpansionNumber, lastAzimuthalExpansionNumber,
             firstRadialExpansionNumber, lastRadialExpansionNumber) = args

            # Create a dummy expansion of the appropriate size.
            nr = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            na = (
                lastAzimuthalExpansionNumber - firstAzimuthalExpansionNumber
                + 1
            )
            arr = []
            for i in range(na):
                arr.append([None]*nr)
            p = ArrayCoefficientExpansion2D(
                arr, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
            )

            # Create a view object to wrap the expansion.
            v = CoefficientExpansion2DView(p)

            # Replace the getCoefficient() method with a method that always
            # returns the constant, as a closure.
            v.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion: 1
            )

        # Return the view.
        return v

    @staticmethod
    def scale(a, scaleFactor):
        """scale

        @param a
        @param scaleFactor
        @return
        """
        # Create a view object to wrap the expansion.
        # Replace the getCoefficient() method with a method that always returns
        # the scaled value, as a closure.
        if isinstance(a, CoefficientExpansion1D):
            v = CoefficientExpansion1DView(a)
            v.getCoefficient = (
                lambda radialExpansion: (
                    scaleFactor*a.getCoefficient(radialExpansion)
                )
            )
        elif isinstance(a, CoefficientExpansion2D):
            v = CoefficientExpansion2DView(a)
            v.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion: (
                    scaleFactor*a.getCoefficient(azimuthalExpansion,
                                                 radialExpansion)
                )
            )

        # Return the view.
        return v

    @staticmethod
    def createConstant(*args):
        """createConstant

        @param firstRadialExpansionNumber
        @param lastRadialExpansionNumber
        @param constant
        @return
        """
        if len(args) == 3:
            (firstRadialExpansionNumber, lastRadialExpansionNumber,
             constant) = args

            # Create a dummy expansion of the appropriate size.
            n = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            p = ArrayCoefficientExpansion1D(
                [None]*n, firstRadialExpansionNumber
            )

            # Create a view object to wrap the expansion.
            v = CoefficientExpansion1DView(p)

            # Replace the getCoefficient() method with a method that always
            # returns the constant, as a closure.
            v.getCoefficient = lambda index: constant

        elif len(args) == 5:
            (firstAzimuthalExpansionNumber, lastAzimuthalExpansionNumber,
             firstRadialExpansionNumber, lastRadialExpansionNumber,
             constant) = args

            # Create a dummy expansion of the appropriate size.
            nr = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            na = (
                lastAzimuthalExpansionNumber - firstAzimuthalExpansionNumber
                + 1
            )
            arr = []
            for i in range(na):
                arr.append([None]*nr)
            p = ArrayCoefficientExpansion2D(
                arr, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
            )

            # Create a view object to wrap the expansion.
            v = CoefficientExpansion2DView(p)

            # Replace the getCoefficient() method with a method that always
            # returns the constant, as a closure.
            v.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion: constant
            )

        # Return the view.
        return v

    @staticmethod
    def add(a, b):
        """add

        @param a
        @param b
        @return
        """

        # Make sure the expansions are compatible.
        # Create a dummy expansion of the appropriate size.
        # Create a view object to wrap the expansion.
        # Replace the getCoefficient() method with a method that always returns
        # the sum, as a closure.
        if isinstance(a, CoefficientExpansion1D):
            Preconditions.checkArgument(a.getLowerBoundIndex() ==
                                        b.getLowerBoundIndex())
            Preconditions.checkArgument(a.getUpperBoundIndex() ==
                                        b.getUpperBoundIndex())
            firstExpansion = a.getLowerBoundIndex()
            lastExpansion = a.getUpperBoundIndex()
            n = lastExpansion - firstExpansion + 1
            p = ArrayCoefficientExpansion1D([None]*n, firstExpansion)
            v = CoefficientExpansion1DView(p)
            v.getCoefficient = (
                lambda radialExpansion:
                a.getCoefficient(radialExpansion) +
                b.getCoefficient(radialExpansion)
            )
        elif isinstance(a, CoefficientExpansion2D):
            Preconditions.checkArgument(a.getILowerBoundIndex() ==
                                        b.getILowerBoundIndex())
            Preconditions.checkArgument(a.getIUpperBoundIndex() ==
                                        b.getIUpperBoundIndex())
            Preconditions.checkArgument(a.getJLowerBoundIndex() ==
                                        b.getJLowerBoundIndex())
            Preconditions.checkArgument(a.getJUpperBoundIndex() ==
                                        b.getJUpperBoundIndex())
            firstAzimuthalExpansion = a.getILowerBoundIndex()
            lastAzimuthalExpansion = a.getIUpperBoundIndex()
            firstRadialExpansion = a.getJLowerBoundIndex()
            lastRadialExpansion = a.getJUpperBoundIndex()
            na = lastAzimuthalExpansion - firstAzimuthalExpansion + 1
            nr = lastRadialExpansion - firstRadialExpansion + 1
            arr = []
            for i in range(na):
                arr.append([None]*nr)
            p = ArrayCoefficientExpansion2D(
                arr, firstAzimuthalExpansion, firstRadialExpansion
            )
            v = CoefficientExpansion2DView(p)
            v.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion:
                a.getCoefficient(azimuthalExpansion, radialExpansion) +
                b.getCoefficient(azimuthalExpansion, radialExpansion)
            )

        # Return the view.
        return v

    @staticmethod
    def createNullExpansion(
        firstAzimuthalExpansionNumber, firstRadialExpansionNumber,
        lastRadialExpansionNumber):
        """createNullExpansion

        NOTE: THE JAVA SOURCE FOR THIS METHOD IS INCORRECT, BUT REPRODUCED
        IN PYTHON BELOW.

        @param data
        @param firstAzimuthalExpansionNumber
        @param firstRadialExpansionNumber
        @return
        """

        # Create a dummy expansion of the appropriate size.
        nr = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
        na = abs(firstAzimuthalExpansionNumber)
        arr = []
        for i in range(na):
            arr.append([None]*nr)
        p = ArrayCoefficientExpansion2D(
            arr, firstAzimuthalExpansionNumber,
            firstRadialExpansionNumber
        )

        # Create a view object to wrap the expansion.
        v = CoefficientExpansion2DView(p)

        # Replace the getIUpperBoundIndex method.
        v.getIUpperBoundIndex = lambda: p.firstAzimuthalExpansionNumber - 1

        # Replace the getCoefficient method.
        # NOTE: This funky syntax was needed in order to get a raise to work
        # inside a lambda.
        v.getCoefficient = (
            lambda iIndex, jIndex:
            (_ for _ in ()).throw(UnsupportedOperationException())
        )

        # Return the wrapper object.
        return v

    @staticmethod
    def convertTo1D(data, lowerBoundIndex):
        """Converts the supplied 2D coefficient expansion by converting it to a
        1D coefficient expansion.

        The fast index is the second index.

        @param data
        @param lowerBoundIndex
        @return
        """

        # Create a 1-D wrapper for the 2-D expansion.
        v = CoefficientExpansion1DView(data)

        # Replace the getLowerBoundIndex and getUpperBoundIndex bound methods.
        v.getLowerBoundIndex = lambda: lowerBoundIndex
        v.getUpperBoundIndex = lambda: (
            lowerBoundIndex + data.iSize() * data.jSize() - 1
        )

        # Replace the getCoefficient method.
        # NOTE: JAVA DOES C-STYLE INTEGER DIVISION! Hence the floor().
        v.getCoefficient = lambda index: (
            data.getCoefficient(
                data.getILowerBoundIndex() +
                floor((index - lowerBoundIndex)/data.jSize()),
                data.getJLowerBoundIndex() +
                (index - lowerBoundIndex) % data.jSize()
            )
        )

        # Return the wrapper.
        return v

    @staticmethod
    def convertTo2D(
        data, iLowerBoundIndex, iUpperBoundIndex, jLowerBoundIndex,
        jUpperBoundIndex):
        """Converts the supplied 1D coefficient expansion by converting it to a
        2D coefficient expansion.

        The fast index is the second index.

        This is not view friendly, as the size of the returned
        {@link CoefficientExpansion2D} is determined at construction time
        (although the values are view friendly).

        @param data
        @param iLowerBoundIndex
        @param jLowerBoundIndex
        @return
        """

        # Create a 2-D wrapper for the 1-D expansion.
        v = CoefficientExpansion2DView(data)

        # Replace the bounds methods.
        v.getILowerBoundIndex = lambda: iLowerBoundIndex
        v.getIUpperBoundIndex = lambda: iUpperBoundIndex
        v.getJLowerBoundIndex = lambda: jLowerBoundIndex
        v.getJUpperBoundIndex = lambda: jUpperBoundIndex

        # Replace the getCoefficient() method.
        v.getCoefficient = lambda iIndex, jIndex: (
            data.getCoefficient(
                (iIndex - iLowerBoundIndex) *
                (jUpperBoundIndex - jLowerBoundIndex + 1) +
                jIndex - jLowerBoundIndex + data.getLowerBoundIndex())
        )

        # Return the wrapper.
        return v

    @staticmethod
    def concat(a, b):
        """Wraps two {@link CoefficientExpansion1D}s by concatenating them
        together.

        @param a
        @param b
        @return
        """

        # Create the wrapper object.
        v = CoefficientExpansion1DView(a)  # This is a dummy argument.

        # Replace the bounds methods.
        v.getLowerBoundIndex = lambda: a.getLowerBoundIndex()
        v.getUpperBoundIndex = lambda: (
            a.getLowerBoundIndex() + a.size() + b.size() - 1
        )

        # Replace the getCoefficient() method.
        v.getCoefficient = lambda index: (
            b.getCoefficient(index - a.getUpperBoundIndex() +
                             b.getLowerBoundIndex() - 1)
            if index > a.getUpperBoundIndex()
            else a.getCoefficient(index)
        )

        # Return the wrapper.
        return v
