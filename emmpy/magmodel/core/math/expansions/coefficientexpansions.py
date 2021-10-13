"""Utility functions for coefficient expansions."""


from math import floor

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
from emmpy.utilities.nones import nones


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
        data = [1/x for x in p.array]
        ace1d = ArrayCoefficientExpansion1D(data, p.getLowerBoundIndex())
        return ace1d

    @staticmethod
    def negate(a):
        """Return a negated view of the expansion."""
        v = None
        if isinstance(a, CoefficientExpansion1D):
            data = [-x for x in a.array]
            ace1d = ArrayCoefficientExpansion1D(data, a.getLowerBoundIndex())
            return ace1d
        elif isinstance(a, CoefficientExpansion2D):
            v = CoefficientExpansion2D()
            v.getILowerBoundIndex = lambda: a.getILowerBoundIndex()
            v.getIUpperBoundIndex = lambda: a.getIUpperBoundIndex()
            v.getJLowerBoundIndex = lambda: a.getJLowerBoundIndex()
            v.getJUpperBoundIndex = lambda: a.getJUpperBoundIndex()
            v.iSize = lambda: a.iSize()
            v.jSize = lambda: a.jSize()
            v.getCoefficient = lambda iExpansion, kExpansion: (
                -a.getCoefficient(iExpansion, kExpansion)
            )
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
            # int firstAzimuthalExpansionNumber, lastAzimuthalExpansionNumber,
            # firstRadialExpansionNumber, lastRadialExpansionNumber
            ce2d = CoefficientExpansion2D()
            # These lambdas are not bound methods.
            ce2d.getILowerBoundIndex = lambda: firstAzimuthalExpansionNumber
            ce2d.getIUpperBoundIndex = lambda: lastAzimuthalExpansionNumber
            ce2d.getJLowerBoundIndex = lambda: firstRadialExpansionNumber
            ce2d.getJUpperBoundIndex = lambda: lastRadialExpansionNumber
            ce2d.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion: 1.0
            )
            return ce2d
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
            data = [scaleFactor*x for x in a.array]
            ace1d = ArrayCoefficientExpansion1D(data, a.getLowerBoundIndex())
            return ace1d
        elif isinstance(a, CoefficientExpansion2D):
            v = CoefficientExpansion2D()
            v.getILowerBoundIndex = lambda: a.getILowerBoundIndex()
            v.getIUpperBoundIndex = lambda: a.getIUpperBoundIndex()
            v.getJLowerBoundIndex = lambda: a.getJLowerBoundIndex()
            v.getJUpperBoundIndex = lambda: a.getJUpperBoundIndex()
            v.iSize = lambda: a.iSize()
            v.jSize = lambda: a.jSize()
            v.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion: (
                    scaleFactor*a.getCoefficient(azimuthalExpansion,
                                                 radialExpansion)
                )
            )
            return v
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

            # Create a dummy expansion of the appropriate size.
            nr = lastRadialExpansionNumber - firstRadialExpansionNumber + 1
            na = (
                lastAzimuthalExpansionNumber - firstAzimuthalExpansionNumber
                + 1
            )
            arr = nones((na, nr))
            p = ArrayCoefficientExpansion2D(
                arr, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
            )

            # Create a view object to wrap the expansion.
            v = CoefficientExpansion2D()
            v.getILowerBoundIndex = lambda: p.getILowerBoundIndex()
            v.getIUpperBoundIndex = lambda: p.getIUpperBoundIndex()
            v.getJLowerBoundIndex = lambda: p.getJLowerBoundIndex()
            v.getJUpperBoundIndex = lambda: p.getJUpperBoundIndex()
            v.iSize = lambda: p.iSize()
            v.jSize = lambda: p.jSize()

            # Replace the getCoefficient() method with a method that always
            # returns the constant, as a closure.
            v.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion: constant
            )
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
        if isinstance(a, CoefficientExpansion1D):
            data = [aa + bb for (aa, bb) in zip(a.array, b.array)]
            ace1d = ArrayCoefficientExpansion1D(data, a.getLowerBoundIndex())
            return ace1d
        elif isinstance(a, CoefficientExpansion2D):
            firstAzimuthalExpansion = a.getILowerBoundIndex()
            lastAzimuthalExpansion = a.getIUpperBoundIndex()
            firstRadialExpansion = a.getJLowerBoundIndex()
            lastRadialExpansion = a.getJUpperBoundIndex()
            ce2d = CoefficientExpansion2D()
            ce2d.getILowerBoundIndex = lambda: firstAzimuthalExpansion
            ce2d.getIUpperBoundIndex = lambda: lastAzimuthalExpansion
            ce2d.getJLowerBoundIndex = lambda: firstRadialExpansion
            ce2d.getJUpperBoundIndex = lambda: lastRadialExpansion
            ce2d.getCoefficient = (
                lambda azimuthalExpansion, radialExpansion:
                a.getCoefficient(azimuthalExpansion, radialExpansion) +
                b.getCoefficient(azimuthalExpansion, radialExpansion)
            )
            return ce2d
        else:
            raise Exception

    @staticmethod
    def concat(a, b):
        """Wrap 2 CoefficientExpansion1D by concatenating them.

        Assumes a.array and b.array are python lists of float.
        """
        data = a.array + b.array
        lowerBoundIndex = a.getLowerBoundIndex()
        ace1d = ArrayCoefficientExpansion1D(data, lowerBoundIndex)
        return ace1d
