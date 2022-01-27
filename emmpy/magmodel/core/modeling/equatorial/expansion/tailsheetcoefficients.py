"""Tail sheet coefficients for an equatorial expansion.

Tail sheet coefficients for an equatorial expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


# Names of computed attributes, used by __getattr__().
computed_attributes = ["numAzimuthalExpansions", "numRadialExpansions"]


class TailSheetCoefficients:
    """Tail sheet coefficients for an equatorial expansion.

    This is a container class for the coefficients used for an equatorial
    expansion. That is, this class holds the symmetric a_n^s, odd a_mn^o, and
    even a_mn^e coefficients used in the expansion.

    Attributes
    ----------
    tailSheetSymmetricValues : CoefficientExpansion1D
        tailSheetSymmetricValues
    tailSheetOddValues : CoefficientExpansion2D
        tailSheetOddValues
    tailSheetEvenValues : CoefficientExpansion2D
        tailSheetEvenValues
    numAzimuthalExpansions : int
        Number of components in the azimuthal expansions.
    numRadialExpansions: int
        Number of components in the radial expansions.
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

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        computed_attributes dictionary.

        Returns
        -------
        result : object
            Value of specified attribute.
        """
        if name == "numAzimuthalExpansions":
            result = len(self.tailSheetOddValues)
        elif name == "numRadialExpansions":
            result = len(self.tailSheetSymmetricValues)
        return result

    @staticmethod
    def createUnity(numAzimuthalExpansions, numRadialExpansions):
        """Create a coefficient set with all values set to unity.
        
        Create a coefficient set with all values set to unity.

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
        # Create the symmetric values.
        tailSheetSymmetricValues = ScalarExpansion1D.createUnity(
            numRadialExpansions
        )

        # Create the odd values.
        tailSheetOddValues = ArrayCoefficientExpansion2D.createUnity(
                numAzimuthalExpansions, numRadialExpansions
        )

        # Create the even values.
        tailSheetEvenValues = ArrayCoefficientExpansion2D.createUnity(
                numAzimuthalExpansions, numRadialExpansions
        )

        # Create the coefficients object.
        tsc = TailSheetCoefficients(
            tailSheetSymmetricValues, tailSheetOddValues, tailSheetEvenValues
        )

        return tsc

    @staticmethod
    def createFromArray(array, numAzimuthalExpansions, numRadialExpansions):
        """Create a TailSheetCoefficients from a 1-D array.

        Create a TailSheetCoefficients from a 1-D array. Note that the values
        in the array are assumed to be in column-major order for the odd and
        even coefficients.

        Parameters
        ----------
        array : 1-D array of float
            Values to use for expansion.
        numAzimuthalExpansions : int
            Number of components in the azimuthal expansions
        numRadialExpansions : int
            Number of components in the radial expansions.

        Returns
        -------
        tsc : TailSheetCoefficients
            Object with values copied from array.
        """
        # Convert the array to np.ndarray format.
        data = np.array(array)

        # Extract the symmetric values.
        i1 = 0
        i2 = numRadialExpansions
        sym = data[i1:i2]

        # Extract the odd values.
        i1 = i2
        i2 += numAzimuthalExpansions*numRadialExpansions
        odd = data[i1:i2].reshape(
            (numRadialExpansions, numAzimuthalExpansions)
        ).T

        # Extract the even values.
        i1 = i2
        i2 += numAzimuthalExpansions*numRadialExpansions
        even = data[i1:i2].reshape(
            (numRadialExpansions, numAzimuthalExpansions)
        ).T

        # Create the new coefficients object.
        tailSheetSymmetricValues = ScalarExpansion1D(sym)
        tailSheetOddValues = ArrayCoefficientExpansion2D(odd)
        tailSheetEvenValues = ArrayCoefficientExpansion2D(even)
        tsc = TailSheetCoefficients(
            tailSheetSymmetricValues, tailSheetOddValues, tailSheetEvenValues
        )

        return tsc

    def getAsSingleExpansion(self):
        """Return the coefficients as a single 1D expansion.
        
        Return the coefficients as a single 1D expansion. Note that the values
        are packed in column-major order for the odd and even coefficients.

        Parameters
        ----------
        None

        Returns
        -------
        ce1d : CoefficientExpansion1D
            Expansion with all coefficients collapsed to 1 dimension.
        """
        # Allocate the array to hold all coefficients.
        na = self.numAzimuthalExpansions
        nr = self.numRadialExpansions
        n_expansions = nr + 2*na*nr
        coeffs = np.empty((n_expansions,))

        # Extract the symmetric values.
        i1 = 0
        i2 = nr
        coeffs[i1:i2] = self.tailSheetSymmetricValues

        # Extract the odd values.
        i1 = i2
        i2 += na*nr
        coeffs[i1:i2] = self.tailSheetOddValues.T.flatten()

        # Extract the even values.
        i1 = i2
        i2 += na*nr
        coeffs[i1:i2] = self.tailSheetEvenValues.T.flatten()

        # Create the 1-D expansion.
        ce1d = ScalarExpansion1D(coeffs)

        return ce1d
