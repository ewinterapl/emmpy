"""Utility functions for coefficient expansions."""


from math import floor

import numpy as np

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


class CoefficientExpansions:
    """Utility functions for coefficient expansions."""

    @staticmethod
    def createExpansionFromArray(*args):
        """Return a view of the array as a CoefficientExpansion1D."""
        if len(args) == 2:
            # param data the array that backs the CoefficientExpansion1D
            # param firstExpansionNumber the first index to be used in the
            # expansion
            # return a newly created CoefficientExpansion1D that is a view of
            # the input array
            (data, firstExpansionNumber) = args
            return ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        elif len(args) == 3:
            # param data the 2D array that backs the CoefficientExpansion2D
            # param firstIexpansionNumber the first index to be used in the
            # first dimension of the expansion
            # param firstJexpansionNumber the first index to be used in the
            # second dimensions of the expansion
            # return a newly created CoefficientExpansion2D that is a view of
            # the input array
            (data, firstIexpansionNumber, firstJexpansionNumber) = args
            return ArrayCoefficientExpansion2D(data, firstIexpansionNumber,
                                               firstJexpansionNumber)
        else:
            raise Exception

    @staticmethod
    def invert(p):
        """Return an inverted view of the supplied expansion coefficients.

        p[i] = 1/p[i]

        param p the set of coefficients p<sub>i</sub> to invert
        return the inverted set of coefficients p'<sub>i</sub>
        """
        data = [1/x for x in p]
        ace1d = ArrayCoefficientExpansion1D(data, p.firstExpansionNumber)
        return ace1d

    @staticmethod
    def negate(a):
        """Return a negated view of the expansion."""
        v = None
        if isinstance(a, ArrayCoefficientExpansion1D):
            data = [-x for x in a]
            ace1d = ArrayCoefficientExpansion1D(data, a.firstExpansionNumber)
            return ace1d
        elif isinstance(a, ArrayCoefficientExpansion2D):
            data = -a
            iLowerBoundIndex = a.iLowerBoundIndex
            jLowerBoundIndex = a.jLowerBoundIndex
            ace2d = ArrayCoefficientExpansion2D(
                data, iLowerBoundIndex, jLowerBoundIndex
            )
            return ace2d
        else:
            raise Exception

        # Return the view.
        return v

    @staticmethod
    def createUnity(*args):
        """Create an expansion of unit coefficients."""
        if len(args) == 2:
            (firstRadialExpansionNumber, lastRadialExpansionNumber) = args
            length = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            data = [1.0 for i in range(length)]
            ace1d = ArrayCoefficientExpansion1D(data, firstRadialExpansionNumber)
            return ace1d
        elif len(args) == 4:
            (firstAzimuthalExpansionNumber, lastAzimuthalExpansionNumber,
             firstRadialExpansionNumber, lastRadialExpansionNumber) = args
            n_az = (
                lastAzimuthalExpansionNumber - firstAzimuthalExpansionNumber + 1
            )
            n_r = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            data = [[1 for j in range(n_r)] for i in range(n_az)]
            ace2d = ArrayCoefficientExpansion2D(
                data, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
            )
            return ace2d
        else:
            raise Exception

    @staticmethod
    def scale(a, scaleFactor):
        """Create a scaled copy of the expansion.

        Create a scaled copy of the expansion.

        Parameters
        ----------
        a : CoefficientExpansion1D or CoefficientExpansion2D
            The expansion to copy and scale.
        scaleFactor : float
            Scale factor for scaled copy of expansion.
        """
        if isinstance(a, ArrayCoefficientExpansion1D):
            data = [scaleFactor*x for x in a]
            ace1d = ArrayCoefficientExpansion1D(data, a.firstExpansionNumber)
            return ace1d
        elif isinstance(a, ArrayCoefficientExpansion2D):
            data = scaleFactor*a
            iLowerBoundIndex = a.iLowerBoundIndex
            jLowerBoundIndex = a.jLowerBoundIndex
            ace2d = ArrayCoefficientExpansion2D(
                data, iLowerBoundIndex, jLowerBoundIndex
            )
            return ace2d
        else:
            raise Exception

    @staticmethod
    def createConstant(*args):
        """Create a constant expansion.

        @param firstRadialExpansionNumber
        @param lastRadialExpansionNumber
        @param constant
        @return
        """
        if len(args) == 3:
            (firstRadialExpansionNumber, lastRadialExpansionNumber,
             constant) = args
            length = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            data = [constant for i in range(length)]
            ace1d = ArrayCoefficientExpansion1D(data, firstRadialExpansionNumber)
            return ace1d
        elif len(args) == 5:
            (firstAzimuthalExpansionNumber, lastAzimuthalExpansionNumber,
             firstRadialExpansionNumber, lastRadialExpansionNumber,
             constant) = args
            n_az = lastAzimuthalExpansionNumber - firstAzimuthalExpansionNumber + 1
            n_r = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            data = [[constant for j in range(n_r)] for i in range(n_az)]
            ace2d = ArrayCoefficientExpansion2D(
                data, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
            )
            return ace2d
        else:
            raise Exception

        # Return the view.
        return v

    @staticmethod
    def add(a, b):
        """Add 2 expansions."""
        # Make sure the expansions are compatible.
        # Create a dummy expansion of the appropriate size.
        # Create a view object to wrap the expansion.
        # Replace the getCoefficient() method with a method that always returns
        # the sum, as a closure.
        if isinstance(a, ArrayCoefficientExpansion1D):
            data = [aa + bb for (aa, bb) in zip(a, b)]
            ace1d = ArrayCoefficientExpansion1D(data, a.firstExpansionNumber)
            return ace1d
        elif isinstance(a, ArrayCoefficientExpansion2D):
            firstAzimuthalExpansion = a.iLowerBoundIndex
            lastAzimuthalExpansion = a.iUpperBoundIndex
            firstRadialExpansion = a.jLowerBoundIndex
            lastRadialExpansion = a.jUpperBoundIndex
            n_az = lastAzimuthalExpansion - firstAzimuthalExpansion + 1
            n_r = lastRadialExpansion - firstRadialExpansion + 1
            data = a + b
            ace2d = ArrayCoefficientExpansion2D(
                data, firstAzimuthalExpansion, firstRadialExpansion
            )
            return ace2d
        else:
            raise Exception

    @staticmethod
    def concat(a, b):
        """Wrap 2 CoefficientExpansion1D by concatenating them.

        Assumes a.array and b.array are np.array.
        """
        data = np.hstack([a, b])
        lowerBoundIndex = a.firstExpansionNumber
        ace1d = ArrayCoefficientExpansion1D(data, lowerBoundIndex)
        return ace1d
