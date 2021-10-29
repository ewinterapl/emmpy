"""Tail sheet coefficients for an equatorial expansion.

Tail sheet coefficients for an equatorial expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import emmpy.math.expansions.scalarexpansion1d as scalarexpansion1d
from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
import emmpy.math.expansions.arraycoefficientexpansion2d as arraycoefficientexpansion2d
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D, createNullExpansion
)
from emmpy.utilities.nones import nones


class TailSheetCoefficients:
    """Tail sheet coefficients for an equatorial expansion.

    This is a container class for the coefficients used for the
    ThinAsymmetricCurrentSheetBasisVectorField class.

    That is, this class holds the symmetric a_n^s, odd a_mn^o>, and even
    a_mn^e coefficients used in the expansion.

    Attributes
    ----------
    tailSheetSymmetricValues : CoefficientExpansion1D
        tailSheetSymmetricValues
    tailSheetOddValues : CoefficientExpansion2D
        tailSheetOddValues
    tailSheetEvenValues : CoefficientExpansion2D
        tailSheetEvenValues
    numAzimuthalExpansions : int
        Number of components in the azimuthal expansion.
    numRadialExpansionsm: int
        Number of components in the radial expansion.
    """

    def __init__(self, tailSheetSymmetricValues, tailSheetOddValues,
                 tailSheetEvenValues):
        """Initialize a new TailSheetCoefficients object.
        
        Initialize a new TailSheetCoefficients object.

        Parameters
        ----------
        tailSheetSymmetricValues : CoefficientExpansion1D
            tailSheetSymmetricValues
        tailSheetOddValues : CoefficientExpansion2D
            tailSheetOddValues
        tailSheetEvenValues : CoefficientExpansion2D
            tailSheetEvenValues
        """
        self.tailSheetSymmetricValues = tailSheetSymmetricValues
        self.tailSheetOddValues = tailSheetOddValues
        self.tailSheetEvenValues = tailSheetEvenValues
        self.numAzimuthalExpansions = tailSheetOddValues.iSize
        self.numRadialExpansions = tailSheetOddValues.jSize

    @staticmethod
    def createUnity(numAzimuthalExpansions, numRadialExpansions):
        """Create a coefficient set of all 1s.
        
        Create a coefficient set of all 1s.

        Parameters
        ----------
        numAzimuthalExpansions : int
            Number of azimuthal expansions.
        numRadialExpansions : int
            Number of radial expansions.
        
        Returns
        -------
        result : TailSheetCoefficients
            Expansion of unit value in all components.
        """
        return TailSheetCoefficients(
            scalarexpansion1d.createUnity(1, numRadialExpansions),
            arraycoefficientexpansion2d.createUnity(
                1, numAzimuthalExpansions, 1, numRadialExpansions
            ),
            arraycoefficientexpansion2d.createUnity(
                1, numAzimuthalExpansions, 1, numRadialExpansions)
        )

    @staticmethod
    def createFromArray(array, numAzimuthalExpansions, numRadialExpansions):
        """Create a TailSheetCoefficients from a float array.

        Create a TailSheetCoefficients from a float array.

        Parameters
        ----------
        array : 2-D array of float
            Values to use for expansion.
        numAzimuthalExpansions : int
            Number of azimuthal expansions
        numRadialExpansions : int
            Number of radial expansions.

        Returns
        -------
        result : TailSheetCoefficients
            Object with values copied from array.
        """
        sym = nones((numRadialExpansions,))
        odd = nones((numAzimuthalExpansions, numRadialExpansions))
        even = nones((numAzimuthalExpansions, numRadialExpansions))
        # n is the radial expansion number.
        count = 0
        for n in range(1, numRadialExpansions + 1):
            sym[n - 1] = array[count]
            count += 1

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(1, numRadialExpansions + 1):
            for m in range(1, numAzimuthalExpansions + 1):
                odd[m - 1][n - 1] = array[count]
                count += 1

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(1, numRadialExpansions + 1):
            for m in range(1, numAzimuthalExpansions + 1):
                even[m - 1][n - 1] = array[count]
                count += 1

        if numAzimuthalExpansions == 0:
            return TailSheetCoefficients(
                ScalarExpansion1D(sym, 1),
                createNullExpansion(
                    1, numAzimuthalExpansions,
                    1, numRadialExpansions),
                createNullExpansion(
                    1, numAzimuthalExpansions,
                    1, numRadialExpansions)
            )

        return TailSheetCoefficients(
            ScalarExpansion1D(sym, 1),
            ArrayCoefficientExpansion2D(odd, 1, 1),
            ArrayCoefficientExpansion2D(even, 1, 1))

    def getAsSingleExpansion(self):
        """Return the coefficients as a single 1D expansion.
        
        Return the coefficients as a single 1D expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : CoefficientExpansion1D
            Expansion with all coefficients collapsed to 1 dimension.
        """
        firstM = 1
        lastM = self.numAzimuthalExpansions
        firstN = 1
        lastN = self.numRadialExpansions
        coeffs = nones((self.getNumberOfExpansions(),))
        count = 0

        # The pressure independent terms.
        for n in range(firstN, lastN + 1):
            coeffs[count] = self.tailSheetSymmetricValues[n]
            count += 1

        for n in range(firstN, lastN + 1):
            for m in range(firstM, lastM + 1):
                coeffs[count] = self.tailSheetOddValues[m, n]
                count += 1

        for n in range(firstN, lastN + 1):
            for m in range(firstM, lastM + 1):
                coeffs[count] = self.tailSheetEvenValues[m, n]
                count += 1

        return ScalarExpansion1D(coeffs, 1)

    def getNumberOfExpansions(self):
        """Return the total number of expansions.

        Return the total number of expansions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Total number of expansions.
        """
        return (self.numRadialExpansions +
                2*(self.numAzimuthalExpansions*self.numRadialExpansions))
