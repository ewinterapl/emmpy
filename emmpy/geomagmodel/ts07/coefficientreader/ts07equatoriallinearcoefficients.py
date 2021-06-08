"""Equatorial linear coefficients for the TS07 model."""


from math import sqrt

from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class Ts07EquatorialLinearCoefficients:
    """Equatorial linear coefficients for the TS07 model.

    author G.K.Stephens
    """

    def __init__(self, coeffs, pdynDependentCoeffs, numAzimuthalExpansions,
                 numRadialExpansions):
        """Build a new object."""
        self.coeffs = coeffs
        self.pdynDependentCoeffs = pdynDependentCoeffs
        self.numAzimuthalExpansions = numAzimuthalExpansions
        self.numRadialExpansions = numRadialExpansions

    @staticmethod
    def create(
        sym,
        symPdynDependent, aOdd, aOddPdynDependent, aEven,
        aEvenPdynDependent, numAzimuthalExpansions, numRadialExpansions):
        """Create a new object."""
        coeffs = TailSheetCoefficients(sym, aOdd, aEven)
        pdynDependentCoeffs = TailSheetCoefficients(
            symPdynDependent, aOddPdynDependent, aEvenPdynDependent
        )
        return Ts07EquatorialLinearCoefficients(
            coeffs, pdynDependentCoeffs, numAzimuthalExpansions,
            numRadialExpansions
        )

    def getNumAzimuthalExpansions(self):
        """Return the number of azimuthal expansions."""
        return self.numAzimuthalExpansions

    def getNumRadialExpansions(self):
        """Return the number of radial expansions."""
        return self.numRadialExpansions

    def getCoeffs(self):
        """Return the coefficients."""
        return self.coeffs

    def getPdynDependentCoeffs(self):
        """Return the coefficients dependent on the dynamic pressure."""
        return self.pdynDependentCoeffs

    def getPdynScaledCoeffs(self, dynamicPressure):
        """Return the coefficients scaled by the dynamic pressure."""
        pDyn0 = 2.0
        pDynNormalized = sqrt(dynamicPressure/pDyn0) - 1
        symPdynDependent = CoefficientExpansions.scale(
            self.pdynDependentCoeffs.getTailSheetSymmetricValues(),
            pDynNormalized
        )
        aOddPdynDependent = CoefficientExpansions.scale(
            self.pdynDependentCoeffs.getTailSheetOddValues(), pDynNormalized
        )
        aEvenPdynDependent = CoefficientExpansions.scale(
            self.pdynDependentCoeffs.getTailSheetEvenValues(), pDynNormalized
        )
        return TailSheetCoefficients(
            symPdynDependent, aOddPdynDependent, aEvenPdynDependent
        )
