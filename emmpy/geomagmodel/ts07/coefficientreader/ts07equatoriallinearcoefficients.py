"""Equatorial linear coefficients for the TS07 model.

Equatorial linear coefficients for the TS07 model.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import sqrt

from emmpy.magmodel.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class Ts07EquatorialLinearCoefficients:
    """Equatorial linear coefficients for the TS07 model.

    Equatorial linear coefficients for the TS07 model.

    Attributes
    ----------
    coeffs : TailSheetCoefficients
        coeffs
    pdynDependentCoeffs : TailSheetCoefficients
        pdynDependentCoeffs
    numAzimuthalExpansions : int
        Number of azimuthal expansions.
    numRadialExpansions : int
        Number of radial expansions.
    """

    def __init__(self, coeffs, pdynDependentCoeffs, numAzimuthalExpansions,
                 numRadialExpansions):
        """Initialize a new Ts07EquatorialLinearCoefficients object.

        Initialize a new Ts07EquatorialLinearCoefficients object.

        Parameters
        ----------
        coeffs : TailSheetCoefficients
            coeffs
        pdynDependentCoeffs : TailSheetCoefficients
            pdynDependentCoeffs
        numAzimuthalExpansions : int
            Number of azimuthal expansions.
        numRadialExpansions : int
            Number of radial expansions.
        """
        self.coeffs = coeffs
        self.pdynDependentCoeffs = pdynDependentCoeffs
        self.numAzimuthalExpansions = numAzimuthalExpansions
        self.numRadialExpansions = numRadialExpansions

    @staticmethod
    def create(
        sym,
        symPdynDependent, aOdd, aOddPdynDependent, aEven,
        aEvenPdynDependent, numAzimuthalExpansions, numRadialExpansions):
        """Create a new Ts07EquatorialLinearCoefficients object.
        
        Create a new Ts07EquatorialLinearCoefficients object.

        Parameters
        ----------
        sym : CoefficientExpansion1D
            XXX
        symPdynDependent : CoefficientExpansion1D
            XXX
        aOdd : CoefficientExpansion2D
            XXX
        aOddPdynDependent : CoefficientExpansion2D
            XXX
        aEven : CoefficientExpansion2D
            XXX
        aEvenPdynDependent : CoefficientExpansion2D
            XXX
        numAzimuthalExpansions : int
            Number of azimuthal expansions.
        numRadialExpansions : int
            Number of radial expansions.
        
        Returns
        -------
        result : Ts07EquatorialLinearCoefficients
            THe new object.
        """
        coeffs = TailSheetCoefficients(sym, aOdd, aEven)
        pdynDependentCoeffs = TailSheetCoefficients(
            symPdynDependent, aOddPdynDependent, aEvenPdynDependent
        )
        return Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, numAzimuthalExpansions,
            numRadialExpansions
        )

    def getPdynScaledCoeffs(self, dynamicPressure):
        """Return the coefficients scaled by the dynamic pressure.
        
        Return the coefficients scaled by the dynamic pressure.

        Parameters
        ----------
        dynamicPressure : float
            Dynamic pressure.

        Returns
        -------
        result : TailSheetCoefficients
            The tail sheet coefficients scaled using the dynamic pressure.
        """
        pDyn0 = 2.0
        pDynNormalized = sqrt(dynamicPressure/pDyn0) - 1
        symPdynDependent = self.pdynDependentCoeffs.tailSheetSymmetricValues.scale(pDynNormalized)
        aOddPdynDependent = self.pdynDependentCoeffs.tailSheetOddValues.scale(pDynNormalized)
        aEvenPdynDependent = self.pdynDependentCoeffs.tailSheetEvenValues.scale(pDynNormalized)
        return TailSheetCoefficients(
            symPdynDependent, aOddPdynDependent, aEvenPdynDependent
        )
