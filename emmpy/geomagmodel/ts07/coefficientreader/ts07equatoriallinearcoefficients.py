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

    def toString(self):
        """Convert the object to a string."""
        return (
            "Ts07EquatorialLinearCoefficients [coeffs=%s, "
            "pdynDependentCoeffs=%s, numAzimuthalExpansions=%s, "
            "numRadialExpansions=%s]" %
            (self.coeffs.toString(), self.pdynDependentCoeffs.toString(),
             self.numAzimuthalExpansions, self.numRadialExpansions)
        )

    def hashCode(self):
        """Compute the object hash code."""
        prime = 31
        result = 1
        result = prime*result
        if self.coeffs:
            result += self.coeffs.hashCode()
        result = prime*result + self.numAzimuthalExpansions
        result = prime*result + self.numRadialExpansions
        if self.pdynDependentCoeffs:
            result += self.pdynDependentCoeffs.hashCode()
        return result

    def equals(self, obj):
        """Check for equality with another object."""
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.coeffs is None:
            if other.coeffs is not None:
                return False
        elif not self.coeffs.equals(other.coeffs):
            return False
        if self.numAzimuthalExpansions != other.numAzimuthalExpansions:
            return False
        if self.numRadialExpansions != other.numRadialExpansions:
            return False
        if self.pdynDependentCoeffs is None:
            if other.pdynDependentCoeffs is not None:
                return False
        elif not self.pdynDependentCoeffs.equals(other.pdynDependentCoeffs):
            return False
        return True
