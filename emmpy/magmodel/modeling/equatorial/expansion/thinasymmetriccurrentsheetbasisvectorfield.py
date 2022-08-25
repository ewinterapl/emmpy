"""Basis vector field for a thin asymmetric current sheet.

Basis vector field for a thin asymmetric current sheet.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


from emmpy.magmodel.math.expansions.arrayexpansion1d import ArrayExpansion1D
from emmpy.magmodel.math.expansions.arrayexpansion2d import ArrayExpansion2D
from emmpy.magmodel.math.trigparity import EVEN, ODD
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetasymmetricexpansion import (
    TailSheetAsymmetricExpansion
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetexpansions import (
    TailSheetExpansions
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetsymmetricexpansion import (
    TailSheetSymmetricExpansion
)
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.utilities.nones import nones


class ThinAsymmetricCurrentSheetBasisVectorField(BasisVectorField):
    """Basis vector field for a thin asymmetric current sheet.

    This module described the tail fields as stated in Tsyganenko and
    Sitnov 2007:

    "Magnetospheric configurations from a high-resolution data-based magnetic
    fields model", eq. 14.

    This is equivalent to the FORTRAN subroutine:
    SUBROUTINE UNWARPED (X,Y,Z,BXS,BYS,BZS,BXO,BYO,BZO,BXE,BYE,BZE)

    Attributes
    ----------
    tailLength : float
        Length of tail.
    currentSheetHalfThickness : DifferentiableScalarFieldIJ
        currentSheetHalfThickness
    coeffs : DifferentiableScalarFieldIJ
        Coefficients for expansion.
    numAzimuthalExpansions : int
        Number of azimuthal expansions.
    numRadialExpansions : int
        Number of radial expansions.
    """

    def __init__(self, tailLength, currentSheetHalfThickness, coeffs):
        """Initialize a new ThinAsymmetricCurrentSheetBasisVectorField object.

        Initialize a new ThinAsymmetricCurrentSheetBasisVectorField object.

        Parameters
        ----------
        tailLength : float
            Length of tail.
        currentSheetHalfThickness : DifferentiableScalarFieldIJ
            currentSheetHalfThickness
        coeffs : DifferentiableScalarFieldIJ
            Coefficients for expansion.
        """
        self.coeffs = coeffs
        self.numAzimuthalExpansions = coeffs.numAzimuthalExpansions
        self.numRadialExpansions = coeffs.numRadialExpansions
        self.tailLength = tailLength
        self.currentSheetHalfThickness = currentSheetHalfThickness

    @staticmethod
    def createUnity(
        tailLength, currentSheetHalfThickness, numAzimuthalExpansions,
        numRadialExpansions
    ):
        """Create a field where all coefficients are unity.

        Creates a ThinAsymmetricCurrentSheetBasisVectorField where all
        the coefficients have been set to 1.

        Parameters
        ----------
        tailLength : float
            Length of tail.
        currentSheetHalfThickness : DifferentiableScalarFieldIJ
            currentSheetHalfThickness
        numAzimuthalExpansions : int
            Number of azimuthal expansions.
        numRadialExpansions : int
            Number of radial expansions.
        
        Returns
        -------
        result : ThinAsymmetricCurrentSheetBasisVectorField
            Field with all coefficients set to unity.
        """
        coeffs = TailSheetCoefficients.createUnity(
            numAzimuthalExpansions, numRadialExpansions
        )
        return ThinAsymmetricCurrentSheetBasisVectorField(
            tailLength, currentSheetHalfThickness, coeffs)

    def evaluate(self, location):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        
        Returns
        -------
        buffer : VectorIJK
            Vector result of evaluation at location.
        """
        buffer = VectorIJK()
        buffer[:] = self.evaluateExpansions(location).sum()
        return buffer

    def evaluateExpansion(self, location):
        """Evaluate the expansion.
        
        Evaluate the expansion.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        
        Returns
        -------
        result : list of VectorIJK
            Components of expansion at location.
        """
        return self.evaluateExpansions(location).getExpansionsAsList()

    def evaluateExpansions(self, location):
        """Recalculate everything.
        
        Recalculate everything.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        
        Returns
        -------
        result : TailSheetExpansions
            All expansion components at location.
        """
        # Preallocate the arrays of vectors for the expansions.
        symmetricExpansions = nones((self.numRadialExpansions,))
        oddExpansions = nones((self.numAzimuthalExpansions,
                               self.numRadialExpansions))
        evenExpansions = nones((self.numAzimuthalExpansions,
                                self.numRadialExpansions))

        # Precompute the wavenumbers for each radial expansion.
        kn = np.arange(1, self.numRadialExpansions + 1)/self.tailLength

        # Make a CartesianVector for the location.
        cartesianLocation = CartesianVector(location)

        # n is the radial expansion number.
        for n in range(self.numRadialExpansions):

            symBasisFunction = TailSheetSymmetricExpansion(
                kn[n], self.currentSheetHalfThickness
            )
            a = self.coeffs.tailSheetSymmetricValues[n]
            symmetricExpansions[n] = symBasisFunction.evaluate(cartesianLocation)*a

            # m is the azimuthal expansion number.
            for m in range(self.numAzimuthalExpansions):
                aOdd = self.coeffs.tailSheetOddValues[m, n]
                oddBasisFunction = TailSheetAsymmetricExpansion(
                    kn[n], m + 1, ODD, self.currentSheetHalfThickness
                )
                oddExpansions[m][n] = (
                    oddBasisFunction.evaluate(cartesianLocation)*aOdd)
                aEven = self.coeffs.tailSheetEvenValues[m, n]
                evenBasisFunction = TailSheetAsymmetricExpansion(
                    kn[n], m + 1, EVEN, self.currentSheetHalfThickness
                )
                evenExpansions[m][n] = (
                    evenBasisFunction.evaluate(cartesianLocation)*aEven)

        return TailSheetExpansions(
            ArrayExpansion1D(symmetricExpansions),
            ArrayExpansion2D(oddExpansions),
            ArrayExpansion2D(evenExpansions)
        )

    def getNumberOfBasisFunctions(self):
        """Return the number of basis functions.
        
        Return the number of basis functions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Total number of basis functions.
        """
        return (
            self.numRadialExpansions +
            2*self.numRadialExpansions*self.numAzimuthalExpansions
        )
