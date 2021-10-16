"""Utility functions for coefficient expansions."""


from math import floor

import numpy as np

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.math.expansions.arraycoefficientexpansion2d import (
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
            raise Exception
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
            raise Exception
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
            raise Exception("Use arraycoefficientexpansion1d.add()!")
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
