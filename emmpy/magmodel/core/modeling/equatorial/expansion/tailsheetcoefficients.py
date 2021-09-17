"""Tail sheet coefficients for an equatorial expansion.

Tail sheet coefficients for an equatorial expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
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
        self.numAzimuthalExpansions = tailSheetOddValues.iSize()
        self.numRadialExpansions = tailSheetOddValues.jSize()

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
            CoefficientExpansions.createUnity(1, numRadialExpansions),
            CoefficientExpansions.createUnity(1, numAzimuthalExpansions, 1,
                                              numRadialExpansions),
            CoefficientExpansions.createUnity(1, numAzimuthalExpansions, 1,
                                              numRadialExpansions)
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
                CoefficientExpansions.createExpansionFromArray(sym, 1),
                CoefficientExpansions.createNullExpansion(
                    1, 1, numRadialExpansions),
                CoefficientExpansions.createNullExpansion(
                    1, 1, numRadialExpansions)
            )

        return TailSheetCoefficients(
            CoefficientExpansions.createExpansionFromArray(sym, 1),
            CoefficientExpansions.createExpansionFromArray(odd, 1, 1),
            CoefficientExpansions.createExpansionFromArray(even, 1, 1))

    def getTailSheetSymmetricValues(self):
        """Return the symmetric coefficients a_n^s.
        
        Return the symmetric coefficients a_n^s.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        result : CoefficientExpansion1D
            Symmetric coefficients a_n^s.
        """
        return self.tailSheetSymmetricValues

    def getTailSheetOddValues(self):
        """Return the odd coefficients a_mn^o.

        Return the odd coefficients a_mn^o.

        Parameters
        ----------
        None

        Returns
        -------
        result : CoefficientExpansion2D
            Tail sheet odd values.
        """
        return self.tailSheetOddValues

    def getTailSheetEvenValues(self):
        """Return the even coefficients a_n^e.

        Return the even coefficients a_n^e.

        Parameters
        ----------
        None

        Returns
        -------
        result : CoefficientExpansion2D
            Tail sheet even values.
        """
        return self.tailSheetEvenValues

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
            coeffs[count] = self.tailSheetSymmetricValues.getCoefficient(n)
            count += 1

        for n in range(firstN, lastN + 1):
            for m in range(firstM, lastM + 1):
                coeffs[count] = self.tailSheetOddValues.getCoefficient(m, n)
                count += 1

        for n in range(firstN, lastN + 1):
            for m in range(firstM, lastM + 1):
                coeffs[count] = self.tailSheetEvenValues.getCoefficient(m, n)
                count += 1

        return CoefficientExpansions.createExpansionFromArray(coeffs, 1)

    def getNumAzimuthalExpansions(self):
        """Return the number of azimuthal expansions.
        
        Return the number of azimuthal expansions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Number of azimuthal expansions.
        """
        return self.numAzimuthalExpansions

    def getNumRadialExpansions(self):
        """Return the number of radial expansions.
        
        Return the number of radial expansions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Number of radial expansions.
        """
        return self.numRadialExpansions

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
